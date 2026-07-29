# S02E14 – Decoding Context Engineering Lessons from Manus



Source: YouTube captions (automatic:en)



[00:00:05.269] All right, welcome back everyone. Um, I

[00:00:05.279] think this week is going to be a really,

[00:00:06.720] really fun conversation between Dasher

[00:00:08.639] and I about a topic that I thought was

[00:00:11.280] going a little viral for a bit. Uh, many

[00:00:14.559] of you might have seen the Manis paper

[00:00:16.240] that came out about all their findings

[00:00:17.840] about context engineering and other such

[00:00:19.840] related things about what benefit um

[00:00:22.640] what benefits that they saw with some of

[00:00:24.400] the techniques that they did. For those

[00:00:25.600] of you that didn't, no worries. we're

[00:00:26.960] gonna go describe all of them and we'll

[00:00:28.320] talk about the trade-offs. But I think

[00:00:30.080] in general the most interesting thing

[00:00:31.439] about that whole thing that I saw was

[00:00:34.160] just how deep this stuff goes. Like it a

[00:00:36.960] lot of us take for granted or it's like

[00:00:39.120] we learned the first level. It's good.

[00:00:41.120] But a lot of the stuff goes really deep

[00:00:42.960] and it's all based out of the

[00:00:44.239] foundational stuff behind how these LLMs

[00:00:46.480] work. It's not always even obvious how

[00:00:49.840] you would predict that if you don't

[00:00:51.200] actually understand how an LM produces

[00:00:53.920] tokens. I think that's kind of what we

[00:00:55.920] should talk about today and how these

[00:00:57.920] findings cannot Go ahead, Dexter.

[00:01:00.239] >> Sorry. No, and like I I really love the

[00:01:02.480] the way you frame that which is like um

[00:01:05.280] there are things that are just

[00:01:06.880] completely beyond your understanding and

[00:01:08.720] they're not hard to understand, but if

[00:01:10.240] you don't know to learn about them and

[00:01:11.840] you don't know to go research them and

[00:01:13.360] figure out how the stuff works under the

[00:01:14.640] hood, uh because none of us is going to

[00:01:16.640] go and get a machine learning PhD in the

[00:01:19.759] next two weeks. But um if you can find

[00:01:23.119] certain things and find understanding of

[00:01:25.200] how things work under the hood um there

[00:01:27.439] are certain slices you can take of that

[00:01:30.080] knowledge that can make you a much

[00:01:31.360] better AI engineer.

[00:01:33.360] >> Yeah. And I think part of the

[00:01:34.960] conversation today is not just going to

[00:01:36.479] be about how what those learnings are

[00:01:39.040] but how you could derive them for first

[00:01:40.880] principles so that you can go on and

[00:01:43.040] perhaps find new things on your own

[00:01:45.200] because I think that's the most valuable

[00:01:46.560] insight. It's not about being able to

[00:01:47.680] copy what other people do. It's being

[00:01:49.040] able to figure out what is a thing that

[00:01:50.479] you can invent and help the rest of us

[00:01:52.479] along the way because if all of us with

[00:01:54.159] all our different backgrounds can go and

[00:01:55.680] investigate these areas, I think we can

[00:01:57.920] converge on what makes good AI pipelines

[00:01:59.840] way faster as a general community

[00:02:02.479] building this stuff out.

[00:02:04.159] >> So,

[00:02:05.600] >> with that,

[00:02:05.920] >> do you want to do quick intros and then

[00:02:07.119] I have a quick announcement and then

[00:02:08.399] let's get into it.

[00:02:09.599] >> Um, cool. So, I'm Dex. Uh, I, uh, well,

[00:02:13.200] the announcement is basically if you're

[00:02:14.879] new to the show, we post every episode

[00:02:16.560] on GitHub. Um, and so you can come here

[00:02:18.480] and see all of them. Uh, if you're

[00:02:20.400] looking for the recaps of the context

[00:02:23.040] engineering for AI agent stuff, you can

[00:02:24.720] find that here. We've done a lot of

[00:02:25.920] episodes on context engineering in the

[00:02:27.599] past. Um, and so just another reminder,

[00:02:31.120] encouragement, we put all of the links,

[00:02:32.879] all the show notes will be here in the

[00:02:34.319] Git repo, um, including links to sign up

[00:02:37.040] for the next episode and all the

[00:02:38.400] whiteboards that we publish. So, um,

[00:02:40.560] without without, uh, further ado, I'm

[00:02:43.040] Dex. I'm the founder of Human Layer. Um,

[00:02:44.879] we've been doing the show since March.

[00:02:46.480] Uh, and uh, this is this is AI that

[00:02:48.640] works, where we teach you to be a better

[00:02:49.920] AI engineer. I don't know. By, you're

[00:02:52.400] gonna have to you're gonna have to pitch

[00:02:53.280] the show for me.

[00:02:54.879] >> Um, I'm Bob. I write some code. That's

[00:02:58.000] about it. Let's talk about fun stuff.

[00:02:59.680] Let's get to the meat.

[00:03:01.680] >> Let's do it.

[00:03:02.560] >> Um, one second. Context engineering.

[00:03:14.070] ESD. Cool.

[00:03:14.080] And now I'm going to go ahead and

[00:03:15.280] screen.

[00:03:17.680] So, I want to go straight into the manus

[00:03:20.080] paper and just go talk about this uh

[00:03:22.879] from the very beginning. I Dexter, I

[00:03:25.360] don't have a second screen today, so

[00:03:26.480] you're going to have to keep be on the

[00:03:27.440] lookout for questions people ask and

[00:03:29.120] just let me know

[00:03:30.080] >> as we go.

[00:03:31.280] >> So, I think

[00:03:31.760] >> you want to make me a host.

[00:03:33.280] >> Yes. I'm surprised I did not do that

[00:03:34.959] already.

[00:03:37.360] >> All right. So, the first thing is like

[00:03:39.519] what is Manis? For those that haven't

[00:03:41.120] seen, it's a pretty pretty cool project

[00:03:42.959] that got a lot of popularity. Um, it's

[00:03:45.920] based I've not signed in. It's bas uh

[00:03:49.040] they still have the the like videos on

[00:03:50.879] the website where you can like see the

[00:03:53.599] like example use cases.

[00:03:55.760] >> Yeah, I think it's probably worth

[00:03:56.799] looking at because I think it tells you

[00:03:58.560] roughly what it is. It basically kind of

[00:03:59.920] just does stuff. It's an agent that is

[00:04:01.360] very generalized and does stuff. Um, and

[00:04:03.680] it's really impressive what it was able

[00:04:05.760] to do.

[00:04:07.519] Um, from it's going to make me sign and

[00:04:10.080] I'll show you guys. And I think part of

[00:04:12.640] what made this app so viral and

[00:04:15.120] impressive is the fact that these folks

[00:04:16.799] figured out some ways to

[00:04:20.160] stop asking just let me show you

[00:04:23.520] what to do. But you'll notice, okay, I

[00:04:25.360] don't have enough credits. Okay, I

[00:04:26.320] already used all my credits when I was

[00:04:27.440] doing this earlier. But um part of what

[00:04:30.000] made the app really impressive was just

[00:04:31.440] how broad of a task it was able to do

[00:04:33.840] and how like how high quality it was

[00:04:36.960] able to handle for the generality of

[00:04:38.400] what it did. And there's small things

[00:04:40.720] like I don't know if you guys noticed

[00:04:42.080] just like when I was even on the

[00:04:43.199] homepage

[00:04:44.800] there's small things here that get

[00:04:46.160] really fast. I do this and it

[00:04:47.520] immediately fills in these things. How

[00:04:49.680] is it so freaking fast? We're all using

[00:04:51.440] the same models. It's not like they have

[00:04:52.720] anything special under the hood. And

[00:04:54.560] these small things around how they

[00:04:55.840] design the UX, how they design the

[00:04:57.120] interfaces, how they make the models

[00:04:58.720] slightly faster are what I think made

[00:05:01.440] Madness go viral because it's one of the

[00:05:02.880] first apps to go do that. I think when

[00:05:04.960] they announced on their techniques, one

[00:05:06.639] of the most talked about techniques was

[00:05:08.800] around this idea of a KV cache, but I'll

[00:05:12.080] talk about that in a little bit later.

[00:05:13.919] Um, it talked about another concept

[00:05:15.680] called masking not removing. And there's

[00:05:17.919] this concept when we use MCPS which goes

[00:05:20.720] around this idea of like how do you deal

[00:05:22.400] with the fact that I don't want to give

[00:05:24.240] my model every single tool all the time

[00:05:27.280] and why you don't want to do that makes

[00:05:29.520] sense cuz I don't want my model to be

[00:05:31.039] dumb and like have choices between tools

[00:05:32.880] it shouldn't have. If it's going to

[00:05:34.400] choose between writing a document and I

[00:05:35.840] know the user wants a notion document,

[00:05:37.520] don't give it the Google Docs tools.

[00:05:39.280] That is literally just going to confuse

[00:05:40.800] it. That makes a lot of sense. But

[00:05:43.600] there's trade-offs in this and what

[00:05:44.880] happens. So we'll talk about that in a

[00:05:46.320] second.

[00:05:47.600] It talked about how you actually

[00:05:48.800] engineer for super large context and

[00:05:50.800] context compression. I didn't use that

[00:05:52.960] word specifically, but I think that's

[00:05:54.320] what they were hinting at, which help

[00:05:56.400] you intelligently compress context when

[00:05:59.199] you have

[00:05:59.600] >> and it's using right.

[00:06:01.680] >> Yeah,

[00:06:02.000] >> this is using basically the same tools

[00:06:03.520] that agents already know how to use a

[00:06:05.120] file system basically. And so it becomes

[00:06:06.800] a really nice way for the agent to

[00:06:08.240] organize its own memories, right?

[00:06:10.160] >> Kind of at least from what I understood.

[00:06:12.000] It might be slightly different. Um, and

[00:06:14.319] I think the other thing that I thought

[00:06:15.600] was um, when he talked about this

[00:06:18.160] concept of how it actually summarizes

[00:06:19.759] steps, this was very similar if you were

[00:06:20.960] here in last episode when Dexter was

[00:06:23.440] talking about how it he does

[00:06:24.880] summarization for his coding workflow

[00:06:26.560] where he does like a research step, a

[00:06:27.759] planning step, and then an execution

[00:06:29.199] step. And the whole idea is you're able

[00:06:31.199] to compress context in a more concise

[00:06:33.360] way simply by some of the techniques

[00:06:36.720] that they discuss here. Um, they talked

[00:06:39.440] about keeping the wrong stuff in and

[00:06:41.039] like how that hurts your system. And

[00:06:43.039] then thing that I often say which is

[00:06:45.840] fuchia prompting sucks. They talk about

[00:06:48.080] why they also found fuchia prompting

[00:06:50.000] sucks

[00:06:51.680] uh more often than not but we'll go into

[00:06:54.080] some of these now for everyone else. Um

[00:06:56.960] just to give us an idea how many of you

[00:06:58.560] have actually read through this or have

[00:07:00.319] ideas around what this thing is so we

[00:07:01.919] know what kind of conversation we're

[00:07:03.120] going to be having today.

[00:07:04.960] >> Is this the one that mentions I think I

[00:07:06.720] saw it as you scrolled up the number of

[00:07:08.560] tool uses that an agent should make.

[00:07:11.199] That's something I remember. I can't

[00:07:12.639] remember if that was talked about here

[00:07:14.000] or not.

[00:07:14.639] >> No, that's not this one. This one does

[00:07:15.919] not talk about the number of tool uses.

[00:07:17.919] >> Okay, so that was like five or something

[00:07:19.360] that I remember.

[00:07:20.720] >> Perfect. In that case, let's just start

[00:07:22.400] with the first one. Designing around the

[00:07:23.919] KV cache. I think that is the most

[00:07:25.599] interesting one out of all of them

[00:07:27.199] because it really inspires

[00:07:29.840] um for everything else around this. And

[00:07:31.599] there's no reason to actually do any

[00:07:32.720] pre-ereading. That's kind of why we have

[00:07:33.919] this conversation over here. Dexter and

[00:07:36.000] I do this stuff for fun and we just get

[00:07:38.240] share about it with you everyone.

[00:07:40.000] >> So, one second. I'm gonna go screen

[00:07:41.599] share, but I think the most important

[00:07:42.800] thing I'm gonna want is a whiteboard.

[00:07:44.240] So, let me pull that up, Dexter.

[00:07:46.400] >> Oh, yeah. Let me let me ship you a

[00:07:47.919] whiteboard.

[00:07:50.400] I'm just gonna buy you a $7 a month for

[00:07:52.880] a whiteboard account. Just Just

[00:07:55.599] >> I don't know if you just like it because

[00:07:56.800] the best part is when you do it, I can

[00:07:58.479] ask you to take the screenshots and not

[00:08:00.000] me. [laughter]

[00:08:02.160] >> Fair enough.

[00:08:03.919] Um, I sent it to you at Slack.

[00:08:07.199] >> Perfect.

[00:08:13.189] And I'm going to go back to screen

[00:08:13.199] sharing. So let's talk about what it

[00:08:14.720] means to design around the K KV cache.

[00:08:17.199] So firstly, when we're act what does it

[00:08:20.319] what what does a KV cache mean? What

[00:08:22.319] what is actually happening? So let's

[00:08:24.400] just start off with the basics of what

[00:08:25.599] an LM is. An LM is a thing that takes in

[00:08:28.639] a bunch of tokens, spits out a bunch of

[00:08:30.720] token probabilities and then you somehow

[00:08:33.200] will apply some algorithm typically like

[00:08:35.440] a soft max or something.

[00:08:38.320] um

[00:08:40.000] to then pick out what is the token that

[00:08:41.919] I should actually be selecting.

[00:08:48.630] And these are just probabilities of

[00:08:48.640] final output tokens. And once you select

[00:08:51.200] your next token, then the LLM will take

[00:08:53.600] this thing back. I don't know how to

[00:08:55.360] draw this arrow, but I suspect will fix

[00:08:57.600] it for me. It'll add this to it'll

[00:09:00.320] append this selected token to the very

[00:09:03.040] next um uh item on the array. and then

[00:09:06.800] it'll just append it and it'll go back

[00:09:08.240] in a loop over and over again. Most of

[00:09:10.320] us probably know this how alams work.

[00:09:12.800] The thing that I think a lot of people

[00:09:14.480] don't realize

[00:09:16.320] is this if you've done software probably

[00:09:19.839] looks like a dynamic programming

[00:09:21.200] problem. This looks like a thing where

[00:09:23.279] you have almost the same array going in

[00:09:25.760] over and over again but then you just

[00:09:27.040] have one new element every single time.

[00:09:29.360] It sounds like we should be able to

[00:09:31.120] repeat some of the math and not have to

[00:09:33.200] redo everything all the time.

[00:09:36.560] If you actually go look into here, what

[00:09:38.320] you'll find is the LM has some

[00:09:40.240] architecture stuff in here that allows

[00:09:41.839] it to not have to repeat all the math

[00:09:43.600] all the time, assuming that you have

[00:09:45.519] some of the stable, some stability

[00:09:47.440] guaranteed. So you can premputee some of

[00:09:49.839] this stuff as a part of the encoder

[00:09:51.440] decoder layer that the LM has inside of

[00:09:53.200] itself. The problem is that precomputed

[00:09:57.760] section is purely dependent on

[00:10:00.880] continuity. So you it's very hard for

[00:10:03.680] you to premputee

[00:10:06.000] um like random segments of it. What you

[00:10:08.720] can do is much easier to premputee

[00:10:10.800] chunks of it along the way. And I should

[00:10:12.320] be using different colors.

[00:10:15.360] So you can premp compute this part, you

[00:10:17.120] can premputee this part, and then you

[00:10:19.360] can premputee this part.

[00:10:21.920] >> I I'm sorry. I'm not quite clear what

[00:10:24.079] like the vertical access means in here.

[00:10:27.040] >> What I mean by here is like the tokens

[00:10:28.399] going in. These are all the tokens that

[00:10:29.920] are in from like index zero. So I should

[00:10:32.240] what I mean by here is like this is

[00:10:33.519] index zero this is index one

[00:10:36.480] and like these are just tokens

[00:10:38.640] >> okay zero index zero index one might be

[00:10:41.440] like

[00:10:43.200] >> the word exactly

[00:10:44.880] >> it would be like

[00:10:45.600] >> think of it like a string that I drew

[00:10:47.040] vertically because of how the model is

[00:10:48.720] laid out and that's easier for me to

[00:10:49.920] think about

[00:10:56.870] >> uh and then you have like index like

[00:10:56.880] >> I see okay so you're caching the first

[00:10:58.640] three words in the sentence and then

[00:11:00.079] once you come back with this next like

[00:11:02.240] once you come back with the the fourth

[00:11:03.839] word in the sentence here that is like

[00:11:06.079] four

[00:11:07.839] uh

[00:11:16.470] and then you ask okay what's the next

[00:11:16.480] token all of all of this part of it

[00:11:18.640] basically is is cached all the math for

[00:11:20.640] this part of it is cached and so you're

[00:11:22.240] just kind of like taking that pre-filled

[00:11:24.880] um whatever they're like matrix of the

[00:11:27.680] meaning of what's being accumulated in

[00:11:29.120] the transformer and so you're just kind

[00:11:31.040] of it's all cost and timing, right? It's

[00:11:33.519] like it's much faster to just say,

[00:11:34.800] "Okay, cool. Now here's the next token.

[00:11:36.640] Now give me the next inference bit."

[00:11:38.240] Right.

[00:11:38.959] >> Exactly. And just to be very clear, like

[00:11:40.800] I know some of you are like, "Ah, but

[00:11:42.880] technically doesn't the walking word

[00:11:44.480] impact what all the other words mean. So

[00:11:45.920] like how can you actually cache this?"

[00:11:47.839] Very

[00:11:48.399] >> great question.

[00:11:50.000] >> Turns out

[00:11:50.399] >> I would not have asked that question.

[00:11:51.680] That's a great question.

[00:11:53.440] >> Well, it turns out the transformer has

[00:11:54.800] like two different parts, encoders and

[00:11:56.160] decoders that are all laid out.

[00:11:58.959] As it turns out, you don't actually run

[00:12:00.640] all the computation all at once. You

[00:12:02.000] actually break down the input string

[00:12:03.279] into smaller subsequences of strings

[00:12:04.959] that then can each be individually

[00:12:07.200] computed and then you can go on stacking

[00:12:09.279] that along the way. So if you go on to

[00:12:11.440] like Enthropic's caching docs,

[00:12:20.550] um we just go here for example,

[00:12:20.560] you'll find that Enthropic has a minimum

[00:12:22.560] cacheable prompt. They do that because a

[00:12:26.639] problem less than 10 24 tokens probably

[00:12:28.639] doesn't fit in whatever cache alignment

[00:12:30.480] block that they have for actually doing

[00:12:31.600] the computation behind some architecture

[00:12:33.279] decisions that they have made. And it

[00:12:35.120] wouldn't make sense for them to catch

[00:12:36.399] that because it's basically throwaway

[00:12:37.680] work because every token outside of 124

[00:12:40.560] is going to cross compete cross um uh

[00:12:43.760] need to do some like cross tension stuff

[00:12:45.279] and actually layer the information

[00:12:46.800] between the words. by the 124 boundaries

[00:12:49.519] they probably have some layer of their

[00:12:50.720] network that can be done in parallel and

[00:12:53.279] have deterministic results. So that is

[00:12:55.600] why it's not just important to go read

[00:12:57.040] the docs but just to understand that

[00:12:58.399] there's some architecture decision that

[00:12:59.839] everyone implementing these models is

[00:13:01.519] going to make that dramatically changes

[00:13:05.519] how fast this works and some of you

[00:13:07.600] might be wondering why is it so much

[00:13:09.120] smaller in opus versus haiku one

[00:13:12.639] intuition I could have I don't know

[00:13:14.720] can't guarantee it is that it's possible

[00:13:17.040] that these haiku models use a different

[00:13:18.639] token vocabulary that is much smaller

[00:13:21.120] than the original models therefore

[00:13:22.480] they're able to compress it better or

[00:13:24.480] these These might be uh these might be

[00:13:26.240] using float 16 instead of float 32 or

[00:13:28.399] float 64. So they can comp double

[00:13:30.480] compress it along the way in terms of

[00:13:32.480] how much data they can stuff into the

[00:13:33.920] same amount of comput computational

[00:13:35.440] unit. But I think the point stands is

[00:13:38.240] that there's some computation in every

[00:13:40.880] uh LLM that can be cached to some degree

[00:13:43.440] of it and that the amount of degree that

[00:13:45.760] can be done is based on how much

[00:13:47.279] similarity you have and how big of an

[00:13:49.200] input space you have that is changing.

[00:13:52.000] But what that is to say is that if you

[00:13:54.639] are constantly running a chat thread and

[00:13:56.399] you're dynamically changing the system

[00:13:57.920] message all the time somewhere in here,

[00:14:00.320] you're basic basically breaking the

[00:14:02.320] entire KV cache every single time. That

[00:14:05.040] means you're having to recomputee all

[00:14:06.560] the work always and you can't take any

[00:14:09.040] benefit of the caching system. That

[00:14:11.040] means

[00:14:11.279] >> so just just to make this a little more

[00:14:12.720] concrete um can I like just draw a

[00:14:16.000] little bit more? So like let's say you

[00:14:17.279] have your your system prompt here.

[00:14:19.360] >> Yeah.

[00:14:20.959] uh system prompt and then you have your

[00:14:23.680] tools are technically like end up part

[00:14:25.040] of the system prompt but I'll just put

[00:14:26.240] them separately. The idea would be like

[00:14:28.320] if at some point you wanted to tell the

[00:14:30.000] agent like okay based on some decision

[00:14:32.320] that's happening way over way over on

[00:14:34.399] the right here uh we want to make sure

[00:14:38.560] that the tool set is like only

[00:14:40.320] browserbased tools or whatever it is.

[00:14:43.680] >> You've basically you're going to get a

[00:14:45.360] slower iteration speed on the max token

[00:14:47.199] that gets generated.

[00:14:48.000] >> Yeah. So when you change this, you

[00:14:49.440] completely if you just like even if

[00:14:50.880] you're just removing stuff, when you

[00:14:52.720] change things, you completely kill the

[00:14:54.720] cache. And so this has to be recomputed

[00:14:56.800] from scratch, which is going to be way

[00:14:58.160] slower and also like four times the

[00:15:00.000] cost.

[00:15:01.279] >> Exactly. There's another subtle thing

[00:15:04.000] that probably isn't even obvious here.

[00:15:05.680] Almost everyone I know that's doing some

[00:15:07.120] sort of chatbot will say like date

[00:15:09.920] in here in their system prompt

[00:15:12.320] >> and that

[00:15:14.880] >> that's killing the KV cache for no

[00:15:17.040] reason. You're literally just hurting

[00:15:18.320] the cash every single time.

[00:15:20.160] >> I mean, if you include the time, right?

[00:15:22.240] If you just put the date, it might be

[00:15:23.760] okay, right?

[00:15:24.720] >> Yes. If you're putting the date, sorry,

[00:15:26.160] I should you are correct on that.

[00:15:28.000] There's some time resolution that you're

[00:15:29.680] definitely killing the KB cache. But

[00:15:31.680] even if you don't include the date, if

[00:15:33.360] you have a longunning thread, like last

[00:15:34.720] time we talked about DRM that was coming

[00:15:36.880] through from that uh last time, the

[00:15:39.519] problem with DRM is it's a long process

[00:15:41.600] >> decaying resolution memory. There's like

[00:15:43.199] the context engineering for a model that

[00:15:44.959] can remember stuff that happened months

[00:15:46.560] ago.

[00:15:47.279] >> Exactly.

[00:15:47.760] >> Not a model, but an agent.

[00:15:49.120] >> But in that case, today's date is going

[00:15:50.880] to break the KV cache all the time.

[00:15:52.959] You're just going to be slower for the

[00:15:54.399] entire workload that's happening. It's

[00:15:56.480] generally always going to be good to put

[00:15:58.320] the dynamic stuff of your system as late

[00:16:00.240] as possible. That means if you have a

[00:16:02.720] giant chat thread that you're running

[00:16:04.079] on, it might actually be if you want

[00:16:06.800] like the best performance.

[00:16:09.199] Why is why can't I not draw a rectangle?

[00:16:11.440] it's probably going to be better for you

[00:16:13.040] to have system prompt or your chat

[00:16:15.040] messages and then your like dynamic

[00:16:17.519] variables at the very end because then

[00:16:19.839] as your chat message grows, you're

[00:16:22.000] actually going to have the ability to KV

[00:16:24.240] cache a chat history as well along with

[00:16:27.839] everything else. So it's better to say

[00:16:29.120] today's date at the very end of this

[00:16:33.920] rather than putting it anywhere

[00:16:35.920] beforehand even at the end of the system

[00:16:37.519] message.

[00:16:40.399] I don't know if these kinds of things I

[00:16:42.240] see

[00:16:42.720] >> align with what

[00:16:43.680] >> this is.

[00:16:44.480] >> So I imagine you're going to go to the

[00:16:46.079] point of like oh if you really want to

[00:16:47.360] dynamically change the tools and you

[00:16:49.199] don't want to think about what we're

[00:16:50.399] about to go to which is like using the

[00:16:52.480] like log probabilities and like zeroing

[00:16:54.800] things out to remove them from the from

[00:16:57.199] the tool set that you could change your

[00:16:59.199] tools and put the tools at the end of

[00:17:00.720] the context window instead of at the

[00:17:02.000] beginning.

[00:17:03.839] >> Exactly. So if you're not if same thing

[00:17:06.000] with the tool set like if you want to

[00:17:07.600] dynamically change your tools you got to

[00:17:09.280] put them at the bottom. If you put them

[00:17:11.199] at the top you are just shooting

[00:17:12.720] yourself in the foot in this system. You

[00:17:14.880] will just get slower API calls more

[00:17:16.640] expensive API calls with no real benefit

[00:17:18.720] that you're really having. There's a

[00:17:21.199] secondary benefit that you get for free

[00:17:23.199] um which is at the very very end if you

[00:17:26.319] put things down here the model is just

[00:17:27.679] likely to pay more attention to it. So

[00:17:29.120] anything that is actually relevant and

[00:17:30.640] highly dynamic, it's way easier to

[00:17:33.120] guarantee that the model won't

[00:17:34.080] accidentally forget it because it has

[00:17:35.440] recency bias in general. So question

[00:17:38.400] like application of that um and I think

[00:17:40.160] that's this is maybe also in the paper

[00:17:41.840] and like I've actually like was doing

[00:17:44.000] some more like reverse engineering of

[00:17:45.440] cloud code with a proxy the other day

[00:17:47.360] trying to figure out what the to-do tool

[00:17:49.440] does and like what I would think would

[00:17:51.120] be hey once you write to the to-dos the

[00:17:52.880] system will occasionally reingject the

[00:17:55.600] list of to-dos near the end of the

[00:17:57.120] context window and say hey by the way

[00:17:59.120] here's what you said you were going to

[00:18:00.240] be working on and so you force the

[00:18:01.919] attention to be on that stuff rather

[00:18:03.840] than like hoping that claude will

[00:18:05.679] remember it did that 15 turns ago.

[00:18:08.480] >> Exactly. And that's kind of what one of

[00:18:10.960] the steps down here talks about. Oh,

[00:18:12.799] bump dashing doesn't really matter. Uh

[00:18:14.880] in the manus paper where they release

[00:18:17.440] some of the same stuff which is

[00:18:23.990] >> where is this?

[00:18:24.000] Where's the repetition one? Oh,

[00:18:26.559] repetitation. So the whole point of this

[00:18:28.640] is saying the same thing.

[00:18:29.760] >> Oh yeah, this is it.

[00:18:30.559] >> Simply just stacking stuff all the way

[00:18:32.400] down. Eventually, your information will

[00:18:34.960] get lost. It's not a just like with a

[00:18:37.840] normal human, if you gave them a giant

[00:18:39.280] to-do list of everything to do and you

[00:18:40.799] have one single paper at the very front

[00:18:42.480] that they have to somehow remember, they

[00:18:44.400] will forget steps. We build processes in

[00:18:47.120] place to make sure that stuff gets

[00:18:48.559] duplicated and done more than once in

[00:18:50.320] like high yield scenarios. If I have a

[00:18:52.799] rocket ship that's going to launch, I

[00:18:54.640] will make sure 15 people make check

[00:18:56.559] every single thing because it's just way

[00:18:58.320] less likely that someone will slip up

[00:18:59.679] and make a mistake on all different

[00:19:00.880] things. the model kind of behaves

[00:19:03.120] similarly as well. The more steps you

[00:19:05.200] put on it and as the models get better,

[00:19:06.880] the distance between how long it can

[00:19:08.799] remember and what can remember does go

[00:19:10.160] up. That's undeniably true. But there's

[00:19:13.600] always a distance at which it will never

[00:19:15.280] work as well. So having some repetition

[00:19:17.440] in there is going to make a huge impact

[00:19:19.840] on your output quality for that same

[00:19:21.840] reason. Because what they're really

[00:19:23.840] saying here is like they found that you

[00:19:25.200] can do about 50 tool calls to actually

[00:19:27.760] produce their task, but most models will

[00:19:29.520] basically go off track somewhere in the

[00:19:31.280] middle. really really fast. What we

[00:19:33.520] found in general and like why does this

[00:19:36.080] happen? Well, if you think about how

[00:19:37.520] attention works, you'll often see the

[00:19:38.799] needle in the haststack problem as a

[00:19:40.640] giant benchmark that people go and

[00:19:42.000] evaluate for.

[00:19:43.679] >> Well,

[00:19:44.080] >> terrible benchmark.

[00:19:45.440] >> I don't know about terrible benchmark,

[00:19:46.720] but like in general in English language,

[00:19:49.600] it makes sense that words near each

[00:19:51.679] other have way more impact than words

[00:19:53.440] far away from each other. It's just the

[00:19:56.880] any sort of data set that you're going

[00:19:58.320] to go train on is always going to have

[00:20:00.160] that the sentence I said at the very

[00:20:02.480] beginning of this uh talk matters way

[00:20:05.520] less than the sentence I just said two

[00:20:07.200] minutes ago and that's the whole point

[00:20:09.840] cont

[00:20:10.559] >> well it matters way less to what you're

[00:20:12.400] about to say next

[00:20:13.679] >> yes sorry yes exactly and that's the

[00:20:16.000] same thing the model is going through

[00:20:17.840] the thing that I want to produce over

[00:20:19.600] here is way way more likely to be

[00:20:22.559] related to something that I'm linking

[00:20:24.799] over here. I don't know how to connect

[00:20:26.480] those than it is to be something I'm

[00:20:27.919] linking over here. Now, that it's true

[00:20:31.120] that system messages

[00:20:34.400] are special and I do want system message

[00:20:36.400] to be treated differently and that's why

[00:20:37.840] the model trainers are working on

[00:20:39.200] training the model to understand that

[00:20:40.720] better. That system messages do have

[00:20:42.799] impact throughout the entire span of the

[00:20:44.480] conversation. But that's a training task

[00:20:46.960] and we can wait for the models to get

[00:20:48.720] trained to do that better. But we don't

[00:20:51.200] have that guarantee. So the easiest way

[00:20:53.440] to provide the guarantee and just to get

[00:20:54.720] the best results is to again just put

[00:20:57.600] things that are most relevant to what

[00:20:59.120] the user needs to do as close to what it

[00:21:00.880] needs to happen next. So if I need to

[00:21:03.360] complete a new task and I know that the

[00:21:05.200] model just checked off. Let's say I I'm

[00:21:07.280] building clawed code and the model just

[00:21:09.600] finished task one,

[00:21:12.000] I should probably repeat the task list

[00:21:13.679] again, assuming I'm using a very dumb

[00:21:15.520] model to say this is the task, which

[00:21:17.840] task should you do next? it's just going

[00:21:20.480] to work better than just having the task

[00:21:22.400] at the top saying I completed task one

[00:21:24.240] now what do I do next because the

[00:21:26.080] distance is just further and in that

[00:21:28.400] case I happen to know exactly what needs

[00:21:30.720] to happen which is I need to make

[00:21:32.080] progress on a task list so it's easy for

[00:21:34.559] me to manually inject that but the more

[00:21:37.520] I can do that sort of behavior the more

[00:21:40.960] um consistency I'll get out of my model

[00:21:43.679] outputs

[00:21:45.120] >> and this this just feels like another

[00:21:46.799] recitation of kind of that same theme of

[00:21:48.720] Like, yeah, you could just go back and

[00:21:50.559] forth with the model forever and use the

[00:21:52.240] default like tool call tool tool call

[00:21:54.080] tool call context window, but if it lets

[00:21:56.880] you push your accuracy by 5% or your

[00:21:59.600] speed or your cache efficiency by 5%,

[00:22:01.760] then why not engineer the thing to be as

[00:22:04.880] good as possible?

[00:22:06.159] >> Exactly. Exactly.

[00:22:09.039] Um, there's two questions really fast

[00:22:11.039] and I want to make sure we talk about

[00:22:12.080] them before we go too deep. Um,

[00:22:13.919] >> oh, sorry. I know I'm supposed to be on

[00:22:15.440] question duty. If you have users using

[00:22:17.840] the same models, how will this cache be

[00:22:20.000] h how this cache will be preserved

[00:22:21.679] between the same user calls? Well, the

[00:22:24.159] way that the model providers do this,

[00:22:25.360] the caching is not something you own

[00:22:26.559] unless you're actually running it on

[00:22:27.840] inference. If you do, then you can

[00:22:29.280] control how long the cache runs. The

[00:22:31.039] model bas the model providers basically

[00:22:32.799] compute some of this work ahead of time

[00:22:35.039] and they just save it into like some

[00:22:36.720] data structure, probably a Reddit cache

[00:22:38.000] or something. I have no idea what they

[00:22:39.120] use under the hood and they just say,

[00:22:41.200] "Hey, if we get the sequence of tokens

[00:22:42.559] again, just pull this data out." It's

[00:22:44.480] almost independent

[00:22:46.720] of your user message because uh Dexter

[00:22:50.320] says this all the time. The only thing

[00:22:51.520] that impacts the model is actually like

[00:22:53.200] tokens in tokens out. So like the fact

[00:22:56.880] that it's a user doesn't really matter.

[00:22:58.320] The model doesn't know that. OpenAI

[00:23:00.080] anthropic don't need to know that as

[00:23:01.600] well. And that's how they kind of um

[00:23:04.480] manage this. Hopefully

[00:23:06.480] >> I think in general most of them will not

[00:23:08.400] preserve the same cache between like

[00:23:10.480] technically if it's content addressable

[00:23:12.240] then like the the hash of the content

[00:23:14.080] will always be the hash of the content.

[00:23:15.440] So you're not leaking you know

[00:23:17.600] precomputed attention between users but

[00:23:20.400] like I think technically people still do

[00:23:22.320] segment it out where it's like hey

[00:23:23.760] you're never going to use the cache from

[00:23:25.200] another user. Yeah, I assume that they

[00:23:27.760] did it. Um

[00:23:30.799] I assume that they did it uh because of

[00:23:33.600] uh oh Eugene I yes that is also true.

[00:23:36.720] The model also has its own cache that

[00:23:38.400] computes stuff because of the

[00:23:39.600] architecture. I'm assuming the caching

[00:23:41.679] the model providers are doing are

[00:23:43.120] slightly different. I think that also

[00:23:44.559] helps quite a lot. The actual inference

[00:23:46.880] time is also faster if you have repeated

[00:23:48.720] tokens. Maybe that is what the paper is

[00:23:51.280] talking about and I misinterpreted that.

[00:23:54.320] Um, but really quickly, I suspect the

[00:23:57.039] model providers don't do the caching

[00:23:58.640] storage per on a across user bases

[00:24:00.640] because they need to have TTLs and those

[00:24:03.120] TTLs are really based on your personal

[00:24:04.720] usage, not on anyone else's. Um, raycast

[00:24:07.919] is a fantastic way to test this out

[00:24:09.840] quickly and locally. Can you introduce

[00:24:11.760] you can introduce dynamic variables? Is

[00:24:13.279] there something else you would use for

[00:24:14.480] the similar purposes? I don't know about

[00:24:15.919] something myself, Jensen. Um,

[00:24:19.520] >> I was just thinking about like a quick

[00:24:21.279] snippet copy paste tool. I don't know if

[00:24:23.120] you store prompts in anything else or if

[00:24:25.440] you have a local thing that you guys

[00:24:26.799] use. I have my own other setup myself

[00:24:29.919] including that. So, just curious.

[00:24:33.600] >> I don't have anything, Dex.

[00:24:35.440] >> Yeah. No, I mean I think I think part of

[00:24:37.200] it is like this is this is a lot more

[00:24:38.960] about like building like this this is

[00:24:41.120] more applicable to like building

[00:24:42.480] software that interacts with models than

[00:24:44.640] for like how you prompt them.

[00:24:46.880] >> Yeah. Yeah. No, I I get that. Um, but I

[00:24:49.840] guess as I iterate, I still test things

[00:24:52.720] locally before I like would put them

[00:24:55.760] into what I'm actually going to use. I

[00:24:58.480] don't know if that makes sense in the

[00:25:00.000] way I'm thinking of it, but

[00:25:03.120] uh if I'm iterating on a prompt

[00:25:05.039] essentially or a structure or workflow

[00:25:07.200] that I'm going to be implementing

[00:25:08.640] through a series of orchestrating

[00:25:10.799] agents, I will iterate on each part of

[00:25:13.200] that separately

[00:25:15.039] through using some sort of way to

[00:25:17.039] iterate on the snippet. basically. And

[00:25:19.520] >> I mean, Vibbop's got a lot of opinions

[00:25:21.039] on how to iterate on prompt snippets.

[00:25:22.799] Maybe we'll get

[00:25:23.520] >> So that's I guess that's where I my

[00:25:24.960] mind's at right now. So sidetracked.

[00:25:27.279] >> I would say like none of this none of

[00:25:29.039] the stuff that we're talking about today

[00:25:30.320] really matters for prompt iteration

[00:25:32.000] speed. That that really doesn't matter.

[00:25:34.640] This only matters for like you have a

[00:25:36.400] prompt, it's working, but you want to

[00:25:38.240] make that thing work faster and better.

[00:25:40.080] How do you go do that?

[00:25:42.320] Cool. Um how should how do we know the

[00:25:44.720] tlet is or isn't cached? uh should there

[00:25:47.039] shouldn't this be managed as it changes?

[00:25:49.760] Yes. Uh to some degree, but really

[00:25:52.320] there's only one way to know that it's

[00:25:53.840] cached, which is if the model provider

[00:25:55.120] tells you that. If they don't actually

[00:25:56.080] give you that information, you can't

[00:25:57.360] possibly know. So, it really depends on

[00:25:59.840] the inference provider.

[00:26:01.279] >> I mean, you can kind of proxy it because

[00:26:03.279] of latency, [clears throat] but not

[00:26:05.039] really definitively.

[00:26:07.440] >> See, this is why me and Vibbove work

[00:26:08.960] well together is he's really good at

[00:26:10.400] just talking through my random questions

[00:26:12.559] and finishing his point. So, please keep

[00:26:14.480] doing that. Um question though like are

[00:26:17.200] you gonna show us today how to use a a

[00:26:21.200] LM client to actually look at the

[00:26:22.960] responses and see the like caching to

[00:26:25.679] like the caching like headers that come

[00:26:27.760] back like I I think that would be super

[00:26:29.520] super valuable to like untangle like the

[00:26:32.240] whether or whatever untangle the

[00:26:34.000] response and see like hey look let's

[00:26:35.600] change the end of it and see how many

[00:26:37.919] cache tokens we got versus changing the

[00:26:39.919] beginning and see that it blows the

[00:26:41.200] cash.

[00:26:42.400] >> Yeah that should be possible. Uh Eugene

[00:26:45.200] had a really good point actually and I

[00:26:47.039] realized I actually had totally missed

[00:26:48.640] this which is there's actually two types

[00:26:51.039] of caching that are going on here which

[00:26:52.960] is one caching done by the actual model

[00:26:56.159] providers in terms of helping with

[00:26:58.000] encoder decoder blocks and then the

[00:27:00.240] actual transformer architecture also

[00:27:01.679] allows you to do another type of cache

[00:27:03.679] in there. Um

[00:27:05.760] I think I can pull this up

[00:27:12.870] architecture. Let's see if I can put up

[00:27:12.880] there's a very famous image.

[00:27:20.950] I put up but basically

[00:27:20.960] uh let's see if I can find this.

[00:27:24.960] Basically a lot of the actual uh nodes

[00:27:27.120] in here a lot of the math can also be

[00:27:28.960] precomputed along the way at any point

[00:27:31.200] in the way. The part that I was talking

[00:27:32.960] about was actually this part which is

[00:27:34.960] the encoder node of the uh transformer

[00:27:37.360] can actually be precomputed based of the

[00:27:39.039] actual um uh input tokens that are going

[00:27:42.320] in and this whole layer can almost be

[00:27:43.919] cached because it's not really dependent

[00:27:46.000] on the output probabilities and these

[00:27:47.760] are going to be able to take some

[00:27:49.279] advantage of that. The second half of

[00:27:51.200] this that Eugene is talking about is

[00:27:53.440] also the K there's a KV cache in the

[00:27:55.919] actual model like matrix multiplication

[00:27:57.760] areas and those can also uh dramatically

[00:28:01.520] improve the amount of computation

[00:28:02.720] throughput you can get out of the actual

[00:28:04.720] transform architecture that may be

[00:28:06.720] actually what the paper is talking about

[00:28:07.760] Eugene I may have missed that

[00:28:09.600] >> yeah I think it is about the cache

[00:28:12.240] inside the model

[00:28:13.520] >> yes um so in that case it's still the

[00:28:16.080] principle is still the same

[00:28:17.760] >> everything's the same except nothing's

[00:28:19.120] going into reddice I probably is the the

[00:28:21.520] key detail.

[00:28:22.880] >> Yes. Well, no, that one's cutting down

[00:28:24.559] on the actual math that it has to go do.

[00:28:26.399] But the main difference is the the

[00:28:28.480] premise is still the same. The number of

[00:28:30.559] continuity tokens you have dramatically

[00:28:32.640] changes the amount of caching that

[00:28:35.200] you're going to get. Anytime you go

[00:28:37.520] change the continuity of the tokens, the

[00:28:39.679] more likely you are going to be to break

[00:28:41.440] the cache at any point and get a miss on

[00:28:43.919] the cache.

[00:28:45.679] Um, how do I how do I eval if my updated

[00:28:48.240] context handling uh will

[00:28:51.679] improve the quality? Um, I think we've

[00:28:54.960] had a couple talks on evals. It's

[00:28:56.559] actually very annoying to do evals and

[00:28:59.440] it's very frustrating, but I think the

[00:29:00.799] first step to do evals is just to define

[00:29:02.399] quality to some degree and what it

[00:29:04.159] means. Understand what is clearly good,

[00:29:06.000] what is clearly bad, what is mostly

[00:29:07.440] good, mostly bad, and then just like buy

[00:29:09.600] be valid in the beginning. And once you

[00:29:11.200] have a better understanding of that

[00:29:12.880] system, then you can go ahead and

[00:29:14.080] actually make these trade-offs. The only

[00:29:15.679] reason that the likely can do this work

[00:29:17.679] or any engineering team can do this work

[00:29:19.360] is because they first have to go ahead

[00:29:20.799] and say this is good and this is bad.

[00:29:23.279] The eval are useless.

[00:29:25.840] >> And I'd say like most of the stuff we

[00:29:27.679] talk about about eval here is about

[00:29:30.720] quality of the outputs in terms of like

[00:29:32.880] accuracy, hostations, using the right

[00:29:35.039] context, things like that. um the

[00:29:37.520] quality improvements that we're getting

[00:29:39.200] here because like at the end of the day

[00:29:40.640] whether you cash it or not it's the same

[00:29:42.159] tokens in which means your chance of

[00:29:43.679] getting the right tokens out is probably

[00:29:45.360] about the same. Um so this is a really

[00:29:47.760] interesting kind of category of eval

[00:29:49.679] talked as much about which is like how

[00:29:51.039] do you evaluate the performance not in

[00:29:53.279] terms of accuracy but in terms of uh

[00:29:56.720] speed and cost.

[00:29:58.320] >> Yeah. Um I think VJ asked an interesting

[00:30:01.120] question. I guess it's Rajes point out a

[00:30:03.360] different thing. If the model weights

[00:30:04.320] are the same, everything is new, how do

[00:30:05.679] you actually get caching? Um, it's

[00:30:08.320] really hard to describe how the math on

[00:30:10.720] a GPU gets cached, but you can do

[00:30:12.799] caching on there. Uh, you should take my

[00:30:14.960] word for it. There's a beautiful video

[00:30:16.399] made by um, if any of you are interested

[00:30:19.600] how this is a this is probably one of

[00:30:22.159] the best videos I've ever seen.

[00:30:24.799] >> Hey everyone, I'm by

[00:30:27.760] >> I'm sorry. I I every time I pull up the

[00:30:31.120] YouTube channel, I I hear I hear you

[00:30:33.120] introducing

[00:30:33.679] >> I'll post the video on here. There's

[00:30:34.880] like a I think uh there's like a

[00:30:36.720] 90-minute video that I watched that

[00:30:38.000] actually talked about how deepseek

[00:30:39.520] actually works under the hood and talks

[00:30:40.799] about the math behind it. Um I think

[00:30:42.640] it's actually this one by

[00:30:45.120] >> this one of the best ones I've ever

[00:30:46.240] seen. It will describe it. It'll

[00:30:47.600] probably teach you more about um

[00:30:51.200] anything you could see. I wish I could

[00:30:52.960] make [laughter]

[00:30:55.200] >> John best video I ever seen pulls up

[00:30:57.600] video of self

[00:30:59.200] >> and it'll talk to you about like how

[00:31:00.640] it's possible to get way better

[00:31:02.000] throughput than anyone else can on the

[00:31:03.919] same math that everyone else is doing.

[00:31:06.720] >> Um

[00:31:08.640] context caching in our app thesis code

[00:31:10.640] is open source if anyone Okay, cool.

[00:31:12.320] There's just an example. If Duck has an

[00:31:14.240] example, then definitely share it, Doug.

[00:31:15.600] And we'd love to have people go be able

[00:31:17.440] to see it.

[00:31:18.399] >> Yeah, drop it in the chat.

[00:31:20.000] >> VJ, we've got a question. We'll take

[00:31:21.360] that and then we'll go to the next part

[00:31:22.559] of the system after that.

[00:31:25.360] >> So if I understood this correctly, uh

[00:31:29.360] for example, let's say our uh model has

[00:31:31.679] an input uh window of 256k tokens and

[00:31:35.279] we're trying to uh let's say take

[00:31:37.360] advantage of that entire context window.

[00:31:39.519] So essentially what you're saying is

[00:31:41.039] whatever we input in that 256k context

[00:31:44.559] uh as much as possible

[00:31:47.360] uh that string should be uh unchanging

[00:31:51.279] or let's say static it should be the

[00:31:53.120] same in next iteration so that you can

[00:31:54.960] get the next token quicker and the end

[00:31:58.320] of that uh input context will probably

[00:32:01.200] be varying per call. So I think the next

[00:32:04.080] step would be to understand how agents

[00:32:06.640] are iterating between different calls

[00:32:08.559] and see what is changing what is not

[00:32:10.240] changing in what we are sending the LLM

[00:32:12.799] and sort of restructure that entire

[00:32:15.039] input uh sequence. Is that is that is

[00:32:17.840] that the next step like is am I thinking

[00:32:20.080] about this correctly? I

[00:32:21.919] >> I think maybe I just maybe I didn't

[00:32:25.120] understand all the words you said

[00:32:26.159] perfectly and it's probably because I

[00:32:28.080] woke up at 4 a.m.

[00:32:28.880] >> Okay, let me simplify it. So we are

[00:32:30.799] sending tokens to the LLM.

[00:32:32.960] >> Yes.

[00:32:34.080] >> The sequence of tokens as much as it is

[00:32:36.799] unchanged the faster we get a response.

[00:32:39.919] >> Yes.

[00:32:40.640] >> Therefore our next step would obviously

[00:32:42.960] be to understand uh a couple of

[00:32:45.519] iterations of what we are sending the

[00:32:47.200] LLM see what is changing what is not

[00:32:49.519] changing and try to restructure that.

[00:32:51.600] Correct.

[00:32:52.399] >> Yes. Exactly. There's

[00:32:54.720] >> there are caveats though in terms of

[00:32:56.240] actual implementation details here that

[00:32:58.000] matter. If you own the model yourself

[00:32:59.840] and you're doing inference, it's a very

[00:33:01.200] different game than if you're actually

[00:33:02.399] using the existing inference providers.

[00:33:04.480] So for example, Enthropic lets you

[00:33:07.200] actually control cache control with this

[00:33:08.799] cache control block. And where you put

[00:33:10.960] it dramatically matters because if you

[00:33:13.440] put at the very beginning of a system,

[00:33:15.039] if you put it your system message, it

[00:33:16.559] will dramatically change the throughput

[00:33:18.399] that you are personally able to get. If

[00:33:20.640] you have a really long chat thread and

[00:33:22.000] you just put it at the beginning of a

[00:33:23.279] chat thread and you don't break apart

[00:33:25.039] your chat threads manually, you're going

[00:33:27.519] to get worse hits. There's just nothing

[00:33:29.360] you can do about that because your chat

[00:33:31.039] thread is basically you put you put a

[00:33:32.799] cache control block on the first user

[00:33:34.399] message and then you in the same chat

[00:33:36.399] control block you put another user

[00:33:37.840] message. It's just a cache miss. It's a

[00:33:40.559] guaranteed cache miss. You can't

[00:33:41.919] actually do anything about that.

[00:33:44.159] So every time you're not reconstructing

[00:33:45.840] the prompt in the same way as close to

[00:33:47.760] possible, you are basically getting a

[00:33:50.640] miss. Gemini, I think I think the way

[00:33:52.880] OpenAI does caching is opaque. So what

[00:33:56.559] that means is I I think they give you

[00:33:59.039] almost no information on how caching

[00:34:01.039] works. But I think they actually what

[00:34:03.760] they do but

[00:34:05.120] >> it's like less control, but they kind of

[00:34:06.640] just try to do it for you. This is a lot

[00:34:08.159] of them just like do a prefix and try to

[00:34:10.000] guess how to do it. I didn't need

[00:34:12.000] actually know this,

[00:34:13.040] >> but now they added like a prompt cache

[00:34:14.800] key. So, it's like

[00:34:18.079] >> prompt cache. And the reason that they

[00:34:20.240] do this, I'm certain uh replace the

[00:34:23.200] user. I don't know what this is, but I'm

[00:34:25.040] pretty certain that the reason they do

[00:34:26.320] this is people just wanted more control

[00:34:27.839] because if you're able to have access to

[00:34:29.520] this and you can control this, you can

[00:34:30.800] just get better hits all the time. Um,

[00:34:34.399] but it is important to go read this

[00:34:36.079] stuff. And the only way you can actually

[00:34:37.359] know if you're hitting this is just by

[00:34:38.480] looking at the usage. There's no other

[00:34:40.399] way to really know

[00:34:42.720] um along unless you own the inference

[00:34:44.960] and most people don't own inference as

[00:34:46.399] far as I know u and most people probably

[00:34:48.639] shouldn't own inference as well. Uh,

[00:34:51.359] Gemini is probably the most flexible

[00:34:54.320] thing I have seen for how they cache and

[00:34:55.919] Eugene is right on that, which is if you

[00:34:58.640] actually go look into how to get caches,

[00:35:00.079] like you do a you do some crap to go

[00:35:03.040] write this code, but the trade-off of

[00:35:05.760] doing this crap is you do get to go get

[00:35:08.720] complete control over what it's doing

[00:35:11.119] and you get to go tell it this and that

[00:35:14.000] helps you as a developer, but it also

[00:35:16.240] hurts you because you have to go build

[00:35:17.440] this stuff yourself.

[00:35:19.440] Um, you also have to manage the TTL and

[00:35:21.040] everything automatically. So, there's

[00:35:22.079] always a trade-off in how much

[00:35:23.200] engineering effort you want to put in

[00:35:24.480] versus what you want to do manually. Uh,

[00:35:26.400] what you want to do automatically. And

[00:35:28.240] generally, if you do something manually,

[00:35:29.680] you will always get better throughput if

[00:35:31.119] you know what you're doing than someone

[00:35:32.480] that does it automatically. But someone

[00:35:34.800] that does it automatically will always

[00:35:36.160] get better than someone that doesn't

[00:35:37.280] know what they're doing manually

[00:35:40.000] because if you blow the cache up time,

[00:35:41.599] it'll be worse.

[00:35:42.720] >> So,

[00:35:43.119] >> okay. So, if you know if you know what

[00:35:44.320] you're doing, use the cache keys. If you

[00:35:45.839] don't, hope for the prefix things. But

[00:35:47.839] don't try to mess with the cache keys if

[00:35:49.440] you don't if you're not willing to go

[00:35:50.960] learn how these systems work.

[00:35:52.800] >> Exactly. And lastly, if you're not act

[00:35:54.640] and if you don't have the time to go

[00:35:55.760] learn how they work, it's not a matter

[00:35:57.119] of like you don't want to. Sometimes you

[00:35:58.320] just don't have the time. We're all

[00:35:59.359] bouncing a lot of things at once. Um but

[00:36:02.240] what comes down to is if your cache

[00:36:03.760] isn't working, you now know why it isn't

[00:36:05.760] working. It's because your prefix key is

[00:36:07.520] not continuous and it's breaking somehow

[00:36:09.599] when whatever system you're using to

[00:36:10.960] break it, you're getting a cache miss

[00:36:12.320] for that reason.

[00:36:14.240] Um, I think the next thing I want to

[00:36:15.680] talk about

[00:36:17.520] is actually talking about this one. The

[00:36:20.800] we talked about recitation a little bit.

[00:36:22.320] So like recite your systems. Think about

[00:36:24.640] what makes sense in your workflows to

[00:36:26.480] recite this. And it can do all sorts of

[00:36:29.119] different things. So for example in the

[00:36:31.200] example that they gave over here what

[00:36:33.200] they're showing in their visual is hey

[00:36:34.800] instead of producing context one and

[00:36:36.400] doing this what I will say is before

[00:36:39.040] even producing action for I will inject

[00:36:42.400] an objective into the statement and now

[00:36:45.280] I can go and produce objective 4. So

[00:36:47.760] there's different ways to go repeat

[00:36:49.599] yourself in the prompt. There's one is

[00:36:51.599] just add it to the very end. One is take

[00:36:53.920] your existing prompt and go inject it

[00:36:56.160] somewhere else in my history. And yes,

[00:36:59.280] this is kind of contradictory to what we

[00:37:00.720] just talked about about breaking the

[00:37:01.920] cache key, but you're doing this

[00:37:04.320] deliberately because you're trying to

[00:37:05.440] get accuracy. So you're like, "Okay,

[00:37:06.640] cool. I will lose the cache on this part

[00:37:08.400] of my prompt. I will still preserve the

[00:37:10.320] cache on everything up until here, but I

[00:37:12.240] will do that in favor of getting

[00:37:13.359] slightly better accuracy and helping the

[00:37:15.440] model understand what's going on."

[00:37:18.640] And the premise here is this objective.

[00:37:20.800] It may be obvious to the model at this

[00:37:22.560] point that action three was best. But

[00:37:24.560] when it's making action four, the model

[00:37:26.320] might forget that because of this

[00:37:28.000] objective, action three was selected

[00:37:29.599] here. So I'm repeating that here's

[00:37:31.680] objectives and this is why you picked

[00:37:33.119] action three. Now pick action four. I

[00:37:35.920] can also just say

[00:37:37.280] >> go ahead.

[00:37:38.320] >> Has anyone ever implemented this like

[00:37:40.320] kind of deterministic injection of a

[00:37:42.800] to-do list into the context window as

[00:37:45.760] it's going?

[00:37:46.720] >> I would be surprised if cloud code

[00:37:48.400] doesn't do something like this. That's

[00:37:50.400] what I'm I'm messing with that idea

[00:37:52.720] right now is what I

[00:37:54.640] >> Cool.

[00:37:55.119] >> Yeah. doing.

[00:38:01.030] >> Cool.

[00:38:01.040] >> Um, so this one I think is really

[00:38:02.720] straightforward and easy to iterate on.

[00:38:04.079] So if you're finding that you have

[00:38:05.040] really really long tool call sequences

[00:38:06.640] and they're diverting from or drifting

[00:38:08.400] from the main action, just like add some

[00:38:10.160] repetition there and you might just get

[00:38:11.839] free throughput uh without having to do

[00:38:14.000] much work. And I think that's that's the

[00:38:15.839] cool thing about this trick. This is

[00:38:16.960] almost no effort.

[00:38:19.440] Um, I want to talk about this. This is

[00:38:21.200] something that we've talked about a lot,

[00:38:23.359] which is a lot of times when in an agent

[00:38:25.520] loop, it'll try and go do many things

[00:38:27.359] and then it will go ahead and go correct

[00:38:29.920] things along the way.

[00:38:32.160] And in this case, I think what they

[00:38:34.560] found is they found in their scenario

[00:38:36.640] keeping if they're running two things in

[00:38:38.240] parallel, getting all the predictions,

[00:38:40.079] actually having the incorrect stuff

[00:38:41.599] helps them. I would just go experiment

[00:38:44.480] and try this. What we have found is

[00:38:46.640] having the incorrect stuff hurts in some

[00:38:48.640] scenarios, but it's possible in their

[00:38:50.320] use case because they're running like on

[00:38:52.240] average at least 50 tool calls that

[00:38:54.240] perhaps having incorrect sequences helps

[00:38:56.000] the model correct itself and not repeat

[00:38:57.680] the same behavior in the case of very

[00:38:59.839] repetitive actions. Eugene, you

[00:39:01.920] >> funny because this is this is contrary

[00:39:03.760] to advice we give a lot, which is like

[00:39:05.680] be smart about sometimes pulling those

[00:39:07.440] out because it becomes very noisy.

[00:39:10.000] >> Yeah, Eugene, you've got a question.

[00:39:11.599] >> Yeah, I got a question. Um yeah, I think

[00:39:13.680] this one on the incorrect observations

[00:39:16.000] is quite intuitive to me. One thing

[00:39:17.440] that's also not so intuitive to me is

[00:39:19.280] the tool call. Do you just store do you

[00:39:22.320] just return to the main model, the main

[00:39:24.160] agent, the output of the tool call or do

[00:39:26.480] you also keep the tool call itself?

[00:39:31.040] So I have different opinions on this and

[00:39:32.960] I think the thing that they're saying

[00:39:34.480] here is so I found when I was reading

[00:39:37.200] this is like I think the reason that

[00:39:39.760] they're seeing this it's that often

[00:39:41.920] having a stack trace helps even a

[00:39:44.000] developer debug the problem and I think

[00:39:47.119] what they're I think the re because this

[00:39:49.680] feels very wrong to me as well but I

[00:39:51.920] think what's happening is manis has a

[00:39:53.839] very broad scope of what it's trying to

[00:39:55.520] do so many times a model will divert and

[00:39:58.240] not do the right thing and in that

[00:40:00.240] scenario assuming that it has to do that

[00:40:02.000] thing again or some it's somewhat

[00:40:03.760] related to the final goal and it might

[00:40:05.359] have to repeat that task again. it's

[00:40:07.359] more likely that the model will get it

[00:40:08.720] right the first time around. If we can

[00:40:10.400] kind of look at it stack trace and say

[00:40:12.000] what did it take to get to the final

[00:40:13.359] correct answer.

[00:40:15.920] That said, I'm not actually yet

[00:40:17.839] convinced that the best way to represent

[00:40:19.839] the tool calls are actually the tool

[00:40:21.520] calling systems that people have. I

[00:40:24.000] think there's a lot more

[00:40:25.280] >> really you think there's a better way to

[00:40:27.280] represent tool calling.

[00:40:29.359] >> Well, I don't know if that's sarcastic

[00:40:30.480] or not, but like even [laughter]

[00:40:32.640] there's like a interesting thing. I'm

[00:40:35.119] teeing you up, man.

[00:40:37.280] uh that I thought was really

[00:40:38.400] interesting. Uh wrong discord

[00:40:41.599] where sorry I'm usually on a desktop

[00:40:44.480] monitor when I'm doing this and it's a

[00:40:46.079] little bit more um showcase. I thought

[00:40:49.200] this was a fantastic thread here that

[00:40:51.119] really helped me understand uh kind of

[00:40:52.960] some of the implications of some of this

[00:40:54.320] stuff. So Pashant who is one of the

[00:40:56.079] people that been playing on both DSP and

[00:40:57.680] BAML learned something really

[00:40:59.119] interesting. uh what he did was he

[00:41:01.440] changed how DSPI represents their prompt

[00:41:03.520] format uh to be away from JSON schema

[00:41:05.920] and go more into like the BAML way of

[00:41:07.440] doing it. And what was really

[00:41:08.800] interesting is just a simple way of

[00:41:10.240] changing how you represent the tool call

[00:41:11.920] for every single model by default was

[00:41:14.079] just better than JSON schema.

[00:41:17.599] But when you add the two together, it

[00:41:19.040] got even better. And I think that goes

[00:41:20.800] into what Eugene is asking is like

[00:41:22.160] what's the best way to represent tool

[00:41:23.520] call? To be completely honest, I don't

[00:41:24.720] [ __ ] know. I have no opinions on

[00:41:26.880] this. But I think in general simplicity

[00:41:28.960] is best. So if you have a thing where

[00:41:31.920] you're generating a bunch of like Luma

[00:41:33.839] URLs, don't put UU IDs into the uh don't

[00:41:39.200] put UU IDs into the

[00:41:42.079] uh into the prompt. It's just going to

[00:41:43.520] hurt even if tool call generates one.

[00:41:45.040] Like replace that out. We have a thing

[00:41:46.880] in our chatbot uh that we made recently

[00:41:49.040] and I I thought it was kind of funny

[00:41:50.800] that and we talk about this stuff all

[00:41:52.480] the time but like if you ask it like um

[00:41:55.119] how do I do this thing like how do I

[00:41:59.440] build a super complex agent?

[00:42:04.000] What I found really funny in here is one

[00:42:05.599] of our uh someone on my team built this

[00:42:07.680] and I've tried my best not to influence

[00:42:09.119] anyone on the team in any meaningful

[00:42:10.400] way. Okay, I want them to discover their

[00:42:11.599] own agent assigned decisions, which is

[00:42:14.240] how do I get help? How do I get help?

[00:42:17.040] Sorry. Which was when they actually put

[00:42:19.440] our Discord link in here, they

[00:42:21.920] originally did this, but this thing was

[00:42:24.319] inconsistent and they had to reprompt it

[00:42:26.960] to actually go ahead and actually change

[00:42:28.480] the boundaryml.com/isord.

[00:42:30.560] In this case, this one was fine because

[00:42:33.040] it actually pulled this page as context

[00:42:35.359] info and fed that into there. So, it was

[00:42:37.920] able to do regurgitation. But when you

[00:42:39.280] left on the system prompt as the main

[00:42:41.200] way of getting help, it didn't work. So

[00:42:43.599] they actually changed

[00:42:44.319] >> I'm sorry. This is the you said the

[00:42:46.400] problem is because this is some weird

[00:42:47.839] long string token that's hard for the

[00:42:49.599] model to remember.

[00:42:50.480] >> And in this case, what they're doing,

[00:42:51.520] they're actually pruning it out and

[00:42:52.720] injecting this page in as the only

[00:42:54.720] contact information page. So it's really

[00:42:56.480] easy for it to regurgitate. It's a

[00:42:58.000] pretty beefy model.

[00:42:59.520] >> But what they found is we actually made

[00:43:01.599] a link called boundarymail.com/isord

[00:43:03.599] and putting this in the system prompt

[00:43:05.359] works almost all the time.

[00:43:08.319] All right. It's the same context. So

[00:43:09.680] it's like just thinking about how to

[00:43:10.960] make these systems work in terms of tool

[00:43:13.280] calls is I don't really know what the

[00:43:14.720] best answer is. But the better you can

[00:43:16.640] do to get towards simplicity in general,

[00:43:19.520] the way more throughput you will get.

[00:43:21.920] Yeah, exactly. Random hashes are just

[00:43:23.440] not good. Like the model is just never

[00:43:24.960] going to be good at that. And I think

[00:43:27.440] it's the same thing here. Like I think

[00:43:29.359] in their scenario kind of works, but I

[00:43:30.800] would just eval this for your own use

[00:43:32.000] case. I suspect if you have a simple

[00:43:33.760] task and it did it wrong twice,

[00:43:36.800] you'll probably get better by just

[00:43:38.079] giving it the right output. If you're

[00:43:39.359] using a smaller model, you probably

[00:43:41.040] don't want to give a smaller model the

[00:43:42.319] entire stack trace because a smaller

[00:43:44.400] model is just going to get lost in the

[00:43:46.079] sauce. If you have a bigger model, you

[00:43:48.400] can be more you're more it's more

[00:43:49.920] forgiving in general for all of this

[00:43:51.440] information. So trying to figure out

[00:43:53.359] exactly what you have to do is both a

[00:43:54.800] parameterization of the problem space

[00:43:56.240] you're working in and the model you're

[00:43:58.319] using. And it's like a fine art of

[00:44:00.000] figuring out what that is exactly.

[00:44:02.880] But the fact that this works for them,

[00:44:04.240] like to me, this slightly changed my

[00:44:05.839] perspective of being completely rigid on

[00:44:07.359] only using observation 2B in the final

[00:44:09.200] prompt. Now, what I do,

[00:44:11.599] >> Go ahead.

[00:44:12.319] >> Sorry. Go ahead. No, finish your

[00:44:13.680] thought.

[00:44:14.000] >> Well, what I was going to say is next

[00:44:15.119] time I have a really hard problem and I

[00:44:16.560] use GD5, for example, I'll probably toss

[00:44:18.480] an entire stack trace and just see how

[00:44:19.839] well it does because it's possible that

[00:44:22.240] models have changed. Last time I built

[00:44:23.680] this opinion was based off of like the

[00:44:25.119] GP40 models

[00:44:27.200] >> and perhaps the models are different

[00:44:28.800] now. And it's good for me to be aware of

[00:44:30.319] that and like be open to changing my own

[00:44:32.240] perspectives.

[00:44:34.560] >> Interesting. I mean, so this is

[00:44:36.319] interesting. It doesn't say so it's like

[00:44:39.359] error recovery, but I'm not it's not

[00:44:42.079] clear as saying like um like this

[00:44:44.319] picture says, hey, like use the

[00:44:47.119] observation to get it to get it

[00:44:49.760] correctly, right? Or use the thing to

[00:44:51.440] get it to get correctly the first time.

[00:44:53.440] But it doesn't seem to have an opinion

[00:44:55.200] on like okay if you have four errors and

[00:44:56.960] then you get it right that you should

[00:44:58.319] clear out those four errors before you

[00:45:00.240] proceed.

[00:45:00.800] >> Yeah. Yeah. It's how they I think what

[00:45:03.200] they're saying is typically many people

[00:45:04.640] never store this information.

[00:45:07.040] >> I think what they're making a case for

[00:45:08.240] is hey consider storing the information

[00:45:11.040] sometimes it might help.

[00:45:13.040] >> Yeah. This is uh factor nine of 12

[00:45:15.280] factor agents is like be thoughtful

[00:45:17.040] about it but yeah tell the model what it

[00:45:18.480] did wrong because it will probably fix

[00:45:19.839] it. Um, and the models are getting way

[00:45:23.040] better. So like the stack traces are

[00:45:25.359] likely more likely to help, especially

[00:45:27.040] as the stuff gets bigger and bigger in

[00:45:28.400] terms of context windows and how well

[00:45:29.760] models perform over long form context.

[00:45:32.640] Um, that said, same thing we talked

[00:45:34.720] about here. Proximity to the cache

[00:45:36.880] matters. Proximity to the observation.

[00:45:39.280] Oh, where did it go? Proximity to the

[00:45:40.960] observations matter. Where? I don't know

[00:45:42.319] where it went. That image, the

[00:45:44.319] repetition one. Proximity to the

[00:45:45.760] observations matter. So like if you make

[00:45:47.280] it too big, you'll probably get loss of

[00:45:49.040] performance at some point for your task.

[00:45:51.680] Um let's talk about prompting. I say

[00:45:53.440] this all the time. Don't do fot

[00:45:54.720] prompting. The reason fot prompting is

[00:45:56.880] bad is for the same reason that we say

[00:45:58.560] all the time, which is you're most

[00:46:00.560] people don't do fot prompting correctly.

[00:46:02.400] You're almost most likely going to bias

[00:46:04.000] the model away towards your fshot

[00:46:06.160] example rather than help it understand

[00:46:08.079] what it's actually meant to do. Well,

[00:46:10.640] and literally building an agent is fshot

[00:46:13.760] prompting. Like everything in your past

[00:46:15.839] context window becomes like influences

[00:46:19.119] the next step. And so if the model

[00:46:20.720] starts like starts a task and launches a

[00:46:22.880] sub agent for the rest of that

[00:46:25.119] conversation, the model will be more

[00:46:27.359] likely to launch a sub agent. And so

[00:46:29.440] like you have to really like understand

[00:46:32.400] and this is why we always say like use

[00:46:34.079] clear rather than resteer. If the model

[00:46:36.079] like starts doing something weird in

[00:46:37.440] your agentic chat, whatever system it

[00:46:38.960] is. Obviously, I care a lot about coding

[00:46:40.240] agents, but like this is true for

[00:46:41.680] everything is like the model starts

[00:46:43.040] going about it in the wrong way, you are

[00:46:45.200] much better off starting with a fresh

[00:46:46.960] context and adding two sentences of

[00:46:48.960] steering or two words of steering, by

[00:46:50.800] the way, don't do this than you are to

[00:46:52.960] be like, stop, do it a different way.

[00:46:55.359] And then because then your prompt is

[00:46:57.040] like your context window says system

[00:46:59.040] prompt, user message, model tried this,

[00:47:01.760] user resteered it. And so you're more

[00:47:03.760] likely for the model to like expect that

[00:47:05.760] the conversation continues as model

[00:47:07.839] tries a bad thing, user resteers, model

[00:47:09.680] tries a bad like you you're telling the

[00:47:11.599] model it's okay to make a mistake and

[00:47:13.920] then get corrected. When what you really

[00:47:15.760] want is the model to think, okay, cool.

[00:47:18.079] I made the right decision. I made the

[00:47:19.359] right decision. I made the right

[00:47:20.240] decision. That's how you craft like

[00:47:22.079] really good agentic context as you go.

[00:47:24.560] >> Also contextual. Just remember undo is a

[00:47:26.480] pretty complex action. The fact that we

[00:47:28.079] can do command Z is nice on a computer,

[00:47:29.760] but it's actually really hard to undo

[00:47:31.599] sequences of actions. And that's why

[00:47:33.119] many apps, ma, most SAS apps you use

[00:47:35.839] don't build command Z. It's really

[00:47:37.839] freaking hard to command Z a lot of

[00:47:39.760] actions. Uh, and the model is just going

[00:47:42.079] to have a hard time too. Uh, Photoshop,

[00:47:44.960] for example, will just eventually forget

[00:47:46.160] that you have you you're past a certain

[00:47:47.839] state. It'll just say you can't undo

[00:47:48.880] past this point. Same thing. Um, in

[00:47:51.200] terms of fot examples, there are ways to

[00:47:52.800] do it correctly. It's just that you have

[00:47:54.160] to be really thoughtful about it. In

[00:47:55.359] this case, if I have a class object

[00:47:56.560] where I want product to mean only people

[00:47:59.520] that actually actively write code, then

[00:48:02.000] someone that's listed as director of

[00:48:03.280] engine team, I can just write a small

[00:48:05.680] thing in here that says because they

[00:48:07.200] don't code themselves category product.

[00:48:09.359] And now the model can kind of this is

[00:48:12.319] perfectly evident that this is an

[00:48:13.839] example to the model. It's I'm not

[00:48:15.920] trying to trick it. I'm not trying to do

[00:48:17.280] anything. It's just like this one is an

[00:48:18.800] example very clearly. I use dot dot dot

[00:48:21.440] to simplify that. I'm showing the schema

[00:48:24.400] without showing the full schema. The

[00:48:26.480] model cannot possibly confuse Vivov

[00:48:28.400] Gupta as that person because I mean the

[00:48:31.760] really really dumb model can but modern

[00:48:33.359] models are just not going to have that

[00:48:34.640] problem. So if you're going to do

[00:48:35.920] fuchsia prompting be clever about it

[00:48:37.520] think about what you're really trying to

[00:48:38.880] have the fat example explain to the

[00:48:41.119] model and only put the minimum number of

[00:48:43.200] tokens you need to explain that concept

[00:48:44.960] itself

[00:48:46.079] >> and not just number of tokens but like

[00:48:48.079] meaning of tokens right like that dot

[00:48:50.000] dot token means placeholder to the

[00:48:52.160] model.

[00:48:52.559] >> Exactly. Yeah. And to almost anyone else

[00:48:54.559] reading it. It's same thing same with

[00:48:56.319] dynamic fshot prompting. Sometimes you

[00:48:58.480] might want to put few shots that are

[00:48:59.680] actually similar to your example.

[00:49:01.359] Sometimes you might want to pick few

[00:49:02.640] shots because they're completely the

[00:49:04.079] opposite of your example. And sometimes

[00:49:05.920] you might want to pick few shots that

[00:49:07.200] are unrelated to your example. Let's say

[00:49:08.559] you're in a healthcare setting and

[00:49:10.160] you're processing doctor patient

[00:49:11.839] conversations.

[00:49:13.359] You probably don't want to talk about

[00:49:15.280] like um I don't know like uh uh like leg

[00:49:19.680] fractures. If you're talking very

[00:49:22.720] commonly if the person currently has a

[00:49:24.319] leg fracture, that's just going to mess

[00:49:26.319] up the accuracy of the system. No matter

[00:49:28.079] what you do, you probably don't want to

[00:49:30.240] put the person's name as the same name

[00:49:32.800] as your patient in your system. You

[00:49:34.559] probably don't want the doctor's name to

[00:49:35.760] be the same. Probably don't want the

[00:49:36.960] hospital name to be the same. You

[00:49:38.880] probably don't want to confuse it with

[00:49:40.160] dates in case of continuity of any kind.

[00:49:42.880] So, finding this sort of stuff out and

[00:49:44.960] picking the right fat example can be

[00:49:46.960] good, but as you're you're probably

[00:49:49.280] figuring this out, it's a lot of work to

[00:49:51.200] be fought prompting correctly. So, most

[00:49:53.200] people are better off not doing it

[00:49:54.480] rather than doing it.

[00:49:57.280] Uh, let's go on to the next topic.

[00:49:58.800] Unless there's more, feel free to keep

[00:50:00.720] typing questions in the chat. U if you

[00:50:02.720] have any

[00:50:04.800] >> um

[00:50:05.359] >> um we might have to do a follow-up

[00:50:06.640] session and do the the coding side

[00:50:08.640] because I don't know if we're gonna have

[00:50:09.599] time.

[00:50:10.800] >> Yes,

[00:50:11.520] >> I really I really want to see an example

[00:50:13.599] of how to look at the B responses and u

[00:50:18.160] >> Okay, cool.

[00:50:19.119] >> Um I think I did want to talk about all

[00:50:20.800] these topics because I thought they were

[00:50:21.839] really really interesting. I think the

[00:50:23.760] most last one that I thought is worth

[00:50:25.359] actually we'll talk about this one first

[00:50:26.480] because it's really easy. Um this what I

[00:50:28.800] read is very much about context

[00:50:30.640] compression at least the way I

[00:50:32.240] interpreted this one which wasn't about

[00:50:34.400] like use the file system in the context

[00:50:35.760] like that's one way to do it but what I

[00:50:37.119] was hearing was instead of putting in

[00:50:39.200] the entire chunk all the time at all

[00:50:41.760] points

[00:50:43.280] see if you can break down the system and

[00:50:44.960] only put in the least amount of system

[00:50:46.400] that's uh least amount of context that's

[00:50:48.480] relevant. So for example, if every uh

[00:50:51.440] and like I think that's the whole point,

[00:50:52.880] everything is meant to be restoable. The

[00:50:54.480] idea is that if you're having a whole

[00:50:55.839] website here, instead of actually

[00:50:57.599] putting the website over here, just put

[00:50:59.520] the URL over here and replace the

[00:51:01.440] original observation action two with

[00:51:03.280] just the URL and say from this URL, I

[00:51:05.119] got this action. From this URL, I got

[00:51:07.280] this action. From this URL, I got this

[00:51:08.880] action. And then

[00:51:10.319] >> Oh, I see. So the model the model may

[00:51:12.880] even load the thing into context and

[00:51:15.760] then you choose the next action and then

[00:51:17.599] you stitch the actual content back you

[00:51:20.000] pull it out of the context window so

[00:51:22.480] that like it can be restored later it

[00:51:24.640] can be pulled back in but it's not by

[00:51:26.480] default present.

[00:51:27.760] >> Exactly. And you can even tell this is a

[00:51:30.079] restorable tool, restore data blob,

[00:51:33.119] restore with this key

[00:51:35.599] >> and the model can then if it needs to

[00:51:37.359] call the restore action. And yes, it

[00:51:39.119] increases the number of tools that you

[00:51:40.559] have to make to call your system, but it

[00:51:42.960] dramatically makes your context window

[00:51:44.800] way more efficient because most of the

[00:51:46.720] time, for example, for a coding agent,

[00:51:48.720] imagine trying to keep every single file

[00:51:50.640] the model had to edit in the context and

[00:51:53.119] all the edits are made in the context.

[00:51:54.720] It's kind of useless. like once it's

[00:51:56.720] made a file edit, I can kind of compress

[00:51:58.319] it and say, "I'm done with this file.

[00:52:00.079] The user is happy and it works. Here's a

[00:52:01.760] summary of what the file, what changes I

[00:52:03.599] made,

[00:52:05.440] but keeping the actual code that it

[00:52:07.280] generated is kind of useless for that

[00:52:08.800] kind of task." And then when I tell the

[00:52:10.960] model, hey, actually that file is wrong,

[00:52:12.559] then it can load the load action to load

[00:52:14.240] the file again, reread it, and go do the

[00:52:16.240] work. And there's a trade-off here

[00:52:18.079] between how many tool calls it takes

[00:52:19.839] versus how accurate the system is versus

[00:52:21.839] how uh versus how like u how big of a

[00:52:27.040] context window I have.

[00:52:29.440] But

[00:52:30.960] if you don't make this a possibility,

[00:52:32.800] then you kind of live in this world

[00:52:34.000] where you have to live in big context

[00:52:35.440] land. And then you're just hoping that

[00:52:36.960] GBT26 has a 20 million token window. And

[00:52:40.319] like maybe it will, but like

[00:52:42.880] I really don't want to work in a world

[00:52:44.960] where like every computer needs to have

[00:52:46.720] 50 terabytes of RAM or else it's

[00:52:48.400] useless. Like that that's just a sad

[00:52:50.960] world to have to live in. And also like

[00:52:53.680] phones.

[00:52:56.000] Uh I would like stuff to work on my

[00:52:57.599] phone without needing to go uh go into

[00:52:59.680] this. Duck asked a question. How does it

[00:53:01.440] work with KV caching? Well, it really

[00:53:04.160] depends if your system I think an

[00:53:06.800] important thing to notice about KV

[00:53:08.000] caches and like people overindex on this

[00:53:09.599] sometimes and I I know I I was trying to

[00:53:11.440] explain it so perhaps that was implying

[00:53:13.200] this but look KV caches don't caching

[00:53:16.559] and latency doesn't matter for small

[00:53:18.480] stuff. If most of your chat messages in

[00:53:20.960] your app or agentic loops are like one

[00:53:22.800] or two system calls long, don't do any

[00:53:25.440] of this crap. It is not worth it. Just

[00:53:27.680] make your system work. This stuff only

[00:53:30.319] matters for stuff that is going to run

[00:53:32.000] for a while. If your tasks are taking

[00:53:34.559] like a minute to run, uh yes, then KB

[00:53:37.599] cache matters. But in that case, if your

[00:53:39.920] task is taking a minute to run because

[00:53:41.200] it's calling like 50 different tool

[00:53:42.480] calls, you'll probably get way better KV

[00:53:44.720] cache optimization simply by changing

[00:53:47.440] the observations in this way as well

[00:53:49.200] where like now I get a KV cache here and

[00:53:51.359] only if I load in a new observation do I

[00:53:53.520] break the KV cache because then I'm

[00:53:55.920] going to load observation one and then

[00:53:57.440] compress it into this format. So now

[00:53:59.440] this thing becomes compressed. But what

[00:54:02.079] I can do here is I can design an

[00:54:03.359] algorithm here that's pretty

[00:54:04.400] straightforward that goes ahead and

[00:54:08.319] says, "Hey, after about 15 observations,

[00:54:10.640] I always compress the oldest one." So

[00:54:13.440] yes, I broke my KV cache, but at any

[00:54:15.359] given time, all my previous context is

[00:54:17.920] always going to be similar and and I'll

[00:54:20.160] basically force the model to reload it

[00:54:22.079] because this once it's compressed is

[00:54:24.480] never reloaded ever again. So this

[00:54:27.119] becomes stable. This basically

[00:54:28.640] stabilizes over time. Does that answer

[00:54:31.040] the question, Doug? [clears throat]

[00:54:42.630] >> Perfect. Um,

[00:54:42.640] and then the debate of showing tool

[00:54:44.319] calls and what to output. Yeah.

[00:54:46.319] >> Yeah, I think you got it perfectly,

[00:54:47.520] Doug. Yeah, exactly. Once it once it

[00:54:49.520] gets the next step and it knows what to

[00:54:50.880] do, then it can do it. And I think this

[00:54:52.720] is also like when people do there's like

[00:54:55.119] certain like compaction strategies that

[00:54:56.960] you can do. Like anthropic talks about

[00:54:58.480] micro compaction which is like pulling

[00:55:00.079] at least like the tool calls out

[00:55:01.760] automatically but it's really hard to do

[00:55:04.400] this in a general purpose way which is

[00:55:06.000] what makes this paper so impressive is

[00:55:07.599] like they've done this for a general

[00:55:08.720] purpose agent. If you're building an

[00:55:09.920] agent for a very specific thing you can

[00:55:11.599] optimize the heck out of it for that one

[00:55:13.280] use case and you know exactly like I

[00:55:15.680] know for sure if a model reads this type

[00:55:17.599] of medical document it's and it once it

[00:55:20.240] makes the decision it never needs to do

[00:55:21.760] it again. Or you can say, okay, once the

[00:55:23.359] model reads in and picks the next thing,

[00:55:24.720] I need to pass it to another model to

[00:55:26.160] summarize the document. Put that in

[00:55:27.760] instead of the whole content and like do

[00:55:29.520] your own like deterministic compaction

[00:55:31.839] based on what types of things are being

[00:55:33.440] pulled into the context.

[00:55:34.960] >> Exactly. Now I want to talk about the

[00:55:36.559] last part that I thought was super super

[00:55:38.800] uh innovative and really changed my

[00:55:40.480] perspective a little bit on some things

[00:55:41.760] as well, which is around how to call

[00:55:43.440] work. So we talked about the KB cache,

[00:55:45.280] we talked about how like having

[00:55:46.480] continuity and not breaking continuity

[00:55:48.240] matters. So, we talked I think one easy

[00:55:50.880] way to go fix this is you can take your

[00:55:52.799] tool calls and simply put them always

[00:55:54.720] guarantee put them at the end of your

[00:55:56.160] context window and now you always have

[00:55:57.839] some amount of caching that you get for

[00:55:59.839] free. But what if you did put them at

[00:56:02.000] the top? Well, many times if you're

[00:56:03.599] building an agent, you'll want to

[00:56:04.559] invalidate and change your tools

[00:56:06.000] dynamically.

[00:56:08.000] That is 100% of the time going to break

[00:56:10.480] your KV cache and you will just get

[00:56:11.920] slower latency all the way through. This

[00:56:13.680] was what the the swarm like the original

[00:56:16.240] iteration of like the open AI swarms

[00:56:18.319] framework or whatever their way of doing

[00:56:20.160] multi-agent was to take the same context

[00:56:21.839] window patch it to a different agent

[00:56:23.680] which had a different system message and

[00:56:25.200] a different set of tools.

[00:56:26.480] >> Exactly. And like it just doesn't really

[00:56:28.400] work. But what they end up doing here

[00:56:30.240] that I thought thought was really

[00:56:31.599] fascinating is instead of actually

[00:56:34.079] giving you these tools, they actually

[00:56:36.480] leave the tools in there. And what they

[00:56:38.480] do is they modify

[00:56:42.000] uh let me change let me delete they

[00:56:44.319] modify a part of the system that I think

[00:56:46.480] most people don't think about which is

[00:56:50.240] let me open up the openi docs because I

[00:56:52.640] think that's it's going to show

[00:56:55.359] openai

[00:56:57.520] responses

[00:56:59.359] API. Okay, cool. Uh they modify the

[00:57:02.799] logits coming out of it.

[00:57:06.559] There you go. And you can basically

[00:57:08.640] invalidate certain tokens as being valid

[00:57:11.520] out of the model. So I don't actually

[00:57:13.359] know how you modify the function calling

[00:57:14.880] tokens. I can go look into that because

[00:57:16.400] it sounds like I don't know if Openack

[00:57:18.000] gives you those, but if you own the

[00:57:19.200] model, you can definitely do this. But

[00:57:20.799] the premise is

[00:57:27.589] uh there we go. The premise is like what

[00:57:27.599] the heck is function calling doing? And

[00:57:29.119] we need to go understand that briefly to

[00:57:31.359] really be able to and appreciate this

[00:57:33.680] technique. So what function calling does

[00:57:37.200] is function calling teaches a model

[00:57:39.200] about a special token called use tool

[00:57:42.000] and the model outputs a token that says

[00:57:44.559] I'm going to output a tool and once it

[00:57:47.520] decides to do that token the model

[00:57:49.200] providers then restrict the model to

[00:57:51.920] only pick tokens that match the tool

[00:57:55.119] specification that you have provided. So

[00:57:57.920] >> is this constrained is this constrained

[00:57:59.680] decoding or is this still just the base

[00:58:01.599] like JSON mode? This is

[00:58:05.359] it. So the base JSON mode does that

[00:58:07.599] which is it basically takes it basically

[00:58:09.520] forces the model to only output

[00:58:10.960] grammarss that are valid uh JSON.

[00:58:13.280] >> Yeah. Yeah. Yeah. Yeah.

[00:58:14.799] >> Constraint decoding constraint

[00:58:16.240] generation or decoding whatever you want

[00:58:17.680] to call it is basically the more general

[00:58:19.440] form of that where instead of taking the

[00:58:21.440] JSON grammar you can basically provide

[00:58:23.040] it the grammar of your choice.

[00:58:24.960] >> Any reax and that just zeros out all of

[00:58:27.119] the log probabilities for anything that

[00:58:28.960] doesn't match your reax. Right.

[00:58:30.880] >> Exactly. So if I go back to the

[00:58:32.319] whiteboard,

[00:58:34.000] what this is doing is this is basically

[00:58:35.839] saying like even though the model has a

[00:58:37.440] really high probability for it, I'll

[00:58:38.559] vote this as zero because it doesn't

[00:58:39.839] match the reax of what's allowed. So

[00:58:42.000] only the only the reax is the valid

[00:58:44.079] consideration and then I pick the best

[00:58:45.760] token from the valid reax. Now the

[00:58:48.880] problem that you will run into with this

[00:58:50.799] is sorry I have a lot of tabs open

[00:58:52.559] today.

[00:58:57.589] >> Yeah, we talked about this a lot this

[00:58:57.599] concept in cracking the prompting

[00:58:59.440] interview, right? That was the one.

[00:59:00.880] Yeah,

[00:59:01.359] >> we talked about like how to get AI to

[00:59:02.880] write better code by allowing it to

[00:59:04.960] write things that might not necessarily

[00:59:07.200] be valid JSON but are like closer to the

[00:59:09.599] way that the model has been trained to

[00:59:11.040] write code which is by like reading code

[00:59:13.520] not as snippets and JSON strings.

[00:59:15.440] >> The function calling system does

[00:59:17.119] basically this. It basically says

[00:59:18.880] instead of having the model always

[00:59:20.799] follow the grammar, it says hey you will

[00:59:23.440] emit a special token that says you want

[00:59:24.960] to take an action and then I will force

[00:59:26.480] you to follow the grammar. So at that

[00:59:28.559] point the model is basically deciding to

[00:59:30.880] some degree and can be taught when it

[00:59:32.400] should follow the grammar that it's

[00:59:33.680] given. And now open has a new thing

[00:59:35.520] which I think is really really good for

[00:59:37.280] everyone which is they've allowed you to

[00:59:39.599] do function calling without a grammar or

[00:59:41.359] with a custom grammar. So now you can

[00:59:43.119] basically let the model say I want to

[00:59:44.319] use an action and then let it free form

[00:59:46.240] output whatever it wants. But what the

[00:59:48.880] manus paper uh article talks about is

[00:59:51.680] that when it actually picks the use tool

[00:59:53.599] action at that point the model is now

[00:59:56.000] going to pick a special token. It's

[00:59:58.160] going to pick a certain uh uh

[01:00:00.720] >> the first thing that comes out is the

[01:00:01.920] name of the function. Right.

[01:00:03.280] >> Exactly. It's going to have to spit out

[01:00:04.720] the name of the function. Instead of

[01:00:06.319] actually letting the model spit out the

[01:00:07.680] name of the function at that point, you

[01:00:09.839] can

[01:00:11.599] effectively Where'd it go? You can

[01:00:14.319] effectively prevent the model from

[01:00:15.760] picking a certain tool at that point.

[01:00:17.920] and say that

[01:00:18.640] >> by just zeroing the probability that the

[01:00:21.599] name of the function matches like the

[01:00:23.520] basically like forcing only allowing the

[01:00:25.200] to the log props that actually match the

[01:00:27.839] tool set that you want to constrain to.

[01:00:29.920] >> Exactly.

[01:00:31.520] So this is actually a really really good

[01:00:33.839] technique but I'm going to show you and

[01:00:36.240] I thought it's really really clever but

[01:00:38.079] I'm going to show you how naming your

[01:00:39.680] tools in an interesting way can

[01:00:42.559] dramatically change the accuracy of this

[01:00:45.520] technique.

[01:00:47.599] cursor

[01:00:48.559] >> and I'm going to do this with an example

[01:00:50.079] I think in code because it's going to be

[01:00:51.599] a little bit better

[01:00:54.400] >> and just while you're doing that the

[01:00:55.760] question was like when talking about

[01:00:56.799] tool calls are we talking about explicit

[01:00:58.480] tool calling via model providers or are

[01:01:00.240] we also thinking about whatever

[01:01:01.119] structured output techniques we're using

[01:01:02.799] I think tool calling structured output

[01:01:05.599] and function calling um while there are

[01:01:08.640] different flavors of each of them I

[01:01:10.240] think those three words tend to refer to

[01:01:12.559] the same thing some people say like oh

[01:01:14.480] tool calling is only when you use JSON

[01:01:16.559] mode and structured output is can

[01:01:18.720] doesn't even need to use JSON mode. But

[01:01:20.480] again, like I use all three of those

[01:01:22.640] terms interchangeably. Tool calling,

[01:01:25.200] structured output, function calling.

[01:01:26.720] >> They're all the same.

[01:01:27.520] >> Is that accurate?

[01:01:28.480] >> I agree. There's technical

[01:01:29.839] implementation differences that might

[01:01:31.200] have different trade-offs, but they're

[01:01:32.400] all the same. Fundamentally, what you're

[01:01:34.160] doing is trying to constrain with the

[01:01:35.359] model output to some degree in some

[01:01:36.960] manner or form.

[01:01:38.480] >> Well, and and it's the constraint. It's

[01:01:40.240] not even about the constraining. I think

[01:01:41.520] more for me it's more so about we're

[01:01:44.240] going to create something that a

[01:01:46.720] deterministic program can consume. It's

[01:01:48.799] not for a human and it's not for a

[01:01:50.240] model. It's for Python code that I

[01:01:52.240] wrote. And so it has to have some

[01:01:54.319] expected structure that I can turn it

[01:01:55.920] into bytes in memory.

[01:01:57.839] >> Yeah. So let's say I have these three

[01:01:59.839] tools.

[01:02:01.359] Um right uh and these are the tools I

[01:02:04.079] have. Call me, call mom, call Dexter. Um

[01:02:06.960] and let's say I'm operating the mode in

[01:02:08.880] like work mode. In work mode, I want the

[01:02:12.480] tools call Dexter and call me to be

[01:02:14.240] available. In nonwork mode, so like uh I

[01:02:18.400] want the tools call mom and call me to

[01:02:20.480] be available. I'll never call Dexter not

[01:02:22.079] work mode. I don't like hanging out with

[01:02:24.000] him that much. So how [laughter]

[01:02:26.799] well what we're going to do the model

[01:02:28.400] decide I I'll say a statement like uh I

[01:02:30.400] need to talk to someone.

[01:02:34.160] I'm going to go write the statement. In

[01:02:35.520] this case, call me is clearly not a good

[01:02:37.200] tool cuz I want to talk to someone else,

[01:02:39.280] not myself. So, it should call mom or

[01:02:41.760] Dexter. If I give it all the tools as

[01:02:44.799] context, it could really pick any of

[01:02:46.720] them and it's random in work mode.

[01:02:48.640] However, maybe there's another thread in

[01:02:51.040] here that says like I'm at work. So, the

[01:02:54.799] model and there's some information I

[01:02:56.400] have in my program state that allows me

[01:02:58.000] to know that. So, I have some at work

[01:03:01.680] boolean as true as true or false.

[01:03:05.200] If it is true, I basically want to say

[01:03:07.680] like disable

[01:03:11.040] call mom

[01:03:14.160] and I want to go disable call mom at

[01:03:15.839] that point. If I'm going to go do that,

[01:03:19.200] um, sorry, I'm going to turn this off

[01:03:20.559] text.

[01:03:22.079] Uh, that was not correct.

[01:03:25.839] If I'm going to go do that,

[01:03:27.280] >> the model will start generating tokens.

[01:03:29.680] Now the problem with this is the model

[01:03:32.079] may want to generate a token that starts

[01:03:34.079] maybe the token vocabulary makes it so

[01:03:36.079] that the tokens are actually call and

[01:03:38.000] then mom. So the tokens end up being

[01:03:40.720] call and then mom. And over here the

[01:03:43.920] tokens end up being call and then

[01:03:46.720] Dexter.

[01:03:48.480] If the model generates a token call,

[01:03:51.359] even though I've invalidated this, I've

[01:03:53.440] invalidated call mom, the model may have

[01:03:55.520] actually thought it was really important

[01:03:56.880] to call mom and it may be actually

[01:03:59.119] accidentally forced to picking the call

[01:04:01.039] Dexter tool.

[01:04:01.680] >> Forced to call me. [laughter]

[01:04:03.039] >> Yeah, because it doesn't have a choice

[01:04:04.640] because it it produced the word call. Uh

[01:04:08.400] >> with the intent to call mom

[01:04:10.400] >> with the intent to call mom because I'm

[01:04:12.400] at work mode and I've accidentally

[01:04:13.920] disabled the call mom tool. And now the

[01:04:16.880] model thinks it's want to call mom

[01:04:18.720] because all my tools are in the context

[01:04:20.960] window. So even if the model know the

[01:04:22.960] model doesn't know it can't actually

[01:04:24.400] pick call mom. As far as the model knows

[01:04:27.119] it can pick call mom. So now it might

[01:04:30.240] even go do this. It might even start

[01:04:31.760] outputting call m because m was a valid

[01:04:34.559] token as well in my token vocabulary.

[01:04:37.520] And funnily enough the model might not

[01:04:39.599] even end up calling du. It might end up

[01:04:41.119] calling me because in the tok to token

[01:04:44.400] vocabulary we have call we have we

[01:04:47.039] obviously have the letter m we have the

[01:04:48.640] letter me we have the word me we have

[01:04:50.319] the letter mom we probably have the

[01:04:52.079] words mo as well

[01:04:54.000] >> oh okay so the probability for mom might

[01:04:56.319] have been 99% and the probability for m

[01:04:58.960] might have been 1% but because both of

[01:05:02.720] them are moving towards mom those are

[01:05:04.640] the ones that got picked

[01:05:05.920] >> exactly and mo might also be higher so

[01:05:08.400] I've invalided mo and mom because it

[01:05:10.559] doesn't meet the grammar of what's

[01:05:11.599] allowed based on what what tools are

[01:05:13.920] valid. But I still will call M. So I'll

[01:05:16.079] call M. And now I might call M. Well,

[01:05:17.680] what's the next best token? Well,

[01:05:18.960] there's only one valid token that's

[01:05:20.240] available here. I have to call it E. So

[01:05:22.799] now I'll end up calling the call me

[01:05:24.240] tool. And you can see how actually doing

[01:05:27.599] this can actually backfire in certain

[01:05:29.200] ways if you're not careful about how

[01:05:31.039] you're naming your tools.

[01:05:33.920] So you have if you're going to use this

[01:05:35.760] technique, it is important to be able to

[01:05:37.599] understand how these models work and

[01:05:39.440] build an intuition for this on your own.

[01:05:41.680] So then when something fails or doesn't

[01:05:43.520] fail, you can go iterate on this and

[01:05:45.440] make it better.

[01:05:54.630] >> Does that um any questions?

[01:05:54.640] >> Yeah, there questions about that. There

[01:05:55.839] was there's a lot of content in there.

[01:05:58.000] Otherwise, we can move to some of these

[01:05:59.359] questions.

[01:06:02.319] Uh, call me versus call me variable

[01:06:05.039] name. No, that's totally arbitrary, I

[01:06:06.960] think. Um,

[01:06:08.079] >> I'll show you like a um a really fun uh

[01:06:12.640] post by someone.

[01:06:15.520] Uh

[01:06:18.000] oh, that's the wrong thing. Let's not

[01:06:19.760] show my DMs.

[01:06:24.950] >> While you're doing that, Dexporty with

[01:06:24.960] the understanding of tool calling can be

[01:06:27.039] either an explicit tool call or

[01:06:28.480] structured out. pick your flavor. In the

[01:06:30.640] work that you are doing, have you

[01:06:32.319] noticed any difference in Asian

[01:06:33.839] performance when using model provider

[01:06:35.599] tool calling versus pamble structured

[01:06:37.200] output? Basically, home rule tool

[01:06:38.960] calling. Uh I have no stake in this. Uh

[01:06:44.240] but I believe there's a lot of agents

[01:06:46.160] out there that are built with native

[01:06:48.559] tool calling that would be better if

[01:06:50.799] they used the pamel structured output

[01:06:52.799] for some of the reasons we've kind of

[01:06:54.559] touched on here, but other things. Uh

[01:06:56.880] but I

[01:06:57.839] >> I don't I need viob to ship the

[01:06:59.520] benchmark again. When are we getting v2

[01:07:01.359] of your of your tool calling benchmark?

[01:07:03.200] >> Well, Sean showed a small benchmark

[01:07:04.960] already that showed

[01:07:06.079] >> that's truely better.

[01:07:07.839] >> Um but I want to show everyone a clear

[01:07:09.520] example of when this matters. So like in

[01:07:10.960] this case the user was doing some sort

[01:07:12.319] of tool calling with Kimmy K2 model and

[01:07:14.559] they asked the model to output approach

[01:07:16.640] and no matter what they did like around

[01:07:18.240] like 2% of the time Kimmy K2 would

[01:07:20.240] literally just pull out a propra

[01:07:23.361] [laughter] and this is so wild that it

[01:07:25.599] would actually do this and I started

[01:07:27.200] looking into this and eventually I was

[01:07:28.720] like okay well there's prompt

[01:07:29.920] engineering techniques that you can do

[01:07:31.119] to go do this. So they did that and

[01:07:34.160] eventually

[01:07:34.640] >> did they just add an alias to the field?

[01:07:36.880] Well, eventually what I did was I just

[01:07:39.280] wanted to go understand this. I was

[01:07:40.400] like, so what did I do? I dumped out the

[01:07:41.839] tokenizer. I literally took the

[01:07:43.359] tokenizer for the K2 model and I dumped

[01:07:45.440] it out. And lo and behold, approach is

[01:07:48.720] two tokens.

[01:07:50.799] So of course the model that's a dumber

[01:07:52.640] model is going to get this wrong because

[01:07:55.280] at this point it wants to do approach

[01:07:56.799] and then it's like it's just too dumb to

[01:07:58.799] actually do this. So the solution this

[01:08:01.440] user had was they actually found a word

[01:08:02.799] that was a single token and now it

[01:08:04.480] works.

[01:08:06.240] That's so sick.

[01:08:07.680] >> And just like but the point is like if

[01:08:09.599] your tool calling is going to use a

[01:08:10.799] similar technique, you have to

[01:08:12.480] understand that there are trade-offs to

[01:08:14.720] how your tokenizer vocabulary works. And

[01:08:17.520] the bigger the model, the shorter your

[01:08:19.359] context window, the less they matter.

[01:08:21.359] The smaller the model, the longer your

[01:08:23.040] context window, the more they matter.

[01:08:25.120] And knowing that is just key to getting

[01:08:26.880] success over here.

[01:08:34.149] >> Love it.

[01:08:34.159] >> Yeah. Um, and like remember tokenizers

[01:08:36.319] are different for every model. So you

[01:08:38.159] have to like in like this user could

[01:08:40.640] have spent forever trying to prompt

[01:08:41.839] engineer the way the heck out of this

[01:08:43.359] trying to make it work and they did. Um,

[01:08:45.440] and I think Sam and our team tried this

[01:08:46.880] too and I tried a couple techniques and

[01:08:48.159] literally I just at some point I was

[01:08:49.279] like the model is just too stupid.

[01:08:50.640] What's going on? And I had to go and dig

[01:08:52.400] deep. So don't be afraid to go do that.

[01:08:54.560] Just literally run the tokenizer code

[01:08:56.400] and just go see what's happening.

[01:08:58.799] Uh, really really easy hack to go make

[01:09:00.799] this work. any model provider that

[01:09:02.159] doesn't give you the tokenizer, it's

[01:09:03.359] kind of annoying.

[01:09:05.040] Just have the model provider spit back

[01:09:06.880] out the word to you and count the tokens

[01:09:08.480] out of the HTTP request. That's often

[01:09:10.640] what I'll do with like entropic models

[01:09:12.080] because they don't actually give me the

[01:09:13.040] tokenizer. So I'll say,

[01:09:14.319] >> oh, you say, "Hey, just say the word

[01:09:15.920] approach to me and then you look at the

[01:09:17.440] token counts in the raw JSON that comes

[01:09:19.520] back and say, how many tokens was that?"

[01:09:21.440] >> Literally what I do.

[01:09:23.279] >> Okay.

[01:09:24.000] >> Um, and it kind of works.

[01:09:27.199] Um,

[01:09:28.960] yeah, if you're curious about the

[01:09:30.319] benchmarks, uh, I can share them

[01:09:32.400] afterwards, uh, on the email that we

[01:09:33.920] send out, um, if you're interested or in

[01:09:36.400] our Discord you ask, we'll have

[01:09:38.000] Discords.

[01:09:39.359] >> Slava's question real quick. Yeah, we

[01:09:41.440] put all the streams in the GitHub repo.

[01:09:43.440] That's where you can find them. Um,

[01:09:44.880] yeah. Do you want to pull it up?

[01:09:50.550] >> Uh, what is

[01:09:50.560] >> there? It is. So, you can come here. You

[01:09:52.719] can see every every recording we've done

[01:09:54.480] since March. You can see the YouTube.

[01:09:56.239] you can see the code. Um, you can sign

[01:09:58.000] up for the next one.

[01:09:59.360] >> And if all you really

[01:10:00.480] >> about the

[01:10:01.360] >> if all you really want to do is just

[01:10:02.719] watch all the content, we have a

[01:10:04.239] playlist somewhere um that you can find.

[01:10:07.120] And I don't hear my voice again.

[01:10:09.360] >> Uh, but they'll have everything on

[01:10:11.440] there. And then I think we tried to make

[01:10:13.520] a interesting version of this

[01:10:17.520] uh where we actually do this with

[01:10:18.560] Dexter. And you can actually just scroll

[01:10:19.760] through here as well.

[01:10:20.719] >> Oh man. Wait, this is sick.

[01:10:23.760] >> Wait, I want this on human layer.dev,

[01:10:25.199] dev too.

[01:10:25.840] >> I'll send you the code. You can post it

[01:10:27.360] over.

[01:10:28.320] >> Amazing.

[01:10:29.440] >> Um uh do you mind me and then point the

[01:10:32.320] resource try this out locally. The thing

[01:10:34.000] about um we'll try and give you some

[01:10:35.600] sample code to go try this out locally.

[01:10:37.280] But honestly, for most of these

[01:10:38.480] problems, just take any of the problems

[01:10:39.760] that you have that you've already been

[01:10:41.120] working on and just like go look at the

[01:10:43.679] inspect the output elements that are

[01:10:45.199] coming out of these problems. So like

[01:10:46.960] for example,

[01:10:48.800] um let's just write a really quick uh

[01:10:52.719] agent. Let's see if I have screen if I

[01:10:55.679] don't have

[01:10:58.239] Let's see if I don't have screen

[01:10:59.920] sharing.

[01:11:05.030] Okay, cool. Uh I'm going to disable

[01:11:05.040] screen sharing really fast while I copy

[01:11:06.480] the curl with my OpenI key. Um and then

[01:11:10.320] I will bring it back.

[01:11:26.149] clear. Okay.

[01:11:26.159] Um I'm going to screen share again.

[01:11:29.520] So if I run this API key uh this

[01:11:32.719] request, I can just see that it

[01:11:34.960] literally cached nothing. And the reason

[01:11:36.560] it didn't cach anything is literally

[01:11:38.000] because I just have too small of a

[01:11:39.520] context window. So if I just increase

[01:11:41.360] this context window

[01:11:44.800] by

[01:11:47.199] make this a real resume example that is

[01:11:51.679] dense

[01:12:04.149] like all the stuff.

[01:12:04.159] Cool. Let's copy and paste this and

[01:12:06.400] let's go run this again.

[01:12:10.080] It still didn't catch anything. I have

[01:12:11.440] to make it even bigger. But the whole

[01:12:14.080] point is right over here. You need to go

[01:12:15.600] ahead and actually understand why this

[01:12:17.040] is happening or not happening. And part

[01:12:18.239] of the reason here is just I know this

[01:12:19.520] is too smaller, too uh too small of a

[01:12:21.920] text.

[01:12:27.189] >> Do you show the token count?

[01:12:27.199] >> It's right here.

[01:12:29.840] Oh,

[01:12:30.000] >> I see.

[01:12:31.840] They won't even trigger caching here

[01:12:34.960] >> like

[01:12:37.440] triple the resume.

[01:12:39.440] >> And just [clears throat] to be clear,

[01:12:40.159] you're just running the same request

[01:12:41.440] twice and seeing if it auto caches it

[01:12:43.280] based on the shared prefix.

[01:12:44.880] >> Exactly. And what I'm doing here is I'm

[01:12:46.800] just trying to have it triple the resume

[01:12:47.920] and that'll do some stuff probably.

[01:12:54.790] And like hopefully I'll make it long

[01:12:54.800] enough. But the way that I can test this

[01:12:56.560] is just I can keep making test cases

[01:12:59.040] until

[01:13:00.719] I'm satisfied with the final output and

[01:13:05.040] I'm going to see if it's actually long

[01:13:06.239] enough where

[01:13:19.669] um the model to get a lot slower.

[01:13:19.679] Uh I'm still not long enough, but you're

[01:13:23.199] getting the point of how I would go do

[01:13:24.560] this. I know that open is probably

[01:13:25.760] catching about 1024 tokens based on what

[01:13:27.679] they said in their docs. So in that

[01:13:29.360] case, I'm just going to make an example

[01:13:30.560] that has 1024 tokens. And I ran into

[01:13:32.800] this personally myself a few times when

[01:13:34.239] I was unit testing some of the code that

[01:13:35.520] we write because I was like, "Oh, why is

[01:13:38.159] caching not working?" Well, it turned

[01:13:39.360] out I literally just wasn't implementing

[01:13:41.280] a long enough prompt and it would just

[01:13:42.560] break all the time. But once I actually

[01:13:44.719] implemented a big enough prompt, I could

[01:13:46.080] consistently see hits on caching

[01:13:49.360] pretty well.

[01:13:52.640] Um, other questions from anyone?

[01:13:54.640] Otherwise, I think we're 20 minutes

[01:13:55.920] over.

[01:14:02.870] I answered Vijay's question. It's about

[01:14:02.880] cloud code proxying. I'm actually I'm in

[01:14:04.480] Austin this week with the uh Gauntlet AI

[01:14:06.800] squad. They have like a school here for

[01:14:08.800] learning AI engineers. And apparently

[01:14:10.719] one of the one of the students here

[01:14:11.920] built a thing called CC proxy that lets

[01:14:13.840] you just like strip all of the traces

[01:14:15.520] out of your quad code running locally.

[01:14:17.840] >> That's cool. That's cool. Um I guess

[01:14:21.600] that's it for today's conversation in

[01:14:23.040] that case. Um thank you guys for

[01:14:25.120] joining. Hopefully it was educational

[01:14:26.719] and hopefully everyone learned a few

[01:14:28.000] things. We'll have a new topic for next

[01:14:30.480] week that I think will be hopefully just

[01:14:32.239] as educational.

[01:14:33.760] >> It's going to be dope. Thank you all for

[01:14:35.920] coming. Thanks Vybob for running the

[01:14:37.679] session today. And uh thanks everyone uh

[01:14:40.159] thanks everyone here.

[01:14:42.640] Bye. Blair.
