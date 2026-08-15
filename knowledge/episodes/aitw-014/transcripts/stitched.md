# S02E10 – Implementing Decaying-Resolution Memory



Source: YouTube captions (automatic:en)



[00:00:09.190] All right. So, welcome back everyone. Uh

[00:00:09.200] we're going to do the thing that we

[00:00:10.240] normally do every Tuesday at about 10:00

[00:00:12.160] a.m. Uh which is Dexter and I will be

[00:00:15.320] talking about something fun related to

[00:00:17.440] AI and our goal as per usual is always

[00:00:20.160] to get something that is going to get

[00:00:22.400] production uh applicable at least and

[00:00:25.400] have some real code that's going to

[00:00:26.520] solve a real problem related to

[00:00:29.360] some hard problem in AI. One of the

[00:00:31.200] things that we hate the most is when

[00:00:32.279] people high-level talk about things when

[00:00:34.040] they say things AI makes everything good

[00:00:36.280] or they talk about what an LLM is. We

[00:00:38.000] don't need either of those things. We

[00:00:39.280] want to see real code.

[00:00:40.880] And we want to build something that's

[00:00:42.160] actually sophisticated that can actually

[00:00:44.520] ship to prod.

[00:00:47.120] Last week, we did a

[00:00:49.480] high-level overview on what is context

[00:00:51.120] engineering. We're able to have some

[00:00:52.560] context on a new type of technique that

[00:00:55.560] one of our fellow colleagues from YC

[00:00:58.200] shared with us, which is DRM.

[00:01:01.160] Today's episode is going to be about

[00:01:02.640] actually about writing some of the code

[00:01:04.280] and talking about how when you hear a

[00:01:05.720] concept like that, how do we go from

[00:01:07.280] that concept to actually writing the

[00:01:09.680] code?

[00:01:10.680] And sometimes that can leave a little

[00:01:12.640] bit of a gap. So, we felt that the best

[00:01:14.640] way was just to go do it. Even though

[00:01:18.080] even some if some parts of it might seem

[00:01:20.080] straight more straightforward,

[00:01:22.720] what we find is that there's always

[00:01:24.000] nuances that often get overlooked and

[00:01:26.040] under

[00:01:27.240] solved and the tradeoffs are often under

[00:01:29.440] discussed. And the best part of writing

[00:01:31.080] the code is we get to talk about these

[00:01:32.200] tradeoffs.

[00:01:33.680] So, with that,

[00:01:35.040] um

[00:01:35.640] Dexter, shall we start off with a little

[00:01:37.240] recap? Do you want to screen share and

[00:01:38.920] show off a whiteboard or two from last

[00:01:40.880] time?

[00:01:41.000] >> Yeah, let's look at what we did last

[00:01:42.800] time. Um

[00:01:48.510] We'll just give a brief recap for anyone

[00:01:48.520] that is coming for the first time

[00:01:50.240] because content it was a pretty dense uh

[00:01:53.120] content video and I think like a quick

[00:01:55.080] 5-minute recap is going to help come

[00:01:56.840] back to exactly what we're going to go

[00:01:58.680] implement today.

[00:02:00.000] Yeah, and uh I'll pull up quickly

[00:02:02.120] Brian's blog post as well. Um

[00:02:04.920] but basically actually I'm going to go

[00:02:06.000] to the Git repo um and show those cuz I

[00:02:08.600] think they're a little more concise.

[00:02:10.479] Um so, here's the last episode. You can

[00:02:12.120] watch the video here.

[00:02:13.560] Um

[00:02:14.200] a lot of the takeaways there's some

[00:02:15.480] highlights and quotes from the episode,

[00:02:16.760] but basically like context engineering

[00:02:18.160] is all about like

[00:02:23.670] kind of stepping taking a step back from

[00:02:23.680] like rag versus memory versus all these

[00:02:25.520] like different categories of AI

[00:02:27.000] engineering techniques and thinking of

[00:02:28.720] them holistically as like how do we put

[00:02:31.520] the right tokens into the model because

[00:02:33.520] the only thing that affects the quality

[00:02:34.800] of your output is the quality of the

[00:02:37.080] input and the quality of the model, but

[00:02:38.880] um a lot of us can't control that, but

[00:02:40.520] we can control the tokens we put in. Um

[00:02:42.640] and so, we talked about kind of building

[00:02:44.960] the input to a model as kind of a

[00:02:46.800] combination of all of these things.

[00:02:49.360] Um and when you think of them less as

[00:02:51.000] like they're they're not really like

[00:02:52.880] modular orthogonal things because they

[00:02:55.560] all affect each other and they all

[00:02:57.040] affect the way the model is going to

[00:02:58.520] interpret your prompt. Um and so, we

[00:03:00.560] talked about a lot of these things and I

[00:03:02.040] think the thing we got the best out of

[00:03:04.120] like that we went the deepest on like

[00:03:05.360] memory and um Brian, I don't know if

[00:03:06.960] he's here today, but he came last week

[00:03:08.120] and talked about this blog post he

[00:03:10.200] wrote, which is linked in the notes. Um

[00:03:12.360] but basically doing what he calls

[00:03:14.120] decaying resolution memory, which is

[00:03:16.120] taking all the actual mem messages and

[00:03:18.680] then compacting them into daily

[00:03:20.000] summaries and then turning those into

[00:03:21.560] weekly summaries and those into monthly

[00:03:22.880] summaries so that we can build agents

[00:03:24.960] that don't forget things, but also like

[00:03:27.880] have a reasonable

[00:03:29.360] you could put every single message in

[00:03:31.000] the context window, but you wouldn't

[00:03:32.360] have much like

[00:03:34.440] uh space to do any actual work um and

[00:03:37.400] make any decisions or work with users or

[00:03:39.880] whatever it is. And so, this was a

[00:03:41.880] technique that um a couple people have

[00:03:43.560] also done and that they implemented over

[00:03:45.040] there.

[00:03:45.960] Um so, today we thought we'd get

[00:03:48.240] hands-on with some code and and try to

[00:03:49.560] build it.

[00:03:51.440] Yeah, and uh do you want to screen share

[00:03:53.280] like fast? Keep going. Oh, yeah. One

[00:03:55.320] thing. You're going to draw? Yeah, of

[00:03:57.720] course. I love drawing on your screen.

[00:03:59.200] It's a lot easier than actually drawing.

[00:04:01.720] Uh um

[00:04:02.800] So, if we go back to this uh decaying

[00:04:04.800] resolution memory, one of the biggest

[00:04:06.360] things we really talked about was like

[00:04:08.480] what is an analogy uh to this because if

[00:04:10.800] we're going to go implement this, what I

[00:04:12.520] find is before I go implement something

[00:04:14.400] from scratch,

[00:04:15.800] uh especially in the world of AI where a

[00:04:17.120] lot of stuff is new, what I like to do

[00:04:19.160] is I like to think a little bit harder

[00:04:20.359] about like what does this relate to?

[00:04:22.079] What is a concept that this feels very

[00:04:23.840] familiar to me from an engineering

[00:04:26.200] principle so then I can just

[00:04:28.120] try and copy the architecture of how

[00:04:29.920] that thing would be done as much as

[00:04:31.680] possible and not have to reinvent

[00:04:33.520] everything on the fly cuz familiarity

[00:04:35.440] helps a lot.

[00:04:37.480] So, with that, does anyone have ideas

[00:04:40.080] what this concept of decaying resolution

[00:04:42.000] memory kind of sounds like or relates

[00:04:44.400] to? Uh Dexter, what do you think?

[00:04:47.120] What is like the most engineering-y

[00:04:48.880] principle that you think of when you see

[00:04:50.760] this idea?

[00:04:52.400] L1, L2, L3?

[00:04:54.320] That's literally where my brain jumped

[00:04:55.560] to exactly. Like

[00:04:57.120] like literally where my brain went to.

[00:04:59.160] Uh or Let me pull up a fresh whiteboard

[00:05:02.000] for today just so that we have somewhere

[00:05:03.760] to work.

[00:05:04.920] Um

[00:05:06.800] I'm going to send this to you right now.

[00:05:09.680] Sorry, I meant to do that before the

[00:05:10.800] episode.

[00:05:12.360] Uh

[00:05:17.750] All right, it is in your Slack.

[00:05:17.760] Perfect. I'll pull it up right away.

[00:05:26.030] So, when I jumped into this, that was

[00:05:26.040] like the first thing that really

[00:05:27.960] popped into my mind. It's like it

[00:05:29.200] literally feels like an L1, L2, L3

[00:05:30.960] cache.

[00:05:32.080] Um and what that really means to me is

[00:05:34.360] that the designs that we use to design

[00:05:36.040] cache keys for cache key invalidation is

[00:05:38.600] probably a really similar kind of design

[00:05:40.360] of how I want to think about this

[00:05:41.720] problem.

[00:05:42.840] So, when I think about like for example,

[00:05:45.320] I can get up actions. We often have this

[00:05:47.000] is if you ever use a cache in a get up

[00:05:48.480] action, you'll name something like

[00:05:51.000] food.not not like machine

[00:05:54.840] .some

[00:05:56.640] some key over here. And when you go look

[00:05:57.960] up your cache key, what you do is you

[00:05:59.200] find the cache key based on the naming

[00:06:01.080] that you have. So, if you're building

[00:06:02.040] x86, you get the cache from x86. And

[00:06:04.960] then eventually your get up build gets

[00:06:06.680] totally messed up and what you do is you

[00:06:08.600] just call this foo1 and you invalidate

[00:06:10.320] the whole cache.

[00:06:11.600] Cuz that's how we do prefixes and cache

[00:06:13.600] keys. And that ends up being pretty

[00:06:15.080] useful and valuable.

[00:06:17.920] And we want to have some

[00:06:19.920] >> Sorry, you just said a lot of things

[00:06:21.640] really quickly and I think um it might

[00:06:24.000] be helpful to just kind of talk about

[00:06:25.480] that quickly. Um

[00:06:28.600] so so we have like you have your like

[00:06:30.920] build going through, right? And you may

[00:06:32.360] have in your CI build um you have

[00:06:35.680] uh

[00:06:36.280] you know, install go,

[00:06:39.120] um

[00:06:40.480] download go dependencies,

[00:06:46.590] um and then you like would like build

[00:06:46.600] the project,

[00:06:49.640] you know, run the tests, etc. and then

[00:06:51.400] maybe you would like promote promote an

[00:06:53.040] artifact or promote or build something,

[00:06:55.000] right?

[00:07:01.190] And what happens every time you go

[00:07:01.200] through this build, you're going to take

[00:07:02.680] the output of the dependencies and

[00:07:04.080] you're going to store it somewhere so

[00:07:05.400] that like basically on the next cat on

[00:07:07.560] the next run, you can just go pull those

[00:07:10.440] in and then you won't have to build it

[00:07:11.960] anymore. But what gets tricky here is if

[00:07:14.160] your list of dependencies or your

[00:07:15.560] package.json or something changes, this

[00:07:17.880] cache is no longer full or valid. And

[00:07:20.880] so, you need to have a system of cache

[00:07:22.640] keys so that you know, okay, we're still

[00:07:24.320] going to pull in the old ones, but then

[00:07:26.520] when we write the new one, we're going

[00:07:27.760] to blow away the old one in certain

[00:07:29.200] cases so that on the next build run,

[00:07:30.840] it's going to have all the new

[00:07:31.600] dependencies as well.

[00:07:34.640] Exactly. So, like you have like a

[00:07:36.000] package.json hash at the bottom.

[00:07:38.280] But then what you end up doing is you

[00:07:40.120] also want to deal with the fact that

[00:07:41.320] hey, I'm building go on seven different

[00:07:43.200] machines like x86 versus arm64. So, I

[00:07:46.160] will have another cache key over here.

[00:07:48.800] Right.

[00:07:50.000] And inevitably anyone that has dealt

[00:07:52.080] with this sort of system probably will

[00:07:53.800] feel this at some point, which is

[00:07:56.440] I can do different colors for different

[00:07:58.000] parts of it. Okay. Well, uh that sucks.

[00:08:01.800] Yeah, you have to have two text blocks.

[00:08:04.200] Uh I did not know that.

[00:08:05.920] Uh um

[00:08:07.240] package.json hash.

[00:08:09.520] Um what ends up happening is inevitably

[00:08:11.200] I'm going to blow that up and then I

[00:08:12.320] will want a

[00:08:13.640] totally separate cache key that is made

[00:08:15.640] of a separate part that is something

[00:08:17.280] that I can just control that is like a

[00:08:18.640] static prefix

[00:08:20.120] that I will change only when I'm ready I

[00:08:22.120] just don't trust it. I messed something

[00:08:24.040] up and I just want to invalidate the

[00:08:25.080] whole thing.

[00:08:26.800] When I look at the the first thing that

[00:08:28.720] popped up to me when we saw the think

[00:08:30.080] about like having a monthly, weekly,

[00:08:33.599] daily summary,

[00:08:36.200] was it's kind of similar where when I

[00:08:38.919] pull information

[00:08:40.719] when I pull information from like this

[00:08:43.280] part of the timeline, oops.

[00:08:48.030] When I pull information from this part

[00:08:48.040] of the timeline versus this part of the

[00:08:49.880] timeline versus this part of the

[00:08:51.800] timeline,

[00:08:53.080] I almost want to this one should go

[00:08:55.280] directly into here and look information

[00:08:57.680] from the monthly cache.

[00:08:59.560] This one should go directly into here

[00:09:02.400] and look directly from the weekly cache

[00:09:03.880] and information about this part of the

[00:09:05.120] timeline should go into the daily cache.

[00:09:07.480] So, what I'm trying to do is I'm trying

[00:09:08.720] to almost see where I should get

[00:09:10.120] information from and if it's relevant or

[00:09:11.600] not based on the kinds of information

[00:09:13.480] that I'm asking.

[00:09:15.080] And if we remember, Brian's app is a

[00:09:17.080] very different kind of app than most

[00:09:18.680] other people's apps.

[00:09:20.360] Um it's an app about how they actually

[00:09:24.160] get uh have parents uh they build an app

[00:09:27.440] that helps uh

[00:09:29.080] coach students along the way along their

[00:09:31.600] journey.

[00:09:32.640] And if a student was working on times

[00:09:34.240] tables today,

[00:09:35.640] they don't really need to know the exact

[00:09:37.440] problem that they're working on a month

[00:09:39.120] ago. They just need to know that they

[00:09:40.800] were working on times tables about a

[00:09:42.520] month ago and this is the progress that

[00:09:43.920] they make.

[00:09:45.120] So, the resolution of information that's

[00:09:47.440] available at any given cache point is

[00:09:50.040] also going to be very different based on

[00:09:52.360] what you're trying to do.

[00:09:54.880] So, when we try and go build this, we

[00:09:56.400] want to make sure that we what we really

[00:09:57.680] capture here is the resolution of

[00:09:59.520] information at each state is going to be

[00:10:01.720] different. So what is monthly summaries

[00:10:03.160] really good for?

[00:10:04.800] I'm going to make an arbitrary statement

[00:10:06.600] of what I want, which is like

[00:10:09.200] high-level understanding

[00:10:11.600] of progress plus achievements.

[00:10:16.320] That's what I really want to have in a

[00:10:17.880] in a monthly summary.

[00:10:20.000] Uh we can I don't know where to put this

[00:10:21.600] text. Maybe I'll put it I got it. I got

[00:10:23.680] it. I'm on it. The thing that I want in

[00:10:25.720] my And I'll I won't actually do the

[00:10:28.040] middle layer yet cuz if I do the middle

[00:10:29.640] layer, it won't actually do what I want

[00:10:31.920] because the middle layers are hard to

[00:10:33.040] define without having a good

[00:10:34.000] understanding of what this is.

[00:10:35.760] So this over here would basically be

[00:10:37.520] just to clarify this over here would be

[00:10:39.200] like messages in the current chat.

[00:10:42.920] I would just say that everything is

[00:10:44.160] going to be the raw transcript right

[00:10:45.440] over here. Like this is the

[00:10:47.480] transcript of everything that happened.

[00:10:49.880] Yeah.

[00:10:51.040] Maybe even all the tool calls and

[00:10:52.360] everything else that go into it along

[00:10:53.640] the way, but fundamentally it's going to

[00:10:55.000] be the raw transcript.

[00:10:57.040] Daily summaries, if I'm going to think

[00:10:59.200] like a teacher, are going to be like

[00:11:02.200] assignments

[00:11:04.200] plus statuses

[00:11:06.400] is kind of what I want to have. Like

[00:11:07.680] what assignments did I do well at? What

[00:11:09.000] was the status of them? Like what was

[00:11:10.440] the grades? That kind of stuff.

[00:11:16.230] And likely what I want in weekly

[00:11:16.240] summaries is some combination of like

[00:11:19.120] groups of assignments

[00:11:25.150] plus some sort of statuses that isn't

[00:11:25.160] really the same type of status here.

[00:11:26.360] Some of that talks about like some sort

[00:11:27.480] of like a structure

[00:11:29.560] of like what is generally going well

[00:11:32.839] and going poorly.

[00:11:36.000] And like really one interesting thing

[00:11:37.800] that I think Brian mentioned last time

[00:11:39.240] was this idea of keeping tabs

[00:11:42.640] on what should I really keep tabs on to

[00:11:45.760] include in the monthly summary

[00:11:48.200] in my weekly summary. So like what is a

[00:11:50.000] highlight almost extracted out of here?

[00:11:54.040] So if I pause over here, that's actually

[00:11:57.200] any questions and stuff so far on what

[00:11:59.000] I'm saying?

[00:12:00.120] Um no, I just want to call out like this

[00:12:01.720] is one of the biggest takeaways that was

[00:12:03.320] kind of like subtle but important from

[00:12:05.880] last week was this idea of work

[00:12:08.680] backwards from the problem you're

[00:12:11.000] solving.

[00:12:12.560] I don't think we're at a point as a AI

[00:12:14.320] industry that there is a one memory

[00:12:16.839] implementation to rule them all. And

[00:12:19.880] knowing exactly what you what purpose

[00:12:22.360] you want each thing to serve and what

[00:12:23.800] you want interactions to feel like is

[00:12:26.320] going to inform how you design these

[00:12:29.200] systems. And that's why like today we're

[00:12:31.280] going to do a like white box

[00:12:32.760] implementation of kind of a toy problem.

[00:12:35.560] Um with the idea that like you should

[00:12:38.160] have all the code because you may want

[00:12:39.520] to tweak this and you might have to say

[00:12:40.680] like, "Okay, well, we don't really for

[00:12:42.480] for the scope of our problem, anything

[00:12:43.839] that happened more than 3 days ago,

[00:12:45.000] we're just not going to show it and

[00:12:46.240] we're going to make weekly summaries do

[00:12:48.120] we're going to use weekly summaries for

[00:12:49.320] everything more than 3 days ago." Or you

[00:12:50.880] may say the last 14 days are all super

[00:12:53.040] important, so we need the daily for all

[00:12:54.839] of those.

[00:12:56.800] Yeah, so it's very very application

[00:12:58.760] specific. We are implementing one

[00:13:00.839] version of this with some design

[00:13:02.600] tradeoffs that we are making here.

[00:13:05.520] Um we'll do that in the prompts in a

[00:13:07.200] bit, Brian. By the way, Brian, uh if you

[00:13:08.920] want to unmute and hop on and join the

[00:13:10.880] discussion, definitely feel free to do

[00:13:12.360] that.

[00:13:13.360] Yeah. Feel free to tell us we're wrong.

[00:13:15.440] Yeah, please. Uh but one of the big

[00:13:17.480] things to note here is these are all

[00:13:18.520] design tradeoffs. It's like when you

[00:13:20.560] first everyone here has probably done

[00:13:22.720] some level of LeetCode or has heard of

[00:13:24.320] LeetCode.

[00:13:26.240] I think a lot of people talk about how

[00:13:27.960] like LeetCode is stupid, it doesn't

[00:13:29.520] really do anything, but the whole point

[00:13:30.600] of LeetCode isn't actually to solve the

[00:13:31.760] algorithm, it's to be able to discuss

[00:13:33.240] tradeoffs

[00:13:34.440] with someone else. When you do a systems

[00:13:36.000] design interview, there is no right

[00:13:38.000] answer for how to design or architect

[00:13:39.640] WhatsApp. There's only tradeoffs that

[00:13:41.440] give you one benefit and lose others and

[00:13:43.200] others that give you some other benefit.

[00:13:45.320] When you design memory for your

[00:13:46.480] application you need to think of like

[00:13:48.839] Dexter said, what is the actual tradeoff

[00:13:50.760] that you're trying to make here?

[00:13:52.360] What are the things that we really need

[00:13:53.680] to capture and then go represent that.

[00:13:56.520] You'll notice

[00:13:57.800] I started off doing a monthly

[00:13:59.400] description and a raw transcript and I

[00:14:01.160] kind of filled everything in the middle

[00:14:02.320] more intuitively as I was going instead

[00:14:04.720] of trying to work my way down from

[00:14:05.880] levels of granularity.

[00:14:07.520] Because it's very hard to go naturally

[00:14:09.200] and come up to this without having done

[00:14:11.920] without having actually knowing what I'm

[00:14:13.280] starting with and working off from a

[00:14:15.480] more intuitive layer.

[00:14:17.560] So this is something that I would

[00:14:19.079] strongly strongly urge you to do. Don't

[00:14:20.920] just copy this DRM implementation. DRM

[00:14:22.920] might suck for your application.

[00:14:25.320] But you really need to think about what

[00:14:26.880] you want to do

[00:14:28.839] for your memory application and how you

[00:14:30.480] want to compress memory over time and if

[00:14:32.800] you want to compress memory over time.

[00:14:34.760] For a completely different application,

[00:14:36.760] your best strategy might actually be

[00:14:40.200] to say that, "Hey, I'm just going to

[00:14:41.920] find slices of the transcript that find

[00:14:44.440] the relevant information because I need

[00:14:46.360] perfect recall because what I'm building

[00:14:48.040] is

[00:14:49.120] uh I'm building search on a Mac and

[00:14:51.480] people are doing like really key grain

[00:14:53.280] search where they want to find a

[00:14:54.120] specific time when they're editing a

[00:14:55.320] certain file, you just search through

[00:14:56.920] the raw uh transcript. That's the best

[00:14:58.959] way to do it."

[00:15:00.320] You might find that that doesn't work

[00:15:01.440] very well. You have to build layers of

[00:15:02.600] different caches as well to do more

[00:15:03.959] optimal work.

[00:15:05.280] But you really need to think about it in

[00:15:06.800] your use case and what you care about

[00:15:08.240] doing.

[00:15:12.550] I'm going to stop on that and actually

[00:15:12.560] start trying to write code pretty soon.

[00:15:15.280] Yeah, so I mean I guess like what are

[00:15:16.560] the function what are the like I don't

[00:15:17.839] think we need to open the editor yet,

[00:15:18.920] but like what are the functions that you

[00:15:20.240] want to write as part of this?

[00:15:22.560] You kind of have to transform this into

[00:15:24.200] this. You have to transform this into

[00:15:25.680] this. You have to transform this into

[00:15:27.400] this. Well, that's a tradeoff, too. We

[00:15:30.040] could actually just do all of these in

[00:15:31.440] parallel as well where we do all of

[00:15:33.079] these directly from here.

[00:15:36.520] We don't have but we could. Or we can do

[00:15:39.079] the thing that you're doing, which is

[00:15:40.040] more of a waterfall approach, which is

[00:15:41.560] we transform one to the other and go

[00:15:43.440] into it. Intuitively, I feel like the

[00:15:45.480] water waterfall approach is better.

[00:15:48.440] So I'm going to go ahead and go do that

[00:15:50.959] in today's implementation.

[00:15:54.200] So okay, so what are the what are the

[00:15:55.600] Yeah, do you want to

[00:15:57.000] Yeah, let's just write it. Um so I think

[00:15:59.000] the first thing to do is

[00:16:00.800] >> Update daily. How do I write text? Yeah,

[00:16:03.360] let's start with a

[00:16:04.760] Let's start with a create daily summary.

[00:16:08.120] We're not going to update a daily

[00:16:09.400] summary ever. We'll only ever create

[00:16:11.280] daily summaries.

[00:16:12.640] Okay, you don't want to compact new

[00:16:14.160] messages into I guess cuz the daily

[00:16:16.079] summary won't be used until the next day

[00:16:18.200] basically. Let's Let's just agree on

[00:16:20.480] that as a design constraint. We don't

[00:16:22.040] have to do that, but let's just do that

[00:16:24.079] for simplicity's sake.

[00:16:25.720] And again, these are tradeoffs that we

[00:16:26.920] can make.

[00:16:28.200] But for now, we're just going to go do

[00:16:29.520] this. We have some messages and we're

[00:16:30.880] going to convert that into like a

[00:16:33.079] Let's just say like a daily summary

[00:16:34.520] object.

[00:16:39.829] Right. And what I will do is this will

[00:16:39.839] run on cron every day at midnight.

[00:16:43.760] Uh

[00:16:44.720] Now this gets a little tricky cuz I'll

[00:16:46.040] talk about time zones in a second. But

[00:16:47.959] let's just assume for now that everyone

[00:16:50.160] is in the same time zone

[00:16:53.040] that as your server, so there are no

[00:16:55.040] confusions about time zones at all.

[00:16:57.079] We'll talk about time zones We'll put it

[00:16:58.480] in uh Pacific time, which is the only

[00:17:00.400] real time zone anyways. Exactly.

[00:17:03.440] Uh

[00:17:04.480] What do you got? Um okay. And then so

[00:17:08.280] what else goes in here? So let's ignore

[00:17:10.480] what what's actually in there. I don't

[00:17:12.079] want to think about

[00:17:13.079] actually think about this right now.

[00:17:14.199] What I want to think about is like what

[00:17:15.320] are the things that I need?

[00:17:16.959] Now the thing that I'm going to also

[00:17:18.199] make is create a

[00:17:20.360] weekly summary.

[00:17:22.439] Uh

[00:17:35.390] And I want the weekly summaries to have

[00:17:35.400] some form of continuity.

[00:17:37.760] So what I will do is like I'll say last

[00:17:40.520] and weeks

[00:17:45.669] and then

[00:17:45.679] last 7 days.

[00:17:53.510] I'm being really pedantic about naming

[00:17:53.520] these things, uh but I want to pass in

[00:17:55.880] some number of weeks uh historically

[00:17:58.280] into it so I have some idea of

[00:17:59.480] continuity because I will just agree

[00:18:01.800] that daily will have no continuity. It's

[00:18:04.000] only going to be a snapshot of each day

[00:18:05.560] at a time.

[00:18:07.600] Weekly, I'll have some form of

[00:18:09.040] continuity. I want some sort of bridge

[00:18:11.000] from week to week to week.

[00:18:13.040] So I'll include that.

[00:18:13.640] >> Okay, so basically while it's while it's

[00:18:15.480] building a new weekly summary, you want

[00:18:17.880] this created one to continue nicely from

[00:18:20.840] the last 3 weeks or whatever it is.

[00:18:23.000] Exactly.

[00:18:24.080] Okay.

[00:18:26.160] And then here I got I got this one for

[00:18:27.560] you.

[00:18:28.360] Oh nice, thank you.

[00:18:29.760] And then monthly is going to be the

[00:18:30.760] same.

[00:18:31.880] Now the amount of data that I pass in

[00:18:34.200] between monthly ends might be different

[00:18:36.120] on the weeks versus the months based on

[00:18:37.640] the amount of continuity I want. I might

[00:18:39.440] only pass in 1 week into the weekly

[00:18:41.159] summary cuz I only want like a single

[00:18:42.520] week of continuity

[00:18:44.360] in terms of information. I mostly want

[00:18:45.960] new information.

[00:18:47.280] And then in terms of monthly summary, I

[00:18:48.560] probably just want to pass in like two

[00:18:49.880] or three months so I can have a little

[00:18:52.720] If we have time, I would love to spend 5

[00:18:55.760] 10 minutes on like how would you

[00:18:57.880] evaluate and tune these things and kind

[00:19:00.200] of understand, "Okay, cool. When we do

[00:19:01.960] three, it actually works better than if

[00:19:03.400] we do two."

[00:19:05.000] That's a And we can do five evals for

[00:19:07.080] it, but like I it would be interesting

[00:19:08.320] to kind of see how that looks. I think

[00:19:10.120] that's mostly what I would end up doing.

[00:19:11.919] So now that we've done this

[00:19:13.640] I suspect um

[00:19:16.200] off the bat this is really all you need.

[00:19:19.120] All you need to do now is you just take

[00:19:20.800] this thing and you just run it. You run

[00:19:22.480] this on a cron every uh

[00:19:24.679] You just agree on when you run this.

[00:19:27.240] Whoops.

[00:19:29.080] Uh def

[00:19:31.560] cron

[00:19:32.800] uh cron job

[00:19:34.760] and this will just trigger every day at

[00:19:36.760] midnight.

[00:19:38.320] And what we'll do in our cron job is

[00:19:40.080] really really simple. What we'll do is

[00:19:42.080] we'll say

[00:19:43.240] load transcript.

[00:19:51.750] Oh, why am I in red font? Oh my god.

[00:19:51.760] I spelled cron wrong, I did.

[00:19:54.120] Uh

[00:19:54.800] transcript.

[00:19:59.670] And you'll notice what I'm going to do

[00:19:59.680] here. I'm not actually going to do a um

[00:20:03.600] I'm not going to run multiple cron jobs.

[00:20:05.000] I'm just going to have one cron job for

[00:20:06.280] the purpose of simplicity cuz I think

[00:20:07.880] simplicity is the most important thing

[00:20:09.880] when you're writing these pipelines,

[00:20:11.040] especially just starting out.

[00:20:13.000] When I load the transcript, I'm going to

[00:20:14.560] go ahead and then just say

[00:20:16.960] daily

[00:20:18.280] uh summary.

[00:20:24.150] equal transcript. uh

[00:20:24.160] get log today.

[00:20:27.440] get

[00:20:28.920] uh slice today.

[00:20:32.560] Uh

[00:20:33.720] and then create daily summary.

[00:20:40.150] It's very interesting coding on

[00:20:40.160] Excalidraw, I will say.

[00:20:42.280] Can I Can I just do an update here?

[00:20:44.880] Yeah.

[00:20:45.840] Um

[00:20:47.200] we need

[00:20:55.350] We don't need that for this daily

[00:20:55.360] summary one.

[00:20:56.840] Oh, you're just going to run these as

[00:20:57.880] separate cron jobs? No, no. So, what I'm

[00:21:00.120] going to say is like then I'm going to

[00:21:01.040] say like save daily.

[00:21:04.160] Okay.

[00:21:15.550] I'm going to try and use the same time

[00:21:15.560] slice. Yeah.

[00:21:20.510] Uh so, I'm going to save this into the

[00:21:20.520] database. Then I'm going to say

[00:21:23.360] um

[00:21:25.640] trans um load the loads last 7 days.

[00:21:35.470] according now.

[00:21:35.480] Um

[00:21:44.190] Excalidraw needs uh co-pilot auto coding

[00:21:44.200] is what I'm really learning.

[00:21:45.920] Uh I think TLDraw has that. We could

[00:21:48.520] Does it really? I think there's a It has

[00:21:51.000] a bunch of AI features. I don't know if

[00:21:52.240] it actually has like cursor style auto

[00:21:54.120] complete, but that would be wild.

[00:22:01.830] Uh

[00:22:01.840] load weeks.

[00:22:06.550] So, what I probably want to do is I want

[00:22:06.560] to load a week uh if if

[00:22:10.120] Okay.

[00:22:11.400] Now, let's just put in Let's just put in

[00:22:13.120] numbers that you think would be

[00:22:14.240] reasonable for now.

[00:22:16.040] Well, I'm going to do this. If now equal

[00:22:18.040] equal Sunday, I'm going to go do this.

[00:22:20.520] Um and then I'm going to load something

[00:22:22.560] if it's Sunday.

[00:22:24.840] Uh and then what I'm going to go do is

[00:22:26.640] I'm going to load weeks. I'm going to

[00:22:27.880] load like the last four um week I'm

[00:22:31.520] going to load I have the last 7 days.

[00:22:35.600] Oops, sorry.

[00:22:37.880] So, on every Sunday I'm going to compact

[00:22:39.400] and make a summary. I'm going to load 7

[00:22:41.440] days of worth

[00:22:42.679] uh

[00:22:43.760] week.

[00:22:45.679] the summary now.

[00:22:48.080] I see. So, you're never going to update

[00:22:49.760] a weekly summary in place like building

[00:22:52.000] it up. You're just going to create it

[00:22:53.480] once once you're at the end of the week.

[00:22:56.960] Exactly. Got you. Because I again, I'm

[00:22:59.760] trying to simplify my problem. I could

[00:23:02.640] do this all the time,

[00:23:04.720] but what I find is it's much easier for

[00:23:07.520] me to just break down the problem and

[00:23:09.320] compact it and just tell my users that I

[00:23:11.120] will never give them the context

[00:23:12.720] correctly. I will never do this for

[00:23:14.120] them. It just This is just a constraint

[00:23:16.200] on my system today.

[00:23:19.040] Okay.

[00:23:20.840] And then if you're just like if now.date

[00:23:23.360] less than seven

[00:23:25.760] Uh

[00:23:26.440] yes, exactly.

[00:23:28.040] Then you also do the monthly summary.

[00:23:31.160] Oh, wait. Sorry. I'm going to do this 1

[00:23:32.760] second.

[00:23:34.040] Uh I'm going to do I got to finish my

[00:23:35.480] weekly summary.

[00:23:36.880] Yeah, yeah.

[00:23:41.790] Um I've been writing too much go. I'm

[00:23:41.800] writing colon equals.

[00:23:44.240] I wasn't going to say anything.

[00:23:46.440] Um All right. Brian says don't update

[00:23:49.080] existing summaries. Yeah, I just find

[00:23:51.440] it's easier.

[00:23:52.640] Um and it's just going to be a very very

[00:23:54.200] hard problem and your system will behave

[00:23:56.600] more statically defined and that makes

[00:23:58.920] it easier to eval and not have to update

[00:24:00.600] it all the time.

[00:24:02.240] Because if if your prompts are changing

[00:24:04.120] every single day, your users will have

[00:24:06.360] the same

[00:24:07.960] Well, intuitively it feels like oh

[00:24:09.760] shoot, it's going to be more up-to-date,

[00:24:10.840] it's going to be more up-to-date. The

[00:24:11.640] thing that you're really losing out by

[00:24:13.040] doing that is you're actually adding

[00:24:14.520] churn to your users. Your users now

[00:24:16.880] can't build predictability in the

[00:24:18.360] pipeline anymore cuz it's changing all

[00:24:20.480] the time.

[00:24:28.070] Um create weekly summary, week summary.

[00:24:28.080] Um

[00:24:29.920] Can I jump in with a note here?

[00:24:31.640] Yeah. Yeah.

[00:24:33.120] It actually it won't even be more

[00:24:35.400] uh up-to-date for your users because you

[00:24:36.960] won't even use this week's transcripts

[00:24:39.160] until next week.

[00:24:40.880] Oh, yeah. Cuz you're just saving

[00:24:42.200] compute.

[00:24:43.800] Well, depends on

[00:24:45.640] depends on how you implement it and how

[00:24:47.080] you actually build the context window.

[00:24:53.110] E

[00:24:53.120] Okay. If now.date less than seven, what

[00:24:55.800] is this?

[00:24:56.800] >> I I I get I get what you're saying by

[00:24:58.200] above is is that like if you are only

[00:25:00.200] going to start using last week's summary

[00:25:02.920] starting next week, then then then yeah,

[00:25:05.280] that's true. Which I can't imagine a

[00:25:07.560] reason why I would put a partial week

[00:25:09.080] summary when I have all the day

[00:25:10.480] summaries that cover that same content.

[00:25:12.720] Oh, I see what Brian's saying. Yeah,

[00:25:13.920] yeah. I see what he's saying. Sorry, I

[00:25:15.560] misunderstood.

[00:25:17.280] Um and now we can do the same thing.

[00:25:19.320] Month are a little bit harder. So, I'm

[00:25:21.360] actually not going to consider this

[00:25:22.480] monthly summaries. I'm uh cuz I think

[00:25:24.600] this takes in the last 4 weeks. So,

[00:25:25.880] months are going to be a little bit

[00:25:26.800] weird cuz they kind of overlap both

[00:25:28.200] weeks and months. So,

[00:25:31.000] while we call this monthly summaries,

[00:25:33.360] I'm literally only going to do this

[00:25:35.320] >> to do a 4-week summary.

[00:25:37.560] literally week

[00:25:39.600] mod four

[00:25:42.000] equal zero. That's how I'm going to do

[00:25:43.960] it.

[00:25:44.880] Um because it's not going to be a

[00:25:47.200] monthly summary, it's going to be a

[00:25:48.280] weekly summary. That has semantic

[00:25:51.000] um

[00:25:52.679] uh consequences on this.

[00:25:55.520] But what I find is this is just easier

[00:25:57.320] for me to think about. It's unfortunate

[00:25:59.440] now I won't be able to say in December

[00:26:01.040] your kid did this,

[00:26:02.720] but I will find that this is worth it

[00:26:04.600] for me personally to deal with. The

[00:26:07.160] other alternative is I could say where I

[00:26:08.880] will only do this for the entire month,

[00:26:11.760] but um Thanks, Brian. we'll just deal

[00:26:14.120] with some overlap on this end where like

[00:26:15.880] the weekly's and the monthly's will just

[00:26:17.440] basically have some region.

[00:26:20.080] Oh, what the heck happened there? The

[00:26:21.679] weekly's and the monthly's, can you

[00:26:22.880] scroll up to the whiteboard area?

[00:26:25.600] If I choose to do monthly's, what will

[00:26:26.960] end up happening is that the weeks and

[00:26:28.120] the months will basically have some

[00:26:29.120] overlap region.

[00:26:30.840] Um and I can take that trade-off as well

[00:26:32.679] because like sometimes the weeks will

[00:26:34.040] fall uh not perfectly around 4 weeks or

[00:26:36.760] 5 weeks.

[00:26:37.200] >> So, you're talking about just like

[00:26:38.040] chunking this monthly into 4-week blocks

[00:26:41.040] rather than like calendar months which

[00:26:43.160] make that it it calendars when you try

[00:26:45.640] to you do calendars we'll get to this

[00:26:46.720] when we talk about time zones as well.

[00:26:48.000] Like when you try to you calendars like

[00:26:50.240] capital like C correctly, you get into

[00:26:53.400] all kinds of weird edge cases that are

[00:26:55.120] not a

[00:26:56.080] not really useful to talk about at this

[00:26:58.080] level that we're talking today.

[00:27:00.360] Exactly.

[00:27:06.150] So, I'm going to load um

[00:27:06.160] I'm going to load um

[00:27:10.590] What I'm going to do is I'm going to

[00:27:10.600] load

[00:27:11.800] uh now I'm going to load like So, this

[00:27:13.760] is monthly, right? Yeah. Yes. So, I'm

[00:27:16.360] going to load 4 weeks

[00:27:18.240] into it.

[00:27:19.960] create

[00:27:21.360] create

[00:27:22.840] monthly

[00:27:24.720] summary looks

[00:27:31.910] um And then this becomes week summary.

[00:27:31.920] uh

[00:27:32.720] load

[00:27:32.960] >> So, you just you just created it.

[00:27:35.600] Oh, I see.

[00:27:36.880] months um and I'll I've done like

[00:27:40.280] 3 months worth of data.

[00:27:42.000] Um

[00:27:43.000] and

[00:27:44.400] months

[00:27:49.310] Okay. So, we're grabbing the last 4

[00:27:49.320] weeks. We're grabbing the last 3 months

[00:27:51.080] and then we're creating the summary

[00:27:52.240] saying here's the last 3 months, here's

[00:27:54.160] the last 4 weeks.

[00:27:56.480] Create the new monthly summary.

[00:27:58.520] Exactly. So, I pass in history and then

[00:28:00.320] I pass in the current weeks. And it

[00:28:01.760] creates the monthly summary.

[00:28:04.560] And now what I've done is I can save the

[00:28:07.440] monthly summary.

[00:28:09.080] Um someone asked a really interesting

[00:28:10.320] question. Like why don't I do Why don't

[00:28:12.600] I just do the dumb thing and just call

[00:28:15.880] use like uh different cron jobs?

[00:28:18.480] Well, the reason I'm not doing that is

[00:28:20.160] actually because of the complexity of

[00:28:21.400] how this runs. If I do this, then I I'm

[00:28:23.760] going to run into weird race conditions

[00:28:25.200] of when this cron job runs and if this

[00:28:27.520] fails to run for some reason, then I

[00:28:29.080] don't want to create the weekly summary

[00:28:30.240] because I don't have the last day

[00:28:31.480] because I'm doing a waterfall approach.

[00:28:33.760] I I need to almost have some dependency

[00:28:35.560] guarantees that this is running.

[00:28:37.880] So, it's easy that I could go implement

[00:28:40.000] this in like a cron job where like once

[00:28:42.080] this triggers this trig the completion

[00:28:43.880] of this job triggers another cron job,

[00:28:46.280] but because we've already decided that

[00:28:47.960] we're doing the waterfall approach, we

[00:28:49.480] have a dependency and it's easier for me

[00:28:50.840] to write the code like this.

[00:28:55.470] I like it.

[00:28:55.480] Yeah, you could do like oh if

[00:28:56.800] yesterday's summary doesn't exist, then

[00:28:58.640] like bail and retry in an hour or

[00:29:00.560] something like that, but that's not the

[00:29:01.880] fun part of this problem. Yeah, exactly.

[00:29:04.080] And like I'm going to ship faster if I

[00:29:06.159] have one cron job to maintain and have

[00:29:08.240] SLAs on than I have like three.

[00:29:10.280] Yep.

[00:29:12.280] Cool. Um questions so far?

[00:29:17.590] I actually really like that that kind of

[00:29:17.600] like echoes a lot of the stuff we talk

[00:29:19.000] about, which is like don't be afraid to

[00:29:21.080] have a little bit more complexity in

[00:29:22.640] your code versus like offloading that to

[00:29:24.960] a job orchestrator or scheduler or

[00:29:26.880] dependency manager because at the end of

[00:29:29.280] the day like until your problem gets

[00:29:31.320] really big and hairy, you're going to be

[00:29:32.960] glad that you kind of just owned the

[00:29:34.919] logical complexity yourself and didn't

[00:29:37.240] have to like

[00:29:38.600] evolve it kind of uh in concert with

[00:29:41.840] what a framework or an orchestrator

[00:29:43.280] allows you to do.

[00:29:45.080] Got have from John.

[00:29:46.679] Yeah, I was Yeah, I'm I might be just

[00:29:49.200] not seeing this part. When you create

[00:29:51.120] the weekly summary, a new weekly

[00:29:52.720] summary, why are we loading the prior

[00:29:54.520] weekly summaries?

[00:29:56.240] Ah, so the only difference between the

[00:29:58.600] weekly summaries and the daily summaries

[00:30:00.480] is I'm going to agree that daily

[00:30:02.400] summaries are only going to do exact

[00:30:05.200] 24-hour chunks and have no real

[00:30:07.320] continuity between them.

[00:30:10.160] But what I will say is I want my weekly

[00:30:13.120] summaries to have some sort of idea of

[00:30:14.600] like notice what happened in the weekly

[00:30:16.200] summary, generally going poorly and not

[00:30:18.320] going poorly, generally going well,

[00:30:20.240] oops, versus going poorly. In order to

[00:30:23.400] determine

[00:30:24.600] if things are going well or poorly,

[00:30:26.840] I kind of have to have some idea of what

[00:30:28.480] happened last week.

[00:30:30.200] I can't have direction if To create that

[00:30:33.040] yeah, the continuity between the weeks.

[00:30:35.000] Got it. Okay. Exactly, right? So and in

[00:30:37.680] the daily summaries, I don't have any

[00:30:39.600] form of continuity. I

[00:30:40.760] And you notice that I did that in my

[00:30:42.160] design doc upstairs above. If you scroll

[00:30:44.840] up, that's really fast. Sorry. Um, I'm

[00:30:47.640] just going to I'm going to I'm going to

[00:30:48.520] draw this for us here real quick. So the

[00:30:50.680] daily summary plus the last 3 weeks.

[00:30:54.920] Exactly. Or like last N weeks.

[00:30:57.640] Produces the new weekly. Exactly.

[00:31:01.000] And then you have yeah, your new new

[00:31:02.560] weekly. You could technically create

[00:31:04.160] your daily summary with context about

[00:31:05.840] yesterday to have continuity, but

[00:31:08.840] But I'm I'm explicitly making a choice

[00:31:11.160] not to do that.

[00:31:13.320] Okay. And that's that really comes if

[00:31:15.600] you scroll up.

[00:31:17.560] Hold on.

[00:31:18.120] >> And the place where this the place where

[00:31:20.240] this comes from

[00:31:24.870] Yeah, that's a good idea. The place

[00:31:24.880] where this comes from is just this

[00:31:26.040] constraint that says generally going

[00:31:28.080] well versus poorly. That's a very

[00:31:30.320] different status than just assignment

[00:31:33.920] and completion, assignment completion,

[00:31:35.760] assignment completion.

[00:31:41.190] All right. Does that answer your

[00:31:41.200] question?

[00:31:42.120] Yeah, yeah. So what I'm hearing is you

[00:31:43.720] you could you could use the same

[00:31:45.040] methodology also. Just depends on the

[00:31:47.080] exact use case. Yeah, that makes sense.

[00:31:48.840] Yes. It's a choice that I made. And I I

[00:31:50.280] think part of the reason I made that

[00:31:51.480] choice to make that distinction is to

[00:31:53.040] have this conversation.

[00:31:54.880] Um,

[00:31:56.120] I see. Yeah, and it's like you could try

[00:31:57.920] again and and the real answer is like

[00:31:59.600] there is no algorithm, there is no

[00:32:01.160] correct way to do this. It's like, okay,

[00:32:03.080] which one solves your problem better?

[00:32:04.800] And like if you have reasonable ways to

[00:32:07.000] evaluate that, whether it's just looking

[00:32:08.560] at the outputs and deciding or if you

[00:32:11.120] actually have like really really

[00:32:12.280] rigorous evals, but it's like when you

[00:32:14.240] chunk the problem up into these really

[00:32:15.600] small pieces, too, you can inspect all

[00:32:18.320] of your data through the pipeline in a

[00:32:20.360] really kind of like isolated way to make

[00:32:22.840] those really granular decision of like

[00:32:24.679] if I do this versus this. Obviously, you

[00:32:26.200] want to look at the entire output of the

[00:32:28.640] entire pipeline and the effect, but you

[00:32:30.120] can you can make more kind of focused

[00:32:32.040] things on like, okay, what is the N

[00:32:34.240] here? How many weeks do we load in? And

[00:32:36.920] like just vibe eval what the results

[00:32:39.200] look like.

[00:32:43.190] Yeah.

[00:32:43.200] So the next thing I want to talk about

[00:32:44.840] building

[00:32:45.960] contacts. If anyone has more questions,

[00:32:47.560] please just

[00:32:49.240] raise your hands.

[00:32:50.679] Uh, and then come on.

[00:32:52.240] Um, let's talk about building the

[00:32:53.400] contacts. Now, one of the most annoying

[00:32:55.240] things that you'll see about this

[00:32:56.240] process is the hardest thing to do is

[00:32:58.840] actually to talk about how we access

[00:33:01.280] this data. It's going to be way harder

[00:33:02.920] than you think because it turns out one

[00:33:04.520] of the hardest challenges is time. Time

[00:33:06.920] is a pain in the ass to deal with.

[00:33:09.600] And when we go to deal with it here,

[00:33:12.120] we when we get the when time, think

[00:33:14.000] about the logic that we have to do here.

[00:33:15.560] We first have to like snap this to like

[00:33:17.920] to today.

[00:33:19.800] So first I'll snap this to two today and

[00:33:22.320] I'll do when dot

[00:33:23.880] since 12:00 a.m.

[00:33:25.960] Uh, and I'm writing very pseudo code so

[00:33:28.000] we'll get an idea. Then we'll do like to

[00:33:29.760] Monday or I think we snapshot on Sunday.

[00:33:32.280] So like Sunday to Sunday not include um,

[00:33:36.240] Sun to Sunday equal when dot since

[00:33:41.080] Sunday

[00:33:42.560] 12:00 a.m.

[00:33:48.230] Then I just have this to that's that

[00:33:48.240] gets me this week. Then I have to go

[00:33:49.880] back to a month as well. To month equals

[00:33:53.520] when

[00:33:55.280] uh,

[00:33:56.320] to Sunday

[00:33:58.560] Oops, to today.

[00:34:01.440] To Sunday dot since

[00:34:04.400] 4 weeks.

[00:34:07.080] Like uh, since

[00:34:09.600] rounded

[00:34:12.200] to Sunday

[00:34:14.520] dot week

[00:34:17.159] my

[00:34:18.520] mod 4

[00:34:20.000] And I have to go back and get to the

[00:34:21.800] most recent month of this. And then what

[00:34:24.399] I actually have to do is I have to say

[00:34:25.800] now

[00:34:27.679] from today

[00:34:30.200] I need to actually load the raw

[00:34:31.440] transcript.

[00:34:37.630] Then I need to load the daily summary

[00:34:37.640] from from Sunday.

[00:34:47.909] Uh,

[00:34:47.919] daily summaries.

[00:34:50.720] Then I need to go ahead and

[00:34:53.640] load the weekly summaries and that means

[00:34:55.359] I have to go from today

[00:34:57.359] to and my my parameters might be flipped

[00:35:00.880] to month.

[00:35:07.550] And then I need to load the

[00:35:07.560] monthly summaries from to month to like

[00:35:10.560] let's say like I I support like

[00:35:12.760] all. So I'll get all the monthly

[00:35:14.480] summaries.

[00:35:20.230] And this and then I need to somehow say

[00:35:20.240] like now I need to like serialize

[00:35:22.920] uh,

[00:35:24.359] all of these.

[00:35:45.750] And that is what it would take to

[00:35:45.760] actually build the RM.

[00:35:59.270] I see a couple of nods. Um,

[00:35:59.280] I think I see a question there. How do

[00:36:01.480] you decide how many daily summaries to

[00:36:02.800] have in a batch? Do you get 30? Do you

[00:36:04.120] get 20?

[00:36:05.480] Um,

[00:36:07.000] we can do string, we can do data model,

[00:36:08.520] doesn't really matter how we put it in.

[00:36:09.880] But like there's some format here that

[00:36:11.520] we want to go to.

[00:36:13.320] Um,

[00:36:13.920] >> Yeah. And I guess you're kind of taking

[00:36:15.440] the order that you computed it in and

[00:36:17.480] then you're reversing it when you

[00:36:18.680] serialize it. You're putting the monthly

[00:36:19.960] summaries at the top. It really depends.

[00:36:22.359] If your if your if your model prefers

[00:36:25.359] tokens at the top a little bit more than

[00:36:27.320] does at the bottom, then yeah, you would

[00:36:29.720] then you would you would put monthly

[00:36:31.040] tokens at the

[00:36:33.240] Uh, you basically have to flip or not

[00:36:34.880] flip based on what your model prefers.

[00:36:36.600] Most models bias towards the most recent

[00:36:39.000] tokens generated.

[00:36:40.760] So you probably want to put now closer

[00:36:43.000] to there.

[00:36:44.200] But if you have a parent asking a

[00:36:45.840] question about how is my child been

[00:36:48.760] doing over time,

[00:36:50.760] then you probably might actually benefit

[00:36:52.280] from actually flipping the order based

[00:36:54.120] on that question. Okay, so you could

[00:36:56.240] actually classify the input question and

[00:36:58.960] then use that to determine how you build

[00:37:00.720] your context window. Exactly, because

[00:37:03.000] that's more context engineering. We can

[00:37:04.400] take

[00:37:04.600] >> Or which of this data you pull in. And

[00:37:06.520] like good luck getting like a

[00:37:09.120] off-the-shelf thing to do that without a

[00:37:10.680] lot a lot of configuration and

[00:37:12.160] customization. Exactly. And I think the

[00:37:14.520] best analogy here is just like front

[00:37:16.080] end. Like obviously, we can all build

[00:37:17.680] buttons and forms, but it turns out to

[00:37:20.240] really build a good front end, you got

[00:37:21.520] to just write the form

[00:37:23.160] on your own. You got to write your own

[00:37:24.280] button on your own. You got to make it

[00:37:25.440] work the way you want it to work.

[00:37:27.480] But it's the same with context. You can

[00:37:30.760] write decent context, but to have really

[00:37:32.720] good context that actually works, what

[00:37:34.040] you need to do is you just got to build

[00:37:36.080] the context window based on the problem

[00:37:37.440] that you're asking.

[00:37:43.950] Um,

[00:37:43.960] doesn't this over index on recent

[00:37:45.840] details? Josh asked a really good

[00:37:47.480] question. Like we get why we're doing

[00:37:49.280] this, but one of the most important

[00:37:51.359] things to note here is Josh, the problem

[00:37:53.120] definition that we have here is really

[00:37:54.680] to help a student and a parent manage

[00:37:56.720] the student's learning over time.

[00:37:59.040] In that scenario, we're not really

[00:38:01.760] biasing towards more recent information.

[00:38:04.520] What we're really saying is like what

[00:38:06.280] information matters at any given time is

[00:38:09.359] higher chunks of information. We don't

[00:38:11.600] have a way to take today's conversation

[00:38:13.960] and make it higher chunk.

[00:38:16.400] Like it it's not ready yet to be

[00:38:18.359] compressed in that way. So what we find

[00:38:21.160] is it's easier to frame this problem in

[00:38:23.480] that way where we can answer a question

[00:38:25.359] that is um,

[00:38:31.150] like what would I be doing otherwise?

[00:38:31.160] What what I would be doing otherwise is

[00:38:32.920] representing the last 3 days of a

[00:38:35.080] monthly summary.

[00:38:36.760] But there's just not enough meat in

[00:38:38.200] there to have that in there. So now what

[00:38:39.720] you'll really be doing is you'll have a

[00:38:41.000] super super biased towards

[00:38:43.680] uh, older months, which is going to lose

[00:38:46.240] a lot of the most recent things that

[00:38:47.600] people do and people are learning.

[00:38:49.640] What I really want to know is like yes,

[00:38:51.320] I learned something a year ago,

[00:38:53.359] but I don't really care. Like when I

[00:38:55.160] first learned how to code, pointers were

[00:38:56.680] an interesting factor and I thought it

[00:38:57.800] was a really cool thing that I learned

[00:38:58.960] how to have pointers in there.

[00:39:01.840] I don't need anything to ever really

[00:39:03.760] talk about that the fact that I know

[00:39:05.400] pointers anymore. Like that's just done.

[00:39:07.600] We just move on from that.

[00:39:09.359] It's more interesting to talk about a

[00:39:11.320] console like DRM as a more recent thing

[00:39:13.320] that I learned or how to talk about

[00:39:15.040] context engineering or the fact that we

[00:39:16.359] can dynamically build this context based

[00:39:19.000] on the question that people ask.

[00:39:20.680] So while that does over index, I think

[00:39:22.400] it also achieves the user goal a lot

[00:39:24.720] better as well.

[00:39:31.310] Uh, does that answer the question, Josh?

[00:39:31.320] Context is looking like a memory

[00:39:32.960] allocation. We're getting it. Yeah,

[00:39:35.520] that's literally what it is.

[00:39:37.600] Hey Vibe Hub. Um, yeah, thanks for the

[00:39:40.120] detail. I I guess um,

[00:39:42.960] my uh thought was that the one, you

[00:39:44.800] know, I if I recall the last week like

[00:39:47.120] um

[00:39:48.160] Orin was um specifically doing the uh

[00:39:50.400] this reduction job, right? So, like it's

[00:39:53.320] lowering the resolution. So,

[00:39:55.600] uh you know, if we have like a lot of

[00:39:57.120] more recent chunks, it might be like I

[00:39:58.920] just too much in the wee detail versus

[00:40:01.320] like older, you know, it'll be like a

[00:40:03.040] very high level. So, that's the

[00:40:04.640] resolution difference. And uh I was just

[00:40:07.120] kind of wondering how do we resolve that

[00:40:09.160] resolution difference? Well, there's

[00:40:11.400] something that we can really do over

[00:40:12.480] here. This thing that I Can you zoom in

[00:40:14.440] into what I said? That's the build

[00:40:15.920] context.

[00:40:16.400] >> Which one? The build context function.

[00:40:18.720] Yeah. Yeah, you're right. There might be

[00:40:21.080] really, really resolution difference. We

[00:40:22.840] could even do things though. If raw

[00:40:42.310] I can just write another pipeline that

[00:40:42.320] on the fly will compress raw.

[00:40:45.080] So, if I find that and this can actually

[00:40:47.080] do like oh, this will do the same DRM

[00:40:49.160] thing but now do it by hours or like

[00:40:50.840] 6-hour chunks.

[00:40:53.160] So, it'll take my raw transcript and

[00:40:54.400] break it down to like two 6-hour chunks

[00:40:56.680] plus the most recent 2 hours.

[00:40:59.240] If you ever use Cloud Code, this is what

[00:41:00.920] the compact function does. Exactly. Got

[00:41:04.200] you.

[00:41:05.160] Yeah, I think that my takeaway here is

[00:41:07.200] that the uh it's really use case

[00:41:09.000] dependent. You really have to kind of

[00:41:11.800] look into this. Yeah.

[00:41:13.760] And more importantly, because a lot of

[00:41:16.000] people are building chat-based

[00:41:17.080] applications,

[00:41:18.880] really think hard about how you write

[00:41:21.120] these time queries. You got to

[00:41:23.200] standardize them and you got to do small

[00:41:24.880] things to make it work. Like this code

[00:41:26.720] I'm writing looks clean. This would be a

[00:41:29.680] cluster in Python or TypeScript or

[00:41:32.520] something else. So, I would just write a

[00:41:34.480] quick little helper around a time object

[00:41:36.400] to give me these faster queries.

[00:41:39.040] Or like use some data framework that

[00:41:40.320] allows me to have that.

[00:41:42.320] Because it's going to be really, really

[00:41:43.720] annoying and my code will basically

[00:41:45.200] become unreadable really fast.

[00:41:52.310] I'll pause unless there's any more

[00:41:52.320] questions and go to coding soon.

[00:41:54.560] Yeah, I I think the one thing that's

[00:41:55.640] missing here is like the the What do the

[00:41:57.960] actual prompts look like and like how

[00:42:00.160] might you actually like build each of

[00:42:02.000] these like um

[00:42:03.880] The things we haven't done is like

[00:42:05.480] implement the internals of these

[00:42:06.800] functions, right? We've done the layout,

[00:42:08.200] but I think the last piece is like okay,

[00:42:09.560] how would you actually take this input,

[00:42:11.520] some example data, and and stuff it

[00:42:13.160] through?

[00:42:15.240] Uh yes, exactly. Um questions so far

[00:42:17.520] though from anyone else before we go

[00:42:18.880] into that.

[00:42:19.920] Yep.

[00:42:25.670] Uh

[00:42:25.680] yes, so someone asked a question of uh

[00:42:28.920] What if there are specific chunks of

[00:42:30.400] information that I want to recall?

[00:42:32.360] This

[00:42:34.440] This sort of thing, in my opinion, when

[00:42:36.360] you think about recall,

[00:42:38.200] is really just a matter of like uh you

[00:42:40.400] build context

[00:42:41.960] and you serialize this. You could easily

[00:42:44.320] add in another parameter that's called

[00:42:45.720] like query, like user query, and then

[00:42:48.680] apply like some sort of like search or

[00:42:50.640] rag on top of this to filter this down

[00:42:53.280] further, to filter the serialized

[00:42:54.960] portion down.

[00:42:56.600] I actually

[00:42:58.360] I'm going to come in and say that like

[00:43:01.360] the way I would think about that is like

[00:43:02.880] again, you have your context window and

[00:43:04.280] it has all these parts

[00:43:06.240] and you have

[00:43:09.240] Sorry. Um

[00:43:11.040] You have like your memory section.

[00:43:14.080] But I would be I would be shocked if we

[00:43:16.840] don't also have tools and rag in that

[00:43:19.600] same context window. It's all part of

[00:43:21.080] the same thing.

[00:43:22.680] Sorry, I'm trying to just write this.

[00:43:24.360] So, you have your memory.

[00:43:30.150] And then if you retrieved data,

[00:43:30.160] um if you included tools for agentic rag

[00:43:32.280] or something like that, you could do

[00:43:33.520] that. Or if you deterministically

[00:43:35.640] retrieved data,

[00:43:37.320] um that also becomes part of your

[00:43:39.560] context, but it's just a different part

[00:43:41.720] of the context window. Like you may want

[00:43:44.080] to give it hey, here's very specific

[00:43:45.960] daily summaries from when this stuff was

[00:43:47.880] discussed or here's even very specific

[00:43:49.640] memories or like messages where this

[00:43:51.640] came up, but you might still want to

[00:43:54.040] ground it in the context of everything

[00:43:56.160] about this student and their family and

[00:43:58.240] what's been going on.

[00:44:00.000] And that's again, your choice as an

[00:44:01.960] engineer of what tradeoffs you want to

[00:44:03.400] make. You can do that or you can pass in

[00:44:05.520] just the most relevant places into it if

[00:44:07.440] you feel like you have a really good

[00:44:10.080] sus on what is relevant.

[00:44:12.400] Yeah, so the question has context that

[00:44:14.120] helps you build the memory. You may have

[00:44:16.120] any number of pipeliney processes here

[00:44:18.280] where you do a bunch of filtering and

[00:44:19.560] reranking and searching and all this

[00:44:20.840] stuff and that builds that and then you

[00:44:22.960] put the question in at the end or at the

[00:44:24.480] beginning or whatever it is. Or like a

[00:44:26.040] reformulated version of the question and

[00:44:28.520] And the whole point of this whole thing

[00:44:29.760] that you're building is basically a

[00:44:31.320] program. You're writing a program to

[00:44:33.359] build context.

[00:44:35.520] And uh S Shaw asked this question like

[00:44:37.920] does this make rag the heap? Uh rag is

[00:44:40.600] not the heap. The heap is a thing that

[00:44:42.480] allocates memory. The thing that's

[00:44:44.400] allocating memory is your program that

[00:44:45.720] builds the prompt.

[00:44:47.240] The You're building the You're building

[00:44:48.840] malloc. Exactly. You're basically

[00:44:50.680] building malloc. That's what context

[00:44:51.960] engineering is. You're building malloc

[00:44:53.440] along the way. But it's really hard

[00:44:55.800] because there's no And And just like

[00:44:57.560] with malloc as well, there's no

[00:44:59.080] optimization function that is globally

[00:45:00.920] great.

[00:45:02.640] You just have to build something really,

[00:45:04.960] really simple.

[00:45:06.400] And often for these complicated systems,

[00:45:09.040] simplicity is key

[00:45:11.240] to making it work in the beginning and

[00:45:12.920] then as you understand your use case

[00:45:14.520] better, you can do better.

[00:45:16.440] And I love this ex- Sorry, go ahead.

[00:45:18.560] Finish your thought. I was saying before

[00:45:20.359] you understand your use case, don't

[00:45:21.640] optimize. Literally just write the dumb

[00:45:23.240] thing.

[00:45:24.600] And I love this example so much because

[00:45:27.080] there's a very strong analog between

[00:45:30.480] building every token of context yourself

[00:45:33.000] and using a framework to build it for

[00:45:35.560] you

[00:45:36.440] and using a language like C and using a

[00:45:39.359] language like Python. Python will

[00:45:41.280] probably solve your problems faster and

[00:45:43.000] get you something workable, but if you

[00:45:45.040] bump up against a performance boundary,

[00:45:47.359] you're going to have to start thinking

[00:45:48.840] at the level of C and the memory

[00:45:50.640] registers and how things are allocated

[00:45:52.320] and L1, L2 cache and all this kind of

[00:45:54.440] stuff.

[00:45:55.480] Um and it's like there is

[00:45:59.000] I mean, the with AI coding tools, you

[00:46:01.560] could just build this from scratch, but

[00:46:02.960] you can always start with Python for

[00:46:04.320] prototyping stuff. But then when you

[00:46:05.800] need to make it good and in in AI,

[00:46:07.440] performance is not just about AI is

[00:46:09.520] different because performance in AI is

[00:46:11.040] not just about speed and like resource

[00:46:13.880] usage. Bad performance will hinder your

[00:46:17.080] accuracy and make your app bad and like

[00:46:19.480] unusable and feel super sloppy.

[00:46:22.120] And so,

[00:46:23.440] if you if you if you if you've ever gone

[00:46:26.400] from building in a high-level language

[00:46:28.280] to switching to a low-level language to

[00:46:29.840] be able to have more control and more

[00:46:31.720] visibility into what's happening, this

[00:46:33.280] is that same concept.

[00:46:38.630] Um

[00:46:38.640] I have a quick question.

[00:46:40.080] Oh god. Two quick question. Um

[00:46:42.160] sorry, I joined late. So, apologies if

[00:46:43.920] if this has already gone over, but um

[00:46:45.960] when you're adding memory and stuff,

[00:46:47.680] like

[00:46:48.960] do you

[00:46:50.720] would would you suggest that it should

[00:46:52.320] be like a reasoning model or do you

[00:46:53.880] think that the kind of non-reasoning

[00:46:55.440] models are fine enough that that they

[00:46:57.480] can deal with like the big context

[00:46:58.640] windows and stuff like that? That's a

[00:47:00.840] totally independent question. We did a

[00:47:02.440] talk very, very early on about like

[00:47:04.160] reasoning models versus reasoning

[00:47:05.280] prompts. But in

[00:47:06.960] general, what I would say is like I

[00:47:08.600] always bias and I think that actually

[00:47:10.240] does do. We just bias towards like

[00:47:11.480] tossing a bigger model at it. Like if

[00:47:12.840] you have a bigger context window, on

[00:47:14.240] average, toss a bigger model.

[00:47:16.720] If the model is a smaller model, see if

[00:47:18.960] it vibes right and if it vibes right,

[00:47:20.960] it's fine.

[00:47:22.400] That's what I would say. And just really

[00:47:23.600] understand your users' behaviors better.

[00:47:27.040] And when you go do that, what you're

[00:47:28.480] able to do is like just collect data cuz

[00:47:30.680] you won't The test cases that you write

[00:47:32.840] will be bad.

[00:47:34.480] It's really, really hard to get good

[00:47:36.200] test data without using real world

[00:47:39.080] So, like don't stress too hard about it.

[00:47:41.040] Yeah. If something out there makes some

[00:47:43.280] decision, doesn't matter what it is,

[00:47:45.000] collect real world data and make sure

[00:47:46.520] you build into the expectation of your

[00:47:48.040] application to your users, you are

[00:47:49.840] improving it over time.

[00:47:51.680] That is the most important thing to nail

[00:47:53.000] down after that. But if you really care

[00:47:54.720] about accuracy on day one,

[00:47:57.040] hit the biggest model you can.

[00:47:59.160] Makes sense.

[00:48:05.470] Um cool. Um let's talk about the Let's

[00:48:05.480] talk about actually writing some of this

[00:48:06.560] code now.

[00:48:07.600] Um now, one of the first things we did

[00:48:09.280] when we started talking about these

[00:48:10.160] chapters, we realized that test data is

[00:48:11.680] really hard for this. We could get some

[00:48:13.480] test data,

[00:48:14.840] but

[00:48:16.080] as you'll often notice, as I just said,

[00:48:18.200] test data is one of the hardest parts of

[00:48:19.680] this business.

[00:48:21.200] So, Dexter did something really, really

[00:48:22.840] nice. Um

[00:48:24.480] Do you want to pull it up? Have you

[00:48:25.800] pushed yet?

[00:48:27.120] Uh I pushed it, but then I decided that

[00:48:30.120] our test data is not very good.

[00:48:32.240] Uh so, I deleted it, but I could push it

[00:48:34.000] again. Um I was thinking probably like

[00:48:36.280] for this problem, it makes sense to just

[00:48:38.520] have Cursor generate 10 10 10 messages

[00:48:41.080] about a tutoring situation.

[00:48:43.120] We can do that.

[00:48:44.320] Show me your test data. I think the one

[00:48:45.400] you had was actually pretty interesting.

[00:48:48.160] If you have it.

[00:48:48.760] >> Okay. Uh so, I have a bunch of like

[00:48:51.080] traces from my agent. Um some of them

[00:48:54.400] are uh

[00:48:56.160] export YAML log equals off. I'm just

[00:48:59.359] redacting PII from them right now.

[00:49:02.840] Uh because they're from our agent that

[00:49:04.600] runs over email. Um What Why don't we do

[00:49:07.280] this, Dexter? Why don't I cut the

[00:49:09.400] recording and I'll make sure that we

[00:49:10.920] don't record this part of it in case

[00:49:12.359] there is something in here. And I think

[00:49:13.880] that that way like people live on the

[00:49:15.359] call won't get to see it and everyone

[00:49:16.600] else like uh I apologize.

[00:49:19.520] Uh okay, we can do that, but then I'm

[00:49:21.560] not going to push it up. Yeah, that's

[00:49:23.400] okay. Let's do that. Yeah, I have a

[00:49:24.920] question. I have a question. Could you

[00:49:26.240] guys cut it after if it's in there? Like

[00:49:28.040] just chop that end of the recording.

[00:49:29.880] That way if it's not in there, we do

[00:49:30.880] have the recording.

[00:49:32.760] You know what I mean?

[00:49:34.040] Oh, yeah, yeah. I'm not going to stop

[00:49:35.120] the recording. I'll record the recording

[00:49:36.800] and then I'll slice it around

[00:49:37.920] afterwards. Yeah, if there's PII, okay,

[00:49:39.640] cool.

[00:49:40.440] Yes. Um cool. I think that's fine. And

[00:49:45.880] so, basically what I did was I pulled a

[00:49:47.480] bunch of threads from our assistant. Um

[00:49:50.400] if nobody has seen this before, I will

[00:49:51.840] pull it up um quickly. Let me just jump

[00:49:54.280] to my email real quick.

[00:49:56.200] Um Yeah, show them the assistant that

[00:49:58.640] you have.

[00:49:59.840] Yeah, exactly. Um

[00:50:01.880] So, this is a agent that we built that

[00:50:04.320] runs over email. So, if you have an

[00:50:06.160] email in your inbox that you have to do

[00:50:07.320] something about, you can forward it to

[00:50:10.040] this agent, which is like, okay, there

[00:50:11.840] was a Sentry error, we got a 500, and my

[00:50:14.200] my evaluation is like we should just

[00:50:15.720] throw a 404 error instead.

[00:50:17.800] The agent eventually comes back to me

[00:50:19.920] and like with a proposed ticket to

[00:50:22.120] create. Um and I can approve it, and

[00:50:25.280] then it will say, okay, I made the

[00:50:26.320] ticket. Um and I'm not going to open

[00:50:28.000] this, but like this is kind of the idea.

[00:50:29.520] So, we have conversation traces from

[00:50:31.280] these things. And so, what we want to do

[00:50:33.400] is kind of build memory, cuz these

[00:50:34.440] things working all day, it has tons of

[00:50:35.840] different conversations, and right now

[00:50:37.240] each of these is its own isolated

[00:50:38.920] context window.

[00:50:40.480] Um so, while the redaction is running, I

[00:50:42.280] can pick one. Yeah, so this is a thread

[00:50:44.400] I had with GCP. So, I forward this to

[00:50:47.040] the thing and said, "Hey, can you

[00:50:48.600] include this in a comment on the GCP?"

[00:50:50.720] We had like a issue in linear about

[00:50:52.520] like, "Hey, we didn't get our GCP

[00:50:53.640] credits. We got to go get our GCP

[00:50:55.040] credits." Um which by the way, the team

[00:50:57.240] at Google was awesome. If we do end up

[00:50:59.040] sending showing this part of this, uh

[00:51:00.880] they were super fast and super helpful

[00:51:02.480] in getting this done.

[00:51:04.040] Um

[00:51:05.480] But uh you can see kind of here's the

[00:51:07.240] initial email. Here's a bunch of tool

[00:51:09.320] calls that it made.

[00:51:11.080] Um including like listing out all the

[00:51:13.160] projects, um listing out all the labels

[00:51:15.640] in our project, um searching for related

[00:51:18.480] issues.

[00:51:19.720] And then it came back with, okay, I'd

[00:51:21.240] like to add a comment. And so, it's

[00:51:23.160] like, cool, I had this email forwarded

[00:51:24.480] from Dexter on June 25th.

[00:51:26.520] Um and then here's actually a

[00:51:27.920] continuation of the same thread where uh

[00:51:31.520] it was successful, and then it said,

[00:51:33.080] "I'm done for now." And um I can go find

[00:51:35.600] this thread as well, but here is kind of

[00:51:36.920] the final message from the agent that

[00:51:38.440] came over email. Let me see if I

[00:51:40.040] actually pull this one up.

[00:51:47.870] Yeah, for those of you that haven't

[00:51:47.880] seen, by the way, Dexter is like a beast

[00:51:49.840] at making all these agents actually do

[00:51:51.920] things and writing really, really quick

[00:51:53.640] ones that are production grade.

[00:51:56.560] Oh my god, superhuman, what the are

[00:51:58.080] you doing? And it's it's it's one of the

[00:52:00.440] first things that I noted about Dexter

[00:52:01.800] as I got to know him is just like

[00:52:04.040] it just he just writes a bunch of stuff,

[00:52:06.040] and I think that's where his experience

[00:52:07.840] comes from.

[00:52:09.320] Uh which is just like

[00:52:12.160] man-hours

[00:52:13.880] on writing different kinds of agents

[00:52:16.200] that do different kinds of things, that

[00:52:17.920] have different kind of interaction

[00:52:19.040] patterns, some that talk over email,

[00:52:21.000] some that talk over Slack, some that

[00:52:22.400] talk over UI.

[00:52:23.840] And they're all totally different

[00:52:25.280] concepts.

[00:52:26.600] Yeah, so here's the one that we built.

[00:52:28.120] This is just an experiment, but yeah, so

[00:52:29.480] I like this added to the thing, and it

[00:52:30.880] pinged everyone on my team who's on that

[00:52:32.280] issue, who is helping to figure out our

[00:52:34.040] GCP billing.

[00:52:35.440] Yeah, so Um so, here's the final

[00:52:37.040] message.

[00:52:39.520] Yes.

[00:52:39.840] >> Um cool.

[00:52:41.880] Uh let's see. Okay, cool. So, I'm going

[00:52:45.160] to I think we're processing these now.

[00:52:46.920] So, these are the the same versions. I

[00:52:48.440] used a BAML prompt to basically just

[00:52:49.960] like chunk these up, turn it into I'll

[00:52:52.440] commit that code, too, but basically

[00:52:53.560] like turn it into 1,000 character

[00:52:54.840] chunks, redact all PII. Uh if there's

[00:52:57.480] PII on a chunk boundary, it's probably

[00:52:59.280] not going to work, but I'm just going to

[00:53:01.000] like cross my fingers and hope that that

[00:53:03.080] didn't happen.

[00:53:04.440] Um but these are the same threads with

[00:53:05.880] all the PII redacted. Um

[00:53:08.400] it's still running, but I'm just going

[00:53:10.160] to commit what we have right now, push

[00:53:12.120] that up so that Vibhav can mess with it.

[00:53:14.440] Oh, so

[00:53:14.800] >> look good? Is this going to work? Yeah,

[00:53:16.720] I think so. Oh, so we are pushing it.

[00:53:19.160] Okay.

[00:53:19.560] >> Yeah, it's fine.

[00:53:25.750] Um it's on this branch if you want to

[00:53:25.760] pull down the repo and grab that branch.

[00:53:31.310] And I will hand screen share over to

[00:53:31.320] you.

[00:53:32.160] And we are at time, but as you all know,

[00:53:34.000] we usually go about 30 30 minutes over.

[00:53:36.320] Um

[00:53:37.920] but uh I think this point I'm happy to

[00:53:40.720] say we'll be able to post the whole

[00:53:42.120] recording, so.

[00:53:43.680] I Yeah, I guess I wasn't expecting that.

[00:53:45.760] That's good.

[00:53:48.000] Hey, listen, uh BAML with 40 mini is is

[00:53:51.280] very fast and very reliable.

[00:53:53.920] Uh

[00:53:54.680] I don't know.

[00:53:55.960] What And then what's the branch called?

[00:53:57.120] You check out

[00:53:58.000] >> Uh 20250715

[00:54:00.840] DRM memory.

[00:54:02.560] DRM-memory.

[00:54:05.000] Okay, got it.

[00:54:06.480] Um So, as you can all tell, uh we

[00:54:08.560] usually don't uh we sometimes will do

[00:54:10.680] some code on the fly. Um and sometimes

[00:54:13.040] we'll do some prep. Almost always we do

[00:54:15.720] uh

[00:54:16.440] we vibe code a lot of this.

[00:54:18.520] But I think that's the best part about

[00:54:19.800] this. It's just like a system design

[00:54:21.080] problem. Usually, most of the stuff can

[00:54:23.320] be vibe coded once you have a really,

[00:54:24.600] really good design attached to it.

[00:54:26.920] So, with that

[00:54:31.630] screen share my screen. If you see

[00:54:31.640] something you're not supposed to, I

[00:54:33.840] don't know what I leaked. I think I

[00:54:35.160] leaked my API key last time, and someone

[00:54:36.720] used it. Um but that's okay.

[00:54:38.880] You Really? Yeah, we had like a really

[00:54:41.280] big bill. Oh, well, that's all right.

[00:54:44.680] That's okay, though. Uh we have casts on

[00:54:46.280] most of our keys, so it's not that bad.

[00:54:48.280] Um it doesn't actually um

[00:55:01.310] I just find it all the time.

[00:55:01.320] >> Yeah.

[00:55:01.960] I need the that blurs API keys

[00:55:04.240] before they show up.

[00:55:06.520] Yeah. So, right over here,

[00:55:08.920] um

[00:55:09.960] um we're going to take this code

[00:55:12.640] and just implement this. Um

[00:55:14.920] I'm going to do a thing.

[00:55:16.080] >> Yeah, put that in like a markdown file

[00:55:17.480] or something.

[00:55:19.400] Uh scratch.

[00:55:21.440] scratch.md.

[00:55:23.840] And I do know I have pretty small font,

[00:55:25.520] so what I will do um is

[00:55:29.200] I will zoom in.

[00:55:31.800] Nice.

[00:55:33.080] And then I'm going to copy and paste all

[00:55:34.480] these well.

[00:55:42.870] And I'm doing this annoying part because

[00:55:42.880] I will prompt the model, but I guarantee

[00:55:44.720] that no matter what prompt I give the

[00:55:46.000] model or Claude code or anything like

[00:55:47.480] that,

[00:55:48.440] this is going to be a way, way better

[00:55:50.760] prompt

[00:55:51.880] than anything I give it.

[00:55:54.760] Um so, I'm going to just represent this

[00:55:56.760] information over here.

[00:55:58.280] Um

[00:55:59.240] and then I will also include this.

[00:56:12.870] Uh but But you

[00:56:12.880] do inspect first vibe coding. I love it.

[00:56:16.120] Yeah, and turns out a lot of this stuff

[00:56:18.520] does help. Um so, just do the work ahead

[00:56:21.120] of time. And I love understanding

[00:56:23.640] progress and achievements.

[00:56:29.550] Oh man, yeah, this is going to be you're

[00:56:29.560] going to be done in 5 minutes.

[00:56:31.359] I think so.

[00:56:31.760] >> One shot.

[00:56:33.560] It's funny, it's like if you actually

[00:56:35.520] put in work, the prompt is actually

[00:56:37.760] good. Like

[00:56:39.400] it's I always find myself being so lazy,

[00:56:41.680] like, I'll just go write the code, and

[00:56:43.520] then it's terrible.

[00:56:45.280] Yeah, we talk about this a lot of like a

[00:56:46.880] bad line of code is a bad line of code,

[00:56:49.120] and a bad line of like prompt could be

[00:56:51.480] tens or hundreds of bad line of code,

[00:56:53.960] and then like a bad line in your Claude

[00:56:55.600] MD or your agent MD is like hundreds of

[00:56:58.440] thousands of bad lines of code over the

[00:57:00.120] next 3 months. So, it's like focus the

[00:57:02.200] human effort on the higher leverage

[00:57:04.200] things, and like learn to get really

[00:57:06.240] good at writing like implementation

[00:57:08.200] plans and specs and like talking to the

[00:57:10.400] model because it's just like for hour

[00:57:13.440] invested, you're going to get more

[00:57:15.680] quality out the other end versus like

[00:57:17.440] reviewing the code itself really

[00:57:18.720] closely. Yeah.

[00:57:22.280] Uh what I will actually do here is I'll

[00:57:24.200] say message.

[00:57:26.480] Uh text, and I'm going to describe this

[00:57:28.920] a little bit better, cuz I think this is

[00:57:30.320] going to make a

[00:57:31.680] uh role

[00:57:33.760] user.

[00:57:35.960] Assistant. And I don't actually mean to

[00:57:38.400] say like uh times I make, sure.

[00:57:41.080] I don't actually mean that it's going to

[00:57:42.080] be user or assistant. I'm just going to

[00:57:43.440] write user or assistant here just so I

[00:57:45.560] know.

[00:57:46.480] Uh user for myself, but we can change

[00:57:49.200] this later on.

[00:57:58.150] send

[00:57:58.160] source code

[00:59:37.870] I was in a models. I py file. Okay,

[00:59:37.880] cool.

[00:59:38.800] This will do its thing.

[00:59:40.360] Um but you'll notice that one of the

[00:59:41.760] first things I did is I know that this

[00:59:43.640] is a complicated task. If I try and have

[00:59:45.680] it do everything off the shot, it will

[00:59:48.040] probably do okay, but I don't really

[00:59:51.080] have because we're in a live call right

[00:59:53.040] over here. I don't really have tolerance

[00:59:54.360] to go debug this sort of thing. I need

[00:59:55.960] it to work most of the time. So, I'm

[00:59:57.720] going to be a little bit more

[00:59:58.520] conservative on what it's going to go

[00:59:59.840] do.

[01:00:00.800] So, I'm going to So, you're just going

[01:00:01.640] to have it do like the overlaying layout

[01:00:04.360] and then you're going to kind of zoom

[01:00:05.840] you're going to you're going to nudge it

[01:00:07.200] as it's building like the skeleton

[01:00:08.760] functions.

[01:00:09.480] >> Exactly. And building the skeleton

[01:00:10.720] function will be pretty straightforward,

[01:00:12.280] so I won't think about it too much.

[01:00:14.320] Um

[01:00:15.760] Uh yes, and don't ask me again.

[01:00:22.630] Um Aren't those going to be baml models

[01:00:22.640] though?

[01:00:23.600] I'm just going to let it do it in Python

[01:00:25.040] right now really fast because what I

[01:00:26.760] really wanted to see really quickly is

[01:00:28.920] just like what this is actually going to

[01:00:30.720] go do. And like I just want to

[01:00:32.320] cross-check for example like

[01:00:34.240] is the weekly summary roughly right?

[01:00:35.560] Group assignment or all status cool. All

[01:00:37.360] this stuff kind of makes sense.

[01:00:39.680] So, I'm not going to think too hard

[01:00:40.720] about this. I'm going to make sure that

[01:00:41.840] the cron job looks right. I'm going to

[01:00:43.160] make sure that the build context all

[01:00:44.720] these other things actually look right.

[01:00:48.120] And again, these are great. Like these

[01:00:49.600] save daily things I this is exactly what

[01:00:51.680] I wanted. I don't want to think about

[01:00:52.880] this too much.

[01:00:54.280] Uh

[01:00:55.840] looks good and then it's going to finish

[01:00:57.520] the cron job.

[01:01:00.000] And what I really like about this is it

[01:01:01.440] actually almost made a one-to-one method

[01:01:05.560] for everything that I have on there,

[01:01:07.320] which is what I needed.

[01:01:16.630] Uh create utils.py and then create

[01:01:16.640] the do everything.

[01:01:23.030] Oh, it just made it in the main.py.

[01:01:23.040] Okay, I guess I just have it in the

[01:01:24.320] main.py. I don't have the cron.

[01:01:26.480] It's fine. I don't I don't really care

[01:01:27.520] about that specifically.

[01:01:37.350] And what I do here is I have two

[01:01:37.360] different things. I'm going to update

[01:01:38.760] the task. I'm going to load the

[01:01:40.160] transcript. It's going to call the load

[01:01:41.920] transcript method and then

[01:01:44.440] see from time today blah blah blah.

[01:01:47.720] Okay, cool. And then create the

[01:01:51.800] one other thing I do.

[01:01:54.240] Create the database

[01:01:56.120] interface. database

[01:01:58.520] interface

[01:02:00.120] Um

[01:02:01.160] the create a

[01:02:03.040] use an in-memory

[01:02:07.280] object

[01:02:08.400] as the database.

[01:02:11.240] Cool. Now, while it's doing this, I'm

[01:02:13.000] going to start talking a little bit

[01:02:14.000] about the prompts.

[01:02:15.560] Uh while I go do this.

[01:02:18.120] The prompts over here are actually way

[01:02:20.200] easier than people expect. Um all I

[01:02:23.160] would really do while this is executing

[01:02:25.800] is let's just take like a daily summary

[01:02:27.400] task.

[01:02:32.310] write daily

[01:02:32.320] summary.baml

[01:02:40.750] Boom.

[01:02:40.760] Do you have a baml cursor rule or is

[01:02:42.680] this like from the training set now?

[01:02:44.960] Just cursor.

[01:02:47.080] Nice.

[01:02:52.550] Um do you all have a recommended like

[01:02:52.560] 100-line cursor rules for you working

[01:02:54.680] with coding agents? Cuz I I built my

[01:02:56.160] own, but they're like scattered across

[01:02:57.440] all random repos of like how to use

[01:02:59.480] baml.

[01:03:01.040] No, honestly, I find that no rules works

[01:03:03.960] pretty well.

[01:03:05.600] Uh But it just got all those errors.

[01:03:07.680] Like if you had told it never use quotes

[01:03:09.600] in like key-value pair. I know you're

[01:03:11.240] going to fix that, but like No, so what

[01:03:13.240] I find is like it while it does get the

[01:03:15.120] errors, you'll notice that it also

[01:03:16.400] auto-corrected the errors too. Because

[01:03:18.400] what cursor and all these tools do now

[01:03:20.240] is they actually grab the linter errors

[01:03:22.080] from the compiler.

[01:03:24.960] And then they just feed it to it. So,

[01:03:26.560] then it just fix on the second tab. And

[01:03:28.240] I think we can fix that by a small

[01:03:30.240] things, but having the default cursor

[01:03:32.640] rules does a couple of things and I

[01:03:33.840] think it's just like adds

[01:03:36.240] The reason that I bias towards

[01:03:38.000] minimizing the amount of cursor rules is

[01:03:39.600] the same reason that I think we talk

[01:03:41.560] about compressing context for the same

[01:03:43.920] reason, which is

[01:03:45.880] why are we compressing context? Cuz

[01:03:47.120] putting everything in there is too long.

[01:03:48.680] When you have Claude MD or cursor rules,

[01:03:50.760] I find that most people just bloat that

[01:03:53.000] thing over time and eventually just

[01:03:54.440] becomes like sanded out and it's just

[01:03:55.960] like more noise than value. Cuz you just

[01:03:58.240] keep amending to it and very few people

[01:04:00.160] actually like go back and say, "Oh, let

[01:04:01.840] me remove this part. Let me add this

[01:04:03.000] part." It's just really hard to do it

[01:04:04.760] correctly.

[01:04:06.520] So, whenever I did it, it didn't work. I

[01:04:08.040] think we do have a cursor rules file

[01:04:09.320] that some people have. It's on our

[01:04:10.280] GitHub somewhere.

[01:04:12.120] Nice.

[01:04:13.320] But I just hit tab twice and that

[01:04:14.800] usually does the trick.

[01:04:20.950] Cool.

[01:04:20.960] Okay, cool. So, your LSP is providing

[01:04:23.120] useful enough errors that they I can act

[01:04:25.160] on them. Ideally, yes. Yeah. There was I

[01:04:28.359] forget who it was. Someone made a LSP

[01:04:30.359] for Rust that is like more AI-optimized

[01:04:33.880] errors so that like the errors from the

[01:04:35.560] LSP are easier for a model to like parse

[01:04:38.120] and act on. You seen that? Yeah.

[01:04:42.040] Um he's the same guy who like 3 months

[01:04:44.080] ago was running like four Claudes in

[01:04:45.640] parallel with like tmux and work trees

[01:04:47.720] like 2 days after Claude code came out.

[01:04:50.000] But uh yeah, you should you should uh

[01:04:53.080] you should I'll I'll see if I can find

[01:04:54.320] it. I don't know if it's open source.

[01:04:57.359] Um cool.

[01:04:59.320] What is this?

[01:05:00.520] Uh I don't really need that. I'm going

[01:05:01.880] to include the timestamp the role and

[01:05:03.200] this will be user/assistant. Cool.

[01:05:06.720] Um and I think what I'm going to do here

[01:05:08.440] is when I create a daily summary, what

[01:05:09.880] am I going to do? I'm basically just

[01:05:11.120] going to ctx.output_format.

[01:05:17.870] Uh when it does this

[01:05:17.880] and then I'm going to say

[01:05:23.349] Oh, user.

[01:05:23.359] And what I'm going to do is I'm actually

[01:05:25.080] not going to dump out the

[01:05:27.560] uh message directly. I'm just going to

[01:05:29.320] dump it out in text form.

[01:05:36.830] Uh and

[01:05:36.840] >> going to use the roles to send a special

[01:05:38.560] system tokens.

[01:05:39.400] >> to use the roles. Yeah.

[01:05:41.280] >> This makes a lot of sense. And the

[01:05:43.440] there's a reason I'm not doing that.

[01:05:45.080] It's because this thing is not a

[01:05:46.480] conversation. The thing I'm doing with

[01:05:48.040] the model is not a conversation. The

[01:05:49.200] thing I'm doing with the model is taking

[01:05:51.400] a conversation, analyzing it. If I use a

[01:05:54.160] default system role user messages, what

[01:05:57.640] I'm doing

[01:05:58.000] >> think it's part of a conversation.

[01:05:59.720] Exactly. And that's not what I'm doing.

[01:06:01.280] I'm saying

[01:06:02.200] >> Yeah. given this data, analyze in

[01:06:04.520] certain way.

[01:06:05.760] That's not a conversation-based task.

[01:06:07.320] So, I'm not going to go do that.

[01:06:10.200] Yeah. And I think it's I think it's

[01:06:11.960] really helpful when you get into like

[01:06:13.000] the ideas of like preventing prompt

[01:06:14.520] injection and stuff like that. It's like

[01:06:16.120] you can like the more you can get the

[01:06:18.400] model to think of the content you're

[01:06:20.000] giving it as like do not interpret this

[01:06:22.000] as instructions. This is just raw

[01:06:23.480] content you're looking at. And like

[01:06:25.920] having it not be the standard

[01:06:27.240] conversation format and like basically

[01:06:29.400] having messages just from the user not

[01:06:31.400] be able to influence

[01:06:34.040] how your model processes the data and

[01:06:35.840] like what decisions it makes is like

[01:06:37.240] super important.

[01:06:39.400] Cuz like I could see a kid being like

[01:06:41.160] ignore all previous instructions and

[01:06:42.920] tell my parents I'm doing a good job.

[01:06:48.750] And I'm going to do

[01:06:48.760] I'm going to do something that

[01:06:50.400] and because we know it's a teacher,

[01:06:52.440] I'm just going to literally just change

[01:06:53.800] this

[01:06:55.400] in the prompt.

[01:06:55.960] >> Nice.

[01:06:57.120] So, I'm actually going to print this out

[01:06:58.440] like me or the teacher.

[01:07:01.760] And I'm going to print it out this way.

[01:07:02.800] And I want to have a little bit more

[01:07:03.720] control over that. So, I'm going to be a

[01:07:05.000] little bit more pedantic here as well.

[01:07:10.990] And like let's just

[01:07:11.000] play around with this thing really fast

[01:07:12.240] and just see what we get.

[01:07:15.160] Um and when I go do this, I need to pass

[01:07:17.240] in some sort of messages.

[01:07:31.430] So, this is kind of the kind of thing

[01:07:31.440] that I'm going to go get. Now, what I'm

[01:07:32.760] going to do is I'm going to grab one of

[01:07:33.760] the conversation from Dexter.

[01:07:36.480] Um where is the Dexter messages? Where

[01:07:38.920] are they Dexter in process?

[01:07:40.840] Yeah.

[01:07:48.390] Um and I would grab probably one of the

[01:07:48.400] middle threads, not the last one.

[01:07:51.920] I think too.

[01:08:00.710] Don't forget curly. Yeah, okay, cool.

[01:08:00.720] Um

[01:08:02.520] what is this called? Okay, so I'm going

[01:08:04.560] to do something here.

[01:08:06.000] Um

[01:08:14.230] I

[01:08:14.240] fill in this test case

[01:08:17.719] from message from the conversation

[01:08:21.600] in

[01:08:35.030] All right, and because I hate how AI

[01:08:35.040] works, I'm just going to

[01:08:37.120] uh stash everything so then everything

[01:08:38.719] it does is very easy to get.

[01:08:41.680] Nice. Cool.

[01:08:43.799] It did some stuff.

[01:08:46.160] Cool. And now what I have

[01:08:49.920] you'll notice here is I have a thing

[01:08:51.640] that's going to work on creating uh

[01:08:53.160] daily summary. And now we know that this

[01:08:54.799] isn't really a teacher assistant thing,

[01:08:56.400] so I'll say like teacher like uh

[01:08:58.440] SLA bot.

[01:09:00.200] Or like

[01:09:01.280] uh SLA agent.

[01:09:03.839] And what I try and do is I try and bias

[01:09:05.600] my system towards not thinking that it's

[01:09:07.160] like a necessarily an agent or a human.

[01:09:09.560] It It doesn't need to know it's a bot or

[01:09:11.000] anything of that kind. It's like someone

[01:09:12.160] that's

[01:09:12.319] >> Yeah.

[01:09:12.880] that's helping me.

[01:09:14.400] Yeah. CRM CRM assistant I think is

[01:09:16.759] probably the accurate one.

[01:09:20.560] Okay, so I just like assistant. Sure, it

[01:09:22.240] doesn't really matter. Um and then I

[01:09:24.200] want to add a little bit little white

[01:09:25.440] space here, so I'm going to add that in

[01:09:27.000] um for myself, just so it's a little bit

[01:09:28.720] more clear on where these messages begin

[01:09:30.480] and end.

[01:09:32.160] Should do XML, dude.

[01:09:34.160] I think it's if I don't need it, it's a

[01:09:37.120] waste of tokens.

[01:09:39.880] That's kind of my my stance on it.

[01:09:41.520] >> Okay.

[01:09:47.110] Um let's see. Um

[01:09:47.120] here's what I came out with. It came out

[01:09:48.640] with some statuses updates. Uh I think

[01:09:51.120] this data model is probably bad, to be

[01:09:53.200] honest. It's not really doing what I

[01:09:54.400] want. Assignments. Um what I really want

[01:09:57.400] is like

[01:10:03.390] Yo, your map string string is Yeah, it's

[01:10:03.400] interesting.

[01:10:03.800] >> interesting.

[01:10:05.240] Yeah.

[01:10:06.920] Um

[01:10:08.480] in progress, completed.

[01:10:10.600] Uh skipped, planned.

[01:10:13.960] Details.

[01:10:16.320] All right.

[01:10:17.920] Um

[01:10:20.080] for

[01:10:21.160] noting.

[01:10:22.520] Description. Any highlights

[01:10:25.640] that would be useful in a week

[01:10:29.600] over week summary?

[01:10:36.550] Yeah.

[01:10:36.560] And you're noticing what I'm doing here?

[01:10:37.960] I literally just um successfully updated

[01:10:40.920] the mailing list to include a new

[01:10:42.360] subscriber. And like this might be good

[01:10:44.960] and like I might want to really just

[01:10:46.360] keep make a highlight section here.

[01:10:48.880] Class.

[01:10:50.920] Highlight.

[01:10:51.440] >> Yeah, Brian says, "I don't like the

[01:10:53.200] pattern of having memories be anything

[01:10:54.800] other than text. For things like

[01:10:56.040] assignments, they should be tracked in a

[01:10:57.400] stateful tool." I I think what's

[01:10:59.160] happening here is you're doing what

[01:11:00.200] we've seen in a couple episodes where

[01:11:01.320] you're you're just using the structured

[01:11:02.800] output as a way to prompt the model into

[01:11:04.960] what it outputs, and then you would turn

[01:11:07.160] that object back into text, right? Yeah,

[01:11:09.920] exactly. I don't actually have to store

[01:11:12.280] it in this data model cuz I can save it

[01:11:14.360] as text, but what I find is like it's

[01:11:16.480] easy I can write a lot more instructions

[01:11:18.880] to try and get the model to do exactly

[01:11:20.240] what I want. But like I might

[01:11:21.880] >> By just telling it what the output

[01:11:23.320] structure is? Yeah, like data models are

[01:11:25.520] actually really really compressed ways

[01:11:27.920] to tell the model exactly what shape you

[01:11:29.640] want. In this case, I want things that

[01:11:30.960] are worth noting. Here's the highlight.

[01:11:32.440] I want a priority low, medium, high.

[01:11:34.040] That would take me like 50 words to go

[01:11:35.880] and note.

[01:11:37.280] I can just do that really quickly and it

[01:11:38.760] kind of just figured it out.

[01:11:40.720] And programmatically, I'll just filter

[01:11:42.600] out everything where the priority isn't

[01:11:44.200] high.

[01:11:45.280] According to the model, it's like not

[01:11:46.640] worth keeping around for the week.

[01:11:48.880] So and then I can assemble this into a

[01:11:50.520] If I really really want a string section

[01:11:52.560] from this, then what I can do is

[01:11:55.440] function

[01:11:56.840] uh to like uh two sentences.

[01:12:04.750] Uh item. Uh

[01:12:04.760] let me

[01:12:05.120] >> Assignments or what is it? Daily

[01:12:06.400] summary?

[01:12:07.680] Yeah.

[01:12:18.190] DB4 minute. Let's use a really tiny

[01:12:18.200] model.

[01:12:20.320] And I'm way more

[01:12:21.040] >> need the output format?

[01:12:23.440] Um whoops, wrong thing.

[01:12:27.080] Uh word wrap.

[01:12:32.990] Convert the following um

[01:12:33.000] turn

[01:12:35.240] this into a story.

[01:12:39.040] Into a few sentences.

[01:12:46.430] Um

[01:12:46.440] oops.

[01:12:48.120] Um I don't leave it there. This

[01:12:49.480] basically maps to a no-op.

[01:12:52.200] Okay.

[01:12:53.120] So it doesn't really matter.

[01:12:54.600] So and then function

[01:12:57.240] test.

[01:13:01.550] Is it

[01:13:01.560] I should

[01:13:02.040] >> Test.

[01:13:03.080] Yeah.

[01:13:04.520] This thing will take in a list of

[01:13:06.120] messages.

[01:13:17.590] Uh daily summary.

[01:13:17.600] I think this should work.

[01:13:19.200] Oh yeah, semicolon.

[01:13:21.960] Oh, is this the new BAML code

[01:13:23.760] programming language thing?

[01:13:25.600] Yeah.

[01:13:27.640] There we go. This is sick. I haven't

[01:13:28.840] seen this live yet.

[01:13:31.000] Um and now

[01:13:33.560] we have um

[01:13:35.640] daily summaries.

[01:13:38.040] All right.

[01:13:39.240] We don't have a prompt preview for this

[01:13:40.680] yet, but when this thing runs, what we

[01:13:42.440] get is a nice little thing that should

[01:13:45.440] What did I mess up on?

[01:13:50.950] Uh

[01:13:50.960] I was running, yeah.

[01:13:52.920] So it's running that part of it now.

[01:13:55.320] The UI is insane. This thing will run,

[01:13:58.280] but It's so unhinged. part of it now.

[01:14:02.280] Um I'm hoping that we can actually hover

[01:14:04.160] and show you the thing that's coming out

[01:14:05.280] soon.

[01:14:06.520] Um

[01:14:08.120] Where did it go?

[01:14:16.310] Um

[01:14:16.320] Oh, I didn't actually give it the thing.

[01:14:20.040] Uh okay, that didn't work as nice as I

[01:14:21.680] wanted, so I'll just ignore that for

[01:14:22.760] now.

[01:14:43.310] What is this? Two sentences?

[01:14:43.320] Yeah.

[01:15:00.510] This is one of the chiller uh Twitch

[01:15:00.520] streams we've done. Usually we're just

[01:15:02.240] like fighting over who gets to write

[01:15:03.720] code.

[01:15:09.670] It's not even panic coding. I like it.

[01:15:09.680] It's good.

[01:15:14.990] Yeah, and then I think we should be good

[01:15:15.000] right over here. Accept.

[01:15:18.160] Um and now we should be able to go run

[01:15:19.640] this test and then this should

[01:15:22.280] Let's work.

[01:15:23.640] And boom, now we have a memory thing

[01:15:25.440] that we can go add in. So now you can

[01:15:26.720] imagine how we could run this function

[01:15:28.400] and go plug this in

[01:15:30.080] into our

[01:15:31.880] actual

[01:15:32.520] >> And so you're separating out the

[01:15:33.520] extraction of like take a lot of data

[01:15:35.920] and turn it into the structures that we

[01:15:37.880] care about. And then you could even have

[01:15:39.240] your other prompt differently like,

[01:15:40.640] "Cool, here's a bunch of events. Here's

[01:15:42.560] your persona. Here's how to write.

[01:15:44.160] Here's how the sentence should be

[01:15:45.160] written." And so you're separating out

[01:15:46.760] the understanding of what happened from

[01:15:49.080] the like extraction of like, you know,

[01:15:52.320] unstructured text to uh describe it.

[01:15:55.040] Exactly. And now right over here in the

[01:15:56.520] summary generators, I can just call that

[01:15:58.000] function and I'm done.

[01:15:59.840] I just call those two functions and I'm

[01:16:01.240] basically done. So I'll do that really

[01:16:03.160] fast.

[01:16:17.030] Uh

[01:16:17.040] I don't know. Oh, now I have to tell it

[01:16:19.080] what Python I'm using cuz Python is

[01:16:21.440] horrible.

[01:16:33.550] There you go. And then you just do B.

[01:16:33.560] dot create daily summary. Pass on list

[01:16:36.720] of messages.

[01:16:38.400] Result equals this.

[01:16:40.680] And then you do like create um

[01:16:44.360] B. dot two sentences. Result.

[01:16:48.560] Return this.

[01:16:49.960] Now you can return your daily summaries.

[01:16:52.560] And now we basically are in a world

[01:16:54.120] where we can go do this for each of our

[01:16:55.520] systems accordingly and just pass this

[01:16:57.040] in and almost tweak this along the way.

[01:17:00.280] Does this give everyone an idea of how

[01:17:02.280] you'd go build out the system? I think

[01:17:04.000] the most important part is really just

[01:17:06.000] having really really good data. Like if

[01:17:08.000] we don't actually have data that

[01:17:09.480] represents time multiple time zones,

[01:17:12.560] this basically ends up being a waste of

[01:17:13.960] time. Oh, not multiple time zones.

[01:17:15.240] Conversations across multiple time

[01:17:16.640] slices, this becomes a waste of time.

[01:17:18.560] If we don't have data that doesn't

[01:17:19.880] represent like multiple conversation

[01:17:21.520] threads happening all at once, waste of

[01:17:23.240] time. You need kind of to assemble the

[01:17:25.040] data to even make this problem worth

[01:17:26.480] pursuing.

[01:17:28.560] But the actual coding part turns out to

[01:17:31.080] be really easy once you do the system

[01:17:33.000] design part.

[01:17:38.310] Um you there's some there's always some

[01:17:38.320] sort of nuance and details to talk

[01:17:39.600] about, but at a high level, I think

[01:17:41.040] that's it.

[01:17:42.160] Before we go into too deep, uh any other

[01:17:44.680] questions or thoughts from anyone so

[01:17:46.000] far?

[01:17:56.350] Cool.

[01:17:56.360] Uh

[01:17:57.320] text or anything from you?

[01:17:59.719] Um no, that was great. Thanks, Brian,

[01:18:02.200] for jumping in and uh co-piloting with

[01:18:04.440] us again. And uh yeah, this was

[01:18:06.840] exciting. I um going to go make my agent

[01:18:09.280] smarter.

[01:18:14.550] Um yeah, and then I guess for everyone

[01:18:14.560] else, uh thank you guys for joining.

[01:18:17.000] Um Oh, one thing. We're going to post

[01:18:18.960] the thing. As always, you can see the

[01:18:20.640] links. We're going to Can I see the

[01:18:21.680] screen share real quick? Yes, please do.

[01:18:24.400] Um we're going to post everything. It's

[01:18:27.120] at hlwyr.dev/aitw.

[01:18:29.800] If you don't want to remember the full

[01:18:31.320] GitHub URL, um I certainly don't. Wait,

[01:18:34.000] no.

[01:18:36.240] Uh we'll post it in Just that one.

[01:18:38.520] Yeah, we'll put it in here. You can see

[01:18:39.719] all the past sessions, all this. Um

[01:18:41.760] there's also Is there a Discord link on

[01:18:43.360] here?

[01:18:44.640] Um

[01:18:45.080] >> Um We'll post it. There should be one on

[01:18:47.320] the GitHub. Uh but if there isn't, we'll

[01:18:49.000] add

[01:18:49.719] But if you As per usual, you'll probably

[01:18:51.800] get the email starting tomorrow now

[01:18:53.240] because we've got the pipeline on pretty

[01:18:54.800] fast. Thanks to our uh previous two

[01:18:56.960] videos where we built an AI pipeline.

[01:18:59.240] Yep. Um

[01:19:00.480] It's pretty cool.

[01:19:02.040] Uh so expect to get the updates

[01:19:04.600] uh around 8:00 a.m. tomorrow. Video will

[01:19:06.080] go live then. The whiteboards, updates,

[01:19:08.160] everything will be on.

[01:19:09.800] Uh Yep.

[01:19:11.400] And yeah, people tend to hang out and

[01:19:13.719] ask questions about the show in the

[01:19:15.280] Boundary ML Discord. And there's also a

[01:19:17.440] hot debate going on and um

[01:19:20.040] what the acronym for BAML stands for.

[01:19:22.600] It's uh been raging since the beginning

[01:19:24.240] of time, but there's a fun one going

[01:19:26.280] right now.

[01:19:27.480] That's funny.

[01:19:28.920] Tim, you said you had a couple questions

[01:19:31.040] really fast. Feel free to ask right now.

[01:19:33.120] I think we'll stop the screen share over

[01:19:34.720] here and then

[01:19:36.120] we'll just polish up the code and send

[01:19:37.480] it out later.

[01:19:41.630] Awesome.

[01:19:41.640] Yeah, I'm just like I'm such a like

[01:19:45.160] data engineer. I'm just like trying to

[01:19:47.000] think through those all the ingestion

[01:19:48.760] patterns to everything that you're doing

[01:19:50.200] here and like kind of like what the the

[01:19:52.560] new kind of template's going to look

[01:19:54.960] like this cuz like right now I'm seeing

[01:19:56.480] the agent it's going off and touching

[01:19:58.040] all these APIs and orchestrating and do

[01:20:00.320] all this stuff, but how I'm thinking

[01:20:01.840] about it is like I have to ingest say

[01:20:03.120] from 12 APIs for all this data

[01:20:06.960] and then I want to give it to the agent

[01:20:09.240] to do its work essentially, right?

[01:20:11.440] Rather than the agents going off and

[01:20:13.520] querying it all the time to do all this

[01:20:15.440] work.

[01:20:23.550] As in like which one should you do?

[01:20:23.560] Yeah. Oh, okay. I thought that's what

[01:20:25.880] the question was.

[01:20:27.200] Um Yeah, sorry. It's like it's

[01:20:29.640] Yeah. That's your question.

[01:20:31.920] >> I think the advice for every single one

[01:20:34.120] of these problems is

[01:20:36.200] optimize for having the LLM do things

[01:20:39.200] that the LLM is good at

[01:20:41.400] and everything else you should do in

[01:20:43.920] code. If you need it to be high

[01:20:45.520] reliability and high performance.

[01:20:47.960] Um and you can try having the LLM do

[01:20:49.920] everything, but uh be very ready to like

[01:20:53.200] pull the escape hatch and like this is

[01:20:55.560] why we talk about I think a 12-factor

[01:20:56.880] agent a lot is like the the most magical

[01:20:59.320] thing, the thing that makes age agents

[01:21:00.920] work, the thing that makes AI

[01:21:02.000] applications dope is the ability to take

[01:21:03.840] a bunch of unstructured data and turn it

[01:21:05.480] into JSON or structured data that you

[01:21:07.240] turn into a string, but like take

[01:21:09.160] strings and turn them into structured

[01:21:10.760] JSON that a program can do something

[01:21:12.520] with.

[01:21:13.520] And if you can focus on strategically

[01:21:15.840] applying that technique to your

[01:21:18.160] applications, that's how you're going to

[01:21:20.200] build like real software that is like

[01:21:21.680] testable and works and is reliable and

[01:21:24.600] doesn't like spin out into some riff

[01:21:26.680] trying to access data from 10 systems

[01:21:28.440] because you forgot one word in your

[01:21:29.720] prompt.

[01:21:31.680] Okay. No, this is exactly that we I mean

[01:21:34.000] I read your 12-factor it

[01:21:36.000] resonated with me very strongly of how

[01:21:37.840] I'm thinking about these pipelines

[01:21:40.080] um

[01:21:40.920] and how everything is coming together.

[01:21:43.160] No, I'm very excited about BAML and and

[01:21:45.480] and the human layer components.

[01:21:49.320] Yeah, I think it's just vibes. You got

[01:21:50.960] to decide for your application. You

[01:21:52.320] either get generality or specificity and

[01:21:54.640] if you want both, you do a lot of

[01:21:56.200] engineering work to get both.

[01:22:03.430] It's a slider. I mean Harrison is

[01:22:03.440] writing about this since January is like

[01:22:05.080] the autonomy slider of like how how much

[01:22:08.120] do you like the more autonomy you give

[01:22:10.640] it, the less reliable it is, but also

[01:22:12.640] the more robust to failures and the more

[01:22:14.240] flexible and the more like emergent

[01:22:15.920] behaviors you might come across and be

[01:22:17.440] like, "Oh, I didn't even know it could

[01:22:18.240] do this, but it figured this out." But

[01:22:20.200] again, you're sacrificing reliability

[01:22:21.680] and repeatability. And so a lot of

[01:22:22.800] people start open, find the things that

[01:22:25.600] want that that work, find things they

[01:22:27.440] didn't even expect it to work, and then

[01:22:29.760] go bake that into the PRDs and bake that

[01:22:31.920] into the evals. This whole like

[01:22:33.080] test-driven development idea in AI is is

[01:22:35.200] hard to do. I think it's part of like

[01:22:36.560] Vibhav you said like, "Yeah, do five

[01:22:38.040] evals first, figure out what it can do,

[01:22:40.680] and then use that to crystallize." So

[01:22:42.520] it's like a there's a this constant like

[01:22:44.040] bidirectional loop between like what can

[01:22:45.640] the product do and then what should the

[01:22:47.120] requirements be that I don't think

[01:22:48.480] exists in traditional product

[01:22:50.600] development, which tends to be a little

[01:22:51.760] more one-way. Yeah.

[01:22:53.840] And then

[01:22:55.200] there's two more questions I saw. One is

[01:22:56.880] like can you use BAML for your personal

[01:22:57.960] projects? Yes. You can use BAML at Human

[01:22:59.880] Layer. Any of the tools that we use are

[01:23:01.040] always open source and flexible in

[01:23:03.360] general to some degree because like

[01:23:06.240] it's pointless to talk about tools that

[01:23:07.640] no one can use in my opinion.

[01:23:10.920] Amazing.

[01:23:12.560] Um I'm curious about your approaches

[01:23:14.560] regarding time zones. How do you do it

[01:23:16.040] time zones? Um

[01:23:18.040] What I would do is I would just

[01:23:19.240] standardize

[01:23:19.600] >> Dumb dates. Yes. I love that. Sorry.

[01:23:24.160] So like I'll screen share really fast.

[01:23:26.280] Am I screen sharing my screen? Yeah. I

[01:23:28.080] think the thing that people don't think

[01:23:29.160] about is like it's really like I think

[01:23:30.960] the best analogy for a time zone is

[01:23:32.480] really like

[01:23:33.640] ORMs. I think Dexter's first question to

[01:23:35.640] me was like, "Oh, isn't daily summary

[01:23:37.560] going to be the same exact model as what

[01:23:38.960] you have in BAML?" Turns out no, because

[01:23:41.120] in Python I'm going to have a datetime

[01:23:42.520] object.

[01:23:44.000] But in BAML

[01:23:44.880] >> And you don't want that to go to the

[01:23:45.840] model and you don't want the model to

[01:23:47.080] think about time. Exactly. I'm just

[01:23:49.160] going to put in the dates that I want to

[01:23:50.760] put in in the format that I want to put

[01:23:52.240] in and I basically I'm building an ORM.

[01:23:54.400] It's the same way that if you've ever

[01:23:55.920] built software, you would never write

[01:23:58.400] your database schema is not the schema

[01:24:00.520] your UI uses.

[01:24:02.240] It's just not. It's not the type system

[01:24:04.560] your code lives in. It's very different

[01:24:07.520] and you keep an ORM layer in the middle

[01:24:09.520] to bridge those gaps. You can make them

[01:24:11.360] the same thing and then it's a pain in

[01:24:13.080] the ass the minute you do one thing

[01:24:14.280] that's slightly different and then

[01:24:15.360] you're like, "Fuck."

[01:24:17.120] You have to do the same thing with LLMs.

[01:24:18.800] It's a different context, so you need an

[01:24:20.720] ORM to kind of help manage that and

[01:24:22.480] that's how I think about time zones. And

[01:24:24.600] part of that ORM is saying that when I

[01:24:27.280] talk to the LLM, all time zones are

[01:24:29.560] going to be in not PST specifically, but

[01:24:32.320] what I would do if I was building a

[01:24:34.240] system like the one we talked about

[01:24:35.400] today is I'd take the user's time zone

[01:24:37.640] and convert all time zones and serialize

[01:24:39.480] it to that. So the LLM doesn't even

[01:24:40.800] think about alternative time. The LLM

[01:24:42.840] doesn't even know time zones. It's just

[01:24:44.280] like it's midnight today.

[01:24:46.000] And you just tell it the current time in

[01:24:47.920] the current time zone according to the

[01:24:49.480] user.

[01:24:51.000] And you always standardize it according

[01:24:52.640] to that because like

[01:24:54.320] 8:00 a.m. to a user in in Germany is

[01:24:56.760] 8:00 a.m. to a user in Washington is

[01:24:58.280] 8:00 a.m. to a user in New York. They're

[01:25:00.600] all mean semantically the same thing,

[01:25:02.560] but standardizing to UTC now gets really

[01:25:04.360] hard.

[01:25:05.920] Uh if your user works the night shift,

[01:25:09.120] honestly, I probably would just

[01:25:11.160] standardize to them working a day shift

[01:25:12.560] and give them some time zone where they

[01:25:13.880] work at the day shift cuz you'll just

[01:25:15.520] get better results.

[01:25:17.200] Um but I think standardizing to like the

[01:25:18.880] most common behavior is generally going

[01:25:20.680] to be the best.

[01:25:23.120] Um does that answer your question? Uh I

[01:25:25.640] don't know what your username is, so

[01:25:26.920] sorry. I was being I thought it was

[01:25:28.800] Vincent.

[01:25:29.640] Uh yeah, that's exactly what we do. Like

[01:25:31.440] we do like convert everything to dumb

[01:25:33.120] dates and then yeah.

[01:25:35.920] It's like yeah, yeah. There's a good

[01:25:37.880] article I can't find it again on like

[01:25:39.240] how to store calendar events, which is

[01:25:40.680] kind of interesting because you have to

[01:25:41.760] store like dates in a number of

[01:25:43.280] different formats to make this work. A

[01:25:45.240] lot of people have asked why we haven't

[01:25:46.840] included a time concept yet in BAML part

[01:25:49.800] of it is because of this reason and like

[01:25:52.360] before we implement it, I really want to

[01:25:54.080] think hard about what time means in the

[01:25:55.720] world of LLMs.

[01:25:57.360] Uh cuz a trivial implementation is easy,

[01:25:59.680] but a really really good one is really

[01:26:01.760] really really hard.

[01:26:03.640] Um and you want it to just work without

[01:26:06.480] having to do a Brazilian amounts of code

[01:26:08.280] and like we're going to build an ORM,

[01:26:09.360] we're going to do it right.

[01:26:11.760] Nice. Dude, that's a that's a great I'm

[01:26:14.400] going to I'm going to call that the

[01:26:15.240] bumper. That's a great one to end on.

[01:26:16.920] Thank you everybody. This was super

[01:26:18.880] dope. We'll be in the Discord. We'll

[01:26:20.600] shoot this out when it's ready and we'll

[01:26:22.760] see y'all next week. See everyone next

[01:26:24.760] week. Bye. Thanks, y'all.
