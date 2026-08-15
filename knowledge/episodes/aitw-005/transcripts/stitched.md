# S02E01 – Designing Evals



Source: YouTube captions (automatic:en)



[00:00:03.909] All right. Awesome.

[00:00:03.919] Yeah. So, evals, like I think eval feel

[00:00:06.240] like this magic button. I think everyone

[00:00:07.680] feels like, hey, my AI pipelines don't

[00:00:09.519] work, but if I somehow solve evals, they

[00:00:12.320] will start to work. Well, and I'll say

[00:00:15.280] some people haven't even gotten there

[00:00:17.039] yet. And like I think there's this like

[00:00:19.760] especially when you're new to building

[00:00:21.680] AI pipelines or you're new to a certain

[00:00:24.400] technique or model which is pretty much

[00:00:26.880] everyone all the time like no one is an

[00:00:28.800] expert on every model and there's new

[00:00:30.240] stuff shipping every every week every

[00:00:32.079] month and I think it can be paralyzing

[00:00:35.280] and it can kind of like kneecap the

[00:00:37.520] productivity of your team when everybody

[00:00:40.160] is trying different things in different

[00:00:42.120] ways and without a way to understand hey

[00:00:46.239] this approach works better than that

[00:00:47.760] approach without a way to evaluate the

[00:00:49.920] performance of whatever like problem

[00:00:52.399] you're your new approach on on the

[00:00:54.399] problem you're trying to solve. It's

[00:00:56.480] it's kind of becomes impossible to make

[00:00:58.320] progress and like by Bob said like it

[00:01:00.800] becomes this magic bullet where it's

[00:01:02.800] like okay if we just had a number from 0

[00:01:05.199] to 100 that said here's how good we are

[00:01:08.640] in this approach versus this approach

[00:01:10.400] versus this approach. Hey we changed

[00:01:12.159] this thing and we got better here but we

[00:01:14.159] got worse here. um it kind of can be

[00:01:17.439] very grounding and helps you bring a lot

[00:01:19.840] more than engineering back into your

[00:01:21.520] process. Does that sound right? I think

[00:01:23.600] so. But I think um I think that's the

[00:01:26.640] feeling at least and the thing that I

[00:01:28.400] have mostly captured. So I think the

[00:01:31.520] first time I really started thinking

[00:01:32.720] about machine learning eval uh came from

[00:01:35.119] when I was working on hollow ones. Um,

[00:01:37.920] and that was the first time where I had

[00:01:39.360] a completely stochastic system, uh,

[00:01:42.079] where you really can't there's no ground

[00:01:44.640] truth because capturing ground. So, for

[00:01:46.799] context, for everyone else that doesn't

[00:01:48.159] know, hollens is an AR headset and part

[00:01:50.640] of the AR headset job is to build a 3D

[00:01:53.280] representation of the world that it sees

[00:01:54.880] through the cameras it

[00:01:56.520] has. And in order to do that perfectly,

[00:02:00.159] the only way you can build eval is to

[00:02:01.840] build a simulation that perfectly

[00:02:03.280] simulates the camera hardware, which you

[00:02:05.119] cannot do. like you cannot actually

[00:02:07.360] mimic how light is captured by the

[00:02:09.039] camera sensors perfectly. So the next

[00:02:11.360] best thing we can do is capture

[00:02:12.800] something that is pretty close to

[00:02:15.400] correct and for that you're going to use

[00:02:17.599] another sensor and that sensor itself

[00:02:19.599] will have some errors. So we built this

[00:02:22.480] pipeline out that had some ground truth

[00:02:24.720] and we tried to use that ground truth

[00:02:26.160] and tried to align it but then we ran

[00:02:28.400] into problems like windows and mirrors

[00:02:30.800] which basically don't get captured by

[00:02:32.879] any sensor very well. Um, and then we

[00:02:35.680] had to like those existed in our data

[00:02:37.840] set. Like I'm in this conference room

[00:02:39.120] right now. I'm surrounded by windows.

[00:02:41.280] That's a real data set and we want we

[00:02:43.920] wanted the hall lens to work in there.

[00:02:45.560] So we had to approximate what it meant

[00:02:48.720] to have some sort of a score. And like

[00:02:51.680] let's say the the hall lens misses one

[00:02:53.920] square meter of an area and capturing a

[00:02:57.319] wall. Is that good? Is that bad? Like

[00:03:00.400] how do you evaluate is one square meter

[00:03:02.239] versus 1.2 two square meters any worse

[00:03:04.239] or better and that's so it almost

[00:03:06.959] becomes like a question of like where do

[00:03:08.400] we spend our time and like what matters

[00:03:10.640] to the actual kind of and output of how

[00:03:13.280] how good is our system as seen from like

[00:03:15.680] what outcome is it trying to drive

[00:03:17.440] exactly so that's one part of it and the

[00:03:19.200] other part is can you even measure

[00:03:20.920] correctness like how do you know if the

[00:03:23.040] one square meter you missed was actually

[00:03:25.920] a real hole or a hole that the other

[00:03:28.959] sensor also missed like is it a hallucin

[00:03:31.920] Funny enough, we used to call them

[00:03:32.959] hallucinations as well. Um, they're like

[00:03:35.680] hallucinated fragments and like how bad

[00:03:37.840] are hallucinated 3D assets that the

[00:03:40.319] Hollands picked up that didn't exist in

[00:03:42.159] the real world? And measuring that was

[00:03:44.799] incredibly hard. We actually had a

[00:03:46.319] full-time person. We actually had like

[00:03:48.640] one and a half full-time people whose

[00:03:50.239] full-time job it was for over two years

[00:03:54.000] to at best approximate some sort of

[00:03:57.120] metric. And we had no real metric in the

[00:03:58.879] end. It was it was just a pseudo

[00:04:00.239] approximation of the real system. And we

[00:04:03.120] did this for all sorts of things. We did

[00:04:04.879] this for handtracking when we built

[00:04:06.239] handtracking. We did this for

[00:04:08.560] eyetracking when we did

[00:04:11.239] eyetracking. And that's when I first

[00:04:13.439] realized like there is no EVOS truth.

[00:04:15.599] There is no golden data set ever for

[00:04:18.400] most real

[00:04:20.040] problems. Um that's funny. Uh Adisha. Um

[00:04:24.560] uh and then it really comes to a matter

[00:04:27.520] of how do you balance engineering time

[00:04:30.639] that you have to do to build a system

[00:04:32.240] that can at best

[00:04:34.040] approximate the actual thing the proxy

[00:04:36.960] for what you're trying to build for.

[00:04:38.560] Does that align with what uh what you've

[00:04:40.560] seen too as Dex in the now the LLM

[00:04:42.639] world?

[00:04:44.800] Yeah. And I I I see it as kind of like a

[00:04:47.000] gradual process too. Like I know I know

[00:04:49.520] we're going to start like we're going to

[00:04:50.720] get into this but like every project

[00:04:53.520] starts with nothing. Like if there was

[00:04:55.520] already an eval a really good eval for

[00:04:57.600] the problem you're solving then it's

[00:04:59.840] almost certain that someone else is

[00:05:01.440] already kind of on well on the way to

[00:05:03.600] solving that problem. And the hard

[00:05:05.040] problems to be solved in AI tend to be

[00:05:07.440] the ones where no eval set exists or no

[00:05:09.759] eval set exists that is appropriate for

[00:05:11.919] the way that you're approaching it or

[00:05:13.360] the way you want to evaluate your

[00:05:14.639] solution. And so I think the tricky part

[00:05:17.520] is like a lot of teams get sucked into

[00:05:20.240] cool, we're gonna spend six months

[00:05:21.600] building our eval set and then we're

[00:05:23.600] just gonna push it out and go. And I

[00:05:25.360] think what's a lot more interesting is

[00:05:27.199] this kind of more agile incremental

[00:05:29.280] engineering approach of how do we start

[00:05:32.000] with nothing? How do

[00:05:34.039] we make it pretty good to start and how

[00:05:36.560] do we keep updating it and evolving the

[00:05:38.800] way we evaluate our software over time?

[00:05:41.840] Yeah, exactly. And Dex and I put

[00:05:44.400] together some topics that we want to

[00:05:46.479] talk about today. Uh Dex, do you want to

[00:05:48.800] copy and paste them into the chat really

[00:05:50.560] fast?

[00:05:52.280] Um I will do you one better. I will push

[00:05:56.720] up um the readme which has the topics in

[00:06:00.400] it. Even better. Okay. Uh and while

[00:06:02.080] you're at it, do you want to and I'll

[00:06:03.120] link that. You just want to screen share

[00:06:04.800] really fast then in that case. Uh sure.

[00:06:07.919] Cool.

[00:06:10.800] So when we first think about evals, I

[00:06:13.039] think it's more of a journey rather than

[00:06:14.479] an answer right now. And any company

[00:06:16.560] that starts off saying that we're going

[00:06:18.639] to build evals automatically. It's just

[00:06:20.400] going to solve everything is going to be

[00:06:22.000] stuck because you could spend you could

[00:06:24.080] spend your entire company's lifetime

[00:06:26.080] building

[00:06:27.000] evals.

[00:06:29.000] Um, so what I want to I think what we

[00:06:31.520] want to talk about is how do we go from

[00:06:33.440] no evals to some evals to really good

[00:06:37.120] evals in an incremental way for any

[00:06:39.440] problem that you have today rather than

[00:06:42.000] just like what exactly is a great eval.

[00:06:44.479] And by the way, we're recording all of

[00:06:45.919] these so we'll post it on YouTube soon

[00:06:48.000] and you'll have access to all of

[00:06:55.590] them. So uh yes, sorry, give me give me

[00:06:55.600] just one second here.

[00:06:58.440] Yeah. Um, and today's conversation is

[00:07:01.440] going to be really, really interactive.

[00:07:02.960] So, if people have problems that they

[00:07:04.479] specifically want to pose that we should

[00:07:06.160] talk about, definitely feel free to just

[00:07:07.840] like chime in and ask, uh, you can post

[00:07:09.759] it in the chat and we're happy to

[00:07:11.199] discuss those as well. Um, the number

[00:07:14.639] one sneak peek that I'll give everyone

[00:07:16.319] before uh, we get too into it is please

[00:07:19.759] stop using numbers to evaluate your

[00:07:21.919] systems. Do not ask an LLM on a scale of

[00:07:24.479] 1 to 10, how good is the answer. stop

[00:07:26.960] asking it confidence scores. Um

[00:07:30.680] because and and I'll give you intuition

[00:07:33.039] how to how to think about this problem

[00:07:34.400] and why that matters. How many of you

[00:07:35.840] actually like ask confidence scores just

[00:07:38.319] like humans? Mike. Um how how many of

[00:07:41.120] you use confidence scores today? Can you

[00:07:42.560] like type in the chat or uh really

[00:07:45.160] quickly?

[00:07:46.759] Okay. Come on all of you please shame

[00:07:49.199] yourselves. I allow you to shame

[00:07:50.880] yourselves. It's okay. It's we're an

[00:07:52.400] open place right now. You should have

[00:07:54.319] you should have asked them first and

[00:07:55.919] then told them that it was bad. No, no,

[00:07:58.000] I think it's, you know, it's part of it.

[00:07:59.759] You gota you got to acknowledge what

[00:08:01.759] five steps of grief. You just got to

[00:08:03.120] acknowledge it first. And once we've

[00:08:05.120] accepted it, um then we can talk about

[00:08:08.639] it. Um Okay, cool. Um Okay, cool. Uh I'm

[00:08:13.599] just going to merge this in right now.

[00:08:14.960] There's some Okay, work in progress

[00:08:17.120] code. Uh some of this may change

[00:08:18.720] throughout the episode folks, but uh

[00:08:22.240] let's pull up the evals workshop. Okay,

[00:08:25.199] cool. So yeah, here's what we want to

[00:08:26.960] talk about today.

[00:08:28.960] So much the main topics are really going

[00:08:31.919] to go about why eval are really good and

[00:08:33.919] what you can do if you have an answer

[00:08:35.599] key. And I think that's hopefully should

[00:08:37.519] be pretty obvious.

[00:08:43.269] Okay, Dex, sorry. I'm gonna make you

[00:08:43.279] call. Sorry. Yeah, I'll get unmuting

[00:08:44.720] folks, too. Okay, there you go. you're

[00:08:47.440] um you're made a co-host and like why we

[00:08:50.399] can what we can do if we actually have

[00:08:51.519] an answer key. Um and that should be

[00:08:53.839] really obvious, but the most important

[00:08:55.120] thing remember we talk about this all

[00:08:56.560] the time on these episodes. The number

[00:08:58.399] one thing you need to build a really

[00:08:59.519] good AI pipeline is a really fast

[00:09:00.880] iteration loop. Evals are your way to

[00:09:03.279] iterate fast. Uh not initially but

[00:09:06.519] eventually. If you have a team of 40

[00:09:08.880] people contributing to your codebase,

[00:09:10.720] you need evals just like you need unit

[00:09:12.959] test because that's what prevents CI/CD

[00:09:14.800] from breaking. And you need to do that

[00:09:17.440] not because developers are bad, but

[00:09:19.279] because we're all lazy and we all do

[00:09:21.120] push code sometimes and CI/CD does a

[00:09:23.120] really good job of checking for

[00:09:24.399] mistakes,

[00:09:25.920] right? So that's that workflow of like

[00:09:27.680] make a change, run the eval, see if it's

[00:09:29.680] better or worse, and then like don't

[00:09:32.080] push code that makes the eval worse.

[00:09:34.560] Yeah. And like how do you measure if

[00:09:36.399] it's worse or not is a totally separate

[00:09:38.240] question. But in proxy that's really

[00:09:40.080] what we want to go do. And you want an

[00:09:41.680] easy way to go do that. Visualizing

[00:09:44.720] results. We'll talk about that in a

[00:09:46.080] second as well. I'm going to flag that's

[00:09:47.440] a good question. Can you add that in

[00:09:48.720] your local notes tab? Yeah. Yep. Yeah, I

[00:09:50.959] was about to do that. I love that. Okay.

[00:09:53.360] Um Oh, you're screen sharing. Okay. Let

[00:09:55.680] me screen share my tab because then we

[00:09:57.600] can

[00:09:59.959] um the next question I want to talk

[00:10:01.920] about is how do you actually build an

[00:10:03.120] answer key? because at least for me most

[00:10:05.120] things I work on have no answer key on

[00:10:07.600] the on the very beginning and those are

[00:10:09.760] also the most interesting things that we

[00:10:12.000] could have. Um so we'll talk about how

[00:10:14.480] to build an answer key from

[00:10:16.120] nothing. Hint the answer is you know how

[00:10:19.440] there's vibe

[00:10:20.760] coding. You should be vibe evaling in

[00:10:23.200] the beginning and vibe coding

[00:10:25.839] but you should be vibe evaling in the

[00:10:28.560] beginning if you haven't used a lot of

[00:10:29.760] LLM. you should 100% be vibe evaling and

[00:10:32.640] we'll talk about why in a second as

[00:10:34.079] well.

[00:10:36.000] The the other

[00:10:38.040] thing the other thing that I think is

[00:10:40.399] really worth noting is a lot of people

[00:10:42.240] look at emails as

[00:10:43.959] holistic but structured data versus

[00:10:46.959] unstructured data is a huge difference

[00:10:48.880] in the way that we do emails and I think

[00:10:51.040] like Dex and I have talked about this a

[00:10:52.800] lot. Uh so like Dex, do you want to

[00:10:54.480] share some thoughts? Yeah. So I mean

[00:10:57.600] like you have all these different So I I

[00:11:01.040] feel like where we got off the track a

[00:11:03.600] little bit like as an industry with eval

[00:11:06.839] was doing all this work to understand

[00:11:11.279] unstructured data and how good it was

[00:11:14.000] because then you get all these things

[00:11:15.360] like sentiment categories and is the

[00:11:18.079] model outputting text that's rude like

[00:11:19.920] you have all these like kind of like

[00:11:20.959] baked in eval becoming a little bit like

[00:11:24.720] industry standard as far as like okay

[00:11:26.720] the first thing you can do is just pull

[00:11:28.000] this thing off and make sure your model

[00:11:29.440] is not recommending that people go you

[00:11:32.000] know do something dangerous I won't go

[00:11:34.160] into details but um um things like that

[00:11:37.600] and so that's like and so it's like okay

[00:11:39.600] we need evals in the sense of like we

[00:11:42.399] need one LLM to read all this

[00:11:43.920] unstructured data and

[00:11:46.279] then decide whether it's yes or no on a

[00:11:50.079] bunch of these like binary classifiers

[00:11:52.000] or like multiple category classifiers

[00:11:55.360] um versus like a problem that I work

[00:11:57.760] with a lot is like extracting structured

[00:11:59.519] data from images and being able to say

[00:12:03.839] like hey here's uh a hundred pictures of

[00:12:07.760] a

[00:12:08.600] passport like can we reliably pull the

[00:12:11.680] data out of that passport and for that

[00:12:13.760] our answer key is very structured it's

[00:12:15.680] literally a list of JSON fields versus

[00:12:18.720] like you know can we get a one to 100

[00:12:21.360] score either you know hey we have a

[00:12:24.000] 100red outputs from the model, which of

[00:12:26.959] how what percentage of them like pass

[00:12:28.639] all our, you know, style guidelines as

[00:12:30.480] far as how we want our chatbot to behave

[00:12:32.320] or something? Does that little rambly,

[00:12:34.959] but does that make sense? That nailed

[00:12:36.720] it. That's um and then really it's like

[00:12:39.200] this and then there's a blend of the two

[00:12:40.959] as well where I have some structured

[00:12:43.360] data and I can eval that with like

[00:12:45.560] programmatically and some of it has to

[00:12:47.760] be eval because I'm getting a summary.

[00:12:49.920] But even summaries, people are like,

[00:12:51.279] "Oh, I can only know if it's a good

[00:12:52.639] summary or not if I use an LLM." But

[00:12:55.920] that's not actually true. Let's look at

[00:12:57.680] the idea of like summarizing something.

[00:12:59.200] I can know how many sentences things

[00:13:00.880] have. I can know how many what the word

[00:13:02.880] count of the summary is. I can and I I

[00:13:05.279] can know how many how long it is. Um,

[00:13:08.320] and then I can even know something like

[00:13:10.720] does it mention specific key words that

[00:13:12.720] it really should mention the summary.

[00:13:14.639] Like if I ask for a summary about like

[00:13:17.160] um uh if I ask for let's say a summary

[00:13:20.079] about like like a Wikipedia

[00:13:22.200] article, it should probably mention some

[00:13:24.399] of the key figures in the Wikipedia

[00:13:26.079] article up front and I should probably

[00:13:28.800] know what those key figures are ahead of

[00:13:30.720] time and some of them. Yeah, I feel like

[00:13:32.639] we need to we need to hit the

[00:13:33.959] whiteboard. People are Pashant is asking

[00:13:36.560] what's an answer key. Um yes, I think

[00:13:39.760] let's let's define some of this stuff.

[00:13:41.440] Um I will drop you the link real quick.

[00:13:44.399] Thank you. Um or do you want to do you

[00:13:46.160] want to share and uh just tell me the

[00:13:48.800] link in my DMs?

[00:13:52.040] Yeah. Um so and and I think sorry for to

[00:13:56.000] catch everyone else. An answer key is

[00:13:57.440] something like a rubric. Like in the

[00:13:58.880] case of like a classification problem,

[00:14:00.800] an answer key could be something as like

[00:14:03.040] uh here's the correct classes for all

[00:14:05.120] these categories. In the case of like a

[00:14:07.600] resume problem, the answer key could be

[00:14:10.079] something more like um here's the fields

[00:14:12.480] that I wanted to extract. In the case of

[00:14:14.240] a chatbot, it could be the sentiment

[00:14:16.480] that a user should be feeling at any

[00:14:18.320] given point in the chatbot

[00:14:21.000] itself. It really depends on the kind of

[00:14:23.680] problem you have, but the idea is that

[00:14:25.360] your answer key is as close to an

[00:14:27.120] approximation about the correctness

[00:14:30.720] uh that you

[00:14:37.910] have. And like it could be sentiment and

[00:14:37.920] yeah, so I'll copy and paste a couple

[00:14:39.519] more thing. It could be sentiment. It

[00:14:40.959] could be like intent

[00:14:43.160] capturing. So like we capture the intent

[00:14:46.000] that the user asks us about correctly

[00:14:48.000] and exact. Okay. So that's something

[00:14:49.199] like someone comes in and says I want to

[00:14:51.680] buy a new phone and we want to validate

[00:14:54.639] that that becomes you know browse

[00:14:57.839] products.

[00:15:00.440] Exactly. Right. And it might even

[00:15:02.560] include browse products subcategory

[00:15:04.560] field a subcategory phone as another

[00:15:07.279] thing,

[00:15:09.360] right?

[00:15:11.279] Like we might want all of that. And that

[00:15:12.720] might be like we might want and the

[00:15:15.519] accuracy of our system that we want

[00:15:17.120] might be, hey, you know what? For our

[00:15:18.800] system, we're we're pretty happy if it

[00:15:20.560] got to the browse products phone. were

[00:15:22.079] very happy if it got to the product's

[00:15:24.720] phone page, but it's like, oh, it's it's

[00:15:28.079] our choice about how strict we want to

[00:15:30.720] go make

[00:15:32.600] this. And I think the key part about

[00:15:35.440] having an answer key here is like if if

[00:15:38.079] we go deep deeper into like this I want

[00:15:40.480] to buy a phone thing that Dex wrote out

[00:15:42.560] is like at this point many of us know

[00:15:44.720] that we're going to have like a

[00:15:45.680] multi-step pipeline. We're going to have

[00:15:47.040] like some sort of intent detection. Um

[00:15:49.440] after we have intent detection

[00:15:52.240] uh yeah after we have intent detection

[00:15:54.480] we might route to like a different part

[00:15:57.440] uh different things based on what the

[00:15:58.959] user is trying to do and we can build

[00:16:01.839] evals for different parts of the system.

[00:16:04.000] So even though this whole thing is the

[00:16:06.680] chatbot, we could build eval just to say

[00:16:09.839] that did we pick the right arrow down

[00:16:12.120] here? Is the intent selection good

[00:16:15.040] without even really arguing about like

[00:16:17.279] whether the subbox in here operated

[00:16:19.560] correctly. It doesn't have to be binary.

[00:16:22.079] That's the whole point that I was

[00:16:23.199] making. It's your choice. Obviously, if

[00:16:25.040] it's binary, it's going to be more easy

[00:16:27.440] to

[00:16:29.240] evaluate. But if it's not binary and

[00:16:31.839] some problems just cannot be binary like

[00:16:34.240] in the case of summarizing an uh

[00:16:36.399] summarizing a Wikipedia article, it's

[00:16:38.639] virtually impossible to make that a

[00:16:40.160] binary

[00:16:41.800] classification. But what it can be is a

[00:16:44.240] great approximation for what we think is

[00:16:46.399] the

[00:16:47.480] truth. And I think that sounds a little

[00:16:49.680] vague. So I want to I want to talk about

[00:16:51.279] how to go do that really quickly.

[00:16:59.430] So okay, see what I'm doing here? Yeah,

[00:16:59.440] does this make sense? Like this is like

[00:17:01.680] how you would basically write this in

[00:17:04.120] Python. Um and obviously you don't want

[00:17:06.319] to handw write a unit test for all

[00:17:07.679] these. This looks a lot like um like a

[00:17:09.760] table table test basically where you

[00:17:12.400] basically for a big set of inputs and

[00:17:15.160] outputs you would just make assertions

[00:17:17.360] about them. And like you could do this

[00:17:19.919] in JSON or you could do it in CSV, but

[00:17:22.559] like you have your input and then you

[00:17:24.720] have your expected output. Exactly.

[00:17:27.919] And like this is not fun. This is not

[00:17:31.520] fun to go right. Yeah. And you can do

[00:17:32.960] this anywhere. Like uh the reason that

[00:17:34.960] like Dexter is probably saying that he

[00:17:36.559] he's writing this in Python directly is

[00:17:38.160] because the more sophisticated your

[00:17:39.200] agent get like as of today like BAML

[00:17:40.880] doesn't allow you to compose functions.

[00:17:42.799] So you just can't write certain types of

[00:17:44.640] expectations really well. Yeah. But one

[00:17:47.520] of the most important things is this

[00:17:48.799] word that Dexter says which is a table

[00:17:50.640] test. And Dexter said this because he's

[00:17:52.880] worked in these kinds of systems for a

[00:17:54.240] while now. But I want to articulate to

[00:17:55.919] everyone what that

[00:17:57.559] means. So when I'm doing a table test,

[00:18:00.799] and this is something to think about as

[00:18:02.160] you build more complicated emails. A

[00:18:04.640] table test for concept is to say that

[00:18:06.320] hey output has multiple fields in it. It

[00:18:08.160] has an input, it has an intent and a

[00:18:10.280] subclass. Just because it doesn't match

[00:18:12.400] this perfectly doesn't mean it failed. I

[00:18:14.880] really want a table that says out did

[00:18:16.799] output.intent match what I want and did

[00:18:18.799] output.ass match what I want. It's a

[00:18:21.360] table test and I can run both of them in

[00:18:23.400] parallel without running only one. And

[00:18:27.760] that is incredibly useful when building

[00:18:30.000] LLM outputs. And I want to show a real

[00:18:35.000] um I'm

[00:18:38.400] just I'm pseudo coding over here. Ad

[00:18:40.640] just talking about summarizer. So I want

[00:18:42.160] to share like a couple different

[00:18:43.600] examples of ideas here. So this is how

[00:18:45.919] we could build an intent classifier test

[00:18:47.840] case. And you could actually imagine

[00:18:50.400] even further, what if this was a

[00:18:52.360] chatbot, but I had like a probe, and we

[00:18:56.000] talked about probes a few times that I

[00:18:58.160] passed into my

[00:18:59.880] system that was able to introspect

[00:19:02.480] specific nodes in here, and then I could

[00:19:04.400] be like

[00:19:06.120] probe. And actually analyze the intent

[00:19:08.480] into my chatbot and actually know

[00:19:10.080] exactly what happened. Oh, I see. So

[00:19:12.960] you're instrumenting through the steps,

[00:19:14.480] but you're actually running you're

[00:19:16.240] actually running you can and you could

[00:19:17.679] also make assertions about the output

[00:19:19.520] but it's actually like you know that if

[00:19:21.280] the what comes what gets bubbled out of

[00:19:23.039] the probe is correct then then that's

[00:19:26.240] cor then then then the output you don't

[00:19:28.960] care like of the non-deterministic if

[00:19:30.799] the output itself is like plain text

[00:19:32.640] then it's really hard to evaluate if

[00:19:34.080] that's it's harder to evaluate if that's

[00:19:35.919] correct or not but you can guarantee

[00:19:37.760] that the internals of the method

[00:19:39.200] actually were executed properly. Exactly

[00:19:42.480] right. So like right over here we talked

[00:19:44.160] about like this chatbot concept where

[00:19:46.000] the output is going to be a message

[00:19:47.280] that's shown to an end user but we know

[00:19:49.440] our chatbot consists of many different

[00:19:51.880] substeps. So right over here one of the

[00:19:54.240] substeps could be intent analysis. So we

[00:19:57.679] called we actually output out of our

[00:20:00.039] system the probe that tells us what the

[00:20:03.280] intent is and any other subcategories or

[00:20:05.280] steps that we find very

[00:20:06.919] useful and then we would actually return

[00:20:09.600] that to

[00:20:11.400] us. Does does that kind of make sense

[00:20:13.919] Dexter? It does. Are you are you

[00:20:16.480] drawing? I'm not seeing your stuff

[00:20:17.760] updating. Okay. Yeah. Um about a couple

[00:20:21.440] more. But people seem to be really

[00:20:22.880] curious about how do you do things for

[00:20:24.240] summarizers and then also how do we do

[00:20:26.400] things for a couple other scenarios. So

[00:20:28.640] while we do this um I'm going to send

[00:20:30.799] over a YouTube video uh to show and I

[00:20:33.200] think this is probably the best example

[00:20:35.120] that I can have. Can I screenshot

[00:20:36.480] Dexter? Yeah. Um okay.

[00:20:41.600] Yeah, you can steal it. Go for it.

[00:20:50.390] Okay. Uh one second. I'm going to do one

[00:20:50.400] more thing.

[00:20:59.190] Okay. So, now let's talk about a couple

[00:20:59.200] more things that I want to talk. People

[00:21:00.480] talked about summarization. So, I'm

[00:21:01.679] going to get to that in a second, but I

[00:21:03.280] want to talk about like other kinds of

[00:21:04.880] things. So, uh we've worked with a

[00:21:07.919] couple finance companies for quite some

[00:21:09.600] time now. And I think a lot of people

[00:21:12.000] don't realize how to think about

[00:21:15.480] eval. So, I'm not going to mute the

[00:21:17.600] video and I'll just talk through it. Uh,

[00:21:19.919] if my internet would catch up, I'm at

[00:21:21.919] 140p. Um, I'm at 1080p. So, what the

[00:21:25.360] Here we go. What the goal of this video

[00:21:27.039] is is we're going to extract data out of

[00:21:29.440] financial records, all kinds of

[00:21:31.280] financial records. Um, and normally I'll

[00:21:33.679] run this code live, but it's just easier

[00:21:35.039] because I don't want to share I don't

[00:21:36.320] have the actual PDFs on me right now.

[00:21:37.840] So, it's just easier to go run this. And

[00:21:40.320] we all know how to go build this sort of

[00:21:42.000] thing. This basically becomes like a

[00:21:43.600] data model that has a a class with all

[00:21:46.559] these fields attached to it. And then we

[00:21:48.799] also add a category near each one to

[00:21:50.720] know what category it is. So in this

[00:21:51.840] case we have cash, mutual fund, um, and

[00:21:54.799] ETFs as a category. And we can see that

[00:21:56.559] the data pulls out. We all know LM can

[00:21:58.320] go do this. It's an extraction problem

[00:21:59.840] out of images. It's not too hard. We can

[00:22:02.000] go write this out. But now we get into

[00:22:04.960] the more interesting part, which is how

[00:22:07.280] could we build an eval system for this?

[00:22:09.600] Well, one way is one of us could

[00:22:12.080] actually handw write the golden JSON for

[00:22:14.240] this automatically.

[00:22:16.320] Um, and if you do haven't done anything

[00:22:18.400] like this before, you should handw write

[00:22:20.480] the golden data set for your JSON

[00:22:22.000] automatically. And the reason that you

[00:22:23.919] should do that is not because there's no

[00:22:27.039] easier way, but because the first time

[00:22:29.840] you handw write a golden data set, you

[00:22:32.159] are actually going to find

[00:22:33.120] inconsistencies in your data model that

[00:22:35.360] make it look wrong. It's going to make

[00:22:37.679] you think about the problem in a way

[00:22:39.679] that very few things ever will. And

[00:22:42.080] that's that's kind of key to all of this

[00:22:43.840] eval stuff is like define if you don't

[00:22:45.600] know what your inputs look like and what

[00:22:47.919] your the structure of your outputs look

[00:22:49.919] like it becomes really hard to build

[00:22:51.840] your test data set. Exactly. Jonathan

[00:22:54.640] said it need to build the intuition and

[00:22:56.799] that's kind of the whole point about

[00:22:58.640] like when we were actually going to when

[00:23:01.600] when we built BAML the whole point of

[00:23:03.039] hitting play in the playground was to

[00:23:04.480] help you build that intuition. That's

[00:23:06.080] why I say five evals are the best

[00:23:08.080] because if you have no eval, the best

[00:23:09.600] thing you can do is look at the output.

[00:23:11.520] That is literally the best thing you can

[00:23:12.960] go do. As the model outputs something

[00:23:14.480] reasonable, you know, you're probably on

[00:23:15.840] the right track. But as you grow, you

[00:23:18.480] can't vibe eval because we're all busy

[00:23:20.960] people and we don't want to vibe

[00:23:22.280] forever. So want to build something

[00:23:24.559] better. So we're going to build

[00:23:25.919] systematic ways to go do this. So So for

[00:23:28.080] this, you can imagine building a golden

[00:23:29.840] data set of all of these exact financial

[00:23:31.919] transactions. And in my golden data set,

[00:23:34.640] I may be okay if asset name doesn't

[00:23:36.720] match perfectly. I'm okay with that. I

[00:23:40.159] want the symbol to be perfect. I want

[00:23:43.039] quantity to be perfect. I want current

[00:23:45.200] price to be perfect. And I want cost

[00:23:47.440] bases and market value to be perfect. So

[00:23:49.919] you can see how I can even have a blend

[00:23:51.440] of correctness on my golden data set

[00:23:53.760] where I want I want a warning if the

[00:23:55.440] asset name doesn't uh fire and I want to

[00:23:58.000] visualize that in some way but I want

[00:24:00.640] everything else to be completely

[00:24:02.840] correct and I think we could all go

[00:24:05.280] write that JSON but now we can do

[00:24:07.840] something

[00:24:08.679] else which is in this specific data

[00:24:12.559] model we actually have some validations

[00:24:14.559] that are built into place and we can do

[00:24:17.120] runtime evals that means eval on

[00:24:19.520] production data naturally over time. So

[00:24:22.880] what would one of those look like? Does

[00:24:24.480] anyone have an idea? Actually, I'm going

[00:24:25.840] to pose this before I spoil it. Does

[00:24:27.520] anyone have an idea of given this data

[00:24:29.600] model, what do they see as a possible

[00:24:32.159] runtime

[00:24:37.350] eval? You can unmute to talk or you can

[00:24:37.360] just like type in chat.

[00:24:45.190] I assume we're not including like the

[00:24:45.200] type of the dollar value should be a

[00:24:47.440] number and not a string, right? Like

[00:24:49.360] let's go beyond that. We get that. So

[00:24:51.600] Matt has a really good idea. Column sums

[00:24:54.400] data from an API is another great one.

[00:24:57.679] Um you could make sure that the cost

[00:25:00.080] basis times the price equals the market

[00:25:02.559] value or I don't know there's some

[00:25:03.760] there's some like row-wise computation

[00:25:05.600] there that's supposed to that that's

[00:25:07.039] supposed to add up, right? I don't do I

[00:25:08.880] don't do finance. Exactly. And like this

[00:25:10.400] is exactly what the mouse is going to

[00:25:11.440] show. It's like quantity current price

[00:25:13.440] should equal market value. We know that

[00:25:16.080] that is a mathematical truth in our data

[00:25:18.320] model. And guess what? We can actually

[00:25:20.240] go build that

[00:25:21.480] out. Like we can actually just go do

[00:25:23.520] that. That's a really really fast

[00:25:25.200] operation that we can go do. It's pure

[00:25:26.799] programmatic. And we can just look at

[00:25:28.320] the delta.

[00:25:30.880] Uh right. And BAML supports this, right?

[00:25:33.039] Are we going to go into that or are we

[00:25:34.159] gonna That's like that's like runtime

[00:25:36.080] evals, right? That's that's kind of

[00:25:38.159] that's a separate thing how you do it

[00:25:39.840] like we can talk about in a second. Like

[00:25:41.200] yes, you can do this in BMAL, but that's

[00:25:42.559] not the point here. I think the point

[00:25:43.919] here is look at your data model and

[00:25:45.840] think about what you can go do with your

[00:25:49.200] data models to see if you have some

[00:25:50.799] constraints you can build in. And this

[00:25:52.080] isn't just a one-way thing you can build

[00:25:53.600] in. You can actually build

[00:25:56.200] in multiple sums given this data model.

[00:25:58.960] I could say that hey, all my cash value

[00:26:01.520] should equal this cash

[00:26:03.880] value. All my mutual fund value should

[00:26:06.799] equal this mutual fund value. I can even

[00:26:08.640] have summings built in, not just

[00:26:10.240] multiplications per row, but AC a sum

[00:26:12.799] across columns as well, which can help

[00:26:14.880] me build even more assurance that the

[00:26:17.440] data is correct. And I'll give you an

[00:26:19.440] example about what happens when this

[00:26:20.640] data goes wrong. So, we have another

[00:26:24.640] document here. I hope you can see and

[00:26:27.440] I'm going to fast forward to the point

[00:26:28.559] where it's like done processing. And and

[00:26:30.799] while you're doing that just like very

[00:26:32.080] clearly this is this is interesting

[00:26:33.679] because it it it draws a line between I

[00:26:35.679] mean we looked a little bit at some of

[00:26:36.960] the testing stuff but basically these

[00:26:38.960] are all deterministic evals. This is not

[00:26:41.600] a model outputting whether something is

[00:26:43.840] yes or no. This is you do the math in

[00:26:46.640] runtime code and decide whether the

[00:26:48.799] extraction is correct or not. Exactly.

[00:26:51.679] So here you can see exactly what the

[00:26:53.279] model did. The model took out this stock

[00:26:54.720] form and pulled out a bunch bunch of

[00:26:56.480] data about it. And check out what it did

[00:26:58.720] here. It said that the price of Nvidia

[00:27:00.320] Corp was

[00:27:02.840] 113.063. And look at this price right

[00:27:04.960] over here.

[00:27:06.960] Oh no. Right. And you can see why the

[00:27:10.080] model did this. It didn't do it for any

[00:27:11.840] other number, but it did do it for

[00:27:13.880] Nvidia. Um, and it looks like what ended

[00:27:16.640] up happening is the model did this and

[00:27:18.080] later realized that that was dumb and

[00:27:19.440] chose not to do it ever again, but it

[00:27:22.520] didn't. Um, and normally this could be a

[00:27:25.520] huge issue if the model did something

[00:27:27.440] like this. Imagine you're transacting

[00:27:28.559] across millions of entries uh and

[00:27:31.200] millions of stocks. You could easily

[00:27:32.559] have this could be a major like major

[00:27:35.520] issue on an accounting balance sheet.

[00:27:37.919] But we can do the same math again. We

[00:27:39.440] turn that on. You can see how fast it is

[00:27:40.880] because we're not actually using an LLM.

[00:27:42.559] We're purely modeling it

[00:27:44.760] out. And now we actually are running

[00:27:48.080] this out and now we found that it's off

[00:27:50.080] by 27 cents. And that makes sense

[00:27:51.600] because 0.003 * 90 is 27 cents. We found

[00:27:55.520] the discrepancy. And the idea here is

[00:27:59.039] often a technique that we use in machine

[00:28:00.640] learning is that one thing might be

[00:28:02.679] wrong. But it's statistically very

[00:28:05.279] unlikely that you get the right you get

[00:28:06.880] the wrong quantity, the wrong current

[00:28:08.240] price, and the market value adds up

[00:28:10.520] correctly. It's very unlikely for that

[00:28:13.120] to

[00:28:14.120] happen. So we we're using law of

[00:28:16.720] probabilities. And then even more

[00:28:18.159] unlikely is that all the market values

[00:28:20.080] added up together will equal to the

[00:28:22.240] total market value up here.

[00:28:24.480] So we're just building probabilistic

[00:28:26.640] systems and obviously mistakes can still

[00:28:28.720] happen, things can still go wrong, but

[00:28:31.760] it's it's we're just building a system

[00:28:33.919] of

[00:28:34.840] unlikely. Uh and that's all we can do.

[00:28:37.039] Just like with humans, it's a

[00:28:38.559] probabilistic system and if we multiply

[00:28:40.559] enough probabilities together, they get

[00:28:42.080] really really

[00:28:43.320] small. So now that we have this mistake,

[00:28:45.840] what can we do about it? Well, the

[00:28:47.679] beautiful thing about building a system

[00:28:49.120] like this is we have a couple of

[00:28:50.640] options.

[00:28:52.440] One, what we can do is we can say we can

[00:28:55.679] just have a human come in and go update

[00:28:58.200] this. Two, we can just record that it's

[00:29:00.720] an error. Three, we can go run this over

[00:29:03.919] and over again until we get the right

[00:29:05.440] answer. Or four, what we could do is we

[00:29:07.440] could have another LM say, "Hey, Nvidia

[00:29:09.600] Corp was off by 27 cents. Give it just

[00:29:12.399] the data for Nvidia Corp and ask it to

[00:29:14.159] extract only Nvidia

[00:29:16.840] Corp." And now the LM is much more

[00:29:20.000] likely to get it correct. because you're

[00:29:21.919] giving it information about the

[00:29:23.240] inconsistency. You don't even have to

[00:29:24.960] say what is inconsistent. You can just

[00:29:27.120] say when I do quantity times current

[00:29:29.279] price uh equals market value, I get a

[00:29:31.440] delta of 27 cents. And now the model can

[00:29:33.919] all autocorrect. So now you've go you

[00:29:36.240] can go solve this

[00:29:38.679] problem.

[00:29:40.200] So I'm going to I'm going to pause here

[00:29:42.640] about numbers. It sounds like people get

[00:29:44.000] the point about numbers and pashant is

[00:29:45.520] asking uh I think the best question

[00:29:48.640] which is how do we do this for string

[00:29:52.679] evals and I think does anyone have an

[00:29:56.240] idea of what I'm going to go

[00:30:09.110] say reax close um I think it's more

[00:30:09.120] about two aspects of it one is In the

[00:30:13.120] very beginning, you should build a

[00:30:15.200] diffing system that allows you to see

[00:30:17.120] the diff between the previous run and

[00:30:18.960] the and the most recent run. Oh yeah,

[00:30:22.480] we've done this when we were like

[00:30:23.840] migrating APIs for super systematic

[00:30:26.159] stuff of like, hey, we're going to move

[00:30:27.679] a 100 endpoints to a new system. Like,

[00:30:30.720] show me the diff between all the old

[00:30:32.399] endpoints and all the new endpoints.

[00:30:34.080] Exactly. And a lot of people ask like,

[00:30:36.000] damn, does that mean I have to build

[00:30:37.120] custom UIs to go do all the stuff or

[00:30:39.679] like can I just use something off the

[00:30:40.960] shelf? And I've gone through this battle

[00:30:43.279] a lot uh in a lot of different orgs and

[00:30:45.440] we've made totally different decisions.

[00:30:47.200] Uh we made different decisions on Face

[00:30:48.799] ID, we made different decisions in

[00:30:50.159] Hollands, we made different decisions at

[00:30:52.080] D Shaw and with all the people that we

[00:30:54.159] worked with, I've seen people make

[00:30:55.200] different choices.

[00:30:57.200] The answer that I have seen

[00:31:00.600] um the uh the answer that I have seen

[00:31:04.799] all the time is actually

[00:31:07.559] that bespoke UIs end up powering your

[00:31:11.120] team a lot more than you think and

[00:31:13.200] because of things like v0ero it's not

[00:31:15.120] that hard to build. I was going to say

[00:31:17.520] in the last year the calculus has

[00:31:19.919] shifted a lot between should we build

[00:31:22.720] something in house to like kind of just

[00:31:24.480] visualize some data real quick versus

[00:31:26.320] like do we need to go get a tool or an

[00:31:28.240] open source project and deploy it off

[00:31:30.159] the shelf like if I were every time I

[00:31:33.279] build evos for any data set this is my

[00:31:35.200] workflow whether no matter what it is I

[00:31:37.279] have a JSON object that I'm rendering I

[00:31:39.039] know the type of that JSON object all

[00:31:40.880] the time um and then every single time

[00:31:43.760] actually for every single use case I

[00:31:45.360] actually build a unique bespoke renderer

[00:31:47.440] for that JSON object. I'm like like diff

[00:31:49.279] these two things for me. And like

[00:31:51.840] sometimes I want I want the diff to be

[00:31:53.279] exact, sometimes I want to be

[00:31:54.240] approximate, I just like vzero my way

[00:31:55.760] through it. It takes about an hour, but

[00:31:58.640] if the system I'm working on is really

[00:32:00.240] sensitive and I'm looking to like 100

[00:32:02.279] plus input output pairs, it is worth

[00:32:05.440] building. If I'm looking at like 10, I

[00:32:07.039] just look at it manually and just look

[00:32:09.200] at and just like compare the files

[00:32:10.679] myself. So the number one go ahead.

[00:32:14.240] Sorry. No, I mean that kind of

[00:32:15.120] attraction was something I think um I've

[00:32:17.519] heard I forget who was saying it but

[00:32:19.200] basically like someone who talked to a

[00:32:20.559] ton of founders doing evals for

[00:32:22.480] production enterprise stuff was

[00:32:23.760] basically like almost nobody is stressed

[00:32:26.799] out about building the test harness for

[00:32:29.760] eval whether it's the thing that runs

[00:32:31.519] the test whether it's the thing that

[00:32:32.799] evaluates the results what whether it's

[00:32:35.360] the thing that visualizes the results

[00:32:37.840] everybody agrees that the hardest thing

[00:32:39.600] is getting the golden data set and

[00:32:41.600] getting the actual answer key correct

[00:32:45.360] Yeah. Uh, one thing I wish were better

[00:32:47.120] for support was for things beyond React.

[00:32:49.120] Yeah, I really wish there was. Um, I

[00:32:51.200] mean, we we've been looking into how to

[00:32:52.559] build different UIs automatically for

[00:32:54.159] different data models for you, but it

[00:32:56.720] turns out to be a very challenging

[00:32:57.919] problem. We're just going to wait and

[00:32:59.120] sit and look a little bit longer before

[00:33:00.799] we like I see something some patterns

[00:33:02.640] more so emerge. But I do think there's

[00:33:04.880] another question here. Um, why why is

[00:33:06.880] the LM doing math in the neural network?

[00:33:08.880] Shouldn't it be using a math tool call?

[00:33:10.960] Oh, this isn't actually doing math for

[00:33:12.880] for by the way, what this data set is

[00:33:14.720] doing is like it's just saying like,

[00:33:16.240] hey, I have this data model and this

[00:33:18.480] data model, if I can pull the whole

[00:33:19.760] sheet up somewhere, this actually has

[00:33:21.840] market value, price, quantity, and

[00:33:23.600] everything in here. And I'm just like

[00:33:24.720] pulling out all the data from like a

[00:33:26.320] data I have. So, this blue column is

[00:33:29.440] basically not computed by an LM. This

[00:33:32.399] blue column is added after the

[00:33:34.240] extraction happens by deterministic

[00:33:36.080] code. Exactly. It's literally just a

[00:33:37.840] React thing that I said where the value

[00:33:39.360] of this column is equal to the

[00:33:40.960] multiplication of these two things. So,

[00:33:42.399] I'm not actually doing this in in the

[00:33:43.519] LM. If if you're doing this in the LM,

[00:33:45.200] you're wrong. Don't do that. Uh don't m

[00:33:48.480] just like multiply the numbers. You

[00:33:50.159] don't need an LM to wait for the math to

[00:33:51.919] do the

[00:33:52.840] math.

[00:33:55.240] Um so, I want to talk about u what yeah,

[00:33:58.960] I want to talk about something more

[00:34:00.159] specific. So, I'm going to pull up an

[00:34:03.039] example that I think is going to help

[00:34:04.559] make everything more concrete.

[00:34:06.880] Um, so for example, my my mother is a

[00:34:10.480] teacher. Um, and part of what she does

[00:34:13.200] is she makes lesson plans and you could

[00:34:15.760] imagine that we can go to an LLM and ask

[00:34:17.599] it to make a lesson plan for us. And

[00:34:20.079] that could be good. So, let's go take a

[00:34:22.240] look at how I'm just going to write a

[00:34:24.000] basic prompt that makes a lesson plan.

[00:34:26.000] And I hope the lesson plan example is

[00:34:27.839] good enough because it's very textually

[00:34:29.960] heavy. And we can talk about how one

[00:34:32.240] could make that better. Does that sound

[00:34:33.919] good to everyone in terms of like a

[00:34:35.440] problem that sounds uh relevant?

[00:34:39.200] So the so the inputs and the outputs to

[00:34:41.280] that system would be like a couple

[00:34:43.200] sentences about the lesson plan and then

[00:34:45.280] the output would be kind of a you know

[00:34:47.599] two-page structured document of like hey

[00:34:49.760] here's how to structure it and here's

[00:34:50.960] all the steps and here's the worksheets

[00:34:52.480] and stuff like that. I don't know. Let's

[00:34:54.639] just see what it does given a All right.

[00:34:56.079] Yeah. Let's see what we get. Something

[00:34:57.200] something like that though, right? Like

[00:34:58.320] the the interface is okay. So it's going

[00:35:02.000] to do something. Yeah. You put in a

[00:35:03.359] topic and then it generates the lesson

[00:35:04.720] plan. Yeah, it'll do something. And like

[00:35:06.880] I think the first question we all have

[00:35:08.640] is how the heck do we measure that?

[00:35:11.640] Um, and like this is probably good

[00:35:14.200] enough. Um, so I'm just going to copy

[00:35:16.400] this and I'm going to open cursor and am

[00:35:18.560] I sharing cursor?

[00:35:21.839] There's a there's a BAML source in the

[00:35:24.960] directory for this episode if you want

[00:35:27.119] to use that.

[00:35:29.280] Am I sure?

[00:35:32.480] Uh oh, we're still seeing your browser.

[00:35:36.599] Which I will share my whole screen, I

[00:35:39.359] guess. Okay. Yeah.

[00:35:44.950] And then let's go to designing evals and

[00:35:44.960] then I'm going to put this and put like

[00:35:46.320] lesson plan in

[00:35:52.710] here. So now we have a lesson plan. Um

[00:35:52.720] and I think the first thing to think

[00:35:54.560] about how to do emails is remember

[00:35:58.079] ignore the fact that it's generated by

[00:35:59.599] an LLM. It doesn't matter. The only

[00:36:01.760] thing I really have to eval here is

[00:36:03.359] given some topic, I will produce this

[00:36:06.160] lesson plan data model. The fact that an

[00:36:08.720] a single LM call produces it, the fact

[00:36:10.880] that a whole composition of workflows

[00:36:13.040] produces it, the fact that I sent it

[00:36:14.880] over to some like mechanical Turk that

[00:36:17.200] filled it out for me doesn't

[00:36:19.720] matter. All that matters is given some

[00:36:22.440] string, I'll produce this data model. So

[00:36:26.640] now I know what I'm building. when I

[00:36:28.480] write an email, I don't I actually kind

[00:36:30.079] of ignore the fact that this lesson plan

[00:36:31.920] works. So like what and this is that

[00:36:33.839] idea of like semi-structured data where

[00:36:35.520] you're outputting JSON but the fields in

[00:36:37.520] the JSON are strings which are hard to

[00:36:39.359] evaluate deterministically. Yeah, like

[00:36:41.520] right over here, right? Like like I

[00:36:43.760] don't even know what it did but it's

[00:36:45.119] like it's outputting something and like

[00:36:46.640] I don't know maybe this is good. So one

[00:36:48.560] of the things that I can do is like time

[00:36:49.920] allocation. Instead of this being a

[00:36:51.839] string, let's just make this like um

[00:36:55.240] int and like alias this to uh time

[00:36:58.640] allocation

[00:36:59.880] mins. So the first thing I can do is I

[00:37:02.079] can put um I can change one of my fields

[00:37:04.320] to be a

[00:37:06.040] number. So now I have a number this like

[00:37:08.400] 45 minutes. Now what I might want to do

[00:37:10.880] when I actually do my lesson plan is and

[00:37:12.400] I think this is the part where people

[00:37:13.760] get

[00:37:15.560] stuck. Evaluate lesson

[00:37:17.960] plan. Oops. uh client. Okay,

[00:37:26.150] cool. Instead of viewing this as an

[00:37:26.160] instead of viewing this as a method, all

[00:37:28.000] I really need to do here is I need to

[00:37:29.680] say given a topic string lesson plan,

[00:37:32.480] I'm going to produce some evaluation

[00:37:33.760] result for it.

[00:37:36.640] What's the result? Is that going to be a

[00:37:37.920] structured object or is that going to be

[00:37:39.280] a string or what? That's the whole

[00:37:40.800] point. I could do a string as an

[00:37:42.960] evaluation for my lesson plan and then

[00:37:45.440] what I could do as a human is I could go

[00:37:47.040] analyze it myself. you go read the

[00:37:49.119] string. I could literally I could read

[00:37:50.480] the string. I could literally be like uh

[00:37:52.720] be like evaluate the lesson plan for

[00:37:54.240] third uh for third grade students blah

[00:37:56.480] blah blah and it'll just output

[00:37:57.760] something and I could and this is

[00:37:59.359] basically like a standard this is like

[00:38:01.440] LLM is judge, right? Like you could this

[00:38:03.680] doesn't even have to be an you could

[00:38:04.960] this could be a dynamic thing you do at

[00:38:07.359] runtime inside your pipelines if you

[00:38:09.040] wanted to, right? and you just save it

[00:38:10.560] somewhere and every single time a user

[00:38:12.400] reports it as bad, you flag that

[00:38:14.720] database entry for the lesson plan with

[00:38:17.520] its evaluation that you don't show the

[00:38:19.359] user Yeah. to someone on your team and

[00:38:22.640] they look at it and you go and now

[00:38:23.760] you've kind of built an answer set of

[00:38:25.440] like of some sort of evaluation set on

[00:38:28.000] there like this topic or this lesson

[00:38:29.520] plan was good, this topic or this lesson

[00:38:31.119] plan was bad and now you've built some

[00:38:32.640] sort of proxy for it and you might even

[00:38:34.640] find like the string to be helpful in

[00:38:36.400] deciding

[00:38:37.320] that. Now there's another thing we can

[00:38:39.839] do. We can actually uh yeah so rating

[00:38:42.880] systems are bad. Please do not use

[00:38:44.160] numbers. Anyone that use numbers is

[00:38:46.599] wrong. So we can actually write an

[00:38:49.119] evaluation from this. Now what makes a

[00:38:51.359] good lesson plan? Like we can say

[00:38:54.119] pacing the how good is the pacing and

[00:38:57.680] the pacing can be can be slow, medium,

[00:39:02.280] fast. And maybe I care about how fast

[00:39:04.960] the system is. And I I just want to know

[00:39:08.240] is the topic too fa fast. Maybe I want

[00:39:11.040] to know like what kind of biasy bias

[00:39:13.040] towards uh

[00:39:15.320] biases uh string array any biases in the

[00:39:18.240] lesson plan that I might want to know.

[00:39:19.760] Like maybe there are topics that we

[00:39:21.680] shouldn't be covering or examples that

[00:39:23.520] we shouldn't be covering and I want to

[00:39:24.640] flag them. They could be examples of any

[00:39:27.599] kind. Uh and I can even like add

[00:39:30.800] something else here. anybody that could

[00:39:32.800] be problematic that could uh make a

[00:39:36.320] student feel uncomfortable and I could

[00:39:39.200] assert that in the lesson plan

[00:39:40.839] evaluation this thing is empty like I

[00:39:43.920] always want biases to be empty and very

[00:39:46.680] very validate that I could talk about

[00:39:48.880] like yeah the the one that really stood

[00:39:50.720] out to me was like a lot of these need

[00:39:52.640] like six different materials like

[00:39:54.400] construction paper and glue and scissors

[00:39:56.480] and stuff like that and like you could

[00:39:58.640] evaluate like price of materials or

[00:40:00.880] something like or like scope of mater

[00:40:08.710] and then so sorry as we build this if we

[00:40:08.720] if we run these things is the idea to

[00:40:11.680] kind of build our eval system and then

[00:40:13.599] tweak our core prompt and then like see

[00:40:17.119] how our score changes exactly and it

[00:40:19.839] actually becomes really easy to even

[00:40:21.119] write this now we have like deaf lesson

[00:40:24.280] plan test

[00:40:30.470] harness and like it can be a topic which

[00:40:30.480] is a stir

[00:40:38.270] Right. Sorry, I can't type very

[00:40:38.280] fast. From client import. Basically,

[00:40:41.520] what we're taking away from this is like

[00:40:42.800] there's there's nothing too fancy going

[00:40:44.560] on here. This is all just prompting the

[00:40:48.200] LM in structured ways to get it to talk

[00:40:51.520] about what's going on. Exactly. And now

[00:40:53.280] I can build I can build

[00:40:55.079] assert. I can build like the

[00:40:57.880] pacing is not equal to

[00:41:01.240] fast right. I can assert that biases

[00:41:06.040] do

[00:41:08.839] len is zero. I can say the cost is less

[00:41:11.920] than like $5. Maybe I'm okay with

[00:41:14.800] student spending $5 on a lesson plan or

[00:41:16.560] something. Um and then I can even say

[00:41:18.880] like like I can even require like I can

[00:41:21.520] say like is

[00:41:23.800] quality equals

[00:41:25.880] input is that

[00:41:28.119] good? I can even like print um print uh

[00:41:33.520] and at the very end I can even have a

[00:41:35.040] last part of my eval just have a human

[00:41:36.800] go look at it. So you can see how I can

[00:41:39.280] build up my systems automatically and

[00:41:41.359] like decide where my criteria is. Like

[00:41:44.640] hey I work in a slightly poor school

[00:41:46.319] district so I want to make sure that

[00:41:47.839] costs are never going to be a problem.

[00:41:49.599] In fact I want all my lessons plans to

[00:41:51.760] be free and I want to build a system

[00:41:53.760] that optimizes for free. And it might

[00:41:56.319] even be like one of the things in the

[00:41:58.160] topics are like

[00:42:00.200] constraints which are a string that I

[00:42:02.319] pass in that should be passed in to my

[00:42:04.079] lesson

[00:42:05.480] plan. And this could be a boolean or

[00:42:08.480] something else. This could even be a

[00:42:09.760] data model of some kind that produces

[00:42:12.480] some string on its own which is like I I

[00:42:15.760] what type of school district are you

[00:42:17.440] working

[00:42:18.280] for? Is there we can evog

[00:42:23.280] uh if this is something being run live

[00:42:25.280] can we evoglo? Yes. So the e-log and

[00:42:27.680] live data is something I always talk

[00:42:29.040] about. So like this is an example that I

[00:42:31.839] use pretty often that many of you would

[00:42:33.520] probably have seen by now. Oops.

[00:42:37.000] Sorry, what is

[00:42:39.400] wrong? Um, sorry. I'm gonna run my Give

[00:42:42.720] me one second. I'm gonna move this so

[00:42:44.000] you don't see my API

[00:42:51.870] key. Okay, there we

[00:42:51.880] go. Give me one second. So, like in this

[00:42:54.560] case, imagine I'm processing millions of

[00:42:56.160] Cambodia visas. And obviously, we can do

[00:42:58.720] things in eval here. One of the things I

[00:43:00.560] can do in Eval is literally build the

[00:43:02.240] exact JSON that they should pull out.

[00:43:04.720] And I'm very sensitive to certain things

[00:43:06.880] like I want to make sure that it

[00:43:08.079] correctly checks these check boxes off.

[00:43:10.480] Maybe I don't care if it I want to make

[00:43:12.000] sure it gets a personal information

[00:43:13.359] perfectly correct. I may not care

[00:43:15.359] perfectly about the address or

[00:43:16.560] everything else because I can use

[00:43:17.520] corroborating information to find that

[00:43:19.280] information. Yeah. Sorry, real quick.

[00:43:22.000] And maybe to guide this a little bit, uh

[00:43:23.760] I'm really curious to know like let's

[00:43:25.680] say you've processed a hundred of these

[00:43:27.440] visa forms and you've pulled out the

[00:43:29.359] schema and you have your golden data

[00:43:30.800] set. Like how can you make a statement

[00:43:33.200] about like I am now confident that we

[00:43:35.599] are 98% accurate in extracting data from

[00:43:38.640] forms like this like how can you how can

[00:43:41.200] you kind of take the past results and be

[00:43:44.079] able to say you know reliably like we

[00:43:47.359] expect our future performance to be 98%

[00:43:50.319] or 91% or whatever it is. Yeah, that's

[00:43:52.800] usually where people struggle and and

[00:43:54.319] the answer is you can't actually make

[00:43:56.160] that statement perfectly. You're missing

[00:43:58.319] a step in order to make that statement.

[00:44:00.720] You make the golden data set once and

[00:44:02.560] now you're like our pipeline works on a

[00:44:04.319] golden data set at this percentage of

[00:44:06.079] accuracy and meets our criteria to ship,

[00:44:08.400] right? How do you know if you've over

[00:44:09.680] bid to that data set though, right? So

[00:44:11.680] what you do then is you actually have to

[00:44:13.839] spot check your production data at some

[00:44:16.960] cadence and continue adding to your

[00:44:18.960] golden data set at some cadence. That I

[00:44:22.400] I know you're I interrupted you in the

[00:44:24.000] middle of talking about this thing, but

[00:44:25.119] it could be useful um after to pull in

[00:44:27.839] and like what does the architecture of

[00:44:29.119] that pipeline look like? like where what

[00:44:30.960] where in the where in where in the

[00:44:32.400] process are you storing stuff and like

[00:44:33.920] how do how do you how do you build that?

[00:44:36.000] So I mean this is just one way to do it

[00:44:37.520] but you don't actually have to just to

[00:44:38.880] be very clear. Um what you really need

[00:44:41.119] to capture when you go down this road is

[00:44:43.599] did I did I capture everything? Oh yeah,

[00:44:45.760] let me change

[00:44:47.400] this. What you really want to do when

[00:44:49.680] you go down this road? How do I change

[00:44:51.040] this 30? You're you're talking about

[00:44:52.640] just like capture every every input

[00:44:55.040] output pair. Literally have to capture

[00:44:56.640] every input output pair and there's no

[00:44:58.079] shortcut around this at all. And more

[00:45:00.480] specifically, what you really want to go

[00:45:02.079] do is give it a second is when this data

[00:45:05.760] comes back in or out, what you really

[00:45:07.440] want to say is like how well is my is

[00:45:09.440] blog post function doing and you just

[00:45:12.240] have to spot check and look at is blog

[00:45:14.319] post. And there's no good shortcut for

[00:45:16.560] this. You have to build up your eval set

[00:45:20.000] continuously over time and you have to

[00:45:21.920] say like for this HTML page, is this

[00:45:25.359] actually the right title on the blog

[00:45:27.040] post? And like you can imagine a title

[00:45:29.040] for a blog post is like I don't freaking

[00:45:32.000] know like maybe um is this the right

[00:45:34.880] title? Is this a blog post? Is this not

[00:45:36.400] a blog post? And for context just to

[00:45:38.319] show everyone what this was running on

[00:45:39.599] is I made a small little demo that I

[00:45:41.440] wanted to go do which was when I go

[00:45:43.760] extract data from like a let's say I

[00:45:46.079] have a bunch of blogs. I want to go see

[00:45:48.000] for every single blog on a entire site

[00:45:51.280] what is it a what's the value ratio? Is

[00:45:53.520] it balance? Is is it an ad or is it

[00:45:56.160] educational content? How deep of

[00:45:58.400] educational content is it? Then like

[00:45:59.839] what insights does it have? So it's

[00:46:02.240] probably very easy for me to like

[00:46:04.640] actually build a golden data set around

[00:46:06.640] primary

[00:46:07.720] intent. That is really easy. Key

[00:46:10.800] insights is going to be much harder for

[00:46:12.560] me to go do. But what I can say is

[00:46:16.599] Nex.js should be mentioned in key

[00:46:18.960] insights

[00:46:19.960] somewhere. So I can just reax for that

[00:46:22.560] for this specific blog post, not for

[00:46:25.040] everything, but for this one. And

[00:46:26.560] that'll take me time. The other thing I

[00:46:28.880] can do is I can rerun this same exact

[00:46:31.280] data model on my next prompt and just

[00:46:34.079] see what it output out next

[00:46:36.359] time and just look at the diff between

[00:46:38.720] these two

[00:46:46.309] structures. Yes, exactly. Yes. For now,

[00:46:46.319] like and it's not it's not even living

[00:46:48.000] in your code. I think that's the most

[00:46:49.359] important part.

[00:46:51.040] It's not even living in your code. It's

[00:46:52.480] living in a hybrid of your code and your

[00:46:55.240] data. And that is the part that most

[00:46:57.680] people miss. Evals are not purely living

[00:47:00.560] in your code because eval are purely a

[00:47:02.319] diffing

[00:47:03.319] mechanism. You have to be able to sorry,

[00:47:06.240] what does living in your data mean? So

[00:47:08.480] like in order for me to actually eval

[00:47:10.160] this correctly, what I need to be able

[00:47:11.520] to do is I have run this like two weeks

[00:47:13.359] ago last time I last time I was building

[00:47:15.760] this prompt. Then a new engineer comes

[00:47:18.079] on and let's assume the models have

[00:47:20.000] stayed constant the whole time. Nothing

[00:47:21.920] has changed about the model in some way

[00:47:23.839] and a new engineer has come and started

[00:47:26.240] updating this prompt in some way. What

[00:47:29.119] they really want to know is the last

[00:47:31.920] time I ran this I got this output. The

[00:47:34.720] next time I ran this I got this output.

[00:47:37.520] And so that's like on your PR you could

[00:47:40.079] get a like output from some eval system

[00:47:42.960] that basically says like cool here's a

[00:47:44.720] here's a link to a page about how all

[00:47:46.400] the outputs have changed between the

[00:47:48.000] first one and the second one and someone

[00:47:49.359] can literally go skim those and eyeball

[00:47:51.119] those and say like oh that that's a huge

[00:47:53.280] block of red let's go see if I broke

[00:47:55.359] some edge case that we know we want to

[00:47:57.200] make sure still works exactly and you

[00:47:59.440] can even build a uh you can even build

[00:48:01.760] like a rule set around that is like hey

[00:48:03.839] my diff for my eval should be small so

[00:48:06.480] you measure the lines of diff in your

[00:48:08.400] eval. So like even even though it's a

[00:48:10.720] text thing, you can build a diffing a

[00:48:13.440] diffing score of how big of a diff you

[00:48:16.040] have. And the and the fact of the matter

[00:48:18.400] is because these are proistic systems,

[00:48:20.560] you really have to go look at

[00:48:23.240] this. Uh what is that question uh that

[00:48:27.359] someone had? I see I can I can imagine

[00:48:30.720] seeing a huge wave of error messages

[00:48:32.480] being mentioned by the LLM being a good

[00:48:35.440] flag for people having issues. I don't

[00:48:37.839] understand that question John if you

[00:48:39.440] could articulate that'd be helpful and

[00:48:40.800] exact I think Jonathan nailed it. very

[00:48:43.040] similar to screenshot UIs like there's

[00:48:46.559] like front end I whenever you work on

[00:48:48.960] front end code for the first time you're

[00:48:50.160] like why does no one write unit test and

[00:48:51.520] you write unit test and you quickly

[00:48:52.640] realize if I write unit test it slows

[00:48:54.559] down my shipping by like a bajillion

[00:48:56.480] orders of magnitude

[00:48:58.640] um and eval systems are really similar

[00:49:01.520] because the way you would write a unit

[00:49:03.440] test is not useful for most of it in

[00:49:06.559] this case I don't need to say I have no

[00:49:09.760] desire to say exactly what the key

[00:49:11.119] insight is there's so many different

[00:49:12.480] ways to say these same

[00:49:14.200] topics. It's totally

[00:49:16.359] useless. But I do want to say one of the

[00:49:18.720] key insights should include the words

[00:49:20.160] React and

[00:49:21.720] Next.js. So like I can go build a a

[00:49:25.359] stronger eval over time. And what I

[00:49:28.240] really need to make sure is no matter

[00:49:29.440] what happens, no matter what the prompt

[00:49:30.880] is, it always answers React and Next.js

[00:49:34.079] in all scenarios. And I have a good

[00:49:36.359] system. My primary intents can be

[00:49:38.960] hardcoded.

[00:49:41.359] um for now. Yes. Uh so is everyone

[00:49:44.559] making their own internal full stack

[00:49:46.480] eval

[00:49:47.480] applications? I wouldn't really say

[00:49:49.280] they're full stack eval applications. I

[00:49:51.359] would just view it as

[00:49:52.839] like when you write like code. Uh when

[00:49:56.480] you write code like this, like you don't

[00:49:58.240] expect anyone else to write your React

[00:49:59.839] components for you. Your React

[00:50:01.280] components are very special to your own

[00:50:03.160] websites. Your functions are very

[00:50:05.359] special to your own system. You might

[00:50:07.119] use really core infrastructure, but you

[00:50:09.359] typically will

[00:50:10.599] use systems and things you don't care

[00:50:13.040] about. You will offload like some we

[00:50:15.119] don't all care about that chat widget

[00:50:16.480] that pops up on our website and we're

[00:50:18.319] okay offloading that to someone else

[00:50:20.400] because we as a social paradigm have

[00:50:22.400] built that sort of paradigm out there.

[00:50:24.800] So even some eval like hey maybe someone

[00:50:26.960] has built a really good sentiment

[00:50:28.240] analysis email eval for like e-commerce

[00:50:31.119] chat

[00:50:32.040] bots. That's okay. We can leverage that

[00:50:34.800] just like we could build we could use

[00:50:36.480] that little chat UI

[00:50:38.119] widget, but we probably won't build our

[00:50:40.880] entire website off of widgets that we

[00:50:42.559] don't

[00:50:44.040] own. And that's that's really what we

[00:50:46.880] recommend, which is learn how to write

[00:50:48.880] the

[00:50:49.800] eval. And then as you write the evals,

[00:50:52.480] it becomes really really easy to kind of

[00:50:55.280] build small little test harnesses like

[00:50:57.599] this one. And then you just run that on

[00:50:59.760] a bunch of data sets and you dump out

[00:51:01.520] files and you build small visualizers to

[00:51:03.839] go do this. And I would never like

[00:51:06.880] Dexter was saying like this is a game

[00:51:08.559] that has changed now. Before you would

[00:51:10.720] have to compromise on worse dashboards,

[00:51:12.960] worse system, but now if you're an

[00:51:14.960] engineer working on a part of a

[00:51:16.000] pipeline, just build it. And it's like

[00:51:18.559] you can building an Nex.js object that

[00:51:20.319] renders a type that is well defined

[00:51:22.559] because you have a type here that you

[00:51:24.960] can just render. You want to render a

[00:51:26.559] lesson plan object, go do that. You want

[00:51:28.240] to build like uh you want to build you

[00:51:31.119] want to render this right? We got you

[00:51:32.800] can we got seven minutes. You want to

[00:51:34.559] show us how you vibe code a eval

[00:51:36.480] visualizer? Yeah. Like let's make let's

[00:51:38.800] make 10 test cases on third grade math

[00:51:40.880] topics and like let's vibe eval. Let's

[00:51:43.200] do it. Let me go run this really fast in

[00:51:44.960] that case. Yeah, we got seven minutes

[00:51:47.119] but I think um as usual we'll probably

[00:51:49.119] go over um let me just ping and see if

[00:51:51.599] we have any other questions. Um yes. So

[00:51:53.440] is everyone making their own internal

[00:51:54.559] full stack eval applications? Sounds

[00:51:57.040] like maybe some people you probably

[00:52:00.079] should maybe um and Andy had a good

[00:52:03.200] question is like is it the same model

[00:52:04.559] call that is generating the eval or a

[00:52:06.640] second agent? Um and I get this question

[00:52:09.040] a lot as well. While you're doing that,

[00:52:10.400] I'll just kind of like think through

[00:52:12.160] this out loud and then I want to get

[00:52:13.440] your answer, which is basically that

[00:52:14.880] idea of

[00:52:16.760] um

[00:52:24.390] like if you ask one model to do a thing

[00:52:24.400] and then you ask another model to

[00:52:26.319] evaluate the thing, maybe you get some

[00:52:28.800] value from cross-pollination. I see this

[00:52:30.640] a lot in like consensus pipelines as

[00:52:32.480] well, where you say like, okay, here's

[00:52:33.760] the question. let me fork it off to four

[00:52:36.160] of the best models and then let me have

[00:52:38.000] a fifth model basically review all the

[00:52:40.400] answers of those four models and then

[00:52:42.240] decide which one is better. Right? I

[00:52:44.000] think DSPI calls this like a consensus

[00:52:46.240] or a judge plan or something like this.

[00:52:49.480] Um,

[00:52:51.000] and the question I always have is like,

[00:52:53.920] well, if the model couldn't get it right

[00:52:55.680] the first time, is the same model going

[00:52:57.920] to be able to get it right the second

[00:52:59.359] time? And or like, if the second model

[00:53:01.839] is smarter than the first model, why

[00:53:03.200] don't you just ask the second model like

[00:53:05.359] in the first place? And I think um there

[00:53:08.160] is a little bit to be said for I think

[00:53:09.760] there's a couple papers on like if you

[00:53:11.359] ask llama 70B the same question 50 times

[00:53:16.240] you get almost as good performance as

[00:53:18.160] llama 405b or something like you there

[00:53:20.640] is value into doing these things over

[00:53:22.160] and over again and then like

[00:53:23.119] synthesizing the results.

[00:53:25.960] Um let's see.

[00:53:29.280] I think u I think that like should use

[00:53:32.079] the same model for everything. Like no

[00:53:34.480] just like your agent should not be the

[00:53:36.079] same model everywhere. Like instead of

[00:53:37.839] viewing this whole thing as like a

[00:53:39.640] separate people I think it's the same

[00:53:43.200] mistake that people do when they build

[00:53:44.559] like entire AI pipelines. They're like

[00:53:45.920] my agent is one thing but your agent is

[00:53:48.160] decomposed of many many boxes. in my

[00:53:50.800] chat agent. The thing that builds the

[00:53:53.920] intent analysis could be a really really

[00:53:55.760] simple GPT40 mini model. Maybe even a

[00:53:58.079] llama 8B. Who knows? But the thing that

[00:54:00.559] generates a SQL query, maybe that can be

[00:54:03.280] a 70B model. And the thing that does a

[00:54:05.520] cipher query against my entire like data

[00:54:08.240] warehouse, we're going to use 03. The

[00:54:11.599] fact that I'm using different models for

[00:54:12.880] them is more of a necessity for how

[00:54:14.559] ambiguous and hard the problem is.

[00:54:17.920] And now what you can do over here

[00:54:20.319] instead is you can just do the same

[00:54:21.920] thing here. Our eval system could use a

[00:54:23.760] different model here. Like in this case

[00:54:25.359] I'm using the same one. I don't think it

[00:54:26.640] really matters, but I will switch to

[00:54:27.920] open eye really fast. Um actually I

[00:54:30.559] don't care. Let's use Sonic. It doesn't

[00:54:31.760] really matter. Um and we'll go run this.

[00:54:34.640] And now I I built this in. So the first

[00:54:36.319] thing I'm going to go do and this is

[00:54:37.760] what gets ends up being really hard

[00:54:39.040] about eval systems is a lot of times

[00:54:42.079] people assume that eval systems are easy

[00:54:45.119] but they end up being really hard

[00:54:47.359] because I do not want like if one of

[00:54:50.800] these asserts fails I get no information

[00:54:52.800] about the other asserts and that's

[00:54:54.720] actually where things end up being

[00:54:55.920] really hard to go read and write and

[00:54:57.359] also if I forget to save the data before

[00:54:59.200] I actually run this that's another thing

[00:55:01.280] that ends up being hard so selfishly I

[00:55:04.160] was actually hoping to show this off

[00:55:05.359] later in about like three weeks because

[00:55:07.040] we had a new thing that was going to

[00:55:08.240] make this way way way better. But I'll

[00:55:10.160] go write the code. Let's see it.

[00:55:13.720] Um uh test

[00:55:17.319] one. So now we have two tests that we're

[00:55:20.079] going to run. And then we'll just run

[00:55:21.359] like I think like pi

[00:55:22.920] test import.

[00:55:26.079] You probably have to UV add it.

[00:55:29.200] Um

[00:55:30.839] yep. Nice. It's probably this. I have no

[00:55:34.400] idea.

[00:55:36.000] UV add pi

[00:55:38.599] test and then one second. I got to put

[00:55:41.119] my API key. Am I still sharing the

[00:55:44.079] window? I'm not. Right.

[00:55:50.390] Uh we don't see the terminal. We just

[00:55:50.400] see the cursor. And yeah, John, that's a

[00:55:53.280] great comment. Evals are a great use

[00:55:54.480] case for switching out a models on which

[00:55:56.480] model delivers the best value for cost.

[00:55:58.960] Exactly. Yeah. And that comes back to a

[00:56:00.559] thing we come to all the time, which is

[00:56:02.240] like make it work. I mean in design and

[00:56:04.559] like product engineer we call it like

[00:56:05.839] make it run, make it right, make it fast

[00:56:08.240] and like in LM world it's like fast and

[00:56:10.400] cheap I guess. Um, but it's it's like,

[00:56:14.720] yeah, get the thing working and then if

[00:56:16.720] you have a good eval set, you can say,

[00:56:18.240] "Cool, we're going to try to rebuild

[00:56:19.520] this pipeline with 40 mini and just make

[00:56:21.280] the prompt really good instead of using

[00:56:23.240] 03." And you'll know exactly how much

[00:56:26.400] better 03 was than 40 mini. And you'll

[00:56:28.880] know exactly how you're doing at

[00:56:30.400] changing your prompts to make, you know,

[00:56:32.839] 040 mini almost as good as

[00:56:35.640] 03. Why is this failing? Well, we'll

[00:56:38.240] find out. I forgot to run dash s. Let me

[00:56:40.640] run that again.

[00:56:43.119] Also, I think you're having like async

[00:56:45.040] io thing. I don't know. Let's see. Uh,

[00:56:48.240] I'm not I'm not running async. I

[00:56:50.000] probably should. Okay. Uh, and I'm

[00:56:52.480] running. So, the first thing I'm doing,

[00:56:53.920] I'm really just going to run this

[00:56:55.280] because I just wrote some test cases.

[00:56:56.799] I'm going to go run it. Test index zero,

[00:56:58.319] test index one, and then it's going to,

[00:57:00.960] and you can actually see what it did.

[00:57:02.400] pulled out the lesson plan

[00:57:05.520] and then it's going to take the lesson

[00:57:06.720] plan and pull this out and said pacing

[00:57:08.000] was medium biases physical activity like

[00:57:10.160] hopscotch might be challenging. That's

[00:57:11.520] true. Like maybe physical activities are

[00:57:13.040] actually bad. Group dance activities

[00:57:14.480] might and then competition is bad. Um

[00:57:18.960] and then now there's another one that

[00:57:20.240] says a pizza uh pizza activity. And what

[00:57:23.359] does this do? And this failed because I

[00:57:25.359] forgot to make a

[00:57:26.520] directory. Uh new folder evals.

[00:57:31.319] Okay. And then what I'll do is

[00:57:43.470] date

[00:57:43.480] equals. And you can see what the most

[00:57:45.599] annoying part about this is, which is

[00:57:46.880] why I wanted to show the cleaner code,

[00:57:48.160] but that's

[00:57:49.160] okay. Um, there we go. Okay, that looks

[00:57:52.240] pretty good.

[00:57:55.119] Well, no. Just like what I mean is like

[00:57:56.880] you can see how there's so much work

[00:57:58.400] that I have to do just to get the data

[00:58:00.000] out of the system. Like when I'm

[00:58:02.160] building an LM pipeline, this is

[00:58:03.520] actually one of the most annoying parts.

[00:58:05.280] So like what what I'm really excited

[00:58:07.119] about is being able to run BML CLI tests

[00:58:09.200] and automatically be able to have the

[00:58:10.480] diffing and everything done for you

[00:58:11.680] automatically and just have JSON stuff

[00:58:13.119] save. Oh, like is it going to dump out

[00:58:15.200] all the input output pairs to like some

[00:58:17.200] temporary storage space or something?

[00:58:19.280] Yeah, exactly. like BAML CLI test and

[00:58:21.839] like be able to even even better just do

[00:58:23.680] something like this

[00:58:25.240] D-pro dash like compare equals prod till

[00:58:31.119] the two and you can just get the last

[00:58:32.559] two entries in prod and compare against

[00:58:34.319] them. Oh, sick. That's like the git

[00:58:36.880] syntax or whatever. Yeah, just use

[00:58:39.040] syntax to kind of invent that for us.

[00:58:40.880] Um, and I have to make a new directory.

[00:58:48.789] Just my two cents. I use BL CLI test a

[00:58:48.799] lot and it's really really good. Gives

[00:58:50.559] me feedback very rapidly, but then you

[00:58:52.559] can't do the diff right now. So I end up

[00:58:54.480] writing manual Python code to do the

[00:58:55.839] diffs. Yep. That's kind of why. And you

[00:58:57.920] can kind of see what I'm doing with the

[00:58:59.119] diff here. Uh and really what I do with

[00:59:01.680] the diff is once I have this generated,

[00:59:03.440] this will generate in a couple

[00:59:05.240] seconds. Um and it'll write everything

[00:59:09.720] down. Um and the other benefit once you

[00:59:12.559] do that is you can get caching and

[00:59:13.920] everything for free. So you can like

[00:59:15.040] modify your eval prompt without having

[00:59:16.720] to modify this prompt. Uh which is kind

[00:59:18.880] of nice. But like we can just see what's

[00:59:20.799] happening and like this looks pretty

[00:59:21.920] good. So now what I would

[00:59:24.119] do is now this is good and this actually

[00:59:27.359] failed. That's fine. I don't really care

[00:59:28.799] because I saved all the data. Um and now

[00:59:31.520] what I would do

[00:59:34.520] is for every run I just build a UI that

[00:59:37.760] actually does this for me. So let me

[00:59:38.880] make an MPM folder.

[00:59:51.589] tsj cdts. If we have time, I have a I

[00:59:51.599] have a funky example cooking over here

[00:59:53.440] as well that we can look at. Okay, but

[00:59:56.319] this is structurally super super

[00:59:57.920] interesting and helpful. Wait, why did

[00:59:59.680] this Oh, I'm dumb. This is another thing

[01:00:02.400] that happens when you do

[01:00:04.839] this. Um, you realize that you save data

[01:00:07.680] into the wrong folder. I need one date

[01:00:10.240] folder for my entire run, not multiple.

[01:00:17.069] Oh yeah, you got to make it one

[01:00:17.079] time. Okay.

[01:00:20.240] Okay, cool. And this is what I end up

[01:00:23.280] doing now. So I'll show you guys my

[01:00:24.880] exact

[01:00:25.640] workflow. I go here. I say I will

[01:00:31.160] run some tests each time. Um and all my

[01:00:38.400] tests will be in that folder

[01:00:43.640] structure for each

[01:00:49.950] run.

[01:00:49.960] Run_ate

[01:00:51.799] slash at

[01:00:54.440] data test

[01:01:02.230] idx.json. Oh I hate this. Stop.

[01:01:02.240] Stop.

[01:01:03.559] Okay. Sorry, maybe I'll cut that

[01:01:06.319] out. Um, and then and then you want to

[01:01:08.880] actually paste in the data format,

[01:01:10.400] right? Here's an example of actually

[01:01:16.079] what I really like to do more than that

[01:01:18.079] is actually

[01:01:20.480] um what I'll often do and this this I

[01:01:22.799] find works even better. Yeah. Um of the

[01:01:28.119] type I'm saving in the JSON. Look, it

[01:01:32.720] wouldn't be an episode of AI that works

[01:01:34.640] if I Bob didn't sneak in a uh BAML is

[01:01:37.520] more token efficient than JSON quip. I

[01:01:40.960] haven't said that yet.

[01:01:43.040] You implied it.

[01:01:46.480] Well, I guess this is putting in the

[01:01:47.680] types rather than the data themselves,

[01:01:49.040] which is probably much more interesting

[01:01:50.960] for building UIs. Exactly. Exactly.

[01:01:53.839] Because like that the model, if I give

[01:01:55.680] it this shape, it won't actually know.

[01:01:57.359] But if I give it lesson plan

[01:02:00.040] string and then what's the next one

[01:02:07.270] evaluation and the thing is like I just

[01:02:07.280] paste the stuff in there and it kind of

[01:02:08.480] just it'll figure something out. It

[01:02:09.839] doesn't really matter. Is lesson plan a

[01:02:11.200] string? I thought it was the Yes, the

[01:02:13.760] lesson plan type. This is why it's great

[01:02:15.680] to have someone else there. Um I want to

[01:02:18.400] render a

[01:02:19.880] diff of Oh shoot. I forgot to say one

[01:02:24.559] more thing. Dang it.

[01:02:27.359] I want to and while this runs I'll rerun

[01:02:29.359] this. I want to render a diff

[01:02:31.400] of diff evaluations per topic

[01:02:35.839] over

[01:02:37.079] multiple multiple runs to

[01:02:41.240] show the diff between lesson plans.

[01:02:47.599] then

[01:02:48.520] also show the

[01:02:51.880] um plans

[01:02:54.559] um and their

[01:02:57.640] evaluations. Cool. I'll let this run.

[01:03:00.640] While I do this, I'm going to fix my my

[01:03:02.319] my sin that I wrote over here, which is

[01:03:04.240] I forgot to dump out the topic.

[01:03:07.520] And this is what I mean by it's very

[01:03:09.280] easy when you go write these systems

[01:03:11.319] out to actually like accidentally do

[01:03:14.240] something that you didn't mean to and

[01:03:15.680] like just forget to go do something. And

[01:03:17.039] like imagine you spent

[01:03:18.599] like two $5,000 running this and you

[01:03:21.359] just forgot to record the topic. You're

[01:03:22.960] basically doomed. You just have there

[01:03:25.520] there's no shortcut. And this is why I

[01:03:27.839] this is so hard to do because it's not

[01:03:30.559] like even me going into this. I know I

[01:03:32.960] need to save the topic and I forgot

[01:03:34.400] until the very end.

[01:03:36.640] So like

[01:03:38.680] uh where did it

[01:03:41.000] go?

[01:03:43.079] Yes. I will run this

[01:03:45.880] again. Um and now it'll go do something

[01:03:48.480] for me and it'll probably be somewhat

[01:03:49.839] reasonable

[01:03:51.520] um when it does this. And now the good

[01:03:53.599] part by the way is like if you want you

[01:03:54.720] can just code gen these types in

[01:03:56.000] TypeScript pretty easily for BAML 2. So

[01:03:57.760] let's just go do that. Why not? Um I

[01:04:01.280] will do that as soon as it's done.

[01:04:08.750] Uh, nice. Now we have this.

[01:04:08.760] Okay. Um, and then this will go do some

[01:04:12.319] stuff for me. The problem is you end up

[01:04:13.839] waiting. But this is way better than

[01:04:15.280] trying to figure out some other system

[01:04:16.880] that isn't going to be perfect. Uh,

[01:04:18.880] because I can get this to be very

[01:04:20.319] correct. Can use eval history to

[01:04:22.240] backfill topic? You can, but then you're

[01:04:24.160] basically just data cleaning and data

[01:04:25.440] cleaning sucks. It's honestly just

[01:04:26.720] faster to rerun it.

[01:04:29.920] But now you can actually see what it

[01:04:31.119] did. It's kind of cool. It actually

[01:04:32.240] built the system out for me. lets me

[01:04:33.760] compare and just lets me pull that out.

[01:04:36.720] Um, and it'll actually show me the diff.

[01:04:38.400] And you can see how fast I did

[01:04:40.920] this, right? It's not that hard as at

[01:04:44.400] all. Um, I just use cursor. It doesn't

[01:04:46.319] really matter. The reason I use v0ero is

[01:04:48.079] because I don't have to spin up a whole

[01:04:49.200] node project. Then I can just see if

[01:04:50.480] it's if it's actually what I want up

[01:04:52.160] front. And once it is, then I then I

[01:04:54.160] download it. Then I move over onto

[01:04:56.440] cursor. Um, if that makes sense,

[01:04:59.440] pashant.

[01:05:04.309] So, but like you can see how fast this

[01:05:04.319] is. It's like great. And I can actually

[01:05:06.079] see the difference. It's like cool. And

[01:05:07.680] it's actually showing me what I

[01:05:09.720] have. And like now I have an email

[01:05:12.000] suite. This is sick. And I'm like, "Oh,

[01:05:14.079] now give me a clickth through button up

[01:05:15.359] here." So I can just click and just

[01:05:16.480] compare, compare, compare, and I'm done.

[01:05:18.160] And then also load this from disk. And

[01:05:20.720] now I built an eval system in under five

[01:05:22.720] minutes. I can iterate on my lesson plan

[01:05:24.240] really, really

[01:05:25.799] fast. This is how I think people should

[01:05:28.240] build

[01:05:29.000] eval. And if you're not doing this,

[01:05:32.559] you're hurting yourself and your company

[01:05:34.640] and your likelihood of success of

[01:05:36.720] building a successful pipeline. So like

[01:05:39.119] the whole goal is go from like

[01:05:42.559] So yeah, I would say like let's like can

[01:05:44.799] we put together a checklist in like the

[01:05:47.280] read me here or something of just like

[01:05:49.280] what's the steps, what should I do first

[01:05:51.440] and like what are the what what are all

[01:05:53.359] my boxes to check to know that I'm kind

[01:05:55.119] of like on the right path to make this

[01:05:56.960] happen. Yeah, that's a great that's a

[01:05:58.799] great thing. So I think step number one

[01:06:00.480] that everyone should be doing vibe

[01:06:02.440] evals. That's it. Just vi. What does

[01:06:04.880] that what So what does that mean to you?

[01:06:07.760] To me what that means is you're going in

[01:06:10.480] the playground and just hitting play

[01:06:12.000] constantly and you're actually looking

[01:06:13.520] at the data. That's part one. Okay. Step

[01:06:18.240] number two. As soon as you've got your

[01:06:20.319] five eval down like that means you're

[01:06:22.240] actually reading your prompt, you're

[01:06:23.680] writing test cases and you're actually

[01:06:25.039] hitting play. And just care think about

[01:06:27.200] what test cases actually make sense. And

[01:06:28.880] even the act of thinking about test

[01:06:31.480] cases is going to help you be better at

[01:06:34.480] your system because you're going to

[01:06:35.520] think about where people can fail. I

[01:06:36.960] remember when the minute I started

[01:06:38.559] talking about eval people like oh uh

[01:06:41.119] there I forgot the messages on here but

[01:06:42.960] in the thread people were directly

[01:06:44.640] saying that there's so many different

[01:06:46.880] ways to measure the lesson plan and

[01:06:48.319] they're like you could think about a few

[01:06:50.000] I forgot the I I don't section people

[01:06:52.160] instantly had ways to judge the plan. do

[01:06:55.200] that for your own prompts. Like just

[01:06:57.839] write a few.

[01:07:00.440] Two, capture the intermediate steps of

[01:07:03.200] your entire pipeline and try and eval

[01:07:06.319] the steps that are most easy to eval.

[01:07:10.000] Don't try and pipeline. Yeah, this comes

[01:07:12.799] back to like the the testing pyramid,

[01:07:14.880] right? Of like you should have small

[01:07:17.039] super granular tests and then you should

[01:07:19.280] also have uh what is it? Testing pyramid

[01:07:26.910] Oh

[01:07:26.920] man, for formal term terminology for

[01:07:30.400] all. Exactly. Yeah. Exactly. Exactly.

[01:07:32.319] This is the thing of like you should

[01:07:33.520] have little incremental tests at the

[01:07:35.359] smallest possible granularity because

[01:07:37.680] these are faster, they're more isolated

[01:07:39.599] and you can iterate quicker and then you

[01:07:41.760] should have end to end I mean in in the

[01:07:43.520] AI case it's not UI tests, it's like end

[01:07:45.839] to end full pipeline tests. Yeah. Um but

[01:07:48.799] this idea like a lot of your tests

[01:07:50.480] should be these smaller more granular

[01:07:52.160] units. Yeah. Because if you know that

[01:07:54.160] the intent capturing is correct, we can

[01:07:56.559] worry about the next steps, not the

[01:07:57.920] first steps. Um, if you know your

[01:08:00.400] messages have the right tone because you

[01:08:02.480] look at them and you vibe eval them, you

[01:08:04.480] can worry about the intent analysis

[01:08:05.839] being correct. Exactly. Engineering is

[01:08:08.319] engineering. Um, there's no shortcut

[01:08:10.400] here. So that's those are like two big

[01:08:12.799] ones. Things that I recommend focusing

[01:08:14.799] energy on as a team is I always

[01:08:16.880] recommend people build structured

[01:08:18.319] outputs uh whenever possible and like

[01:08:20.319] break your problems down. Like Daxter

[01:08:22.080] says this all the time and is one of

[01:08:23.120] those things like think of all LM things

[01:08:25.120] as tools or really just classes that

[01:08:27.120] you're

[01:08:27.960] returning like once you're able to do

[01:08:30.480] that it becomes really really easy to

[01:08:32.480] write evals for certain parts of your

[01:08:34.920] pipeline. Um and then really it's more

[01:08:38.719] about don't use numbers for confidence

[01:08:40.799] scores. Uh and the reason you don't use

[01:08:42.640] numbers because like when I got an

[01:08:44.480] English paper I remember this all the

[01:08:46.239] time. I don't understand why I got a 92

[01:08:48.799] instead of a 97 half the time. It felt

[01:08:51.279] like discretion. Well, okay, that's I

[01:08:54.000] realize this was the uh Are we bragging

[01:08:56.239] about our English paper scores now? Let

[01:08:58.400] me be more honest. An 82 instead of a

[01:09:01.799] 97. Um, listen, you don't have to lie.

[01:09:04.400] We love you for who you are. Um, yes.

[01:09:06.640] Uh, that's right. But in reality, I

[01:09:08.560] never understood what those numbers

[01:09:10.080] meant because they felt very

[01:09:12.199] arbitrary. And most people when they

[01:09:14.560] give a numerical system don't have a

[01:09:16.400] system. They have like a completely

[01:09:17.839] arbitrary system. So it's like you

[01:09:19.279] notice that when I actually wrote the

[01:09:20.400] eval system when I was writing it is I

[01:09:22.319] just asked it and like the model came up

[01:09:24.799] with a good idea for what an eval system

[01:09:26.640] is for that but categorical

[01:09:29.480] categorical systems are generally way

[01:09:32.239] better than numerical systems because no

[01:09:34.640] one knows the difference between score

[01:09:35.759] seven and eight. So don't don't put a

[01:09:38.560] category in there that has no meaning.

[01:09:40.719] This is do you put like emu enums in

[01:09:42.880] that as well of like outputting like a

[01:09:45.279] string that represents like a category?

[01:09:47.920] Yeah. when you had like slow versus

[01:09:51.199] medium versus fast, right? Exactly.

[01:09:54.600] Exactly. And like Jonathan said it

[01:09:56.640] right. It's like it's same with stars on

[01:09:58.159] Yelp. Like I don't go to a restaurant

[01:09:59.280] that has less than 4.8 because that

[01:10:00.719] means they suck. Uh like if they don't

[01:10:03.120] have a 4.8, they're just really bad. Um

[01:10:06.640] and it's more about thinking about

[01:10:08.239] categories better. And you can add

[01:10:10.000] descriptions to categories to say

[01:10:11.600] exactly what they mean and just break

[01:10:13.600] your problem down to a classification

[01:10:15.480] problem. you on the probe on the probe

[01:10:18.640] question real quick that just came up. I

[01:10:20.480] I think the idea here would be like in

[01:10:22.480] your we'll share this in the whiteboard,

[01:10:24.560] but basically like you have your full

[01:10:26.320] pipeline where you pull out an intent

[01:10:28.560] and then you list the products for that

[01:10:30.000] intent and then you build your answer

[01:10:31.679] and you return the answer and you also

[01:10:33.679] return things about the intermediate

[01:10:35.360] step so that in your test you get the

[01:10:37.920] output and the probe. And we're actually

[01:10:39.440] not going to make assertions about the

[01:10:40.880] answer because it's like a chatbot

[01:10:42.480] generated big string. Maybe you can. But

[01:10:44.960] the idea is like let's make assertions

[01:10:47.040] about so that when this test fails for

[01:10:49.760] some reason, maybe we are also

[01:10:50.960] evaluating the answer. We immediately

[01:10:53.199] have assertions about each intermediate

[01:10:55.920] step as well that we can see like oh the

[01:10:57.520] intent was wrong and so everything was

[01:10:59.600] screwed up. And the alternative here is

[01:11:02.800] this concept is I think the concept that

[01:11:04.719] people are most familiar with that looks

[01:11:06.159] like this is mocking.

[01:11:09.679] So instead of uh instead of actually

[01:11:12.239] doing it's like you could technically

[01:11:13.679] mock what get in intense does and then

[01:11:16.880] you kind of have um you can kind of eval

[01:11:20.000] just the next part of your system if

[01:11:21.600] that makes sense, right? You test your

[01:11:23.520] get intense function and then you can

[01:11:25.199] mock it in your pipeline and you say hey

[01:11:27.040] as long as we get the intents right and

[01:11:28.400] we get the products right then the we

[01:11:31.600] are just now testing the final chat

[01:11:33.679] output. So that's an alternative to

[01:11:35.840] probes right? Can you they're kind of

[01:11:38.080] similar. Can you go back to your system

[01:11:40.320] the diagram that you had really fast

[01:11:41.760] just to articulate this better? So like

[01:11:44.239] here you can imagine that I wrote it. So

[01:11:46.000] probes are one way to do it. It's the

[01:11:47.280] easiest way for most people to do it for

[01:11:49.199] people that are more uh that are more

[01:11:51.199] comfortable with mocking. What I would

[01:11:52.400] recommend is in and in chatbot you could

[01:11:55.520] just mock the get products function and

[01:11:58.000] the chat response function to return a

[01:11:59.760] fixed thing. Well, you don't have to

[01:12:01.440] pass it in. You can just use a mocking

[01:12:02.800] library. Sure. And then you can just

[01:12:04.960] mock what get products and chat response

[01:12:06.800] does like like yeah there's exactly you

[01:12:10.800] get the point. And now what you can say

[01:12:12.159] is now you can basically assert what

[01:12:14.320] intent should be in your mocked

[01:12:17.400] functions. So there's multiple ways to

[01:12:19.760] go write this code out. Yeah.

[01:12:26.430] Exactly.

[01:12:26.440] Exactly. Oh, I can't believe you

[01:12:28.239] actually know this off top of your head.

[01:12:29.440] This is why you're a much better

[01:12:30.480] engineer than me. I don't know about

[01:12:33.199] that. Um I do not know this stuff. I

[01:12:36.000] just uh Yeah. So, and then you can

[01:12:38.640] Exactly. And so then you don't really

[01:12:41.120] care about this probe stuff anymore and

[01:12:43.440] you're just going to like break down the

[01:12:45.280] problem and solve it at each level of

[01:12:46.960] the pyramid basically. Exactly. So now

[01:12:49.600] if you have ever seen this talk, we'll

[01:12:51.840] put in the show notes. Uh I think it's

[01:12:53.920] JD

[01:13:01.110] Reignsburgger degraded test scam. Uh,

[01:13:01.120] this is an incredible talk. Um, yeah,

[01:13:03.679] integrated tests are a scam. It's an

[01:13:06.560] hour and five minutes on why only

[01:13:08.640] testing things end to end is going to

[01:13:10.800] destroy your team and your product and

[01:13:12.960] your company and the value of like

[01:13:15.199] following this pyramid and focusing on

[01:13:17.120] small pieces and the contracts between

[01:13:19.199] parts of the system. Yeah. And then can

[01:13:21.760] you go back and then uh Yeah. Yeah.

[01:13:24.000] Yeah. Sorry, not to here to the

[01:13:25.880] dashboard uh to the notes that you're

[01:13:28.080] writing. Yep.

[01:13:30.400] Um and really this is a checklist and

[01:13:32.640] and I think the most important part is

[01:13:34.560] uh yeah what else is missing from this?

[01:13:35.920] Oh sorry one last thing use prod data to

[01:13:38.320] build up your build up your golden data

[01:13:40.480] set continuously over time do not stop

[01:13:44.239] uh specifically you should write only

[01:13:45.600] integration only using integration tests

[01:13:47.920] is a scam.

[01:13:49.920] Sorry. Yeah integration tests are

[01:13:51.920] fantastic and you should have

[01:13:52.880] integration tests but if you only have

[01:13:54.880] integration tests you are being scammed.

[01:13:57.360] Yeah. Well, it's like if you're if

[01:13:58.640] you're using an integration test to

[01:14:00.880] catch a thing that broke between these

[01:14:02.640] two small components of the system, it's

[01:14:05.040] quickly going to explode into 700

[01:14:08.320] integration tests that are very slow to

[01:14:10.440] run and very slow to run one of them,

[01:14:13.520] let alone run all of them. And when one

[01:14:15.520] of them breaks, it's going to be very

[01:14:17.840] unclear which part of the pipeline

[01:14:19.520] broke. Exactly. Um, and I and I'm going

[01:14:23.040] to pause here because I think uh

[01:14:24.960] hopefully what I can do is I can send

[01:14:26.640] over like some actual like tooling

[01:14:28.159] scripts that we have that have been

[01:14:29.760] useful, but we'll share some of them

[01:14:32.000] pretty soon. But really, you want things

[01:14:33.440] that can

[01:14:34.360] pull pull d. What you really need is you

[01:14:36.880] need something that can pull data from

[01:14:38.000] prod. You need to build tooling to

[01:14:39.760] visualize the differences between

[01:14:41.199] different

[01:14:42.360] outputs. And you just need to make that

[01:14:44.480] really easy so that every engineer wants

[01:14:46.480] to go do that all the time. And I think

[01:14:48.480] the best analogy I have at this is like

[01:14:50.080] back at the hedge fund that I was

[01:14:51.360] working at, they have they had like

[01:14:54.000] around I think um their unit test used

[01:14:57.120] to take like 30 something hours to go

[01:14:58.640] run. So obviously none of the engineers

[01:15:01.040] ever ran the unit test or they'd run

[01:15:02.560] like the one file that they know. But we

[01:15:04.719] all know that changing one um one file

[01:15:09.600] running one file unit test is often not

[01:15:11.360] good enough.

[01:15:13.520] So like what we found was we built a

[01:15:16.320] system that could say given a git diff

[01:15:18.239] we wanted to predict exactly all the

[01:15:20.080] unit tests that would need to be run and

[01:15:22.800] we actually built that system and we

[01:15:25.040] found that on average for 90% of commits

[01:15:27.199] people had about five minutes of test to

[01:15:28.920] run and that changed how people ran

[01:15:31.280] worked because they always ran all the

[01:15:32.920] tests like because they just and what we

[01:15:35.120] did was we made a single command. It was

[01:15:36.719] called delta test. you would just run

[01:15:38.480] delta test and look at your diff and be

[01:15:40.800] like, "Ah, this is what you need to

[01:15:41.920] run." It would just run it for you. And

[01:15:43.679] that was actually even easier for people

[01:15:45.360] to run than actually determining

[01:15:49.840] um than actually like even thinking

[01:15:51.199] about the file that they're run because

[01:15:52.560] even one less work work

[01:15:55.159] item. And I think people need something

[01:15:57.920] like that for AI systems. Like if

[01:15:59.600] someone is working on a prompt, they

[01:16:01.120] don't have to think about running a unit

[01:16:02.159] test for that prompt. They want to run

[01:16:03.360] something like delta test and basically

[01:16:06.000] say run the entire pipeline that depends

[01:16:08.320] on that test and never think about it

[01:16:10.600] again. And I think that is going to be

[01:16:12.800] the answer. Steve, you had a question.

[01:16:16.000] So now that you've teased everyone with

[01:16:18.400] this magic system, how was that? How

[01:16:21.679] were the what training was used to then

[01:16:24.760] predict you know what tests to run? Like

[01:16:27.360] what did that look like at a high level?

[01:16:28.960] I wrote an

[01:16:31.000] algorithm. There was really an algorithm

[01:16:32.960] that I wrote. So were you like parsing

[01:16:34.320] the parsing the a of the entire codebase

[01:16:37.040] and then doing a like analyzing the

[01:16:39.360] graph basically? Yes. But the only

[01:16:42.080] problem is in Python you can modify

[01:16:43.679] global variables and changes the a quite

[01:16:46.080] in nasty ways and then you have C Python

[01:16:48.159] code that you have to deal with and then

[01:16:49.679] network dependencies and data

[01:16:50.880] dependencies. So I wrote an algorithm to

[01:16:52.239] deal with that. Um it was fun. It was

[01:16:55.440] very fun. um a lot of state um testing.

[01:17:01.120] So I think we'll probably end up

[01:17:02.880] building something like that for um LMS

[01:17:05.520] because I think people want something

[01:17:06.480] like that as well. We got a good

[01:17:08.400] question from Adisha here. Um struggling

[01:17:11.760] a bit to understand the value of the

[01:17:13.120] different UI. Okay, let me let me tell

[01:17:15.199] you why why you want the dipping UI. Can

[01:17:17.679] we like whiteboard out like the workflow

[01:17:19.440] steps or something like that? Yeah. What

[01:17:21.360] screen am I sharing? This is

[01:17:24.040] cursor.

[01:17:25.640] Cursor. Do you see cursor? What do you

[01:17:28.480] see now?

[01:17:30.480] Uh I saw trees for a sec and now I see

[01:17:32.560] cursor. Oh yeah, now I see it. Okay. Why

[01:17:35.040] is this better? Well, Adisha, the most

[01:17:37.199] important part here that you have to uh

[01:17:39.280] kind of uh get around is that when you

[01:17:41.600] go do

[01:17:42.760] this, this is just easier to go read

[01:17:45.360] than looking at JSON dumps. And when

[01:17:47.679] you're looking at hundreds of them, you

[01:17:49.280] need to go do this. And it's not

[01:17:50.719] actually it's not embarrassing at all.

[01:17:52.480] It's actually it's really really

[01:17:53.840] intuitive. It's it makes sense like hey

[01:17:55.600] we're programmers we're engineers we run

[01:17:57.120] all this stuff programmatically why are

[01:17:59.120] we suddenly building UIs for this and I

[01:18:01.360] think the best analogy is data science

[01:18:03.920] we all have recognized Jupyter notebook

[01:18:05.679] is incredibly powerful for data

[01:18:07.360] scientists and for machine learning

[01:18:08.880] people and the reason Jupyter notebook

[01:18:10.560] is really powerful because it combines

[01:18:12.320] visuals with

[01:18:14.120] code and that's what you need to do when

[01:18:16.560] you're in this world you need to look at

[01:18:18.320] visuals plus code to get really fast

[01:18:20.239] feedback and really this isn't even good

[01:18:22.320] enough it's like I want to I want an

[01:18:24.719] arrow I can click to

[01:18:28.440] quickly skim test uh

[01:18:33.480] indexes. Like I really want an arrow

[01:18:35.760] that I can click that'll just like do it

[01:18:37.040] for me so I can just like make it really

[01:18:38.560] really

[01:18:39.480] fast. Um and I think once you get in the

[01:18:42.640] habit of thinking of it this way, like I

[01:18:44.880] used to get so annoyed every time I had

[01:18:46.400] to spin up a Jupyter notebook because I

[01:18:47.520] was like I have to install IPI kernel

[01:18:49.199] and I have to like remember what it is.

[01:18:51.120] But once you get in the habit of it,

[01:18:52.320] it's like there's no better way to build

[01:18:53.600] plots and analyze data because I'm

[01:18:56.000] manipulating things all the time. Um,

[01:18:58.960] and I think normally I would say stick

[01:19:01.679] to Python if that's what you're most

[01:19:03.199] comfortable in. But the problem is you

[01:19:07.520] we're no longer looking at graphs and

[01:19:09.199] analytics. We're looking at things that

[01:19:11.120] are a lot less graphical.

[01:19:14.000] No, they don't just like plug into

[01:19:15.440] standard components like an XYaxis or a

[01:19:18.239] pandas table. Exactly. And that's not

[01:19:20.320] what we're doing. So it's like, okay,

[01:19:21.360] now I have to just like and now I just

[01:19:22.719] want to like rotate here and just like

[01:19:24.000] go do this. And it's like I don't know

[01:19:24.960] why it's taking forever to load. It's so

[01:19:27.040] slow. I'm like, okay. And I'm I'm

[01:19:29.280] literally just going to tell like

[01:19:30.320] instead of

[01:19:32.760] loading load everything at once, then

[01:19:37.040] show it so it doesn't

[01:19:41.400] lag when I uh press

[01:19:46.679] next. And like it'll it'll just figure

[01:19:49.040] things out. And I don't actually spend a

[01:19:50.400] lot of time while I'm doing this because

[01:19:51.440] what I often do is like I'm iterating on

[01:19:53.120] this thing while it's running and then

[01:19:54.320] while I'm on there I'm actually like

[01:19:55.520] just running stuff in the playground

[01:19:57.040] looking at things manually to build a

[01:19:58.960] better you're changing your prompt and

[01:20:00.560] then you're looking at how the diff

[01:20:01.840] change and then you're changing your

[01:20:02.880] prompt you're changing the order of

[01:20:04.320] functions. I mean, this is all about

[01:20:05.840] again that quick like iteration loop at

[01:20:09.280] the end of the day. Like, yes, this is

[01:20:10.800] useful as an artifact to like before PR

[01:20:13.360] goes in like eyeball and make sure it's

[01:20:15.120] not going to break anything too

[01:20:16.159] impactful. But it's also it's like cool,

[01:20:18.480] I'm trying to make this thing more

[01:20:19.600] accurate or I'm going to try to like I'm

[01:20:21.360] trying I'm trying to get it. It's 99%

[01:20:23.199] but it always up this weird edge

[01:20:24.719] case. Can I change the prompt or change

[01:20:26.239] the pipeline or change the format to get

[01:20:28.320] this weird edge case? And this becomes

[01:20:30.239] the thing that you can do to be like,

[01:20:31.920] cool, I solved my problem. Oh, but I

[01:20:33.920] broke seven other things. And it's very

[01:20:35.760] visually like I clicked three times and

[01:20:37.280] I can see that it's broken. So, we have

[01:20:38.800] to go back to the drawing board.

[01:20:40.000] Exactly. And it's just going to be

[01:20:41.120] faster to iterate. It's it's it's really

[01:20:43.520] annoying. I know for a lot of people

[01:20:44.960] this feels annoying, but um like I

[01:20:48.960] honestly I have nothing to say. And

[01:20:50.960] you're going to see how like nice this

[01:20:52.000] is. I can just like look at this like

[01:20:53.280] cool and I can just like manually see

[01:20:55.679] like what's happening between the two

[01:20:56.960] and I can be like cool this is the

[01:20:58.320] difference.

[01:21:00.719] Yeah. And you can show this to a

[01:21:02.239] non-technical person and you can say

[01:21:03.760] like, "Hey, here's how we're improving

[01:21:05.280] this week versus last week." Exactly.

[01:21:08.880] Um, and this is really it just makes

[01:21:10.960] life way

[01:21:17.030] faster. And and by the way, don't do

[01:21:17.040] this the minute you start writing your

[01:21:18.400] prompts. Do not do this. The answer

[01:21:21.800] is look at it 5 valid. Honestly, I ship

[01:21:25.280] things with five evals and that's okay.

[01:21:26.960] I've seen many people do that because

[01:21:28.640] what we want to do is 5 eval. that's

[01:21:30.640] good enough. Ship it to prod, collect

[01:21:32.719] prod data, use prod data to build golden

[01:21:35.760] data sets, and then build diffing and

[01:21:37.440] all this other tooling. After that, we

[01:21:40.159] had a we had a really mediocre prompt

[01:21:43.280] live in our production systems for about

[01:21:45.679] 12 weeks. And then one day, a customer

[01:21:48.080] wrote in was like, "Hey, it did this one

[01:21:49.360] thing weird." And we went and we found

[01:21:51.360] the exact data from the weird thing it

[01:21:53.040] did. We added that to our test case

[01:21:54.560] suite and said, "We need to handle this

[01:21:55.840] as well." And we grabbed a couple other

[01:21:57.520] weird test cases while we were in there.

[01:21:58.880] like some of this stuff doesn't look

[01:22:00.000] right. And the issue was we had this

[01:22:01.760] thing where like a smaller model like a

[01:22:03.280] 40 mini was kind of just like

[01:22:04.880] regurgitating data from its training

[01:22:06.800] set. I don't know if you all have ever

[01:22:07.920] seen that thing. It was like okay cool

[01:22:10.000] like let's add a couple tests for these

[01:22:12.080] weird things and let's change the

[01:22:13.280] prompt. And we actually ended up

[01:22:14.320] changing the model which broke a bunch

[01:22:16.320] of our existing tests. So we had to

[01:22:17.679] change the because 40 is a lot more it

[01:22:21.120] it's a lot smarter but it's also a lot

[01:22:23.280] smarter. And so some of the things that

[01:22:25.120] we were relying on GPT4 many to do

[01:22:27.360] cleanly because it's too dumb to

[01:22:28.880] actually think about the problem. We had

[01:22:31.040] to go like change the prompt to be like

[01:22:32.639] don't try to be smart about this. Don't

[01:22:34.159] try to answer the question. Just just

[01:22:35.760] pull the text

[01:22:37.080] out. Um but anyway that that's like a

[01:22:39.520] real workflow that we had in production

[01:22:40.719] where it's like we shipped a prompt that

[01:22:41.920] was like pretty good. I vibed it on a

[01:22:43.280] couple things and then I waited for it

[01:22:44.560] to break and then we iterated as we go.

[01:22:47.040] I mean, putting things that you know are

[01:22:48.719] going to break is bad, but also like

[01:22:50.159] spending six months on evals before you

[01:22:51.920] ship a product to somebody and like find

[01:22:53.760] out if they even want it is really

[01:22:55.600] dangerous. Yes, it's way worse. And

[01:22:58.719] think of it like that fake buy now

[01:23:00.400] button that we used to have on websites,

[01:23:02.000] but they literally just do that to see

[01:23:03.280] if you clicked on it and if you clicked

[01:23:04.239] on it, they'd be like, "Shit, we should

[01:23:05.280] sell that thing." And then they'd go

[01:23:06.960] sell it. Yeah. And now you're called it

[01:23:09.199] the fake door test. You'd be like, "If

[01:23:10.639] people try to open the door, then you

[01:23:11.760] know they want to go in there and then

[01:23:12.960] you go, you know, build out whatever's

[01:23:14.239] supposed to be behind it." Yeah. If

[01:23:15.760] people are complaining about your

[01:23:16.880] system, then you you have real data that

[01:23:18.800] you can work with to make it better. All

[01:23:21.040] right, let's do one or two more

[01:23:22.320] questions and then we should probably

[01:23:23.280] wrap up. Yes, we're 30 minute 25 minutes

[01:23:25.440] over. Two last questions and we will

[01:23:27.600] call it quits for today. Um, and if

[01:23:29.440] there no more questions, we can call it

[01:23:30.560] quits and go back to

[01:23:36.470] work. What's a good mental model to when

[01:23:36.480] to split a prompt into intermediate

[01:23:38.239] steps? Um, I don't think there's

[01:23:40.719] generally a great model because it

[01:23:42.400] really depends on the capacity of the

[01:23:43.760] model that you're using. If you're using

[01:23:44.960] an AB model, it's probably earlier

[01:23:46.400] rather than later. If you're using a if

[01:23:49.280] you're using a if you're using a

[01:23:50.480] stronger model, but your your steps are

[01:23:52.960] very very intertwined, it might be

[01:23:54.719] earlier rather than later because you

[01:23:56.320] might want have value in discreetly

[01:23:58.800] defining those steps. It's really about

[01:24:01.280] how well you can define the problem. And

[01:24:03.280] honestly, just like press play and keep

[01:24:04.960] on testing it until you get to a good

[01:24:06.480] point. Like you you have to build that

[01:24:08.800] intuition yourself based on your domain.

[01:24:11.719] Yep. All right. One more question. Would

[01:24:14.080] it make sense to self- introspect on

[01:24:15.600] outputs during runtime and correct them

[01:24:17.440] if the LMS take no time to output and

[01:24:19.520] eval?

[01:24:27.350] Yeah. Uh that's basically what we did

[01:24:27.360] the deterministic runtime evals that we

[01:24:29.360] did of adding stuff table-wise and

[01:24:31.040] row-wise. Does it make sense to also do

[01:24:33.520] kind of introspective LLM based evals at

[01:24:36.000] runtime if they're if they're fast?

[01:24:38.400] I mean I mean whether you're using an

[01:24:40.159] LLM or like math to do that calculation

[01:24:43.040] doesn't really matter. It's up to you

[01:24:44.159] and you can definitely definitely do

[01:24:45.440] that. And we have people the the

[01:24:48.000] financial thing I've shown is I've seen

[01:24:49.760] multiple people take variations of that

[01:24:51.360] approach to build like document uh

[01:24:53.120] validation for all sorts of things and

[01:24:56.239] like we have people running pipelines

[01:24:57.920] with 99% plus accuracy on like a 100page

[01:25:02.000] plus PDFs on data extraction. it works

[01:25:05.040] because what ends up happening is when

[01:25:06.560] things go wrong, they literally ask an

[01:25:08.080] LLM to go fix the thing that went wrong.

[01:25:10.320] And because of how LM's work, because

[01:25:12.400] they're now focusing on just one part of

[01:25:14.159] it, they're able to go get the right

[01:25:16.080] answer more often than not

[01:25:18.760] afterwards. So, if you get feedback from

[01:25:22.000] an LLM, like a really tiny one, maybe a

[01:25:23.840] 1D model or something that you're

[01:25:25.280] running on an edge device, you can use

[01:25:27.760] that to build corrective behavior as

[01:25:29.440] long as as long as the thing that you're

[01:25:30.960] measuring on is actually good. Um, and I

[01:25:33.600] was showing this for example, like right

[01:25:35.040] over here, like you can imagine for this

[01:25:37.120] visa form, I could build the same

[01:25:38.480] system. I'll find everyone that was

[01:25:40.800] flagged as first trip to Cambodia true

[01:25:43.520] in my data set, and if they're flagged

[01:25:45.760] as true, first trip to Cambodia, I'll

[01:25:47.679] make sure a human looks at it. If it's

[01:25:50.159] false, what I'll do is I'll literally

[01:25:51.920] look up their passport number or

[01:25:53.280] whatever I have in here, I'll look up

[01:25:55.199] their passport number in my database and

[01:25:57.760] see how much of the information

[01:25:59.520] validates. If everything matches and

[01:26:02.400] it's all the same, but the address is

[01:26:04.239] different, I'll kick it off to human and

[01:26:05.600] have them only compare the address and

[01:26:07.280] say like, is this the right is this a

[01:26:08.880] good up-to-date address? Should we

[01:26:10.080] update this? Or maybe even email the

[01:26:11.760] person be like, are you are you sure you

[01:26:13.520] want to validate your address at this at

[01:26:15.920] this way? And I've kind of built this

[01:26:17.520] automated system. That's an incredible

[01:26:21.199] note to close on. Um to summarize all of

[01:26:24.320] this is building evals is not that hard

[01:26:27.280] and it's not that much code. Um, I think

[01:26:30.480] there's a lot of like eval systems off

[01:26:32.400] the shelf that you can buy that force

[01:26:34.480] you into a very structured way of

[01:26:36.080] thinking about this problem, but at the

[01:26:38.000] end of the day, none of them will let

[01:26:39.440] you build the pipeline that Vivov just

[01:26:41.639] described. And as you scale, it might

[01:26:44.639] make sense to grab a solution off the

[01:26:46.480] shelf. But at the start, you should

[01:26:48.800] understand what you're testing, how

[01:26:50.800] you're testing it, and like keep the

[01:26:52.719] flexibility to build this however you

[01:26:54.400] want, so that you can have a really

[01:26:56.040] flexible pipeline architecture, and you

[01:26:58.639] can evolve your testing systems with it.

[01:27:02.080] Dexter nailed it. I I will add the

[01:27:04.239] links, the vzero, and we'll push the

[01:27:06.320] code up so you can just see what that

[01:27:07.520] ends up looking like as a whole. Real

[01:27:09.920] quick announcement, thank you, Andrew.

[01:27:11.360] Uh we are doing a workshop. If you're in

[01:27:13.040] San Francisco, um we'll post the link.

[01:27:15.360] Um but um we are going to do a all day

[01:27:18.080] workshop mini conference in SF. Um so if

[01:27:21.520] you're in town uh come hang out. It's

[01:27:23.760] going to be a good time. We just did it

[01:27:24.719] in New York last weekend. People loved

[01:27:26.000] it. So should be great. Um and then um

[01:27:29.040] we'll see you guys next week.

[01:27:31.360] All right, folks.

[01:27:33.280] Bye everyone. See you. Bye.
