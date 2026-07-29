# Agentic RAG + Context Engineering



Source: YouTube captions (automatic:en)



[00:00:04.150] All right. Hello, hello, hello.

[00:00:04.160] We're gonna go right into it today.

[00:00:06.400] We're going to go start talking about

[00:00:08.480] agentic rag and talk about if we can get

[00:00:11.599] to work, how you would might want to go

[00:00:13.280] do it, and exactly what we want to do.

[00:00:16.080] Before we get started,

[00:00:16.960] >> this is

[00:00:18.400] >> Go ahead, do the intro. You're doing the

[00:00:19.760] intro. Go for it.

[00:00:21.119] >> All right. This AI that works. Every

[00:00:22.640] week, Dexter and I get together and we

[00:00:24.560] talk about building real pipelines that

[00:00:26.160] actually work.

[00:00:28.080] If uh if you can think it, you can build

[00:00:30.800] it. That's the whole idea. And my name

[00:00:33.120] is Vivov. I work on BAML, which is a new

[00:00:35.760] programming language.

[00:00:36.559] >> I'm stacks. I work on uh lots of things,

[00:00:39.680] including code layer, which is a new ADE

[00:00:41.600] to get coding agents to solve hard

[00:00:43.760] problems and complex code bases.

[00:00:46.320] >> And I'm super excited to get into it.

[00:00:48.879] This is going to be I have a feeling we

[00:00:50.879] were thinking about this episode before

[00:00:52.320] we got on. And uh I have a feeling

[00:00:55.120] there's going to be some spicy takes and

[00:00:56.800] some back and forth. So my favorite

[00:00:58.480] episodes are when me and Vibv actually

[00:01:00.160] don't fully agree on stuff. So we might

[00:01:01.920] get a little bit of that today, but I'm

[00:01:03.039] going to let him get into the demo. Show

[00:01:04.080] them what we're building and uh looking

[00:01:06.080] forward to it.

[00:01:07.119] >> Okay. So as many of you probably know, a

[00:01:09.439] rag system is not an aentic system like

[00:01:12.400] cloud code or something is not something

[00:01:13.680] you can really build um in let's say

[00:01:16.000] like within 1 hour. So, I did something

[00:01:19.600] else, which is I built this thing um

[00:01:22.720] mostly uh last night just to show you

[00:01:25.439] what it could do. But I want to just

[00:01:27.360] start with the demo and show you exactly

[00:01:28.799] what it is and then based on what it

[00:01:30.640] works, we can then talk about how it

[00:01:32.720] works. So, I'll just make the terminal

[00:01:35.439] the whole thing. Uh can you see? All

[00:01:37.600] right, Dexter.

[00:01:38.799] >> Yeah, it looks good. That's a that's a

[00:01:40.159] good zoom.

[00:01:40.960] >> Okay, then I'll leave it at the zoom

[00:01:42.479] level. Um I'm just going to run this

[00:01:45.520] thing. Uh we're what this thing is I

[00:01:48.560] gave it a directory. I'm in the BAML

[00:01:50.000] directory right now and I'm just going

[00:01:50.960] to ask it what does the form fern folder

[00:01:52.799] do and you'll notice what this agent

[00:01:54.880] does. It actually has the ability to go

[00:01:56.880] ahead and set some stuff. So it's going

[00:01:58.159] to take the user query. I'm using GD5

[00:02:00.320] for now because I don't want to think

[00:02:01.840] about model stuff. So I just used the

[00:02:03.520] best model I could on the market.

[00:02:05.040] >> Did you just did you build a coding

[00:02:06.640] agent?

[00:02:07.759] >> Yeah, I built a coding.

[00:02:08.879] >> Is that what this is?

[00:02:09.840] >> From scratch. Um

[00:02:11.280] >> Okay.

[00:02:11.599] >> It took me a net of about 3 hours. So it

[00:02:13.760] actually went through it did a glob

[00:02:15.120] looked through the firm folder and I was

[00:02:16.239] like cool this worked.

[00:02:17.680] >> Um I'll ask it question using these

[00:02:20.319] docs.

[00:02:21.840] How does how do I use the Gemini models

[00:02:26.239] with BAML? Cool.

[00:02:27.760] >> It should in theory take this agent and

[00:02:30.640] there's my user query. It'll go ahead

[00:02:32.560] and probably glob some stuff. Um make

[00:02:35.440] some other GP. It has a GP tool that it

[00:02:37.360] looked into. It's going to go take the

[00:02:40.000] results. And I don't stream the thinking

[00:02:41.680] tokens yet. I haven't built full

[00:02:42.959] streaming into this yet. That'll

[00:02:45.599] probably take another two or three hours

[00:02:46.800] to get working. Uh file

[00:02:50.160] >> and then what will it do? Let's just

[00:02:51.840] keep seeing what it does.

[00:02:52.959] >> I got a question.

[00:02:54.000] >> Yes.

[00:02:55.040] >> Um where you're snipping that result at

[00:02:58.480] the end where it says 4,300 cars total.

[00:03:00.879] Is that also being snipped for the model

[00:03:02.720] or is that just being

[00:03:03.680] >> trimmed? The model sees the full 4,000

[00:03:05.840] characters.

[00:03:06.560] >> Okay.

[00:03:07.200] >> Um cool. It actually gave me an example

[00:03:08.800] of how to do this. Um, can you check

[00:03:11.760] against the Google Docs if Gemini 2.5

[00:03:14.560] Pro is the latest model or not? Or are

[00:03:16.239] there newer ones?

[00:03:18.159] >> Did you also give it web search?

[00:03:20.400] >> And while this thing runs, like I guess

[00:03:23.599] a really really important part to think

[00:03:25.440] about here is what exactly are we trying

[00:03:29.519] to do with agentic rag? I know there's

[00:03:31.840] quite a few people who probably have an

[00:03:33.599] idea of what agentic rag is. What is

[00:03:35.840] your definition of it, Dexter?

[00:03:38.239] Um, and I think it's probably worth

[00:03:39.680] zooming out a little bit now that we've

[00:03:41.040] kind of seen the demo. Um because I

[00:03:44.239] think for me agentic rag is basically um

[00:03:48.640] to be to be like counterposed with um

[00:03:52.799] traditional rag which is a little bit

[00:03:54.959] more actually aligned with what we might

[00:03:57.519] describe as context engineering which is

[00:03:59.840] you know uh some query comes in I do a

[00:04:03.519] bunch of deterministic code to fetch

[00:04:05.519] data related to that query whether it is

[00:04:08.319] doing a search on an API like linear or

[00:04:11.360] notion or something like that or whether

[00:04:13.599] it's like pulling things out of a vector

[00:04:15.599] database. Like for me like

[00:04:18.639] retrieval augmented generation doesn't

[00:04:20.320] have to use vectors. It doesn't have to

[00:04:21.600] use search. It's just based on what the

[00:04:24.400] user asked or based on some logic that I

[00:04:27.120] know in my business application. We're

[00:04:28.639] going to retrieve data and give it to

[00:04:30.320] the model deterministically every single

[00:04:32.320] time. So when the model gets the user's

[00:04:34.160] question or query or task or whatever it

[00:04:37.759] is, you are always going to be injecting

[00:04:40.080] some set of and it's probably not the

[00:04:41.600] same every time, but it's deterministic

[00:04:43.360] code mostly that defines what goes in

[00:04:45.360] there. And maybe there's searches and

[00:04:46.639] lookups and XG boost and vectors and

[00:04:48.400] things like that, but that's kind of

[00:04:50.080] basic like your code decides the logic.

[00:04:53.600] And so with agentic rag, it's it's kind

[00:04:56.080] of a little bit more open-ended. It's

[00:04:57.600] this just agent calls tools in a loop.

[00:05:00.080] And so it's the agent's job to define

[00:05:03.199] what context gets pulled into the

[00:05:04.800] context window. And sometimes if the

[00:05:06.560] context is bad, it's still in the

[00:05:08.000] context window, but it's the agent's job

[00:05:09.680] to call tools to try to get the enough

[00:05:12.560] information to resolve the user's query.

[00:05:15.440] >> Yeah, I I'll tell you how I think about

[00:05:16.960] it. And probably it's probably slightly

[00:05:18.639] different, but slightly aligned as well.

[00:05:20.560] Um

[00:05:22.240] my theory is

[00:05:24.720] I think agentic rag the whole purpose of

[00:05:27.120] it is it's actually not a definition of

[00:05:29.919] how you implement it. It's actually more

[00:05:31.360] of a definition of what the goal of the

[00:05:33.039] problem is. So when I think about the

[00:05:35.440] world, I think about a rag system as a

[00:05:38.479] much narrower system. And this might be

[00:05:40.479] exactly what you're saying. But when I

[00:05:42.880] think about um in the sense of like a

[00:05:45.360] narrow system, what I mean by that is

[00:05:47.440] you have a you as a developer have an

[00:05:49.919] understanding of the scope of the

[00:05:51.680] problem that the user is asking. And an

[00:05:54.240] agentic rag pipeline is designed to go

[00:05:56.639] solve for a problem where you as a

[00:05:58.880] developer don't have a scope for knowing

[00:06:00.479] what the user is asking. Well, and this

[00:06:02.639] is what we always talk about is the the

[00:06:04.319] kind of spectrum between the kind of

[00:06:06.240] full open-ended yolo just call tools in

[00:06:08.800] a loop versus the specific pipeline. And

[00:06:13.120] so when you write the pipeline, you have

[00:06:14.479] more deterministic code. You have less

[00:06:17.520] like the problem space you can solve is

[00:06:20.800] smaller. But the idea is by by being

[00:06:23.759] deterministic about the things you know

[00:06:25.280] are always going to work in a certain

[00:06:26.720] way, then you can actually solve that

[00:06:29.199] problem better. like the open-ended

[00:06:30.960] agent can do more things, but if you

[00:06:33.360] want accuracy, you actually want to say,

[00:06:34.960] "Well, we're always going to do these

[00:06:36.080] three steps in this order. Why are we

[00:06:37.520] going to prompt the agent to call those

[00:06:39.360] three tools? Just we'll just call those

[00:06:40.800] APIs and inject it every time."

[00:06:42.560] >> Yeah, exactly. So, here's the thing. I I

[00:06:45.360] want to talk through the code that we

[00:06:46.639] built today, but I think one of the most

[00:06:48.800] important things that I really want to

[00:06:49.919] talk about is

[00:06:51.840] I I had a hot take that I built while

[00:06:54.080] building the system. I think

[00:06:56.319] >> you you learned something new by

[00:06:57.680] building.

[00:06:58.479] >> Yeah. Uh well,

[00:07:00.160] If you are deciding whether or not you

[00:07:01.599] should build an agentic rag system or

[00:07:03.199] not, um you should just build one. It's

[00:07:05.199] way easier than you think. I built the

[00:07:06.479] whole thing, like I said, in 3 hours

[00:07:07.840] using cloud code. Um I wrote I wrote

[00:07:10.479] probably around um I think I wrote about

[00:07:13.840] 30% of the code by hand and 70% of it is

[00:07:16.800] AI generated. I don't think I could have

[00:07:18.479] done 100% uh by AI generated personally

[00:07:21.440] uh just because of how nuanced and like

[00:07:22.960] some of the decisions were, but like 70%

[00:07:24.880] of the code is actually all UI code.

[00:07:27.199] very little of it is actually agentic

[00:07:28.800] code. Almost all of it is pure UI UI

[00:07:32.000] stuff I have to build. But I think one

[00:07:35.199] of the first things that I realized

[00:07:36.319] while building this is actually that

[00:07:37.520] most people should not build

[00:07:40.639] rag aentic rag systems for their

[00:07:42.880] workflows. If you're building a software

[00:07:44.880] stack, most problems are not so wide

[00:07:48.319] that you need an agentic rag system.

[00:07:51.599] And the reason I felt this was because

[00:07:54.879] it turns out it's it's very similar to

[00:07:57.759] different kinds of problems. But the way

[00:08:01.120] if you have an Excalibur, let's do some

[00:08:03.120] drawing.

[00:08:03.440] >> I'll send it to you on Slack.

[00:08:04.639] >> I'll show you exactly why I came to that

[00:08:06.080] conclusion after building this. And you

[00:08:08.319] might disagree.

[00:08:10.160] I did not use the cloud agent SDK. I

[00:08:12.319] actually specifically whenever I really

[00:08:13.759] want to go learn something, one of the

[00:08:15.759] first things that I try and do is I

[00:08:18.319] really want to learn it from first

[00:08:19.599] principles and I just find personally

[00:08:21.680] for myself writing the code helps me

[00:08:23.440] understand how it works. If I use the

[00:08:24.720] cloud agents SDK, I don't actually

[00:08:26.879] understand how like what a system is

[00:08:31.199] doing. And by actually writing the code,

[00:08:33.680] I now just I can tell you every little

[00:08:36.159] bit of a system design decision that you

[00:08:37.760] might make trade-offs for and like where

[00:08:39.039] the cloud agent SDK might be useful and

[00:08:40.719] where it might not. But honestly, I

[00:08:43.120] don't think I would have won any more

[00:08:44.560] time by using the cloud agent SDK. I

[00:08:47.360] think it would have actually like cost

[00:08:48.720] me probably more time because certain

[00:08:50.080] things would have been harder and other

[00:08:51.200] things would have been easier.

[00:08:54.399] >> Code in a second.

[00:08:56.160] >> Yeah. And I I would love to talk through

[00:08:58.240] also like the implications for like

[00:09:00.640] building the SDK when you are also

[00:09:04.640] working at the lab that creates the

[00:09:06.800] model because it gives you some

[00:09:08.240] interesting other unlocks that we can

[00:09:09.760] dig into and we'll look into some of the

[00:09:11.279] stuff under the hood in cloud code that

[00:09:13.040] that that you can see if you look at the

[00:09:15.600] full tool responses.

[00:09:17.920] >> So I'm going to go share my screen and

[00:09:19.600] show you the whiteboard.

[00:09:22.320] >> Amazing.

[00:09:22.720] >> Uh share screen. Um,

[00:09:25.920] all right. We're going to talk about

[00:09:28.000] this and we're going to talk about

[00:09:29.120] agents and how how I at least learned

[00:09:31.680] about it. Oh, that was not a good ink.

[00:09:34.959] Uh, whatever. We're going to do it. Um,

[00:09:37.200] so I think the first thing that I

[00:09:38.240] learned was actually the fact that what

[00:09:40.160] is it? What is this agentic rag system

[00:09:42.399] that we have? So, there's actually two

[00:09:44.000] parts here that are really interesting.

[00:09:45.600] The first part is we're going to have a

[00:09:47.680] user query come in and then we're going

[00:09:49.839] to have a we're going to have a response

[00:09:51.120] come out like a user is going to send us

[00:09:52.640] a message like what I've said like what

[00:09:54.000] does the Fern folder do or how do I use

[00:09:55.440] a Gemini API at some point I'm going to

[00:09:57.600] get some sort of reply from the user

[00:09:59.040] that is like something friendly for the

[00:10:00.800] user to go do. Now there's a whole bunch

[00:10:03.279] of hoopla that's going to happen in here

[00:10:04.800] as well that I probably want to deal

[00:10:06.560] with at some point. Uh that is probably

[00:10:09.839] some agent stuff but for now as far as

[00:10:12.800] the user is concerned they're going to

[00:10:14.000] send a query. they're going to get a

[00:10:15.200] response and then after that what I'm

[00:10:17.440] going to do is I'm going to I'm

[00:10:18.480] basically just going to build blocks of

[00:10:20.399] this over and over again in sequence and

[00:10:23.600] that is what builds this agentic system

[00:10:25.680] and I think that is the first insight

[00:10:27.519] that I had which was like what is this

[00:10:30.160] stuff a user query comes in a bunch of

[00:10:32.079] stuff has to happen here and the model

[00:10:33.600] is deciding what is going to happen in

[00:10:35.200] here and at some point the respond comes

[00:10:37.360] out and then I go in that is the key

[00:10:39.040] part that made it agentic for me and

[00:10:40.560] then I decided what are all the tools

[00:10:41.920] that I want to give it over here so I

[00:10:43.440] just came over the list of tools.

[00:10:46.480] Um, and come up is a is a bad term. What

[00:10:49.200] I really did is I just took the list of

[00:10:50.720] tools that cloud code has and I built

[00:10:52.399] all of them. Uh, GP, uh, I had GP, I had

[00:10:56.880] Glob, I had ls,

[00:11:00.240] and then I built these in along with

[00:11:01.839] like a bunch of other tools and I'll

[00:11:03.120] show you every single tool I have in

[00:11:04.240] there. And like I said, all the code is

[00:11:05.279] completely open source so you can

[00:11:06.240] actually go read it really easily. And I

[00:11:08.160] built all these tools out and I even

[00:11:09.839] have like an agents tool that actually

[00:11:11.200] allows you to spawn sub agents. I didn't

[00:11:13.760] show that off. I'll show

[00:11:14.560] >> you build sub agents.

[00:11:15.680] >> I built sub agents too. Sorry. I built

[00:11:17.120] the whole

[00:11:17.440] >> of course.

[00:11:18.240] >> I mean subtasker is like actually

[00:11:19.839] conceptually not that complicated. We've

[00:11:21.839] talked about it a lot. It's just new

[00:11:23.120] context window.

[00:11:24.000] >> Most of the time actually came from UI

[00:11:25.920] time, not from anything else.

[00:11:28.560] >> And I just wanted to build this

[00:11:29.680] workflow. And once this thing completed,

[00:11:31.440] I then wanted to get the response from

[00:11:33.040] the user. And then once the response

[00:11:34.480] came in, the user could send another

[00:11:35.920] message. And then I just do this over

[00:11:37.200] and over again. So for for terminology

[00:11:39.519] just because we're kind of talking about

[00:11:40.560] a lot of things. I think you called

[00:11:42.240] these like the internal things in one of

[00:11:44.720] these blocks is you have like n

[00:11:46.160] iterations. You name calling them

[00:11:48.079] iterations through the tools.

[00:11:49.760] >> Yes.

[00:11:50.079] >> And then I would call one of these like

[00:11:51.760] a turn.

[00:11:53.279] >> Sure. Yeah. We let's we can call that. I

[00:11:55.200] think that's a good that's a good

[00:11:56.560] nomenclature. Uh it's going to make it a

[00:11:58.720] lot easier. I I did come up with a name

[00:12:00.160] for the internal thing cuz I was like

[00:12:01.279] getting confused.

[00:12:02.800] >> What did you call it? I just called it

[00:12:04.800] iterations uh because I needed a word

[00:12:07.360] and that was the word that existed and

[00:12:09.920] I'll post some screenshots just so you

[00:12:11.279] guys have an idea of what that means.

[00:12:12.720] This is Google Chrome is hiding my so

[00:12:16.320] when I go over here this is kind of what

[00:12:18.000] it looks like. I do the same thing. So

[00:12:19.279] like an iteration over here is an

[00:12:21.279] iteration I call a tool and it's

[00:12:23.680] basically a tool transaction list that

[00:12:25.519] runs forever until it basically decides

[00:12:28.000] the only tool that I choose to terminate

[00:12:29.760] on is a tool that replies to a user.

[00:12:32.959] Now, because this can go off spinning

[00:12:34.880] into a loop forever, I actually have to

[00:12:36.399] do some work to just set max iterations

[00:12:38.000] as well. So, like at some max iteration

[00:12:39.600] loop, I just stop it. Uh because I don't

[00:12:42.000] want it to spin forever um and just burn

[00:12:44.959] money. Uh but in theory, I didn't have

[00:12:47.920] to do that. Uh I just needed that. Uh

[00:12:49.680] but now that this worked, what was the

[00:12:51.600] hard part about this? Like why do I

[00:12:52.959] think that most people should not build

[00:12:54.880] this system? Well, it turned out that

[00:12:57.600] the number one problem with this system,

[00:12:59.519] I wonder if anyone can guess. Dexter,

[00:13:01.200] what's your guess about what you think

[00:13:02.160] the hardest part about this whole system

[00:13:03.440] is?

[00:13:03.920] >> Designing the tool prompts and the tool

[00:13:06.480] responses to be usable by the model and

[00:13:10.079] context efficient for the model.

[00:13:13.120] >> Um, tool prompts was actually the I

[00:13:15.200] actually never touched the tool prompts

[00:13:16.800] after the first time of writing them.

[00:13:19.120] >> Did you just steal the cloud ones or did

[00:13:20.639] you write them yourself?

[00:13:22.160] >> I you asked

[00:13:23.279] >> Claude wrote them.

[00:13:24.160] >> I just asked cursor to write it.

[00:13:25.680] Actually, oh, sorry. I said Claude. I

[00:13:27.440] actually used cursor this whole time. I

[00:13:28.720] just wanted to try new age agent. I

[00:13:29.680] actually used cursor the whole time. It

[00:13:31.200] was 70% cursor, 30% me.

[00:13:33.360] >> Um,

[00:13:33.680] >> how was how was the cursor agent?

[00:13:35.519] >> I told you I built the whole thing. If

[00:13:36.800] you think this agent is cool, I built

[00:13:38.000] the whole thing up there.

[00:13:39.519] >> Okay.

[00:13:39.839] >> Um,

[00:13:41.360] so I did that. Um, I also did a couple

[00:13:44.480] more things while I did this. Um, what

[00:13:46.880] what I found was the hardest, sorry,

[00:13:48.560] I'll talk about that in a second. What I

[00:13:50.000] found the hardest part about here wasn't

[00:13:51.600] actually the tool definitions. It was

[00:13:54.240] actually the implementation of the

[00:13:55.600] tools. And when I noticed agent quality,

[00:13:58.480] what's surprising is when I tried this

[00:14:00.320] thing uh with even the best models, the

[00:14:02.560] key difference to making this work was

[00:14:04.240] actually how I changed how the tools

[00:14:05.839] were implemented. Everything else made

[00:14:08.639] zero impact or negligible impact on the

[00:14:11.279] quality of the agent based on the kinds

[00:14:12.560] of tasks that I was doing and the way

[00:14:14.639] >> that's the that's the promise of agents.

[00:14:17.040] That was the promise of agents a year

[00:14:18.480] ago, right? which is like use use a

[00:14:20.720] framework, use the loop and then just

[00:14:22.639] bring your own tools and you control

[00:14:25.199] kind of your own destiny by just like as

[00:14:27.600] long as you build good tools and you

[00:14:28.959] implement them well the agent can do

[00:14:30.560] anything

[00:14:31.519] >> kind of but effectively what I found was

[00:14:33.680] if I need if I define my tools well then

[00:14:35.920] it did work but the other problem that I

[00:14:37.760] did have to do was I did need to have my

[00:14:39.680] tool def my prompt was semi- tied to my

[00:14:42.639] tools and that part was very tricky to

[00:14:44.399] go do right

[00:14:46.079] >> yeah I've seen that a lot I've seen a

[00:14:47.519] lot of people building coding agents

[00:14:48.880] They have it in the system message and

[00:14:51.040] in the tool definitions and then

[00:14:52.880] sometimes even injected to the end of

[00:14:54.800] the user message as well.

[00:14:56.480] >> Conniey's got a very interesting comment

[00:14:58.240] about like testing and evals. Um yes,

[00:15:00.959] while I was building this whole thing, I

[00:15:02.320] was actually constantly testing. So my

[00:15:03.760] iteration loop for running this was

[00:15:05.279] actually one of the first things I did

[00:15:07.199] as I actually built a really really good

[00:15:10.240] CLI tool that was pretty good. And as

[00:15:12.720] soon as I built a CLI tool, I actually

[00:15:14.320] built a TUI because the CLI tool quickly

[00:15:18.000] became unusable

[00:15:20.079] because of how printing stuff came out

[00:15:22.000] to be. And I needed something to

[00:15:23.760] actually

[00:15:25.600] uh I actually needed something to make

[00:15:27.839] my problem be a lot easier to

[00:15:29.839] understand. So, for example, when I get

[00:15:31.920] the GP tool, when I had a giant log

[00:15:33.680] system here, I needed to see the

[00:15:35.440] difference between one tool versus the

[00:15:37.120] next tool very clearly and I needed to

[00:15:39.600] not override my 2E when I was actually

[00:15:42.320] like writing stuff and typing stuff out

[00:15:44.800] into the terminal and that was really

[00:15:46.800] hard to do with just a pure CLI. So, I

[00:15:48.720] found it to be very useful to actually

[00:15:50.079] just build a TUI and just tell the model

[00:15:51.440] to do that. And once I did that, funnily

[00:15:53.920] enough, cursor actually built the right

[00:15:56.079] abstraction layer for my agent as well,

[00:15:57.759] which was it was an agent that ran that

[00:15:59.680] had hooks for every interaction that

[00:16:01.680] happened. Then I could just like observe

[00:16:02.880] it with different states. And that's the

[00:16:05.600] exact UI I wanted. So the CLI and the

[00:16:07.279] TUI both interface the same thing. And I

[00:16:08.880] could have built a web UI that

[00:16:10.240] interfaces the same thing because it's

[00:16:11.920] all

[00:16:12.240] >> so it just emits events and then there's

[00:16:14.320] an out like the interface to it is you

[00:16:16.240] just render the events as they happen

[00:16:18.240] >> basically. Yes.

[00:16:19.519] >> Okay.

[00:16:19.839] >> Uh along the way. So

[00:16:21.920] UI UI loop was really hard designing it.

[00:16:24.880] And then once I designed the UIUI loop

[00:16:26.639] for actually iterating on the tools and

[00:16:28.639] then I could actually go ahead and try a

[00:16:30.320] bunch of prompts. So I actually tried

[00:16:31.440] the Fern thing over and over again until

[00:16:32.880] I finally made it work. And the first

[00:16:34.560] version of this system did not work. The

[00:16:37.440] second version of um the second version

[00:16:40.720] of the system

[00:16:42.720] also didn't work. And eventually I just

[00:16:44.399] annealed it closer and closer to finally

[00:16:46.480] make it work. And I think what I really

[00:16:48.000] want to share today is one the coding

[00:16:50.240] architecture of how I had to go do this.

[00:16:51.839] So let's talk about the tool

[00:16:52.800] definitions. The second thing I want to

[00:16:54.880] talk about is what I did to actually

[00:16:57.199] make the tools better. And the third

[00:16:59.440] thing I want to talk about

[00:17:01.040] >> is what I would do to make this even

[00:17:02.800] better going forward.

[00:17:04.720] >> Cool. So I I I would love to hear more

[00:17:07.120] about kind of what you had in the tools

[00:17:09.120] before you changed them and what you

[00:17:10.720] learned about like what works well and

[00:17:12.319] what didn't.

[00:17:13.039] >> I will I will gladly do that. So let's

[00:17:15.760] get into this. Uh, Dexter, I won't be

[00:17:17.520] watching the chat at all. Uh, so if you

[00:17:19.360] see stuff on the chat, that is worth it.

[00:17:20.959] I'll let you track it. And I'm just

[00:17:22.799] going to walk straight through um

[00:17:25.280] straight through the code.

[00:17:28.000] Um, I'm going to share my whole screen.

[00:17:29.840] Again, if you guys see something I'm not

[00:17:31.280] supposed to, please flag in the chat so

[00:17:32.720] we can cut it out of the stream um

[00:17:35.600] eventually.

[00:17:36.320] >> Careful. We're now live on on Twitter.

[00:17:38.720] So, uh,

[00:17:39.840] >> shoot, this is forever. Um, let's start

[00:17:42.000] with the code architecture now that this

[00:17:43.679] thing works. Uh, I can show sub agents

[00:17:45.760] if you want, but I'll do that at the end

[00:17:46.880] because I think that's the least

[00:17:47.840] interesting part about this. So, I'm

[00:17:49.919] just going to start with the tool

[00:17:50.880] definitions because I think that's the

[00:17:52.080] best entry point to the system. So, I

[00:17:54.480] have two systems that I built. I built

[00:17:57.840] an agent loop that just takes a state.

[00:17:59.760] It has a giant prompt in here. I don't I

[00:18:01.520] don't even think this prompt makes a

[00:18:02.559] difference. I just wrote a cursor wrote

[00:18:04.160] and I just like, okay, leave it as as it

[00:18:06.000] is. Uh, and I just dump out the state

[00:18:08.400] into the prompt and I let it run. And

[00:18:10.400] then I have a separate function for sub

[00:18:11.840] aent loop. And the main reason I have

[00:18:13.520] this is because uh and I don't like this

[00:18:15.840] about BAML. I had to go fix this u once

[00:18:18.080] I discovered this is I have a bunch of

[00:18:20.320] tool definitions. But one second before

[00:18:22.480] I show the tool definition, remember all

[00:18:24.160] this agent can do is it can either reply

[00:18:25.760] with one of the tools or a response to a

[00:18:27.760] user to render something. That's it.

[00:18:29.600] Nothing else is allowed to happen. Same

[00:18:31.840] with this agent. It can either pick one

[00:18:33.120] of the sub aent tools or reply to a

[00:18:34.720] user. Now what are the tools that I

[00:18:36.320] allow? An agent tools are basically the

[00:18:38.640] sub aent tools plus the agent tool.

[00:18:40.640] That's it. That's so the agent tool is

[00:18:43.039] actually call a new agent basically.

[00:18:45.120] >> Exactly. It spawns a new agent. I can go

[00:18:47.120] read this if you want. This is what it

[00:18:48.240] does. Launch a new agent that has access

[00:18:49.600] to any of this stuff.

[00:18:51.760] >> And there's a bunch.

[00:18:52.480] >> This looks like the claw code prompt.

[00:18:54.640] >> I literally just copied the and pasted

[00:18:56.240] most of it.

[00:18:57.280] >> Okay.

[00:18:57.919] >> And then what I did, it's just a

[00:18:59.440] description plus a prompt like nothing

[00:19:01.520] special. It just kind of plumped it

[00:19:03.360] through. Then the sub aent tools are

[00:19:05.760] basically I have a batch tool, a glob

[00:19:07.440] tool, grab tool, less tool, exit plan

[00:19:09.440] mode, read tool, write, web fetch,

[00:19:11.760] to-do, to-do, write, and web search. Web

[00:19:13.919] fetch and web uh search are slightly

[00:19:16.320] different. This uses search API. This

[00:19:18.000] uses actually only the like a fetch to

[00:19:20.559] get a specific URL along the way.

[00:19:22.320] >> Can you can you zoom in a little bit?

[00:19:24.320] >> Yes, I can.

[00:19:25.360] >> Yep. And then the other question from

[00:19:27.039] John was, is it on is the code on GitHub

[00:19:29.200] yet? I think we're going to push it

[00:19:30.240] after this. So, we'll send out an email

[00:19:31.760] after the episode with all the code.

[00:19:33.360] Exactly. So I just want to look at some

[00:19:35.520] of these tools and I this what I want to

[00:19:37.200] talk about is like I actually never

[00:19:38.480] changed these definitions at all. Once I

[00:19:40.240] wrote them it just works. Um and the

[00:19:43.360] only key part to every tool is every

[00:19:44.960] tool has a field called action called

[00:19:47.520] glob action with the name of the action

[00:19:50.160] itself and then the actual pattern that

[00:19:51.840] it rendered. uh and then all the

[00:19:54.000] parameters that came with it and some

[00:19:55.760] and that why I use the action key is

[00:19:57.679] because it makes it a really cool

[00:19:58.960] discriminator for any sort of stuff I do

[00:20:01.280] afterwards to make sure what is actually

[00:20:02.880] happening.

[00:20:04.400] Now this was the easy part. Writing the

[00:20:07.760] actual system was actually quite easy

[00:20:09.039] and once I actually wrote this I think I

[00:20:11.520] have a test case somewhere here. I might

[00:20:13.440] not uh

[00:20:16.400] one second

[00:20:18.720] restart.

[00:20:20.640] There we go. Okay. Once I actually wrote

[00:20:22.640] this, I actually read the prompt and I

[00:20:23.919] think it's worth reading the prompt a

[00:20:25.200] little bit. Uh the model can basically

[00:20:27.360] answer one of these. Uh it just lists

[00:20:30.720] this down and says, "Okay, one of the

[00:20:32.080] actions is bash, tells describes that

[00:20:33.679] one." It then lists the glob action and

[00:20:35.200] then lists all of these. Um funny

[00:20:37.440] enough, I actually only read this prompt

[00:20:40.320] at certain points, which was when a tool

[00:20:42.400] failed. So I actually started off not

[00:20:44.320] reading the prompts at all. Uh and then

[00:20:46.720] I just let it vibe. And the reason I did

[00:20:48.400] that is because I know Cloud Code works.

[00:20:50.159] I know a lot of these tools are probably

[00:20:51.919] based off of cloud code directly. So I

[00:20:54.000] kind of had a good intuition that this

[00:20:55.440] was going to work up front.

[00:20:57.600] Um what I did do however that I think

[00:21:00.000] was not ob what I did do pretty much on

[00:21:02.400] within the first iteration is I I listed

[00:21:04.480] some scary tools. Edit tool, multi-edit

[00:21:06.720] tool, write tool, uh notebook edit tool.

[00:21:08.880] I just didn't want it to write to the

[00:21:10.000] file system. So I just plum these out. I

[00:21:12.799] just

[00:21:13.200] >> I love using scary tools. I was I've

[00:21:16.080] been using the word scary tools since

[00:21:17.760] since we did all this human layer stuff

[00:21:19.440] for human in the loop. What are the

[00:21:20.640] things you want to get approval on?

[00:21:21.919] Right.

[00:21:22.240] >> And really bash tool should also be in

[00:21:23.919] scary tool, but bash is too useful. So I

[00:21:25.679] kind of left it.

[00:21:29.120] >> Scary but not as not as uh as uh plus

[00:21:32.080] EV, I guess.

[00:21:33.120] >> Yeah, I really just didn't want to

[00:21:34.720] change the file system because this was

[00:21:35.919] a reader agent mostly. It's like

[00:21:37.440] supposed to answer questions about docs.

[00:21:39.600] >> One one question in the chat that I

[00:21:41.120] think we should make sure we get to is

[00:21:42.240] like um how did you eval these tools?

[00:21:44.159] How did you score? How did you know that

[00:21:45.840] new definitions were better than old

[00:21:47.360] ones? Was it just vibes or do you have a

[00:21:49.520] testing harness?

[00:21:50.400] >> I just kept on running the tool over and

[00:21:52.400] over again and rather than doing

[00:21:53.840] anything else. And the reason I did that

[00:21:55.600] is because like when I'm in the flow

[00:21:58.000] when I'm in like flow state and I'm

[00:21:59.440] trying to just make it something that

[00:22:00.799] works

[00:22:02.400] running an eval system and like like

[00:22:05.120] okay, I'll show you guys what what the

[00:22:06.880] actual chat log looks like so you guys

[00:22:08.320] can get an idea.

[00:22:08.799] >> I mean, you did you did make an eval. It

[00:22:11.440] was just you uh you picked a a test case

[00:22:14.799] and you ran the same case over and over

[00:22:16.559] again live test case looks like for this

[00:22:18.720] eval right like at at iteration loop

[00:22:20.720] number at iteration loop number seven I

[00:22:22.880] just have a giant message array that I

[00:22:24.559] have to deal with and like how do I eval

[00:22:27.760] this thing in a way that's reasonable I

[00:22:29.360] can't I can't actually go read it. So I

[00:22:30.960] started doing instead is I would just

[00:22:32.240] run the loop and I just look at what

[00:22:33.760] sequence of tools were called in what

[00:22:35.120] order and once I knew what sequence of

[00:22:37.120] tools the parameters I would look at

[00:22:38.960] sometimes cuz the parameters rarely

[00:22:40.480] mattered. I just need to look at the

[00:22:41.679] sequence of tools and there's different

[00:22:43.039] ways I could have done that. I could

[00:22:44.159] have looked at it here. I could have

[00:22:45.600] looked at it in the terminal UI. It

[00:22:47.679] really doesn't

[00:22:48.159] >> what's the chronology here is the the

[00:22:50.640] read is the last one is at the top

[00:22:52.559] right.

[00:22:52.880] >> The top one is the most recent time

[00:22:54.000] stamp right here.

[00:22:54.880] >> What's this red? Why is it red? What

[00:22:56.559] does that mean?

[00:22:57.120] >> So I'll talk about this stuff. It turns

[00:22:58.559] out models don't always follow tool

[00:23:00.080] calling uh in a lot of scenarios. So

[00:23:02.480] I'll talk about hacks that I had to do

[00:23:03.760] to make it actually work like super

[00:23:05.440] reliably.

[00:23:06.720] >> Did it like output a tool that wasn't

[00:23:08.240] valid or like blew up the parser or

[00:23:09.840] something?

[00:23:10.240] >> Yeah, exactly. It would just make up

[00:23:11.840] tools sometimes. And even if it didn't

[00:23:13.919] make up tools, sometimes it would reply

[00:23:15.360] to a user with some interesting code.

[00:23:17.360] >> So

[00:23:17.679] >> that's uh I read that in the crew AI

[00:23:19.520] prompt a long time ago was like do not

[00:23:21.200] hallucinate tools. Do not make up any

[00:23:23.039] tools. They even built a feed feedback

[00:23:25.280] system in to like if the tool was

[00:23:27.120] unknown, it would feed that error back

[00:23:28.559] into the model and be like you picked a

[00:23:29.840] tool that doesn't exist, try again.

[00:23:31.440] >> Yeah. So that that is not that is kind

[00:23:33.600] of pointless. So I didn't do that, but I

[00:23:35.760] did do something else that I think made

[00:23:37.120] it a lot better. So what do I do? I

[00:23:39.440] basically have a run loop system where

[00:23:40.720] you take in a user message and as a user

[00:23:42.799] message comes in you just basically run

[00:23:44.159] the iteration loop and then you just go

[00:23:46.159] exit out and then you wait for another

[00:23:48.320] user message

[00:23:50.320] and once a new user message comes in

[00:23:52.159] then you just keep on going again. So

[00:23:53.520] basically as soon as the user gives you

[00:23:54.720] a new message you just run this loop

[00:23:56.159] over and over again. Why do I have two

[00:23:58.559] loops here? Well one I just want to run

[00:24:00.880] an n number of iterations. So you can

[00:24:02.240] think of this as a turn. Dexter calls it

[00:24:03.919] a turn. I

[00:24:04.960] >> call this the the inner loop versus the

[00:24:07.360] outer loop is what we'll talk about when

[00:24:09.280] we talk about 12 factor agents

[00:24:10.799] >> and I called iteration like this was

[00:24:12.559] kind of how I thought about it and then

[00:24:15.520] the all the iterations themselves ran

[00:24:17.360] inside of this and what each iteration

[00:24:19.200] did was something really simple um it

[00:24:21.919] basically took the iteration it called

[00:24:23.520] the agent loop function that I had over

[00:24:25.039] here uh which is defined over here which

[00:24:27.120] is the agent tools which had all the sub

[00:24:30.000] aent tools and the agent tool described

[00:24:31.760] into it um and then I got the response

[00:24:34.400] and ignore all this stuff. Ignore the

[00:24:35.600] retry logic over here. I'll talk about

[00:24:36.880] that in a second. But once the response

[00:24:38.880] came in, I basically just checked if

[00:24:40.480] it's a reply to the user, I basically

[00:24:42.240] just called the call back for reply to a

[00:24:44.320] user which was rendered on the screen.

[00:24:46.000] And then I exit out of the loop and then

[00:24:47.600] I kept on going. So that iteration has

[00:24:50.159] ended at that point. Uh this iteration

[00:24:52.559] also told me a couple more things. It

[00:24:54.400] was telling me whether or not I should

[00:24:57.120] exit the exit this um whether or not I

[00:25:00.880] should exit the iteration. So what this

[00:25:02.320] thing returns is it returns is complete.

[00:25:05.200] If it tells me I am ready then I return

[00:25:07.919] the result to the outer loop. Otherwise

[00:25:10.240] I just keep going in this loop. And

[00:25:12.320] that's how I manage the system cuz this

[00:25:13.919] system had was a single iteration.

[00:25:17.200] Now once the once the instance came

[00:25:19.200] through I basically checked the um I

[00:25:21.679] didn't need to do this response adder.

[00:25:23.360] It's guaranteed to have it. But I I

[00:25:25.520] guess Claude the cursor wrote that code.

[00:25:28.080] Once it actually wrote this, I did some

[00:25:30.080] hook stuff over here.

[00:25:31.679] >> I checked for interruptions because I

[00:25:33.440] wanted to be able to interrupt it with

[00:25:34.799] control X and other stuff along the way.

[00:25:37.120] So, I was only able to check for

[00:25:38.640] interruptions. Basically, if an action

[00:25:40.080] tool came in, if other tools came in, I

[00:25:41.679] didn't. I checked right beforehand. And

[00:25:43.279] then again, uh cuz it's like

[00:25:45.200] multi-threading, I guess.

[00:25:47.679] I sent a hook to the front end to say I

[00:25:50.159] have a tool call that I'm making. And

[00:25:52.480] then I actually go ahead

[00:25:54.720] and uh where'd it go? Then I go ahead

[00:25:57.200] and execute the tool. Now this was again

[00:26:00.080] most of it. So there's very important

[00:26:01.440] thing. If the tool was a sub aent then

[00:26:03.200] the sub aent we know spawns another

[00:26:05.200] loop. So it would just it actually had

[00:26:07.200] to be handled slightly differently and

[00:26:08.640] it just wrote the re it rewrote the loop

[00:26:10.880] in here with some duplicate code which I

[00:26:13.279] really didn't like but that's okay. It

[00:26:15.200] did the work and then it does it. And

[00:26:16.960] remember sub agent can't spawn other sub

[00:26:18.799] aents. Um so I didn't have to worry

[00:26:20.799] about it calling this over and over

[00:26:22.320] again. It was kind of guaranteed to be

[00:26:23.600] safe. It could originally call sub

[00:26:25.600] agents and that was one of the key

[00:26:26.960] things that I had to stop it from doing.

[00:26:29.039] >> Question.

[00:26:29.840] >> Go ahead.

[00:26:30.880] >> How much of the outer loop passes along

[00:26:32.960] context and history or does it start

[00:26:34.720] fresh on every iteration?

[00:26:36.000] >> Every sub agent starts fresh

[00:26:38.320] >> but uh the outer loop in general.

[00:26:39.840] >> The outer loop preserves the history.

[00:26:42.159] >> Cool. Because you have that array of

[00:26:43.679] messages and so you're just keeping all

[00:26:45.279] of the message objects. So like if I

[00:26:47.440] send another message object here uh if I

[00:26:50.000] actually show what okay if I actually

[00:26:52.880] I'll refresh this page again. If I

[00:26:54.559] actually show my messages object here so

[00:26:56.240] you can get an idea like every single

[00:26:58.240] time I ran this it actually just kept on

[00:27:00.480] building into it or it just built more

[00:27:03.440] and more into it. And you can actually

[00:27:04.480] just read the full prompt and I'll go to

[00:27:05.679] the bottom so you can see these get

[00:27:08.000] really long. It just like when I did

[00:27:10.080] extract the latest announcements from

[00:27:11.600] Gemini, it actually like go did this and

[00:27:14.480] it would just like render this for me

[00:27:15.840] and let me know if it was going on if

[00:27:17.360] that makes

[00:27:17.760] >> sense. So I just stacked everything. I

[00:27:19.440] didn't I did not clear the context

[00:27:20.720] window at all.

[00:27:21.760] >> So two more questions. What is this eval

[00:27:23.760] tool you're using?

[00:27:25.200] >> Um this is a thing for boundary studio

[00:27:28.799] but I'll talk about that later.

[00:27:30.159] >> Uh this wasn't really uh we'll talk

[00:27:32.159] about this separately.

[00:27:34.320] >> Uh what I really want to talk about is

[00:27:35.600] how the agent works. So how does the

[00:27:36.960] agent actually work?

[00:27:37.679] >> Keep going. So, we have the sub agent.

[00:27:39.440] We're able to execute tools. Let's look

[00:27:41.120] at some of these tools. So, what's cool

[00:27:42.799] about this is I actually just did this

[00:27:44.159] and I just said tool.action. I rendered

[00:27:46.000] this. What's really nice is you guys

[00:27:47.520] remember how my certain tools were scary

[00:27:49.520] tools and they're not included in here.

[00:27:51.200] I can actually see that because it knows

[00:27:53.679] that even though these tools exist,

[00:27:54.880] it'll actually never get called cuz

[00:27:56.080] action is not allowed to be any of those

[00:27:57.440] types. So, you get really nice type

[00:27:59.360] safety of knowing what tools you're

[00:28:00.559] using. But now that we're doing this,

[00:28:02.720] what is actually happening? Let's look

[00:28:04.080] at one of these tools.

[00:28:06.000] I think LS is a good No, not LS.

[00:28:10.080] LS is not a good

[00:28:10.960] >> I'd like to see like Glob or Grap or

[00:28:12.960] something.

[00:28:13.360] >> Let's look at Glob. Glob is actually I

[00:28:15.440] think a good example. No, Glob is also

[00:28:18.000] not a good example. I Glob actually I

[00:28:20.240] didn't have to do much with to make it

[00:28:21.360] work. I just did the GP was the one that

[00:28:23.600] I had to do. GP was actually really

[00:28:25.679] challenging to get right. And there's a

[00:28:27.840] couple things. The first thing is the

[00:28:29.440] first bug I had is I wasn't actually

[00:28:30.720] passing the working directory into the

[00:28:32.240] system. So I had to manage state for the

[00:28:34.080] working directory. That was very

[00:28:35.360] annoying. Um, once I got that working,

[00:28:37.760] it was much better. This is also why

[00:28:39.279] cloud code has a CD tool. It's because

[00:28:41.840] when it does the CD tool, it's able to m

[00:28:44.240] it's able to change its own working

[00:28:45.840] directory and its own state

[00:28:47.120] representation

[00:28:48.640] as it's running. And when it's doing

[00:28:50.399] that, what it can do now is it can

[00:28:52.240] actually have it can pass in better

[00:28:54.000] context into the model. If you just call

[00:28:56.080] CD via GP or via bash tool, the model

[00:28:59.120] can't detect that. So what I would do if

[00:29:01.200] I were running the bash tool is I would

[00:29:03.039] at the end of the bash tools execution

[00:29:04.880] loop I would actually grab the current

[00:29:06.640] directory and pass that in. So the

[00:29:08.559] current directory is always relatively

[00:29:10.880] correct for the agent agent.

[00:29:14.080] >> Sorry I want to I want to double down. I

[00:29:15.919] know we have a lot to cover but um

[00:29:17.520] you're saying that if cla in if the

[00:29:19.760] model while running commands includes a

[00:29:22.399] change directory you want to preserve

[00:29:24.799] that directory and leave the agent in

[00:29:26.799] that directory going forward.

[00:29:28.720] >> Exactly. I think that's trash. I hate

[00:29:30.960] that. I actually there's a there's a

[00:29:32.559] flag and claude code where you can

[00:29:34.000] disable that behavior where like when it

[00:29:36.559] runs bash and changes directories

[00:29:38.640] afterwards it will always put the agent

[00:29:40.799] back in the directory it was in. And I

[00:29:43.039] find I get so many better results that

[00:29:45.200] way. And I can I can tell you why if you

[00:29:46.720] want, but I know we have a lot more to

[00:29:47.919] go through. I'll tell you actually we

[00:29:50.159] should talk about this. I'll tell you

[00:29:51.120] why I found it to be better for my agent

[00:29:53.120] specifically because my agent preserves

[00:29:55.360] the entire call stack. the model thinks

[00:29:58.000] it's in that directory.

[00:29:59.279] >> Yeah. But also, can we go back to the

[00:30:00.720] whiteboard?

[00:30:01.520] >> Yes, we can.

[00:30:03.440] >> Um, so here's the here's the problem I

[00:30:06.080] always hit with that is um Claude's

[00:30:08.960] let's say Claude's trying to run the

[00:30:10.159] test, right? And so you go and it runs

[00:30:13.039] this command like, you know, cd uh hld

[00:30:17.200] and go test dot dot dot, right?

[00:30:20.640] >> And then it gets the results back. uh it

[00:30:23.600] makes some changes

[00:30:25.520] and then it tries to run that again and

[00:30:27.600] it so it's it's fshot prompted itself

[00:30:29.840] that the way to run the test is do this

[00:30:32.000] cd and go test dot dot dot but the

[00:30:34.320] problem is is that if you keep the

[00:30:35.600] directory this then fails and so you get

[00:30:38.480] an error and then it has to like think

[00:30:41.279] about like oh I'm actually

[00:30:43.679] >> and like reason about what directory

[00:30:45.360] it's in and then it has to run go test

[00:30:47.520] again or it needs to like cd do

[00:30:50.080] >> I I do my comp which I actually tell it

[00:30:52.320] that the directory change.

[00:30:53.600] >> Ah okay.

[00:30:54.559] >> So see so it makes a s

[00:30:56.720] >> tell it the current working directory in

[00:30:58.640] the prompt so that it knows where it is

[00:31:00.320] and it can think of things.

[00:31:01.600] >> Exactly. Okay.

[00:31:02.399] >> Like if you actually go what do you go

[00:31:04.960] if you go read the prompt that I sent to

[00:31:06.480] the model.

[00:31:07.520] >> Yeah

[00:31:07.919] >> I do that and I give it the full path. I

[00:31:10.720] don't give relative path actually.

[00:31:12.320] >> Yeah. Yeah.

[00:31:13.679] >> I tried relative paths and that actually

[00:31:15.279] did not work. I had to go to full paths

[00:31:17.440] >> at the end.

[00:31:18.000] >> How did you decide to put this at the

[00:31:19.679] top? did you try putting this anywhere

[00:31:21.360] else or were you always just your

[00:31:22.720] instinct was to have

[00:31:23.840] >> queries that I was running over and over

[00:31:25.120] again to go test it and like it just

[00:31:26.720] worked. So I was like okay good enough

[00:31:28.320] and remember I'm using the openi

[00:31:29.919] responses with the GBD5 thing. So like

[00:31:32.799] it's possible that if I was using a

[00:31:33.919] shittier model like sonnet or like uh

[00:31:35.919] GPD4 or something it wouldn't work as

[00:31:37.760] well but like this worked pretty well. I

[00:31:39.600] know openi specifically really heavily

[00:31:41.600] indexes on trusting the system directory

[00:31:43.760] system uh stuff. What I would probably

[00:31:46.399] also do if I were doing this again is

[00:31:49.440] whenever the directory changed uh if I

[00:31:52.559] ran the batch to I actually built the

[00:31:54.080] thing that detected that in batch tool I

[00:31:56.240] would actually put a additional message

[00:31:59.360] as a part of the prompt that actually

[00:32:01.679] solved for that. So like what I would do

[00:32:02.799] is like whenever I did CD as soon as a

[00:32:04.720] tool happened I would actually just plum

[00:32:06.960] in it's like the directory changed and

[00:32:08.480] put that into there personally because I

[00:32:10.320] think that would make life a lot easier

[00:32:12.000] for the model.

[00:32:13.440] >> Okay. Um cool. Okay. Okay, so you were

[00:32:15.120] in the middle of explaining the GP tool

[00:32:16.320] and how it pulls a directory through.

[00:32:17.840] >> So firstly, I know there are a couple

[00:32:19.039] questions there. I did use RG. You

[00:32:20.880] should use rip grap. If you're building

[00:32:22.159] a grap tool and you don't use rip grap,

[00:32:24.399] uh, incorrect. Just use rip grap. Uh,

[00:32:28.399] rust is great for developer tools. Rip

[00:32:30.480] is rust grap built in Rust and just way

[00:32:33.360] better ergonomically.

[00:32:34.960] >> Yeah. And it used to be so the original

[00:32:37.679] fun trivia the original RG was based on

[00:32:39.679] a tool called AG which is called the

[00:32:41.519] silver searcher which was like written

[00:32:43.519] in pearl and did all this parallelism

[00:32:45.760] through like threads. Uh but it was yeah

[00:32:48.640] it was time to rewrite it in rust.

[00:32:50.480] >> So firstly every single GP tool every

[00:32:52.799] single tool I have is that it will

[00:32:54.320] always return a string. That's what I

[00:32:55.679] did over here. I wish I didn't have to

[00:32:57.039] but I did. The last thing I did was

[00:32:59.360] every single time I ran any subprocess

[00:33:01.039] every single one of them has a timeout

[00:33:02.320] built in guaranteed. I had to do that.

[00:33:05.840] I did a couple more things in here. I

[00:33:07.840] actually had to limit how many files

[00:33:09.120] were allowed to be returned. It just was

[00:33:11.919] going to be too bad in a lot of

[00:33:13.120] scenarios because sometimes like uh the

[00:33:15.840] other reason that I have scary tools is

[00:33:17.120] I saw the model look at my root

[00:33:18.559] directory and I was like hell no, I'm

[00:33:20.640] not going to let it look at slash and

[00:33:22.799] that also had problems with glob and

[00:33:24.559] other tools that I was trying to run. So

[00:33:26.240] I had to go simplify that. So the first

[00:33:27.600] thing was limit directory searches.

[00:33:30.320] Now, once I did that, I realized that

[00:33:32.320] there was another problem that ended up

[00:33:33.600] happening, which was when I did the read

[00:33:35.600] tool.

[00:33:37.200] Many of you probably know Cloud Code

[00:33:38.559] doesn't read every single line of code.

[00:33:40.960] It can't in every file. It's because

[00:33:43.039] it's too complex. So, I had to go build

[00:33:44.720] the same thing out. So, I actually built

[00:33:46.559] a limiter on how reading worked. And I

[00:33:49.200] originally when I didn't do that, it

[00:33:50.880] actually had a much smaller limit of

[00:33:52.480] like 2,000 characters or something that

[00:33:54.000] was just too small. So, I increased the

[00:33:55.679] limit to 20,000 characters, but also

[00:33:57.679] 5,000 lines. So either one of those two,

[00:34:00.480] whichever one is fine.

[00:34:01.120] >> But that's 20k per line, right?

[00:34:03.440] >> No, no, no. It's total.

[00:34:05.360] >> It says line characters. Line truncated

[00:34:08.000] at 20,000 characters.

[00:34:08.879] >> That's a bug. I should fix this.

[00:34:10.800] >> Um,

[00:34:12.240] >> it should have been 20.

[00:34:13.280] >> Really, it should be by tokens, right?

[00:34:14.879] But you're not going to bring a

[00:34:15.679] tokenizer.

[00:34:16.320] >> I'm not bring tokenizer. It's not worth

[00:34:17.520] it. But the other thing I had to do when

[00:34:19.280] this actually worked is I actually had

[00:34:20.639] to go write this code to say when with

[00:34:22.560] the truncation notice. Originally, I

[00:34:24.079] wrote just truncated.

[00:34:26.240] But now what I actually had to do was

[00:34:27.839] actually say that oh instead of

[00:34:28.800] truncation this I actually wanted to

[00:34:30.879] have the output the output is truncated

[00:34:32.879] starting at this line to this line and I

[00:34:34.480] gave it information about where the line

[00:34:36.159] was

[00:34:37.040] >> so that it can go through if it really

[00:34:39.200] wants to. Right.

[00:34:40.240] >> Exactly. And then I actually told it to

[00:34:42.480] use a read tool with this parameter. So

[00:34:44.159] I was very very specific in how to go

[00:34:46.320] deal with this along the way. And once I

[00:34:48.560] did this this was actually the crux to

[00:34:50.879] making this work the whole time because

[00:34:52.240] a lot of stuff was actually a lot of

[00:34:54.000] stuff is actually designed to be

[00:34:55.040] truncated. So, for example, web search

[00:34:56.639] and fetch was also truncated. This one

[00:34:59.359] doesn't work as well because I didn't do

[00:35:00.960] that. I had another one where I did

[00:35:02.480] this. Uh, what? No, that's different.

[00:35:05.119] This is the UI stuff. I had another

[00:35:06.720] truncation somewhere. I have to go find

[00:35:08.160] it.

[00:35:08.800] >> Um,

[00:35:09.200] >> so AOS is asking, um, this is great

[00:35:11.920] explanation, but I don't see the rag

[00:35:13.839] related context here. Am I missing

[00:35:15.599] something? Do you want to talk about how

[00:35:16.800] this like maps on to retrieval and

[00:35:18.800] search?

[00:35:19.280] >> Yes, let me go do that really fast. So

[00:35:21.920] what this probably just goes down to

[00:35:23.839] definitions of exactly what is rag. So

[00:35:26.079] rag is a system that takes in a user

[00:35:27.760] query and looks into some database of

[00:35:30.480] some kind that says hey given this

[00:35:32.160] database let me go get a subset of the

[00:35:35.040] database that is relevant here.

[00:35:38.400] I can't delete that dot. So it's going

[00:35:40.160] to go ahead and get like a subset of the

[00:35:41.599] database from this system that matches

[00:35:44.320] the query in some form factor. The

[00:35:46.320] typical way of doing rag is you use a

[00:35:48.800] vector search and you basically look at

[00:35:50.160] all this and you say hey given the

[00:35:52.320] vector search which ones are the ones

[00:35:53.760] that have the highest score and then I

[00:35:55.280] will just go get those and now you have

[00:35:57.280] a rag system that takes a query look

[00:35:59.680] through a database gets you the top

[00:36:01.440] scoring element. Yeah, I think it's it's

[00:36:03.680] really like the difference between like

[00:36:05.359] traditional rag and agentic rag is again

[00:36:07.520] like are you letting the agent call

[00:36:09.359] tools to search for stuff whether it's

[00:36:11.599] GP or glob or vectors or whatever or web

[00:36:14.640] search or whatever it is or are you

[00:36:17.040] basically doing that ahead of time and

[00:36:19.119] just almost like not quite

[00:36:20.560] deterministically but kind of more

[00:36:22.720] deterministically injecting stuff into

[00:36:25.119] the context window regardless of what

[00:36:28.240] tools the agent calls.

[00:36:30.160] >> Exactly. So what I do over here is 100%

[00:36:32.560] of the time when the user query comes in

[00:36:34.000] I call a vector database and like what

[00:36:35.760] is an example of this well like this

[00:36:38.240] system is agentic rag right over here

[00:36:40.079] give it a second so I'll search like how

[00:36:42.960] do I use gemini this thing every single

[00:36:45.520] time queries the database finds all the

[00:36:48.480] relevant pages to this and I hopefully

[00:36:50.000] this will work finds all the relevant

[00:36:51.520] pages to this and like right over here

[00:36:54.320] and then produces a response and this is

[00:36:57.040] great I think for a doc search this is

[00:36:58.800] not bad But what this system is able

[00:37:02.160] what this system is able to do when we

[00:37:04.079] don't 100% of the calling call a vector

[00:37:05.760] database is I decide

[00:37:09.280] if I need to rag anything at all like

[00:37:13.920] for example in order for this system to

[00:37:16.880] actually decide what let's say I sent

[00:37:18.880] this query is that is 1.5 pro the latest

[00:37:24.400] model what this will do in this scenario

[00:37:27.520] is this is still going to actually make

[00:37:29.760] the vector database call and go do this

[00:37:31.839] and it just looks only at my at our blog

[00:37:34.000] post and our docs to go do this because

[00:37:35.920] it's hardcoded to 100% of the time pull

[00:37:38.320] out context in that form factor.

[00:37:40.000] >> Okay. So there's no tool call there.

[00:37:41.839] You're just when you ask when you ask

[00:37:43.680] the question you will always do a search

[00:37:45.680] and always hand that to the agent based

[00:37:47.520] on you know vector similarity to the

[00:37:49.119] user.

[00:37:49.680] >> Exactly. What I do over here is I just

[00:37:52.800] decide if the the model is deciding if

[00:37:55.040] it needs to rag anything at all. And I'm

[00:37:57.920] basically letting it decide exactly

[00:37:59.680] which of the few things I may want to

[00:38:02.160] rag. So for example, one of the things I

[00:38:04.640] could give it is I could give it access

[00:38:06.079] to the same vector database that that

[00:38:07.599] Bammy chat has in our docs. I can also

[00:38:10.800] build what I did today, which is I built

[00:38:14.000] a I basically gave it access to our

[00:38:15.680] entire source code and I said, "Hey, you

[00:38:17.599] can just use this source code however

[00:38:19.839] you want." like search through or do

[00:38:21.040] anything else you want on it. And what

[00:38:22.960] that does for it is it basically treats

[00:38:24.720] it like a rag problem. Um,

[00:38:28.000] >> and you can still do all the rag stuff

[00:38:30.160] in your tool calls. You can do the

[00:38:31.680] reranking, you can do the embeddings,

[00:38:33.200] you can do the search. It's just the

[00:38:34.800] agent is saying, "Okay, I'm going to

[00:38:36.480] search for this." It's going to look at

[00:38:37.920] what it got back and then the model can

[00:38:39.680] decide, do we need to do another search

[00:38:41.040] or do we have all the information? And

[00:38:42.560] that's all kind of encapsulated

[00:38:44.240] generically in the agentic loop. Right.

[00:38:46.480] >> Exactly. It's basically the key part is

[00:38:48.480] like how the decision is being made.

[00:38:50.640] Usually in some code you have some you

[00:38:52.720] have some system making the decision and

[00:38:54.640] here you're just letting the model make

[00:38:56.000] the decision completely and this covered

[00:38:58.480] a lot of different trade-offs. One of

[00:39:00.160] the trade-offs is this question the

[00:39:02.000] ability to ask if 1.5 Pro is the latest

[00:39:04.160] model. That was just something we can't

[00:39:05.920] do in this in the current system as it

[00:39:07.680] is today. We can do it in this system

[00:39:10.560] where I asked the model like is Gemini

[00:39:12.160] the is this the latest model? And what

[00:39:13.920] it did is actually just did a web

[00:39:15.359] search, looked into Google Docs,

[00:39:17.520] actually got the change I guess got the

[00:39:19.200] change logs from the Gemini API.

[00:39:20.960] Additionally, got another change log

[00:39:22.560] from the models page and also uh I think

[00:39:25.920] it did a web where did it go and it also

[00:39:28.800] did a web search for like just where do

[00:39:31.280] I go look for the Gemini API on this

[00:39:33.040] page and that's how it found those

[00:39:34.560] links. It got it and then it was

[00:39:36.240] actually able to tell me way more

[00:39:37.920] information than my docs could ever have

[00:39:39.280] because I'm not indexing and like

[00:39:40.480] updating the vector database every

[00:39:41.680] second of the entire internet.

[00:39:43.599] which is it saying that it is the latest

[00:39:45.520] GA model but there are nonGA models that

[00:39:47.599] are available and there's pros and cons

[00:39:49.680] to both approach

[00:39:51.680] but that's the key difference does that

[00:39:53.200] answer the question well

[00:39:54.800] >> I think that was a great I think Akos

[00:39:56.400] said it was answered well that was a

[00:39:57.920] great question Akos glad we spent time

[00:39:59.520] on that um we have a little bit of time

[00:40:02.079] left um I want to make sure um we can

[00:40:06.720] talk a tiny bit about like RL and owning

[00:40:08.880] both the model and the tool chain and I

[00:40:10.960] also would think it would be really

[00:40:12.160] interesting on this search topic to look

[00:40:14.480] at how you implemented the web search

[00:40:16.000] even if it's even if it's simple because

[00:40:17.839] I imagine you're doing some stuff of

[00:40:19.359] like hey let's take all the HTML and

[00:40:21.280] then use a model to make it more context

[00:40:23.599] efficient things like that

[00:40:24.960] >> that is actually I did none of that

[00:40:26.400] stuff

[00:40:27.359] >> amazing

[00:40:28.240] >> enough like I said this took me a total

[00:40:30.720] of three hours to build the whole thing

[00:40:32.560] so most of the stuff I did was I

[00:40:35.040] implemented to-do tools I implemented

[00:40:36.640] most of these tools every single one of

[00:40:37.839] these tools is basically just baked by

[00:40:39.599] generated by cloud code I did modify

[00:40:42.079] some of them. I'd like to show you the

[00:40:43.280] ones I modified. So, I modified the read

[00:40:44.800] tool.

[00:40:46.480] I did modify the execute batch tool. For

[00:40:48.400] some reason, it didn't have the timeout

[00:40:49.920] in here. I don't know why. It just

[00:40:51.119] didn't. So, that was important to go add

[00:40:52.640] in. The error messages were really

[00:40:54.320] important. Having custom error messages.

[00:40:56.000] Cloud code did that pretty naturally cuz

[00:40:57.440] I prompt not cloud code. Cursor did that

[00:40:59.119] pretty naturally because I prompted it

[00:41:00.240] that I wanted good error messages that

[00:41:01.680] were human readable every single time.

[00:41:04.000] Um,

[00:41:05.520] Glob I had to go change like I said with

[00:41:07.280] the limit to the matches. That was

[00:41:09.040] important. Otherwise, it just added

[00:41:11.119] everything. GP. I showed you how I

[00:41:12.640] changed Grep. Uh, Grep. Did I show you

[00:41:14.800] how to change GP? The big change that I

[00:41:16.400] made to GP was whenever GP was resulting

[00:41:19.280] in itself, uh, one of the things that it

[00:41:21.920] did was it actually outputed the full

[00:41:23.760] path to the directory. I actually

[00:41:25.520] changed GP to always show you relative

[00:41:27.200] path

[00:41:28.079] >> and that was really important for

[00:41:29.119] accuracy. It actually worked way better

[00:41:30.880] once I did that. Before that, it just

[00:41:32.400] >> that's context engineering, dude. That's

[00:41:34.079] context engineering. How do you make it

[00:41:35.359] more context efficient? How do you give

[00:41:36.560] model just the information it needs?

[00:41:38.560] >> Love it. I really wish there was an

[00:41:40.319] easier way to model this, but there

[00:41:41.760] wasn't and it was really annoying. But I

[00:41:43.599] really wish that whenever I rendered

[00:41:44.880] this in the prompt, it would actually

[00:41:46.000] render as just the relative path.

[00:41:47.599] >> But that's that's context engineering.

[00:41:49.359] It's like go under the hood, do the

[00:41:50.800] janky weird thing, whatever it takes to

[00:41:52.800] get the right tokens into the model and

[00:41:55.040] every single token counts. When you're

[00:41:56.880] especially as your contacts get long,

[00:41:58.560] when you save 20 tokens per call and

[00:42:01.520] you're going to GP 30 times, that makes

[00:42:03.359] a huge difference in your outcome.

[00:42:05.119] >> It was really, really different. It was

[00:42:07.440] really, really big. This was one this

[00:42:09.280] was like one of the first failure cases

[00:42:10.640] I ran into. This is also why I started

[00:42:12.480] passing the working directory because I

[00:42:13.760] realized that the reason I need to pass

[00:42:15.520] this in was actually to produce relative

[00:42:17.280] paths and then that also made me uh want

[00:42:20.480] to go update the path as it was running.

[00:42:23.760] This is the other reason by the way

[00:42:25.040] Dexter that you really want to do where

[00:42:26.960] you want the agent loop to have access

[00:42:28.800] to the working directory because you

[00:42:30.640] kind of need to know what directory

[00:42:31.839] you're in to go do this

[00:42:33.440] >> to set up the relative paths and things

[00:42:34.960] like that.

[00:42:35.200] >> To go relative paths. Yes,

[00:42:36.880] >> there was a good comment as well, and I

[00:42:38.400] know we're not going to have time to

[00:42:39.280] talk about it, but having the directory

[00:42:40.800] at the start of your prompt basically

[00:42:42.960] wrecks the entire cache probably, but

[00:42:45.359] that's like an optimization we can do

[00:42:46.880] later, right?

[00:42:47.599] >> I I wasn't trying to optimize for that

[00:42:49.359] in that way. I could have left it as is

[00:42:50.960] and I could have just injected new tools

[00:42:52.319] saying like directory change, directory

[00:42:53.599] change, directory change and not have

[00:42:55.839] modified that if I wanted, but I do know

[00:42:57.599] OpenAI really favors that. So, I would

[00:42:59.920] if that was

[00:43:00.640] >> they favor the first the first beginning

[00:43:02.800] of the system prompt more so than like

[00:43:05.040] down problem. I would actually just move

[00:43:06.800] it out of the system prompt and put it

[00:43:08.000] into a user message saying this is my

[00:43:09.440] current directory artificially and then

[00:43:11.440] inject that in. That's how I would

[00:43:12.640] modify that if I had to.

[00:43:15.599] I definitely wouldn't leave it as a

[00:43:16.960] system prompt and then not modify it.

[00:43:18.960] >> Execute ls, ls had similar things uh

[00:43:21.359] that I had to do where instead of

[00:43:23.119] outputting everything when I ls it, I

[00:43:25.359] actually like tell ls tools exactly if

[00:43:27.599] it's a directory or a file when it

[00:43:29.119] actually ls. So, like if I go up here

[00:43:30.720] and you go look at this. Um

[00:43:32.560] >> Mhm.

[00:43:33.359] >> what you'll see what I mean. This is

[00:43:36.240] another big difference that came out of

[00:43:38.240] this. I hate that I use a thinking

[00:43:40.800] model. Do you see how I actually run

[00:43:42.560] this out? Makes a huge difference in how

[00:43:44.720] you actually read this. It just makes it

[00:43:46.160] easier for the model.

[00:43:47.920] >> And it looks noisy for a human, but it's

[00:43:50.800] actually that's always going to be just

[00:43:52.720] one token. Dur and file are each

[00:43:54.480] probably almost certainly going to be

[00:43:55.520] one token.

[00:43:56.240] >> Yeah, probably. So, it's just not worth

[00:43:57.760] it. It's just way better for me to do

[00:43:59.440] this and not. So that was one thing I

[00:44:00.640] had to do with the ls tool. The read

[00:44:02.319] tool I compressed using the line

[00:44:04.319] truncation thing with instructions of

[00:44:06.000] how to deal with shorter lines, how to

[00:44:08.640] deal with longer lines. Uh execute edit

[00:44:11.760] uh edit tool. I didn't look at I just

[00:44:13.200] removed it.

[00:44:13.839] >> So your edits, did you do old string,

[00:44:15.359] new string, just like string replace

[00:44:17.040] basically?

[00:44:17.839] >> That's clock code.

[00:44:18.560] >> Okay.

[00:44:19.680] >> Um Jupyter notebooks, they actually have

[00:44:22.000] to be dealt with differently compared to

[00:44:24.400] most systems. So the model

[00:44:26.000] >> which is easier to interact with the

[00:44:27.760] cells instead of like editing the raw

[00:44:29.760] JSON. Right.

[00:44:30.480] >> Exactly. So that's why cloud code builds

[00:44:32.319] like a Jupyter notebook editor in that

[00:44:34.000] way. Uh web fetch I didn't really

[00:44:36.000] modify. This is exactly the same. I just

[00:44:37.440] use BS4. Uh

[00:44:38.720] >> when you say you didn't modify it like

[00:44:40.400] what do you mean? Like you mean it's

[00:44:41.839] just once it was generated I didn't

[00:44:44.560] touch like once cursor wrote the

[00:44:46.400] function I just didn't touch it.

[00:44:48.640] >> So how are you okay? So soup.get text is

[00:44:51.200] just stripping out all the HTML and just

[00:44:53.119] giving you the raw text content. Yeah,

[00:44:54.560] that's it. That's all I do in fetch and

[00:44:56.400] I just give a really long give it

[00:44:58.240] truncated and there's no way to get more

[00:44:59.680] truncated. So

[00:45:00.720] >> I know that uh when you use cloud code

[00:45:02.640] it will take the some maybe it's ripping

[00:45:05.440] the text out but I think it just take it

[00:45:06.880] might even just be all the HTML and it

[00:45:08.560] passes it to haiku and it's like here

[00:45:10.160] was the question that the parent model

[00:45:11.920] asked. Can you strip this down and

[00:45:13.440] summarize it as markdown? This is

[00:45:15.280] interesting.

[00:45:16.560] You could add a BML call or something

[00:45:18.000] and this is like deterministic LMS

[00:45:19.839] inside your non-deterministic agentic

[00:45:22.079] rag pipeline the same way you could have

[00:45:23.920] a reranker pipeline or something like

[00:45:25.520] that inside a tool.

[00:45:26.720] >> I could do that here to do call haiku to

[00:45:29.599] summarize the content given the query

[00:45:32.240] >> um and how it's related. I could do that

[00:45:36.720] and I could pass in the summary. The

[00:45:38.240] other thing I could do is I could say

[00:45:39.760] truncated. If you need more information,

[00:45:43.920] use bash to fetch the content.

[00:45:46.560] >> Just tell to use curl to a file or

[00:45:48.480] something.

[00:45:50.000] >> Oh, wait. Not to store.

[00:45:52.880] >> Then you don't get the HTML stripping,

[00:45:54.800] but it's probably

[00:45:55.760] >> I mean, I can I can probably uh And then

[00:45:59.520] what I can pro I could probably do

[00:46:00.960] something around this like or write a

[00:46:02.160] Python command or something.

[00:46:03.920] >> Yeah. Or you could give it a code

[00:46:05.119] execution tool that runs the Python for

[00:46:07.520] you and goes and fetches the thing and

[00:46:09.119] does it. Yeah. Cool.

[00:46:10.160] >> Yeah. Or or I can or I can just modify

[00:46:12.240] my Here's another thing I can do. Agent

[00:46:15.440] tools.

[00:46:16.000] >> I think context 7 has in some of their

[00:46:18.240] fetch tools, they have a parameter that

[00:46:20.079] is like max tokens. And so the model can

[00:46:22.400] call the tool again and allow for more

[00:46:24.880] tokens and it goes into whatever

[00:46:26.720] summarizer model uh has that limit as

[00:46:29.680] its max tokens and like its expected

[00:46:31.920] amount of output.

[00:46:32.960] >> Yep. There you go. Um, path.

[00:46:36.720] >> Ah, cool. Okay.

[00:46:37.839] >> I can just tell it this just like tell

[00:46:39.280] me

[00:46:39.599] >> and then you would just tell it, hey, it

[00:46:40.880] was written to this path and the model

[00:46:42.319] can use the read tool to go get it. I

[00:46:43.839] love that. Actually, that's how that's

[00:46:45.280] the right way to solve this.

[00:46:46.720] >> Exactly. So, like

[00:46:47.599] >> we do this with our linear tool as well.

[00:46:49.119] Sometimes our linear tool, our CLI

[00:46:50.880] brings back way too much markdown

[00:46:52.400] content and so it's like cool, it will

[00:46:54.880] just automatically save it to a file,

[00:46:56.880] the CLI will, and just output, hey, it

[00:46:58.640] was too long, so we put it in this file

[00:46:59.920] and then the model can go read it.

[00:47:01.200] >> Exactly. Um,

[00:47:03.599] uh call the web fetch tool again with

[00:47:06.880] the rest of the content. That's actually

[00:47:08.960] a really good like takeaway in general

[00:47:11.359] for building these agents and designing

[00:47:12.960] these tools is like if you know the code

[00:47:14.800] it's a coding agent and it has a read

[00:47:16.640] tool and a search tool then you should

[00:47:18.880] almost always rather than truncating the

[00:47:20.960] output for the model you should just

[00:47:22.319] write it to a file tell the model where

[00:47:24.079] it is and then let the model decide

[00:47:25.680] which parts of it it wants to read

[00:47:26.960] >> and this is the whole point of like what

[00:47:28.240] an aentic rag system can do it's very

[00:47:30.160] dynamic so in this case I know some web

[00:47:31.920] pages are going to be really long so

[00:47:33.200] I'll just tell that but I'll

[00:47:34.560] specifically put a cloth if you need

[00:47:35.839] more information call the web fit

[00:47:38.079] go again to get the rest of the contents

[00:47:40.079] with a file path and it will probably

[00:47:42.319] figure itself out. Like I I don't have

[00:47:43.760] to think about this too hard. Um, and I

[00:47:46.000] trust that this will work.

[00:47:48.640] Uh, and then like it'll go ahead and do

[00:47:50.240] its thing and then marin content will go

[00:47:52.800] into here. And specifically what I would

[00:47:54.480] actually do is over here. This error

[00:47:56.960] message should actually not go there.

[00:47:59.920] Uh, what I should do truncation. I have

[00:48:03.359] a feeling this one's going to go more

[00:48:04.560] than an hour, which I'm super down for.

[00:48:07.760] >> Message this. And I apologize for the

[00:48:09.839] live coding. Boom. And now I add this

[00:48:12.960] added trim.

[00:48:14.319] >> Oh, your your audio your audio bell is

[00:48:16.640] is fascinating. I do not have that

[00:48:19.200] turned on.

[00:48:20.319] >> I I use it now because of like cursor

[00:48:22.880] and stuff all the time. Um, so now we

[00:48:24.800] have this we have a truncation message.

[00:48:26.400] Uh, to-do rewrite tools. I didn't modify

[00:48:28.160] at all. They just kind of worked along

[00:48:29.520] the way. Uh, web search. I just used

[00:48:31.760] Excel. I didn't even try. Um, it was

[00:48:35.040] actually really easy to just use Excel.

[00:48:36.480] It was great.

[00:48:37.040] >> They just have a Python SDK. You don't

[00:48:38.720] have to use the MCP or anything. You

[00:48:40.240] just you just launch

[00:48:41.280] >> Python SDK. Don't even think about it.

[00:48:42.800] It's not worth it.

[00:48:44.480] >> And it worked. It was beautifully

[00:48:45.680] worked. And I didn't have to think about

[00:48:46.640] it. Boom. Got the results. Joined it.

[00:48:48.240] Put it in.

[00:48:49.280] >> Uh, again did some more truncation. Uh,

[00:48:52.000] and I can say the same thing again. And

[00:48:54.880] I can again I should do I should

[00:48:56.319] probably do the same thing right over

[00:48:57.520] here too. Uh, and I should really just

[00:48:59.440] make this 5,000. Sick.

[00:49:02.000] Coming up on time, we got another

[00:49:03.599] question.

[00:49:05.520] What do you think about mapping the GP

[00:49:06.960] results to metadata turn one, it shows

[00:49:09.520] file names along with count per year and

[00:49:11.200] tool response and then you search Q?

[00:49:13.680] >> Yeah, I mean you can do a variety of

[00:49:15.680] things to make this better. But I think

[00:49:17.359] the key part that I really want everyone

[00:49:18.960] to take away is what was the difference

[00:49:21.040] here? The bulk of the time that I spent

[00:49:23.119] wasn't actually on tool definitions at

[00:49:25.200] all. almost all uh almost all the time I

[00:49:27.920] spent was actually looking at how the

[00:49:29.119] tools were implemented and like making

[00:49:31.119] sure that it was really really friendly

[00:49:32.640] for an agent. I spent a lot of time I

[00:49:34.960] spent the first I probably spent about

[00:49:36.880] an hour getting the whole thing up and

[00:49:38.400] running. Then I spent another hour

[00:49:41.280] purely getting um uh then I spent

[00:49:44.559] another hour purely doing um basically

[00:49:47.200] UI work to make the UI really good to

[00:49:49.760] iterate on and then once I did that then

[00:49:52.960] I actually add made the tools better. So

[00:49:55.920] that and the reason was because I tried

[00:49:57.599] to make the tools better without making

[00:49:58.800] the UI better and I just couldn't I just

[00:50:00.800] couldn't process the information well

[00:50:02.400] enough about what was going on in the

[00:50:04.800] agent loop to decide like where the

[00:50:06.319] failure cases were.

[00:50:07.839] And once I understood where all the

[00:50:09.280] cases were, then and once I could

[00:50:11.359] actually see and feel the agent, then I

[00:50:14.079] could be like, "Oh, cool. Yes, the LS

[00:50:16.480] tool needs to have dirt and file."

[00:50:19.040] >> Oh, yes. Obviously, the GP tool should

[00:50:21.599] be relative or the the uh the glob tool

[00:50:24.480] should or GP one of those tools should

[00:50:26.720] give the relative directory, not the

[00:50:28.079] full directory. Oh, yes. Obviously, I

[00:50:30.480] need to change my working path and the

[00:50:31.920] system message and make sure the model

[00:50:33.200] knows what directory it's in.

[00:50:35.040] >> You want to see something cool? Um yes,

[00:50:37.520] always.

[00:50:38.160] >> Okay, so um one thing that we found in

[00:50:41.280] digging in uh is like if you're going to

[00:50:43.280] build these agents, it's actually

[00:50:44.400] interesting to see how the coding

[00:50:46.160] harness. So you won't see this if you

[00:50:47.520] run cloud code. Um but in code layer, we

[00:50:50.079] like to actually show you the exact

[00:50:52.079] responses from the agent, not just the

[00:50:54.400] contents of the file.

[00:50:55.920] >> And one thing you'll notice is like I

[00:50:57.200] assumed you didn't do this where you

[00:50:58.480] actually put the line numbers in

[00:51:01.119] >> to the file

[00:51:02.000] >> if Well, I didn't do an I I should

[00:51:03.839] >> Well, it depends on the model, right? So

[00:51:05.440] you this is cloud code and this is like

[00:51:07.200] the benefit you get when you're building

[00:51:08.480] the model and the coding agent harness

[00:51:11.359] is you can RL the model because the

[00:51:13.040] model's going to have to make edits to

[00:51:14.240] this right and so what's useful here is

[00:51:16.400] like you can see when it does this old

[00:51:19.280] string new string it can pick the line

[00:51:21.520] numbers and it can see when it's

[00:51:23.119] navigating or reading or pulling through

[00:51:24.800] the file there's something been done

[00:51:26.880] where these numbers are kind of rled in

[00:51:29.839] such a way that it doesn't have meaning

[00:51:31.839] as a number

[00:51:32.800] >> I think you can do it with any model I

[00:51:34.079] bet if I did this in my For instance,

[00:51:35.280] some GPT models would work. Gemini

[00:51:36.720] models would work on this.

[00:51:38.240] >> I'm sure I'm sure it would work, but I'm

[00:51:40.079] sure if you wanted to like push it push

[00:51:42.000] push the limits of like exactly exactly

[00:51:44.319] what outputs you would want from this.

[00:51:46.559] Um, the training the training would help

[00:51:48.480] to basically like deemphasize the

[00:51:50.720] meaning of these things to ensure that

[00:51:52.559] the weights imply when it's in this

[00:51:54.400] format in this kind of file that it's

[00:51:56.079] line numbers and not any other meaning

[00:51:58.000] of that number. Maybe um maybe um but

[00:52:01.760] like

[00:52:02.079] >> we can only theorize at this point

[00:52:03.440] because it's a closed model but

[00:52:04.960] >> yeah my my hunch says that like most of

[00:52:07.280] these systems probably work just fine

[00:52:08.880] with any model. I think if you take a

[00:52:10.559] model of like equivalent capacity the

[00:52:12.559] key thing that makes a model really good

[00:52:13.920] is how well it understands semantics and

[00:52:16.319] that semantic of like hey this is a line

[00:52:18.240] number not content should be pretty

[00:52:19.760] obvious with the pattern of it

[00:52:21.520] >> even without like any extra training. I

[00:52:23.440] suspect training will get you a little

[00:52:24.960] bit of a boost on top of it, but like as

[00:52:27.359] the models get better and better and

[00:52:28.640] they have more training data, that

[00:52:29.599] probably matters less and less would be

[00:52:31.359] my hunch.

[00:52:33.040] >> Interesting. Yeah, I haven't looked

[00:52:34.160] under the hood at things like Codex and

[00:52:36.000] AMP and see if they use the same format.

[00:52:37.920] But that would be that would be a sim if

[00:52:40.559] you looked at Cotus and how it does file

[00:52:42.319] reads and it didn't have those line

[00:52:43.839] numbers, then that would be a signal to

[00:52:45.839] me that they are being trained

[00:52:47.599] differently as far as like how they

[00:52:49.440] interact with the coding harness itself.

[00:52:51.359] May maybe probably where my my hunch

[00:52:54.000] comes from is that the cursor agent is

[00:52:55.520] pretty good. I don't think it's it's

[00:52:57.119] that much worse than like cloud code or

[00:52:58.800] anything else like all these agents are

[00:53:00.160] roughly the same from my perspective. Um

[00:53:03.040] >> interesting

[00:53:03.839] >> cuz I've been toggling now between like

[00:53:05.359] cursor I've been toggling between codeex

[00:53:06.720] and I've been toggling between um cloud

[00:53:08.720] and I personally don't see a huge uptake

[00:53:10.720] on any one specific agent. I actually

[00:53:12.800] find that the thing that makes the

[00:53:14.079] biggest difference to my efficiency is

[00:53:16.160] actually the UX of how I interface with

[00:53:17.760] these agents, not the actual like

[00:53:21.040] uh context. And I find that like the way

[00:53:22.960] that they implement the tools probably

[00:53:24.400] makes a bigger difference. But because

[00:53:26.640] all the tool calls are basically going

[00:53:28.400] to be sending web API requests anyway,

[00:53:31.760] all of these basically converge on very

[00:53:33.359] similar tool calls because as soon as

[00:53:34.559] one strategy gets discovered as soon as

[00:53:36.000] enthropic discovers that hey we should

[00:53:37.920] do GP in this way, I can promise you

[00:53:40.160] cursor is like we should do GP in this

[00:53:41.839] way and as soon as cursor discovers that

[00:53:43.599] Enthropic is like we should do GP. It

[00:53:44.960] just basically just cycles forever and

[00:53:46.559] this stuff

[00:53:47.200] >> because cursor is using the same models,

[00:53:48.720] right? So they kind of have to take the

[00:53:50.000] lead from anthropic to like figure out

[00:53:51.599] okay here's what

[00:53:52.160] >> I use the Gemini models I use code clog

[00:53:54.000] GBT5 models but what I'm saying is I

[00:53:56.559] think like if I were if I were Codex I

[00:53:58.960] would just watch and I would just have a

[00:54:00.160] harness test that says hey let's just

[00:54:02.800] have a unit test that says anytime the

[00:54:04.480] tool changes in I would just write a

[00:54:06.240] bunch of unit tests that say trigger

[00:54:07.920] these specific tools with these unit

[00:54:09.359] tests observe what is happening

[00:54:12.960] >> for all these tests and anytime the

[00:54:14.480] format changes notify a user on the team

[00:54:16.800] to be like we should look at this the

[00:54:18.559] other agents have changed the format in

[00:54:20.160] some way

[00:54:20.800] >> because it might make a difference.

[00:54:22.559] >> I'll show you another one is if you come

[00:54:24.720] in here and you you we're using the

[00:54:26.480] cloud code harness uh for everything in

[00:54:29.359] code layer. Um and I will zoom in. Thank

[00:54:31.839] you for thank you for the nudge. Um but

[00:54:34.559] um if you go here and you change the

[00:54:36.720] model to a different like if we go use

[00:54:38.880] like um oh I'm going to stop sharing so

[00:54:42.319] I can set my API key real quick. Sorry.

[00:54:45.359] >> Um talking for a second. I I think some

[00:54:47.839] of the models are definitely worse, but

[00:54:49.119] I would try using like OpenAI GBT 5.

[00:54:51.599] >> Uh so that one I don't have right now.

[00:54:54.000] Um but if we go to open router and we

[00:54:56.720] put in our open router API key, I'm just

[00:54:59.920] going to show you what happens if you

[00:55:01.119] use the like a non-cloud code model with

[00:55:04.800] a uh with a with a cloud code harness.

[00:55:09.520] >> Interesting.

[00:55:10.240] >> Go. Let's grab this.

[00:55:14.640] While decks are setting that up, what I

[00:55:16.160] would advise everyone is I actually

[00:55:17.599] wouldn't the reason that I actually am

[00:55:19.280] really bearish on everyone implementing

[00:55:21.280] aic rag and the these live agent systems

[00:55:24.160] is because most people don't have

[00:55:25.599] systems that need to be that broad. Like

[00:55:28.400] while it is kind of nice, your users are

[00:55:30.880] going to be a lot more confused when it

[00:55:32.400] doesn't work. And I only spent 3 hours

[00:55:34.559] making these tools better, but before I

[00:55:36.079] shipped this, I would have to spend a

[00:55:37.280] lot more hours actually trying a bunch

[00:55:39.040] of scenarios on every single type of

[00:55:41.440] system that I built. And there's a lot

[00:55:43.200] of other stuff that is really hard to do

[00:55:44.960] with these systems. For example,

[00:55:46.160] streaming just takes a lot more effort

[00:55:47.440] and engineering time to get right. If

[00:55:49.520] you want to go do like for example

[00:55:52.319] uh while I go what model are you using?

[00:55:54.960] >> This is GPTOSS120B.

[00:55:56.960] >> Okay. Yeah.

[00:55:57.920] >> Much smaller model than Clad or Claude

[00:56:00.079] Sonnet or Clad Opus, but we'll see. It's

[00:56:01.839] also going to be a little bit faster

[00:56:03.040] which is cool.

[00:56:04.559] >> Yeah. So like before you go do any of

[00:56:06.559] this stuff and decide to build a aentic

[00:56:07.920] rag system I personally have found it

[00:56:09.440] very useful to go ahead and build a

[00:56:11.920] regular system without agentic rag and

[00:56:15.920] once you've implemented that then you

[00:56:18.079] can go ahead and then build uh a gentic

[00:56:20.319] rag on top of that because then you have

[00:56:21.599] some sort of expectation and baseline

[00:56:23.040] that you're comparing against and it's

[00:56:25.760] very similar to like a reference

[00:56:26.960] implementation in any sort of software

[00:56:28.720] where you always say like do the

[00:56:31.040] reference implementation every single

[00:56:32.160] time and that I personally find helps

[00:56:34.799] you iterate much faster. It's kind of

[00:56:36.240] similar to an eval loop, but instead of

[00:56:38.000] regular eval, you're just doing AB

[00:56:39.440] comparisons, which is actually what I

[00:56:40.960] think is the more useful thing in these

[00:56:42.799] sort of outcomes.

[00:56:43.520] >> Okay, this GPT OSS appears to be

[00:56:45.680] working. Um,

[00:56:47.280] >> so yeah, you can you can do this for

[00:56:49.119] simple stuff probably.

[00:56:50.640] >> I Yeah, I think it's actually more about

[00:56:52.160] model capability more than specifically

[00:56:53.839] anything. I that's why I said like you

[00:56:55.119] can you can probably swap in any model.

[00:56:56.559] I was actually trying I I did GT5. I did

[00:56:59.599] try the quad models. I tried Sonnet. I

[00:57:01.839] did give it GPD40 nano uh GPD5 nano that

[00:57:05.200] did not work very well

[00:57:08.160] and like it just does it just doesn't

[00:57:09.920] have the capacity I think that like GP5

[00:57:11.920] has uh on the nano models.

[00:57:15.119] >> Yep.

[00:57:16.400] >> Like

[00:57:16.880] >> uh Okay,

[00:57:18.160] >> go ahead.

[00:57:18.640] >> Sorry. Yeah, go ahead. I I was just

[00:57:20.160] Let's just do like two more questions

[00:57:21.280] and then we can call it for the day.

[00:57:23.119] >> Um we've got a couple more questions

[00:57:24.720] here. Let's just identify like where

[00:57:26.240] does RL help here?

[00:57:27.839] >> Um I think the point that Dextro is

[00:57:30.000] making

[00:57:31.520] Econ uh is that if you if you as a model

[00:57:36.160] provider are also building a coding

[00:57:37.599] agent, you can collect special data that

[00:57:40.000] is specifically tied to your tool

[00:57:41.520] implementations and you can actually

[00:57:42.880] post-train the model to favor your

[00:57:47.119] tooling format. So like fundamentally

[00:57:50.400] anytime you're doing fine-tuning or

[00:57:51.680] prompt engineering or context

[00:57:52.880] engineering of any kind, all you're

[00:57:54.000] doing is you're trying to tweak the

[00:57:55.040] weights of the model to do what you want

[00:57:56.240] it to do. with with fine-tuning and

[00:57:59.440] reinforcement learning, you're doing it

[00:58:00.640] at the weight layer. With prompt

[00:58:02.640] engineer and context engineering, you're

[00:58:03.839] doing it by modifying the input tokens.

[00:58:06.160] >> Mhm.

[00:58:06.640] >> So technically, there's a way to go in

[00:58:09.440] RL here without having to change the

[00:58:11.440] prompt again. Say for the static prompt,

[00:58:13.359] make the result better.

[00:58:15.440] >> Yeah. And so like I think if you

[00:58:16.960] probably if you took an open model and

[00:58:18.799] you trained it on this like harness that

[00:58:22.640] you have built your your tools, your web

[00:58:24.799] search, your file reading, all this kind

[00:58:26.319] of stuff and you gave it a bunch of

[00:58:28.000] coding problems, you could probably get

[00:58:30.000] it better at using your specific tools

[00:58:32.799] and in the exact way that they give

[00:58:34.799] their outputs.

[00:58:35.760] >> I mean, let's just do it really fast.

[00:58:37.040] Why not?

[00:58:37.520] >> Mik wants us to do a nano chat episode.

[00:58:39.920] >> The GVD5 Mini is the model name, right?

[00:58:42.799] >> Uh, sure.

[00:58:45.119] I I don't know. Probably.

[00:58:46.640] >> And if this thing runs and I know it's

[00:58:48.079] working. Okay, that seems to work. Cool.

[00:58:51.760] So, we can just see what this does. It's

[00:58:54.000] going to run the same Fern tool as

[00:58:55.280] before. What does a Fern folder do? It

[00:58:58.000] read my to-dos. It was like, okay, cool.

[00:59:00.160] No to-dos. It's going to glob the Fern

[00:59:02.000] folder. And it seems to have produced

[00:59:04.640] something

[00:59:06.400] right over there. Uh, so it did produce

[00:59:08.240] this and is able to understand this. How

[00:59:09.680] do I use Gemini

[00:59:12.400] with BAML? And I think this is again the

[00:59:14.319] thing that Dash always say just like try

[00:59:15.839] it and build your own intuition for

[00:59:17.200] whether or not this works.

[00:59:19.599] >> Um,

[00:59:20.240] >> all right. We're going to make you learn

[00:59:21.359] nano chat for the next episode. It's

[00:59:23.200] been decided.

[00:59:24.079] >> The first thing that I noticed that's

[00:59:25.359] different, by the way, is check out this

[00:59:26.640] GP. See how I did Gemini over here for

[00:59:28.400] the GP tool?

[00:59:30.079] >> When I did my old system, it actually

[00:59:32.160] didn't when I actually did my old GP,

[00:59:34.079] you'll notice the model actually made a

[00:59:35.440] much better grip. It actually came up

[00:59:36.960] with way more turn. So, that's one big

[00:59:39.040] difference that we see right away in the

[00:59:40.640] tiny model versus the small model.

[00:59:43.119] Um, and also it didn't automatically

[00:59:45.280] give me their example. It actually just

[00:59:46.559] dumped out simply an understanding of

[00:59:48.559] what it is, but it didn't actually give

[00:59:49.920] me the example because it didn't

[00:59:51.040] actually trigger the read tool probably.

[00:59:54.000] So that was like another learning I had

[00:59:55.359] when I was going to go do this was just

[00:59:57.040] a really quick understanding of what is

[00:59:58.640] actually happening under the hood. That

[01:00:00.319] said, if we go look at how much this

[01:00:02.240] thing costs, I suspect

[01:00:04.880] >> cheaper.

[01:00:05.359] >> Um, we are going to get very different

[01:00:07.040] cost functions over here.

[01:00:09.680] >> That's still right. we are getting much

[01:00:12.319] much smaller costs and why is this split

[01:00:14.319] uh this is split because the model

[01:00:16.079] changed so the so the data database

[01:00:18.640] actually split on itself automatically

[01:00:21.760] uh because if the type signature of the

[01:00:23.200] model changes then you get two different

[01:00:24.400] data points

[01:00:26.400] uh so when I did the grab like it's just

[01:00:28.079] a lot cheaper and I think I find that to

[01:00:30.400] be interesting to go look at and think

[01:00:32.319] about

[01:00:32.720] >> cool

[01:00:33.599] >> so as always uh try stuff look at what

[01:00:36.000] happened understand it feel the vibes

[01:00:38.079] look at the data understand the accuracy

[01:00:40.000] and the timing and the cost and all of

[01:00:41.599] this and uh you know there's no right

[01:00:44.480] answer. Agentic rag versus deterministic

[01:00:47.359] rag versus a mix of the two versus

[01:00:49.839] reranker pipelines inside your tools.

[01:00:51.839] The answer is like what solves your

[01:00:53.119] user's problem.

[01:00:54.480] >> Do you want to see one last thing while

[01:00:55.760] I'm here? Uh one really interesting

[01:00:57.440] thing that I actually did when I was

[01:00:58.720] running this code.

[01:01:00.559] >> You might enjoy it.

[01:01:02.000] >> Yen says you promised you'd get back to

[01:01:03.839] this eval tool that you showed us.

[01:01:06.240] >> Sorry. Um I'll talk about the code a

[01:01:08.160] little bit more. Bob's building a really

[01:01:09.599] cool evolve tool over at BAML and he's

[01:01:11.520] embarrassed to talk about it cuz it's

[01:01:13.440] it's really dope.

[01:01:14.880] >> It's not ready yet. But um the whole

[01:01:17.599] point of this is when I did the Asian

[01:01:19.440] loop, there's a couple of different

[01:01:20.400] things that happen. Sometimes the model

[01:01:21.680] didn't respond to tools. Um but if you

[01:01:24.000] notice my actual prompt that I actually

[01:01:25.440] sent to the model,

[01:01:27.839] uh let me render this again so you can

[01:01:29.200] actually go read the full prompt. Like

[01:01:30.559] the actual prompt that I sent to the

[01:01:31.920] model, the way that I render tools, I

[01:01:33.440] did a bit of context engineering. I

[01:01:34.640] don't actually render tools the right

[01:01:35.520] way. I actually render them this way.

[01:01:36.559] It's like to-do read, here's no to-dos.

[01:01:38.960] Then I actually render the tool again. I

[01:01:40.400] say clob and then here's the actual tool

[01:01:42.240] response. So I actually render the tools

[01:01:44.000] in a very trivial way rather than with

[01:01:45.839] pure JSON because again it's like I

[01:01:47.359] don't want to render JSON and stuff in

[01:01:48.720] the tool pattern. I want to dump it in

[01:01:50.000] as a part of the context message. But

[01:01:52.240] every now and then the model would

[01:01:53.520] actually reply with like a similar kind

[01:01:56.160] of reply where it just would say like oh

[01:01:58.559] here's the here's a tool that I want. In

[01:02:01.680] that scenario, I would actually want the

[01:02:04.240] model to know even if it replied in that

[01:02:05.760] way, I want to be very explicit and tell

[01:02:07.359] the model it's like invalid response,

[01:02:09.359] you must respond with one of the types.

[01:02:11.440] So the model knows that hey, this is

[01:02:13.040] invalid and I actually hide this from

[01:02:14.319] the user. So the user will never see

[01:02:15.680] this. Similarly, sometimes the model

[01:02:17.920] will not reply with the reply to user

[01:02:19.599] tool. It won't actually reply with this

[01:02:21.200] structure. In that scenario, I actually

[01:02:23.440] do a couple trivial checks. I'm like,

[01:02:25.040] hey, if the model responds with a J with

[01:02:26.960] back to JSON and doesn't start a curly

[01:02:28.640] brace or um or this, then the model

[01:02:31.440] probably was trying to reply to the

[01:02:32.880] user. It just messed up. So rather than

[01:02:34.160] doing a retry, I just take that

[01:02:35.359] assumption. What does that look like in

[01:02:37.200] practice? Is like some of these parsing

[01:02:38.720] failures that you see over here.

[01:02:41.119] I'll show it. Yeah, like this one. This

[01:02:43.200] is a parsing failure because the model

[01:02:44.720] actually responded like this. It said it

[01:02:47.599] just responded plain text. And that's

[01:02:50.160] okay because the model responded plain

[01:02:51.920] text. What I do is I just say, "Oh, if

[01:02:53.839] you're running in plain text and you're

[01:02:55.040] not starting with a curly or this or

[01:02:57.040] like tool something, then it's probably

[01:02:59.520] right." So just send take it as a reply

[01:03:01.040] to the user and just assume that the

[01:03:02.559] model meant the reply here.

[01:03:03.839] >> The model was just like too small and

[01:03:05.599] dumb to follow the explicit instructions

[01:03:07.440] of like here's the entire

[01:03:08.960] >> context window got really big. So like

[01:03:10.319] sometimes you'll see like a cursor gives

[01:03:11.839] this error message. I saw this yesterday

[01:03:13.280] where it's like the tool format wasn't

[01:03:14.960] correct. It's like you can just patch

[01:03:16.240] this really trivially. This is what I

[01:03:17.520] mean by implementing your tools can make

[01:03:18.799] a huge difference in some ways. getting

[01:03:20.720] what tool to use is another tool of its

[01:03:22.880] sort. So the way I implemented it was a

[01:03:25.119] little bit smarter basically where it's

[01:03:27.119] like if the model was trying to go do

[01:03:28.559] something and it didn't exactly obey it,

[01:03:30.160] I would just like recognize that it's

[01:03:31.839] trying to do that and just like let it

[01:03:33.359] keep going with that assumption. The

[01:03:35.520] other thing I did was I said in the case

[01:03:37.839] of it actually run turning an inval if

[01:03:39.839] again if it parse if it was a parsing

[01:03:41.839] failure rather than taking the exception

[01:03:43.520] and dumping it in directly I actually

[01:03:46.079] again made a slightly prettier error

[01:03:48.480] message that says return an invalid

[01:03:50.000] response dump the response I said must

[01:03:51.599] be one of the types specified and with

[01:03:53.119] that the model was able to go and fix

[01:03:54.640] almost every bug and I never had any

[01:03:56.400] more issues with the model not obeying

[01:03:58.559] tool calls and I I put max retries three

[01:04:01.599] I only ever really took one and what's

[01:04:03.599] really important here is that this these

[01:04:05.920] temporary states are actually temporary

[01:04:07.839] states. They never go into the pure

[01:04:09.839] state array of the of the final agent.

[01:04:12.640] >> Uh so you put the feedback in, you let

[01:04:14.240] the model correct itself, but then that

[01:04:16.000] doesn't stay in the context window.

[01:04:17.760] >> Exactly. And this was also really

[01:04:19.440] important to making this work.

[01:04:21.039] >> Yeah. And that's the other trade-off,

[01:04:22.400] right? The manis folks are big on like

[01:04:23.920] leave the errors in so it doesn't make

[01:04:25.280] the same mistake again. But I think I

[01:04:27.119] think you you were vibing with it and

[01:04:28.799] you found what worked and and and this

[01:04:30.799] was the thing that you wanted to do to

[01:04:32.480] get the right results. Exactly. And the

[01:04:34.640] model just doesn't make this message

[01:04:36.480] make this type of error very often. So

[01:04:38.640] because it doesn't make this kind of

[01:04:39.920] error very often, it's not worth

[01:04:41.839] breaking, if that makes sense.

[01:04:45.440] >> And you and you've proven that this

[01:04:46.960] reliably fixes it. So like it's not

[01:04:49.200] really actually that expensive to drop

[01:04:51.520] this in and then rip it back out because

[01:04:53.520] >> I sent it to the full agent loop as a

[01:04:55.599] whole just in case it made a different

[01:04:57.039] error message. But I could have sent it

[01:04:58.480] to a more trivial function that only job

[01:05:00.640] is to fix it.

[01:05:02.720] I just didn't want to risk it, so I just

[01:05:03.920] send it to the full agent loop.

[01:05:06.079] >> A look under the hood at how to best

[01:05:08.400] build AI AI pipelines and AI agents.

[01:05:10.960] This has been a really fun episode.

[01:05:12.240] >> Yeah, this whole thing is going to be

[01:05:13.520] live. Uh you will be able to just run UV

[01:05:15.839] install and UV run sync and just run it.

[01:05:18.400] Um it was a ton of fun to build and

[01:05:22.160] while this was really really fun, I

[01:05:24.319] would highly highly highly recommend

[01:05:26.400] that every single one of you like

[01:05:28.400] actually go build something like this.

[01:05:30.079] you will learn so much by writing the

[01:05:32.319] code and I like I always had an

[01:05:34.960] intuition that aentic rag was uh pretty

[01:05:37.680] cool. Uh but I didn't think I realized

[01:05:40.079] how

[01:05:41.839] how interesting it is for different

[01:05:43.680] product surface areas for certain kinds

[01:05:45.200] of things that I could never build

[01:05:46.400] without it. So our Bammy chat agent what

[01:05:48.799] I actually plan on doing is actually

[01:05:50.960] plan on giving it a way to go abort out

[01:05:53.440] of its main rag pipeline so it can go

[01:05:55.920] into an agentic loop. The problem I have

[01:05:58.400] with agentic loop is that it's just

[01:06:00.559] super freaking slow. I just don't want a

[01:06:04.079] system to be that slow. And for that

[01:06:06.640] reason alone, I'm going to keep the

[01:06:08.640] deterministic rag pipeline because it's

[01:06:10.240] way faster. But every now and then,

[01:06:12.240] someone will ask it a question like,

[01:06:13.520] "Hey, how does this work?" And I want a

[01:06:15.920] way to go trigger it into an agentic rag

[01:06:17.920] pipeline. And the answer to that might

[01:06:20.640] be there might be a button in the UI

[01:06:22.240] that we build at the very bottom that

[01:06:24.880] says something like uh let me clean my

[01:06:28.480] window again. There might be something

[01:06:30.160] here in here that says oh does this look

[01:06:33.440] wrong to you? And I might put a button

[01:06:34.880] here that says does this look wrong? And

[01:06:37.359] if you press it it will actually trigger

[01:06:38.880] the aentic rag system instead of the

[01:06:40.400] main rag system. And that's a way for me

[01:06:42.799] to opt into this without doing it all

[01:06:44.640] the time and design it in a really nice

[01:06:46.319] way. This is the same thing as you're

[01:06:48.240] like, "Hey, look, we have a really tight

[01:06:50.720] specific model that does 20 kinds of

[01:06:53.200] classification." And then if the model

[01:06:54.799] selects other or the user says it's

[01:06:56.799] wrong, then you go to the big slow

[01:06:58.720] expensive LLM to try to solve it.

[01:07:01.119] >> Imagine imagine you're on this doc site

[01:07:02.880] and you ask how to do this and it takes

[01:07:04.079] you like you saw how long the other

[01:07:05.440] system took. It's better, but it's

[01:07:07.039] slower.

[01:07:08.799] I just don't want that for here. And

[01:07:10.400] like coding is different because in a

[01:07:11.920] coding, why does why do coding agents

[01:07:14.079] tolerate this kind of UX? Well, it's

[01:07:16.240] because like the cost of me typing the

[01:07:17.680] code is always long. It's always long.

[01:07:20.880] So, it doesn't matter how long it takes

[01:07:22.400] because it's always going to be faster

[01:07:23.520] than me writing the code.

[01:07:25.280] >> Hey, Ken, you want to do something fun?

[01:07:27.920] >> Do you want to paste the research

[01:07:29.200] codebase prompt into your coding agent

[01:07:31.520] and see what happens?

[01:07:33.440] >> My cloud code agent?

[01:07:35.359] >> Your no your CLI agent that you wrote.

[01:07:37.920] Take the take the research codebase

[01:07:39.760] prompt that we use for uh working with

[01:07:41.680] Claude.

[01:07:42.240] >> That's actually really fun. And just see

[01:07:43.760] if it works

[01:07:44.720] >> here. I'll put it in the chat here.

[01:07:46.720] >> Um, before I do that, I will take two

[01:07:48.640] seconds and show you guys how this thing

[01:07:50.000] works if you guys are curious.

[01:07:51.680] >> Um, I think one of the key premises that

[01:07:53.520] we had when we started this thing was

[01:07:54.799] just I think it's important that people

[01:07:56.480] should be able to see their code really

[01:07:57.920] easily. So like one of the things that

[01:07:59.280] we started with is just we just like

[01:08:00.559] types. So we just store all your type

[01:08:02.960] systems into the codebase and then you

[01:08:05.039] can see your state messages and this is

[01:08:06.400] a rendering bug because you can actually

[01:08:09.200] turn this system into a quick little

[01:08:11.039] test case that you can run locally

[01:08:12.720] really really really fast. So, like if I

[01:08:14.559] for whatever reason that agent wasn't

[01:08:16.239] working, boom, I can just put this test

[01:08:18.480] case over here. And now I think there's

[01:08:21.920] some bug.

[01:08:22.400] >> Now you have an eval of like, hey,

[01:08:23.839] here's a long context. Can we get it to

[01:08:25.679] still spit out the right answer even

[01:08:27.040] with this long context?

[01:08:28.319] >> Exactly. And then I can just build this

[01:08:29.600] eval out really easily. And there's some

[01:08:30.960] small stuff that I have to do uh in this

[01:08:33.199] syntax like get rid of these commas.

[01:08:36.159] But we're working on this and making

[01:08:37.359] this better. So as soon as this is live,

[01:08:39.199] we'll share it out. But one of the key

[01:08:40.960] parts that we really wanted was just a

[01:08:42.319] really easy way to understand how type

[01:08:44.080] system work. Uh you want to be able to

[01:08:46.000] see like the raw web requests that the

[01:08:47.359] model actually made and make it super

[01:08:48.560] easy for you to go see. So if it did

[01:08:49.920] like reasoning of any kind, you should

[01:08:51.600] just be able to see that trivially.

[01:08:53.679] >> Cool.

[01:08:54.239] >> You should be able to see network

[01:08:55.199] requests, see timings, and everything

[01:08:56.799] else on here. So like this took 60. That

[01:08:58.799] looks wrong.

[01:08:59.759] >> It's cuz you busted the cache, dude. Or

[01:09:02.000] there's a bug.

[01:09:02.640] >> No, that that's a bug. This is why this

[01:09:04.880] isn't ready yet. We're just doing like a

[01:09:06.159] quick few things on the type system. And

[01:09:07.759] like one of the coolest things that we

[01:09:08.960] really worked on was if you change the

[01:09:10.960] type signature of any kind or you change

[01:09:12.880] like the model or something else, the

[01:09:14.239] data gets split out automatically for

[01:09:15.759] you. So in this in this scenario that we

[01:09:17.920] changed the model. So you notice that

[01:09:19.600] there's two agent loops. One for model

[01:09:21.440] A, one for the GD5 mini models and the

[01:09:25.279] other one for the GD5 model that we had

[01:09:27.520] here. And this kind of happens without

[01:09:28.880] you having to think about it. So your

[01:09:30.239] data is extremely clean is the premise.

[01:09:32.799] And obviously stuff

[01:09:35.600] >> had a really good summary of this. Let's

[01:09:37.120] do the thing.

[01:09:37.600] >> You want to paste it in. All right. I

[01:09:38.799] put it in the in the chat if you want to

[01:09:40.480] grab it.

[01:09:41.279] >> Where? In the chat. In Riverside.

[01:09:42.960] >> You scroll up like four messages in

[01:09:44.400] Riverside.

[01:09:45.279] >> I see it. I'm going to take this.

[01:09:46.400] >> Paste it in. See what happens. I don't

[01:09:47.679] think you you don't have a right file

[01:09:49.040] tool, so it might not actually uh

[01:09:51.920] >> it might not actually write the file,

[01:09:53.040] but it will probably print it out to

[01:09:54.320] you.

[01:09:55.360] >> So, I've copied the codebase. Sorry, I

[01:09:56.719] had to not screen share just in case I

[01:09:59.280] showed something that I shouldn't.

[01:10:01.600] Um, so let's go run this over here. What

[01:10:04.480] we're going to do is we're going to do

[01:10:05.760] two ti uh when we do this.

[01:10:07.360] >> No, I mean just paste it into the CLI.

[01:10:09.120] Oh, you're going to give it the edit

[01:10:10.080] tool.

[01:10:10.560] >> Of course.

[01:10:12.239] >> Uh so you want the right tool then cuz

[01:10:13.840] it's going to write a Oh, yeah. There

[01:10:14.960] you go. Okay.

[01:10:15.360] >> I'll give it all the scary tools. Screw

[01:10:16.800] it.

[01:10:17.199] >> Ship it.

[01:10:18.480] >> Yeah, I guess

[01:10:19.520] >> you already gave it bash.

[01:10:21.360] >> Yeah, basically.

[01:10:22.800] >> You're going to have to like cat that

[01:10:25.280] thing.

[01:10:25.840] >> No, no, no, no. I I have I have You

[01:10:27.600] don't have to do that. It just starts.

[01:10:28.880] Can I not? Okay. Well, that's not going

[01:10:30.640] to work.

[01:10:32.080] Um, I did not build command V into here.

[01:10:34.880] Uh, let me run this again.

[01:10:37.840] >> Oh, you can't paste.

[01:10:39.600] >> No, I did not build command V into

[01:10:41.520] there.

[01:10:42.400] >> All right,

[01:10:44.239] there might be quotes in here. So, you

[01:10:47.280] will have to use I think try single

[01:10:49.360] quotes around it instead.

[01:10:50.880] >> Okay, let me try. Sorry, guys. This is a

[01:10:53.199] live demo.

[01:10:53.840] >> I'm putting Vib on the spot.

[01:10:56.000] >> Okay, I'm

[01:10:56.960] >> think there's any single quotes.

[01:10:58.320] >> Okay,

[01:10:59.280] >> unless there's like punctuation. What

[01:11:01.520] does the fern folder do there?

[01:11:05.120] >> Didn't like that. All right, we'll try

[01:11:06.960] this later. We can put up a clip of it.

[01:11:08.640] All right, we'll try one more. I think

[01:11:10.080] there's punctuation. You got to do like

[01:11:12.080] cat out of eof or whatever.

[01:11:16.080] >> Here. You know what you got to do is uh

[01:11:18.080] it's dash I

[01:11:20.640] >> dash I What do you want me to do? I

[01:11:22.480] >> I'm going to put it in I'm going to put

[01:11:23.520] in the chat here. make this

[01:11:25.679] >> welcome to the uh

[01:11:27.679] >> into uh terminal within single quote.

[01:11:31.040] >> You just got to give it the path to

[01:11:32.400] that.

[01:11:32.800] >> I'll just see what this does. This might

[01:11:34.320] work.

[01:11:35.280] >> Okay.

[01:11:36.960] >> Um

[01:11:37.440] >> No, you're just going to remove all the

[01:11:38.640] single quotes.

[01:11:39.600] >> I don't know. Um probably.

[01:11:41.360] >> Oh, yeah. You could put in a file and

[01:11:42.640] then just make it read the file. Nope.

[01:11:45.040] Wrong.

[01:11:46.080] >> No. What did it do? No.

[01:11:47.840] >> Just save the file and then give it the

[01:11:49.280] path to the file.

[01:11:50.640] >> I haven't built that.

[01:11:52.960] Oh, it can't read a file.

[01:11:54.480] >> Yeah, it's Oh, maybe it can. Um Oh,

[01:11:58.080] maybe. Oh, I didn't think about that.

[01:11:59.280] That's a good idea. Uh I'm dumb. MD.

[01:12:01.920] Okay, cool. Let's run this. Uh I think

[01:12:04.480] this will work.

[01:12:06.000] >> Yeah. Okay. So, just tell to read

[01:12:08.960] research.m MD.

[01:12:10.239] >> Okay. Read research.m

[01:12:13.840] MD. Then uh then figure then use that to

[01:12:20.320] learn what the fern directory does.

[01:12:24.960] >> I have no idea what's going to happen.

[01:12:26.400] >> See what's up. This is like a full like

[01:12:29.040] curses toy. So when you resize the

[01:12:31.120] window, it doesn't rerender.

[01:12:32.960] >> It does eventually. Okay. So it did read

[01:12:35.760] research MD. Did it not find it? I I

[01:12:38.159] spelled it wrong. Okay. It's going to ls

[01:12:40.320] and then it'll run again. Oh shoot.

[01:12:43.679] Sorry.

[01:12:45.360] Uh, my interruption was not built

[01:12:46.960] perfectly. It was correct.

[01:12:49.440] Read research.m

[01:12:52.640] MD then uh, learn what the fern.

[01:12:59.679] Yeah, it only rerenders every few loops.

[01:13:01.360] This is what I meant. The hardest part

[01:13:02.400] about building this whole system is

[01:13:03.760] actually not the agent loop. It's

[01:13:05.199] actually all the tooling around it. So,

[01:13:06.560] like making this UI really good actually

[01:13:08.239] took way more than I found. And like you

[01:13:09.520] saw that it's kind of cool. Like I made

[01:13:10.719] a to-do. Um, and like it's just going to

[01:13:12.640] go build this out. But like having the

[01:13:14.400] UI in influence was actually really

[01:13:16.800] really hard. So we'll just see if the

[01:13:19.199] cloud code prompt works.

[01:13:20.719] >> Is this rich or typer or what is you

[01:13:23.040] what is your UI framework?

[01:13:24.640] >> I have no idea. This is cursor picked

[01:13:26.320] one.

[01:13:26.640] >> Updated the to-dos.

[01:13:28.080] >> Yep. And eventually it'll rerender. I

[01:13:30.719] think uh maybe that's a bug in the to-do

[01:13:32.480] implementation.

[01:13:33.840] >> This is also going to prompt it to use

[01:13:35.199] sub aents. We'll see if it actually

[01:13:36.640] launches sub agents. I don't know how

[01:13:38.320] your sub aent UI looks. It just it will

[01:13:41.120] trigger a sub agent. It'll show you. It

[01:13:42.719] should be very obvious if it's

[01:13:43.600] triggering a sub agent. Did you call it?

[01:13:45.600] It should call a sub agent. If it

[01:13:47.120] didn't, I mean, we can see if it did or

[01:13:48.960] not.

[01:13:50.080] >> You had a reply. It just said it read

[01:13:51.920] that file path. Are you still using GPT5

[01:13:54.640] Mini?

[01:13:55.280] >> Yeah, I am.

[01:13:56.320] >> Yeah. So, that's just not going to work.

[01:13:58.080] There's too many instructions. Yeah.

[01:13:59.600] See, it returned with tool colon.

[01:14:02.320] >> Yeah. Yeah, exactly. Oh, that's because

[01:14:04.400] my freaking loop was not good. Uh, I had

[01:14:06.880] another bug over here. Uh,

[01:14:08.880] >> yeah. This it looks like this block

[01:14:10.400] didn't get hit.

[01:14:11.199] >> There you go. This one, too. I need

[01:14:12.560] both.

[01:14:13.360] >> All right.

[01:14:15.679] >> As you guys can see, this is a very,

[01:14:17.440] very, very, very live demo. I did a

[01:14:20.880] couple things. I swapped the model and I

[01:14:23.040] returned and I also added that edge case

[01:14:26.960] over here.

[01:14:27.520] >> There's no way you're going to get GBT 5

[01:14:29.600] mini to be able to to to do research

[01:14:32.320] like that. Did you switch it back to

[01:14:33.679] main?

[01:14:34.239] >> I did.

[01:14:35.199] >> Okay, cool. All right. And then in four

[01:14:38.400] minutes, we're going to call this

[01:14:39.440] episode for real because I know we both

[01:14:40.960] have we both have companies to build.

[01:14:42.880] >> So, it did build the to-dos. That's kind

[01:14:44.800] of cool. I think I just don't have a

[01:14:47.280] good UI for to-dos. There's some syncing

[01:14:49.040] issue that I have in my UI.

[01:14:50.800] >> Did you know that Claude removed the

[01:14:52.560] to-do read tool because they they had

[01:14:54.719] found that like the model was trained

[01:14:56.239] well enough to just reinforce itself

[01:14:57.920] with to-do write and it doesn't have to

[01:14:59.600] be able to read its own to-dos.

[01:15:01.679] >> Interesting.

[01:15:03.280] >> Um

[01:15:03.679] >> that might be it. So another thing to

[01:15:05.679] notice is that one of the things that

[01:15:06.960] cloud code does is you'll notice that it

[01:15:08.719] sends you error messages and how it

[01:15:10.000] keeps state. So like if you try and

[01:15:12.080] write to a file that you have not read

[01:15:13.600] yet, it forces it to read the file first

[01:15:16.400] >> before it does that. That's another kind

[01:15:18.719] of thing that you can do over here.

[01:15:20.239] Cloud code also keeps track of what

[01:15:22.000] files have been modified.

[01:15:25.520] >> It like hashes it every time you read

[01:15:27.440] it. And if you try to write it since the

[01:15:29.440] last time you wrote it or read it, then

[01:15:31.520] you don't get to

[01:15:32.239] >> exly and it basically will say, "Oh, the

[01:15:33.679] file has changed since you last read it.

[01:15:35.040] Read the file again." And it actually

[01:15:36.640] does a lot of work in that world to make

[01:15:38.560] that easier.

[01:15:39.440] >> It's same with context engineering

[01:15:40.719] around how you keep like file iteration.

[01:15:42.239] So like for example, one of our past

[01:15:44.000] episodes were about dynamic memory and

[01:15:46.719] like I think the person in that episode

[01:15:48.320] or perhaps the episode after that was

[01:15:49.760] talking about how like if you read the

[01:15:51.600] same file five times, you probably don't

[01:15:54.000] need to keep all five versions of the

[01:15:55.679] file in the in the actual history of

[01:15:57.920] what you're showing off. You probably

[01:15:59.120] can show a different variation of it. So

[01:16:00.640] like there's ways to manipulate the

[01:16:02.000] context window historically and show a

[01:16:04.159] different thing based on what your

[01:16:05.360] current state representation is. And I

[01:16:07.600] think having that idea is personally

[01:16:09.520] like very useful.

[01:16:11.199] >> Yeah. I mean, I think a lot of people

[01:16:12.560] have been talking about like, hey, look,

[01:16:14.000] like small context gets better results.

[01:16:15.920] And people would rather just like be

[01:16:17.760] constantly mutating the context window

[01:16:19.600] to make it smaller and more compact than

[01:16:21.760] lean on like even if it breaks the

[01:16:23.440] cache, it just like I'd rather have that

[01:16:25.760] cloud code do that thing where it's like

[01:16:27.760] it will file reads from 10 turns ago

[01:16:30.480] basically get condensed down into like,

[01:16:32.159] hey, you read this file and here's what

[01:16:33.520] happened versus like the fullon like

[01:16:35.840] every single file we've read being

[01:16:37.520] sitting in the context window.

[01:16:38.960] >> That's cool. So, it made the to-dos and

[01:16:40.560] now it finished reading that one and now

[01:16:42.159] it's locating the fern folder. Um, and

[01:16:44.320] then it should

[01:16:45.679] >> 17 already.

[01:16:47.360] >> This is the problem with the aentic rag

[01:16:48.880] systems is like while they might work in

[01:16:50.880] the end, they are really really

[01:16:52.000] unbounded and how many times they work

[01:16:53.760] and like I have no idea why it's calling

[01:16:55.199] to-do right and to-do right over and

[01:16:56.719] over again. Um, I'd have to like debug

[01:16:59.280] that slightly better. So, like if I go

[01:17:00.640] look into this like why is it doing

[01:17:02.000] this?

[01:17:02.560] >> You should just get rid of the to-do

[01:17:03.920] tool. I think to-do lists are silly. You

[01:17:06.000] should just not have along you should

[01:17:07.520] you should not give a model enough tasks

[01:17:09.199] that it needs a to-do list. You should

[01:17:10.640] just use fresh context all the time.

[01:17:12.719] >> Why is it? Oh, it's because it's doing

[01:17:14.320] like globs and stuff like along the way.

[01:17:16.560] And then it did a spam of to-dos.

[01:17:18.719] >> Oh, it's just not showing those in the

[01:17:21.679] >> Yeah, it's just not showing them in the

[01:17:22.800] UI. And this is again why I like this.

[01:17:24.480] It's like I can actually go see what

[01:17:25.600] it's doing. Like why is it globing? It's

[01:17:26.880] like infern. Okay, cool. That makes

[01:17:28.560] sense. And like why is it writing to-do,

[01:17:31.440] right? It's probably because there's

[01:17:32.320] some bug in my to-do rendering. like

[01:17:33.840] whatever bug is causing this to not

[01:17:35.440] render here. It's probably the same bug

[01:17:37.199] that is causing the model to go do this

[01:17:38.880] and like and like not

[01:17:40.560] >> it is slowly making progress though.

[01:17:42.480] >> It is. And I think it will make progress

[01:17:44.159] like it actually added a lot more docs

[01:17:46.480] into like what the to-do is based on

[01:17:48.640] this. And like why is doing a to-do read

[01:17:50.640] every single time? I have no idea.

[01:17:51.920] >> Yeah.

[01:17:52.640] >> Um sick.

[01:17:53.440] >> I have I should probably figure this out

[01:17:54.960] and get this working a little bit more

[01:17:56.400] fully. But if someone wants to go play

[01:17:57.920] around with this and gets the to-do app

[01:17:59.440] actually working, I think that'd be

[01:18:01.040] super worth it for someone to go pursue

[01:18:02.480] and think about. about how can you make

[01:18:03.840] this system uh to do and figure out what

[01:18:07.040] the bug is yours. I think it's like a

[01:18:08.239] cursor bug to be honest.

[01:18:09.280] >> Apache 2 license, go steal Vibbop's code

[01:18:11.440] and turn it into a company.

[01:18:13.199] >> Yeah, go do that. I don't care. Yeah,

[01:18:14.719] this is a great do. If you make if you

[01:18:16.800] if you make a business doing this, I'd

[01:18:18.159] be so happy for you.

[01:18:19.840] >> Amazing. All right, this was a super fun

[01:18:21.600] episode. Uh biggest takeaway, I think

[01:18:23.679] we've already said it, um but is

[01:18:26.880] basically a rag, deterministic rag, it's

[01:18:29.360] all balance. It's all solving problems

[01:18:30.800] for your users. Make sure you actually

[01:18:32.400] have a real use case to build against

[01:18:34.239] and uh engineer the right amount of

[01:18:36.159] things in the right places in the right

[01:18:37.840] way.

[01:18:39.040] >> Yeah. Uh just write a [ __ ] ton of code

[01:18:41.679] and you will probably get better at

[01:18:43.120] building this kind of system.

[01:18:44.960] >> Amazing.

[01:18:45.440] >> Um

[01:18:46.480] >> cool. Thank you.

[01:18:47.840] >> Next episode, Tuesday, 10 a.m. Pacific.

[01:18:50.239] We'll see you there.

[01:18:51.199] >> All right. See you.

[01:18:52.239] >> All right, fam. Take care. Tip.
