# No Vibes Allowed - Live Coding with AI Agents



Source: YouTube captions (automatic:en)



[00:00:01.750] iz that people can't actually join the

[00:00:01.760] stream.

[00:00:04.080] >> Um, so if you have the

[00:00:06.000] >> I'm going to set up the I'm going to set

[00:00:07.440] up the link

[00:00:08.400] >> or just Yeah, just shoot me the public

[00:00:10.160] link so I can drop it in chat. Um, hey

[00:00:12.880] everybody, we're live. We're going to do

[00:00:15.040] some very fun live coding today. Uh, and

[00:00:18.000] this is an episode I've been wanting to

[00:00:19.439] do for a very, very long time. So, I'm

[00:00:21.520] very stoked to be here and uh I can't

[00:00:24.080] wait to write some code and uh get

[00:00:27.199] yelled at by by Vivov.

[00:00:29.840] >> All right, event is updated.

[00:00:32.480] >> Um I sent them to you as well. We've got

[00:00:34.399] some people in the chat and we should

[00:00:36.000] get a few more coming too. What kind of

[00:00:38.559] hard features are we building today? We

[00:00:40.239] will get to this in just a second.

[00:00:43.280] But this is um like Dexter said, I think

[00:00:46.320] a lot of people underestimate how good

[00:00:48.320] bite coding can be. Uh and a lot of

[00:00:50.000] people view it as like it's great for

[00:00:51.680] throwaway code. It's great for stuff

[00:00:53.440] that we don't really leverage for a lot

[00:00:56.800] of situations,

[00:00:58.480] but I think I've been convinced

[00:00:59.840] otherwise. I've been convinced that you

[00:01:01.680] can use uh coding agents for really

[00:01:04.479] really hard problems in a maintainable

[00:01:06.159] way. So we're going to try that today

[00:01:08.479] live on stream for a problem that has

[00:01:10.880] been aching us for a while. in BAML. And

[00:01:14.640] obviously I know the BAML codebase

[00:01:16.320] really well, but Dexter has no idea what

[00:01:19.840] the BML codebases.

[00:01:21.520] >> Well, we did ship one feature a couple

[00:01:23.600] months ago, but you were driving almost

[00:01:25.439] all of that. So

[00:01:26.799] >> yeah. Uh but even then, like the fact

[00:01:28.400] that Dexter really doesn't know the file

[00:01:29.840] system. He doesn't really know how we

[00:01:31.119] organize code in there. He doesn't

[00:01:32.720] >> I don't know how to run the tests.

[00:01:34.079] >> You don't know how to run the test.

[00:01:35.200] There's a lot. Do you know how to run

[00:01:36.159] the tests?

[00:01:37.360] >> I mean, Claude knows how to run the

[00:01:38.640] tests.

[00:01:39.280] >> Yeah. But the point here is like Dexter

[00:01:41.119] really has almost no information about

[00:01:42.479] what the real system does over here. So

[00:01:45.439] I think a big part of today is going to

[00:01:47.360] be to see if we can go from nothing to

[00:01:49.680] something from scratch. Um but for

[00:01:53.040] everyone that's tuning in um one of the

[00:01:55.840] whole this is a thing that we do every

[00:01:57.759] Tuesday. We call it AI that works and

[00:01:59.600] the whole point is to show shipping

[00:02:00.960] workflows that actually leverage AI in

[00:02:03.520] some interesting way whether it's to

[00:02:04.719] build pipelines talk about how to the

[00:02:06.479] method of building the pipelines or

[00:02:07.759] actually the pipelines themselves but

[00:02:09.679] show real mechanisms for actually

[00:02:11.280] leveraging AI. My name is Fibof. I work

[00:02:13.680] on BAML.

[00:02:15.440] >> My name is Dex. I work on uh code. Oh,

[00:02:18.239] sorry. Do you want to finish the the

[00:02:19.360] oneliner?

[00:02:20.239] >> No, that's it.

[00:02:21.200] >> BAML is a great programming language for

[00:02:23.120] working with uh LLMs and AI agents. Uh,

[00:02:26.239] and it's getting cooler and cooler and

[00:02:29.200] uh, weirder and weirder as as the days

[00:02:31.599] go by. I'm very excited to see uh, what

[00:02:34.000] y'all are solving soon. Uh, I'm Dex. I

[00:02:36.239] work on human layer

[00:02:38.080] >> and

[00:02:38.480] >> this is the part where you tell people

[00:02:40.000] how why

[00:02:41.840] >> I mean I think actually people are going

[00:02:44.640] to get to see it. So rather than talking

[00:02:46.239] about it, I think it's going to be a

[00:02:47.360] really interesting way to just mechanize

[00:02:48.720] how we how you can work with the coding

[00:02:50.720] in in in an interesting way. If you find

[00:02:53.599] this stuff interesting, this is the URL

[00:02:55.360] that you can usually sign up for to see

[00:02:56.720] our Tuesday events. And if you sign up

[00:02:58.879] there, you can subscribe and we'll send

[00:03:00.160] you event invites out every single time.

[00:03:02.959] But with that, let's get started.

[00:03:05.599] >> Um, cool. Uh, I'm going to pull up uh

[00:03:09.120] I'm going to share my screen.

[00:03:11.920] >> Why don't we start with just showing the

[00:03:13.360] problem up front so then people can get

[00:03:14.879] a spec for what we expect to get done

[00:03:16.640] today.

[00:03:17.680] >> Yeah. So right before this, literally

[00:03:20.480] right before this call, I messaged

[00:03:22.000] Dexter a couple of tickets that we want

[00:03:24.319] to get solved. This is a specific ticket

[00:03:26.000] which is in BAML. One of the things that

[00:03:27.519] you can do is you can configure any LLM

[00:03:29.200] you want and with to with retry policies

[00:03:31.200] and all sorts of mechanisms.

[00:03:33.680] Now one thing that a lot of people have

[00:03:35.920] been asking for is timeouts. Uh so we

[00:03:38.319] want to expose that capability so that

[00:03:40.000] users can configure timeouts for uh for

[00:03:43.040] themselves.

[00:03:44.720] As a part of this work, we started

[00:03:46.159] thinking about it. So there's a GitHub

[00:03:47.280] issue that we started with. Then we

[00:03:48.480] spent some other time thinking about the

[00:03:49.599] actual syntax and stuff along the way.

[00:03:52.319] But once we realized what the syntax and

[00:03:54.000] everything was for timeouts, I kind of

[00:03:56.159] just shared all the information with

[00:03:57.280] Dex. And Dex, if you want to screen

[00:03:58.640] share and just show people what I showed

[00:04:00.000] you. Let's start with the GitHub issue

[00:04:02.480] and then from there we can work through

[00:04:04.319] to the docs that we have.

[00:04:06.879] And for context for everyone watching,

[00:04:08.400] like how long have you been working on

[00:04:09.680] timeouts? Well, we thought of this we

[00:04:12.480] thought of this GitHub issue. When did

[00:04:13.920] it when was it proposed? On March 18th.

[00:04:16.000] That was the initial proposition for it

[00:04:17.600] where the idea is that you can say that

[00:04:20.000] there's a connection timeout, there's a

[00:04:22.000] response timeout, there's a total

[00:04:23.360] timeout and then with fallbacks where

[00:04:26.000] like you're actually falling back to a

[00:04:27.600] different model if the first one fails

[00:04:28.960] for whatever reason. Then you want to

[00:04:30.720] have a total timeout for the entire

[00:04:32.160] fallback or retry policy kind of

[00:04:33.919] attached to itself.

[00:04:35.919] And then similarly, if you scroll down

[00:04:37.360] further, uh we realize some problems

[00:04:39.919] with like an actual problem is like you

[00:04:41.280] want some sort of nesting. So it's not

[00:04:42.720] actually like really verbose to write

[00:04:44.560] out. But as we did this, I actually

[00:04:47.280] assigned this to one of the engineers on

[00:04:48.639] our team to go take a stab at. And the

[00:04:51.120] engineer did take a stab at this.

[00:04:53.199] >> Is your engineer code arena bot?

[00:04:55.199] >> No, the code the engineer is not that.

[00:04:56.479] That's like a coding agent that we tried

[00:04:57.759] to go solve this problem. The coding

[00:04:58.880] agent failed.

[00:05:00.960] >> But do you want to show the do you want

[00:05:02.639] to show the markdown stuff that you had?

[00:05:05.360] >> Yeah. Yeah. Yeah. So um just for a

[00:05:07.120] little more context here and just kind

[00:05:08.479] of make sure I understand this properly.

[00:05:10.400] Um, I'm going to go back to the AI that

[00:05:12.160] works repo and just pull this up in VS

[00:05:14.960] Code. I know I said I don't really use

[00:05:16.320] VS Code that much anymore, but um, in

[00:05:18.960] this today we're going to look at it.

[00:05:20.320] So, because we have lots of good BAML

[00:05:21.759] code examples in here. So, if you look

[00:05:24.160] in BAML source, um, you will have

[00:05:26.160] autogenerated a client's file. And so,

[00:05:28.479] this is BAML code that talks about

[00:05:30.160] different ways that your prompts can

[00:05:32.400] talk to LLMs. And so, we have this thing

[00:05:34.880] called extract date. And you can set a

[00:05:37.039] client here or you can say my what is

[00:05:39.360] it? custom sonnet,

[00:05:41.280] >> whatever you want to name it. Yeah.

[00:05:43.120] >> Yeah. So that is mapped to something in

[00:05:45.840] here called custo I guess this got

[00:05:47.360] cleaned up a little bit. Oh yeah,

[00:05:48.560] there's custom sonnet. So you can have

[00:05:50.400] very basic options like just model an

[00:05:52.080] API key and then you can create a you

[00:05:55.680] know higher level abstraction over it

[00:05:57.600] that lets you do fallbacks and round

[00:05:59.199] robins and retries and things like this.

[00:06:01.759] Um but what's missing in here is is

[00:06:04.400] timeouts. So, if I want to say, "Hey, we

[00:06:06.400] want to try Gemini 2.5, but if it takes

[00:06:08.720] too long, we're going to fall back to

[00:06:09.759] GPT40 Mini because it's better to give

[00:06:11.440] the user something than nothing." Um, we

[00:06:14.319] wanted to be able, it sounds like you

[00:06:15.520] wanted to be able to add a and then VIBO

[00:06:18.160] did a thing that I think is really

[00:06:19.280] really interesting which is actually um

[00:06:22.240] this like reminds me of this technique

[00:06:24.080] that Amazon kind of talks about a lot

[00:06:25.919] called working backwards which is

[00:06:27.680] basically like write the documentation

[00:06:29.520] or write the blog post first before you

[00:06:32.400] go write any code especially for dev

[00:06:35.039] tools. So this is like a preview of a

[00:06:36.479] doc of like how do we actually want this

[00:06:38.240] to work in reality.

[00:06:39.840] >> I did not do this. Greg did this. I want

[00:06:41.759] to call that out. But our team generally

[00:06:43.440] does abide by this philosophy. I think

[00:06:45.120] for AI agent coding, it's actually

[00:06:46.800] really good.

[00:06:48.800] >> And then you had sent me one other thing

[00:06:50.720] with like the clarified format, right?

[00:06:53.199] >> Slack.

[00:06:54.080] >> Okay.

[00:06:54.800] >> Yeah.

[00:06:55.199] >> Um I'm going to go through the really

[00:06:57.120] fast just so people Yeah, you may want

[00:06:58.639] to share your whole screen.

[00:07:00.240] >> Um I'm just going to grab that client

[00:07:02.240] because there are other sensitive things

[00:07:03.919] in that Slack thread.

[00:07:07.360] Uh let's see. Okay, cool. We'll go back

[00:07:10.000] to sharing the full screen. Um,

[00:07:13.520] so one thing that we have,

[00:07:15.120] >> let's look at the docs really fast just

[00:07:16.720] so people get caught up on exactly what

[00:07:18.319] the objective is that we're going to get

[00:07:19.680] to. So if you go read these docs, can

[00:07:22.639] you zoom in a little bit, Dexter?

[00:07:24.160] >> Yeah.

[00:07:25.360] >> If you go read these docs, this is what

[00:07:26.639] we're going to want. We're going to want

[00:07:27.520] to add a couple new keys in here that

[00:07:29.120] are like connection timeout MS, which is

[00:07:31.759] like time to establish connection, time

[00:07:33.680] to first token because sometimes the

[00:07:35.039] stream might not come back yet. Uh, keep

[00:07:37.520] on going.

[00:07:39.599] idle timeout where it's like you're

[00:07:41.039] getting you want to delay like the

[00:07:42.560] stream is just stalled out at some point

[00:07:44.080] you want to restart in that scenario

[00:07:46.560] request timeout which is like just a

[00:07:48.400] total request as a whole for end to end.

[00:07:51.520] Uh and then for composite clients like

[00:07:53.599] fallbacks and retry policies and other

[00:07:55.440] things you want to be able to put like a

[00:07:56.639] total timeout. Um the only thing we

[00:07:59.520] didn't like about this is now we're

[00:08:00.960] adding arbitrary key value pairs inside

[00:08:02.639] of here that can be really noisy and

[00:08:04.000] hard to detect and we might have

[00:08:05.440] conflict. So I sent text one more update

[00:08:07.840] to this and this this documentation file

[00:08:10.160] should be updated accordingly.

[00:08:12.720] >> Can you show the HTTP thing that I sent?

[00:08:15.199] >> Yeah, let me just um

[00:08:17.039] >> Yeah, which is instead of doing it some

[00:08:18.960] other way, all the timeout options

[00:08:20.400] should be under HTTP. So all the timeout

[00:08:22.639] options should be under an HTTP key. So

[00:08:24.240] we therefore we don't occupy too much of

[00:08:26.000] the key the key name space inside of

[00:08:27.840] options.

[00:08:28.879] >> Yeah. You don't want thousands of

[00:08:30.560] parameters at the top level here.

[00:08:32.800] >> Exactly.

[00:08:33.760] >> Yep. Cool. So that's the only

[00:08:36.240] constraint. Um

[00:08:37.839] >> I think this is pretty well speced out.

[00:08:39.519] I feel pretty confident that this is

[00:08:40.959] something that we want. Take it away

[00:08:42.399] Dex. What should we do? So

[00:08:43.760] >> cool. So the first thing I want to do is

[00:08:45.760] I want to get this doc as markdown

[00:08:47.440] because this actually serves

[00:08:48.720] documentation is a great specification.

[00:08:50.959] We're saying exactly how the user

[00:08:53.440] experience should look.

[00:08:54.800] >> And so here's our spec. Yeah. Go ahead.

[00:08:57.920] >> I was going to say uh I'll let you do

[00:08:59.920] your thing really fast. So I'm first

[00:09:02.080] thing I'm going to do is I'm just going

[00:09:03.040] to have Claude update the spec to match

[00:09:04.640] the new format with the nested key.

[00:09:06.399] >> And while we do this, one of the things

[00:09:08.080] that we're going to talk about is this

[00:09:09.440] concept of research implement uh

[00:09:12.320] research plan implement.

[00:09:14.160] >> Yes.

[00:09:15.200] >> And while we go code implement this, I

[00:09:17.519] want everyone to uh we'll get to

[00:09:20.080] everyone kind of understanding what this

[00:09:21.680] means

[00:09:23.360] in a second. But the idea is that the

[00:09:25.839] one of the first thing that we're going

[00:09:26.880] to do before we even go do this is first

[00:09:28.640] we're going to make sure our spec is

[00:09:29.680] actually correct. it's properly

[00:09:31.200] specified.

[00:09:32.959] And once we've done that, we're going to

[00:09:34.720] try and do a little bit of work to go

[00:09:36.800] and look through the codebase to be

[00:09:38.160] like, did we miss something? Cuz as

[00:09:39.839] clarified as the spec is, we really want

[00:09:42.080] to make sure it's actually in line with

[00:09:43.360] what the codebase would expect to some

[00:09:44.959] degree and figure out all the parts of

[00:09:46.160] the codebase that are relevant, not that

[00:09:48.720] not that need to be changed, just are

[00:09:50.560] relevant.

[00:09:51.519] >> Yeah. And this is all about context

[00:09:53.839] engineering. And like we'll we'll give

[00:09:55.680] you the high level of this, but if

[00:09:57.839] you're watching this and you haven't

[00:09:59.040] seen that, like you should go back and

[00:10:01.440] watch the episode we did on using

[00:10:03.519] context engineering with coding agents.

[00:10:05.440] Um, but the basic idea is like the less

[00:10:07.600] context you use, the better results you

[00:10:09.440] get. And so we're building our workflow

[00:10:11.360] around what I call like frequent

[00:10:12.880] intentional compaction. And so phase one

[00:10:15.440] is like take the spec and create a

[00:10:18.000] research document that documents how the

[00:10:20.399] codebase works today and everything

[00:10:22.399] about it that is relevant to solving

[00:10:24.399] that problem. And then we use that to

[00:10:27.040] build a plan. And all that means is like

[00:10:29.760] instead of having to research like read

[00:10:31.519] all the code and then build a plan, the

[00:10:33.519] model already has a baked understanding

[00:10:36.000] of how the codebase works. So when it

[00:10:38.399] gets to planning, it's actually writing

[00:10:41.600] the plan in the sweet spot part of the

[00:10:44.079] context window because we always

[00:10:46.720] >> you want to let it rip while while we

[00:10:48.399] talk because it takes time. And one of

[00:10:50.800] the things I want to call out here is

[00:10:52.240] this is like we're literally live coding

[00:10:54.000] all this on the fly. We have no idea if

[00:10:55.279] this is going to work. It may work. It

[00:10:56.480] may not work. While you folks have

[00:10:58.160] questions about this, ask questions

[00:10:59.760] along the way. Uh and we'll try and make

[00:11:01.519] sure that we're it's totally up to date

[00:11:02.959] with everyone uh and their understanding

[00:11:05.279] of it. HTTP key. Um,

[00:11:10.079] what is this issue number?

[00:11:12.000] >> I have no idea.

[00:11:12.959] >> 16:30.

[00:11:13.839] >> Yeah.

[00:11:14.160] >> And I'm just going to commit these so we

[00:11:15.440] can see the diff. And we're just going

[00:11:16.480] to let Sonnet do this one cuz it's

[00:11:17.839] pretty quick. But it's going through,

[00:11:19.200] you can see it's going through the spec

[00:11:20.560] and actually making the changes.

[00:11:21.920] >> Nice.

[00:11:23.760] >> And I'm going to go back to dark mode

[00:11:25.680] cuz

[00:11:27.200] >> Thank you.

[00:11:28.079] >> Yeah, it's just putting all this stuff.

[00:11:29.680] Does this look right to you, Baba?

[00:11:31.680] >> Um, this does look right. Uh BKT is

[00:11:34.640] asking if this is a demo coder. Codler I

[00:11:36.640] think personally I think is a great tool

[00:11:37.839] to do this but really it's really a demo

[00:11:39.440] of the process. You could do this

[00:11:41.200] directly in cloud code if you wanted as

[00:11:42.720] well. Um but similar to how I like to

[00:11:45.440] use BAML to building a lot of agent

[00:11:46.800] stuff because it makes certain things

[00:11:48.160] easier. I personally found code layer to

[00:11:50.560] be a great way to to be a nice wrapper

[00:11:52.720] around

[00:11:54.480] um cloud code because it's for me

[00:11:56.399] slightly prettier and therefore I

[00:11:58.399] navigate the UI a little bit faster.

[00:12:00.640] >> Wow. Okay. This is actually just like a

[00:12:02.560] million parallel tool calls all coming

[00:12:04.160] through Sonnet. So, let me put it on

[00:12:05.519] auto approve and I think we might be

[00:12:07.279] done now.

[00:12:08.320] >> Yeah, it looks pretty good. Um,

[00:12:12.079] let's just have a quick look at this.

[00:12:14.639] Just skim it. This all looks right.

[00:12:17.519] >> By the way, this is one thing I've

[00:12:18.880] actually learned deeply while working

[00:12:20.639] with Dexron on how to do VI coding. Cuz

[00:12:22.480] to be completely honest, I didn't do a

[00:12:23.839] lot of VI coding. And the reason I don't

[00:12:25.279] do VI coding is because like I'm a

[00:12:26.560] pretty damn good engineer and I it slows

[00:12:28.240] me down in the beginning. But the reason

[00:12:30.240] that I was actually getting worse vibe

[00:12:31.920] coded is because I wasn't actually

[00:12:35.120] uh what was it called? I wasn't actually

[00:12:36.560] reading every line of the code. So like

[00:12:37.920] the thing Dexter did here where he

[00:12:39.600] actually went through and opened the

[00:12:41.279] diff to go look at it in a real format.

[00:12:43.839] That is important. If you don't read the

[00:12:45.760] code, you are going to be screwed. So

[00:12:47.920] read

[00:12:48.639] >> you have to read this stuff. This is

[00:12:50.800] this is not magic. You have to read what

[00:12:52.639] it does. The idea is not that like oh if

[00:12:54.720] you do research you it's the magic

[00:12:56.320] prompt that just makes everything

[00:12:57.600] better. This is all about giving you and

[00:13:00.320] I we do all these slides in other

[00:13:01.760] episodes, but it's all about giving you

[00:13:03.040] more leverage, right? You still have to

[00:13:04.880] do the work, but you have to you have to

[00:13:07.279] you you're doing it on on higher

[00:13:08.720] leverage thing.

[00:13:10.480] >> Yeah. So, let's go back. Uh let's see. I

[00:13:13.200] think can you go back to reading and

[00:13:14.560] just make sure it all looks correct.

[00:13:16.079] >> Yep.

[00:13:16.639] >> And for context, by the way, here I have

[00:13:19.200] more context on the [ __ ] codebase. So, I

[00:13:20.880] will read this stuff and be like, is

[00:13:22.079] this good or is this bad? Can you go up?

[00:13:23.600] I want to read that complicated one. the

[00:13:26.399] for fallbacks clients. So fallback

[00:13:28.560] clients are interesting. They don't

[00:13:29.760] actually have uh I don't want them to

[00:13:31.360] have connect timeout, idle timeout, or

[00:13:32.959] any of this stuff.

[00:13:35.120] >> Okay. I only want them to have uh total

[00:13:37.760] timeout.

[00:13:39.279] >> Interesting. Um

[00:13:41.120] >> we should probably tell the agent that

[00:13:43.040] in the dock in the

[00:13:44.320] >> Yep.

[00:13:44.959] >> Yeah.

[00:13:45.360] >> Or the fallback one. What was it?

[00:13:47.600] >> Fallback roundroin.

[00:13:50.880] Uh

[00:13:52.560] yeah, fallback roundroin retries. Um,

[00:13:55.680] >> just the timeouts.

[00:13:57.600] >> Just total timeout. Total underscore

[00:13:59.199] timeout

[00:13:59.760] >> because I think there what was the the

[00:14:01.440] docs basically had it was this one,

[00:14:03.199] right? Cuz this is actually

[00:14:04.079] >> the doc was wrong. Oh,

[00:14:05.600] >> okay.

[00:14:06.399] >> Yeah. Yep. Let it let it rip

[00:14:09.040] >> the lowle.

[00:14:11.760] We'll skip the need for the lowlevel

[00:14:15.680] timeouts to be passed through. Direct

[00:14:19.120] clients are the FT,

[00:14:22.720] etc.

[00:14:23.600] >> Yeah. Cool.

[00:14:25.279] >> Perfect. Um, only caveat D is I think

[00:14:28.079] you should be using your voice stuff

[00:14:29.199] like you normally do.

[00:14:30.639] >> Yeah, I will be using voice plenty

[00:14:33.199] today. When it's names of variables, I

[00:14:35.680] find sometimes the voice one doesn't

[00:14:37.279] have a lot of context. And if it's a

[00:14:38.560] codebase I work a lot in, I'll go into

[00:14:40.240] super super whisper and like update the

[00:14:42.880] vocabulary basically. So like it knows

[00:14:45.680] how to do quad cloud code. It knows the

[00:14:48.079] names of certain people that I talk

[00:14:49.760] about a lot um or even occasionally. But

[00:14:52.800] like I had to put your name in there

[00:14:54.160] because it keeps putting you in as uh

[00:14:56.000] VIBO.

[00:14:57.070] [Laughter]

[00:15:02.150] >> That's funny.

[00:15:02.160] >> Yeah.

[00:15:02.639] >> Um

[00:15:04.480] >> Yeah. And I think one of the one of the

[00:15:06.160] other things that I have learned is like

[00:15:07.519] if you guys are really really vibe

[00:15:09.040] coding and you get the hang of this,

[00:15:10.480] once you've done this a few more times

[00:15:12.079] where you actually can go read

[00:15:13.360] something, I highly highly highly

[00:15:16.480] recommend

[00:15:18.800] um starting to do task in parallel. We

[00:15:21.040] won't do that today because doing 2,000

[00:15:23.040] in parallel while having to talk to the

[00:15:24.800] stream is too hard. It is really hard.

[00:15:27.600] >> But and and like I'll tell you why I

[00:15:28.959] think that works is because your like

[00:15:31.600] points that you check in with the agent

[00:15:33.600] or it's not just you have five cloud two

[00:15:35.279] cloud sessions going and writing code

[00:15:36.720] all day and you have to figure out which

[00:15:37.839] one is which and all this. But it's like

[00:15:39.199] because everything you review is all

[00:15:41.199] kind of shaped the same and you know

[00:15:43.360] what to expect in between your like

[00:15:46.800] prompt sessions and letting it go off.

[00:15:48.959] it becomes easier to like mentally model

[00:15:51.680] what's happening and you don't have to

[00:15:53.279] do as much context switching even when

[00:15:56.160] you're switching contexts. Does that

[00:15:57.839] sound right by Bob? Does that m match

[00:15:59.360] your experience?

[00:16:00.240] >> Uh, I think so. Honestly, it's just that

[00:16:02.079] it seems to work and I have no real

[00:16:03.839] context about why. Um, but it mostly

[00:16:06.959] works and it's like it feels good. I

[00:16:08.959] guess

[00:16:10.560] >> vibes are a big part of this. The best

[00:16:12.480] the best engineers I know like they

[00:16:14.399] don't use evals. They just they just

[00:16:16.160] know what works better cuz they spend 70

[00:16:18.320] hours a week talking to Claude.

[00:16:20.079] >> Okay, so what have we done?

[00:16:21.360] >> Okay, so we have our low-level stuff

[00:16:22.880] here. Yeah, so here's the note that got

[00:16:25.040] added. Um, total timeout present

[00:16:26.800] upperbound regardless of the fallback

[00:16:28.880] change exhaust. No further clients are

[00:16:30.639] attempted. Low-le timeouts should be

[00:16:32.000] defined on individual clients, not on

[00:16:33.600] the fallback client itself.

[00:16:34.959] >> Yeah.

[00:16:36.560] >> Um,

[00:16:37.199] >> that looks great.

[00:16:38.399] >> Cool. Okay. Uh, I'm going to kick off

[00:16:41.759] the research. Um

[00:16:45.040] uh we'll start a new context window for

[00:16:46.800] this one since we've already used about

[00:16:48.160] 30%. That's the other idea is like the

[00:16:50.320] goal here is you always want to have um

[00:16:53.120] context and I'm actually going to

[00:16:56.560] I'm going to grab the new versions of

[00:16:58.639] the prompts here. So uh you don't have

[00:17:02.160] to include these in the PR vibe off but

[00:17:04.240] um I'm going to drop them in here. I'm

[00:17:06.480] >> Yeah, go for it. Is it

[00:17:08.079] >> here?

[00:17:08.799] >> Watching someone type feels so archaic

[00:17:10.880] now.

[00:17:12.480] It's like, oh,

[00:17:13.679] >> you need to make uh someone actually

[00:17:15.120] contribute a CLI that does this for you.

[00:17:18.000] >> Really?

[00:17:18.720] >> Yeah.

[00:17:20.720] Oh,

[00:17:21.919] >> I don't have called

[00:17:24.160] >> agents. You spelled agents wrong.

[00:17:26.400] >> Yeah, I know. Something uh in my shell

[00:17:29.440] does

[00:17:29.760] >> I don't have a folder called agents

[00:17:31.120] inside of BAML.

[00:17:33.200] >> Yeah. Yeah. Okay. So, we'll make that.

[00:17:34.799] Something in my shell drops the G key

[00:17:36.960] when I paste.

[00:17:39.200] >> Really?

[00:17:40.240] >> Yeah. Oh, you're going to love this. If

[00:17:41.760] you're not using the sub agents, you're

[00:17:43.200] going to this is going to change your

[00:17:44.400] world.

[00:17:45.360] >> Okay.

[00:17:45.840] >> All right. I think we're

[00:17:47.600] >> I'm down. Just merge it. If this works,

[00:17:49.919] you'll get the whole thing merged in.

[00:17:52.000] >> Amazing. There we go. We're We're

[00:17:54.000] calling in installing some agents into

[00:17:55.679] your repo right now. Um, okay. Research.

[00:17:58.400] What is the number? 1630.

[00:18:01.760] There we go. Now we got the good one.

[00:18:03.600] Um, let's read the spec in at spec. I'm

[00:18:09.280] actually going to rem rename this and

[00:18:12.799] research all parts of the codebase that

[00:18:14.559] are relevant to implementing this

[00:18:16.000] feature. Um, it doesn't exist today, but

[00:18:18.000] I just want to know everything where

[00:18:19.280] timeouts are handled. Um, make sure you

[00:18:21.600] don't get into the details of how to

[00:18:23.360] make an implementation plan. Just tell

[00:18:25.600] me all parts of the codebase, how the

[00:18:27.280] testing works, how the integration tests

[00:18:29.520] work, any codegen that's used in the

[00:18:31.200] repo to make this feature work, and uh,

[00:18:34.000] explain it all for me so that uh, the

[00:18:35.919] next agent can pick it up and get to

[00:18:37.520] work. Um Josh asked a really good

[00:18:39.520] question. Why are we making a new

[00:18:42.320] context window? Is that to optimize the

[00:18:44.559] catch?

[00:18:45.200] >> It's actually not about it's not about

[00:18:47.280] that. It's more about like fundamentally

[00:18:49.600] I mean we talked about this last week

[00:18:50.880] when we talked about the entropic models

[00:18:52.320] and where they degraded because they use

[00:18:53.679] the million million token window and

[00:18:55.919] million tok million context model

[00:18:58.000] instead of the shorter context model.

[00:18:59.919] These systems generally work better when

[00:19:01.679] you get the least amount of context you

[00:19:03.200] need to to actually um make it slightly

[00:19:06.880] better. And part of why

[00:19:10.799] uh why we often recommend controlling

[00:19:13.520] the full context window is because a

[00:19:15.919] really really important part of this

[00:19:17.039] whole workflow is actually getting the

[00:19:18.960] system to work well. So once we got the

[00:19:20.559] spec right, all the work that we did

[00:19:22.480] ahead of time in the context window to

[00:19:24.400] make the spec correct can be deleted and

[00:19:27.520] we can just recede the whole context

[00:19:29.120] window with just the right spec. So the

[00:19:31.039] model doesn't have to be confused about

[00:19:32.640] the old spec, what we changed and then

[00:19:34.720] the new spec. It just says purely here's

[00:19:37.760] the spec that I'm implementing and it

[00:19:39.200] forget it doesn't need to remember the

[00:19:40.880] history of what led us to there.

[00:19:43.039] >> Yeah. Because basically the less of your

[00:19:44.880] context you use the better. And so as

[00:19:47.120] soon as like all of the work to do the

[00:19:49.280] writing and building the spec up so that

[00:19:51.039] we were actually upstream of this over

[00:19:52.720] here. Um I'm just going to drop this in

[00:19:55.039] to the white.

[00:19:55.840] >> Uh if you guys want the commands I'll

[00:19:57.760] post them for you guys.

[00:20:01.039] >> Yeah.

[00:20:01.919] >> So we actually were over here writing

[00:20:03.840] the spec. So the spec is part of our

[00:20:06.320] initial user message which is like hey

[00:20:07.919] go implement that thing.

[00:20:09.039] >> Yeah. If any of you want the commands,

[00:20:11.440] uh, they're in there posted in the chat

[00:20:13.280] and you're welcome to go and check out

[00:20:14.640] the cloud code yourself.

[00:20:16.720] >> Yep. They're there. We've linked them

[00:20:18.480] and documented them before.

[00:20:20.160] >> Yeah,

[00:20:21.520] >> I actually and if you all saw, I

[00:20:23.120] actually cancel the old one and because

[00:20:24.799] it was on sonnet and for the research,

[00:20:26.960] uh, I really tend to think that if

[00:20:29.600] you're not using Opus, you're not going

[00:20:30.960] to get good results. Sonnet is fast and

[00:20:32.480] it writes damn good code, but when you

[00:20:33.919] want to reason over a large complex

[00:20:35.360] codebase, you should almost always be

[00:20:37.440] using Opus. it's worth the money.

[00:20:39.760] >> Uh I would say even even differently,

[00:20:42.080] it's more expensive for you to have to

[00:20:44.240] stop and then start again if you get the

[00:20:47.200] wrong result. So it's better to pay a

[00:20:49.120] tax uh the more expensive tax to get it

[00:20:51.520] right the first time around because

[00:20:53.360] large a large part of vibe coding is

[00:20:55.200] actually feeling good about the process

[00:20:57.039] and if you just feel bad about the

[00:20:58.559] process, you're not going to see it

[00:20:59.840] through. So I highly highly recommend

[00:21:02.720] just using the better model at least in

[00:21:04.240] the beginning until you build confidence

[00:21:05.679] about what is working or not. Also,

[00:21:07.120] Dexter, we're seeing your forehead, just

[00:21:08.799] so you know.

[00:21:10.559] >> Can you see my face now? Sorry. It's uh

[00:21:13.440] I have a new AV setup today and uh the

[00:21:16.240] laptop blocks just the very bottom of my

[00:21:18.559] screen. So, when I need to see something

[00:21:20.240] at the bottom, I move it.

[00:21:21.440] >> Yada asked a really good question. Is it

[00:21:23.200] possible the spec and code connect? What

[00:21:25.120] if the code changes? So, the whole point

[00:21:27.440] of this workflow, Yamada, is actually

[00:21:29.919] not to make the spec and code directly

[00:21:32.159] connected. What we're really doing is

[00:21:33.760] really imagine when you're working with

[00:21:35.679] a colleague and you're right and you're

[00:21:37.280] working together and like pair

[00:21:38.640] programming. It doesn't need to stay

[00:21:40.799] connected forever. You just need to be

[00:21:42.559] correct about whatever you're

[00:21:43.600] implementing right now so your colleague

[00:21:45.440] can go write something. And that is

[00:21:48.640] really

[00:21:50.720] um that's really what we're doing here.

[00:21:54.080] And this is this is also why I am very

[00:21:56.880] bullish on like um basically like or I'm

[00:22:01.200] I'm I'm not I'm I'm kind of like meh on

[00:22:04.080] like what I might call um like codebase

[00:22:06.880] documentation and using agents to update

[00:22:09.039] the codebase like using agents to update

[00:22:11.280] the documentation for other developers

[00:22:12.960] to use because I think like one of the

[00:22:15.039] problems with AI generated code is if

[00:22:16.960] everyone on your team is shipping a

[00:22:18.320] thousand lines of code every couple days

[00:22:20.080] because they're all doing these

[00:22:21.039] techniques the research basically gives

[00:22:23.679] you ondemand upto-date codebased

[00:22:26.559] documentation in you know 10 minutes or

[00:22:29.120] so.

[00:22:30.000] >> So let's see let's see what the and this

[00:22:31.760] will be really clear as soon as we start

[00:22:33.280] reading the research and funny enough

[00:22:35.679] you guys will understand a little bit of

[00:22:36.880] the BAML codebase as the research is

[00:22:39.039] done because then you'll be like oh cool

[00:22:40.640] I see where this is relevant and I'll

[00:22:42.799] show you some interesting things that I

[00:22:44.159] suspect the research pipeline will pick

[00:22:45.840] up

[00:22:46.960] >> if it's done.

[00:22:48.240] >> Yep. So these are these are all running.

[00:22:50.240] So you can see it's invoking these

[00:22:51.679] special sub aents that are defined in

[00:22:54.000] the um they're here public in the human

[00:22:57.360] layer repo which is where I got

[00:22:58.799] >> I posted the link.

[00:23:00.080] >> Yeah. So I'm just going to pull one of

[00:23:01.520] them up. Um so we have the research

[00:23:03.600] prompt itself. Um which is yeah this

[00:23:08.000] one.

[00:23:09.919] So it's like the research again it's the

[00:23:11.440] only job is to document and explain. So

[00:23:13.679] it's like analyze the thing, launch

[00:23:15.280] these parallel sub aents, and then we

[00:23:17.120] tell it the document format we want. So

[00:23:19.200] we want some front matter at the top, we

[00:23:21.440] want the user's question and topic, and

[00:23:23.120] then we want detailed findings on how

[00:23:24.880] all of the relevant components work with

[00:23:27.840] really concise. What makes this so good

[00:23:31.360] is that the other the next model that's

[00:23:33.600] picking up in the next fresh context

[00:23:35.440] window doesn't have to search and find

[00:23:37.200] and learn how all this works. It can

[00:23:39.280] just go straight to reading files to

[00:23:41.039] figure out what changes need to be made.

[00:23:43.600] Exactly.

[00:23:44.559] >> And then the agents,

[00:23:46.640] sorry, let's let's look at the agents

[00:23:48.080] real quick. Um, so like the codebase

[00:23:50.640] locator, its job is to document the

[00:23:52.720] codebase, right? And so all all its job

[00:23:55.039] is to just here's this file, here's what

[00:23:56.559] it does. Here's this file, here's what

[00:23:58.080] it does. So it's just finding things.

[00:23:59.520] This is like your super grip. And then

[00:24:01.919] the analyzer's job gets instructions

[00:24:04.400] like basically like find the entry point

[00:24:07.440] to the whether it's an API endpoint or a

[00:24:09.840] CLI or something trace the data flow

[00:24:13.200] from like wherever X happens all the way

[00:24:15.919] down to the database or all the way down

[00:24:17.600] to the external service or whatever it

[00:24:19.520] is and understand how things change

[00:24:21.840] along. And so we use a mix of these

[00:24:24.240] different agents and like the research

[00:24:25.840] prompt uses them de facto and it just

[00:24:28.720] says like hey here's here's here's the

[00:24:30.559] one to use and where you can also steer

[00:24:33.200] Claude to use one of these agents by

[00:24:35.279] hand. Um okay cool we're in the I'm

[00:24:38.320] going to put this on skip permissions

[00:24:39.760] also.

[00:24:41.440] >> We should almost be done. Um Josh asked

[00:24:43.919] a really good question of Manis

[00:24:45.840] recommended keeping the wrong stuff in.

[00:24:47.440] How do you decide to keep it versus to

[00:24:49.279] start a new thread? Well, I think Josh,

[00:24:51.600] this goes back to two elements. This

[00:24:53.120] this is this can vary both based on when

[00:24:55.600] you build your agent and based on uh and

[00:24:59.520] based on what you do with your coding

[00:25:00.880] agent when you're using a coding agent

[00:25:03.440] like using an agent and building an

[00:25:05.120] agent kind of have the same philosophy.

[00:25:06.880] And what I would say is like it really

[00:25:08.240] depends. So for example, let's say what

[00:25:10.400] I'm trying to do is debug. If I'm trying

[00:25:12.320] to if my if what I'm trying to do is

[00:25:13.919] debug in that scenario, it's actually

[00:25:16.080] really useful to keep the history of it

[00:25:17.840] in. But once I have debugged and I'm

[00:25:20.559] moving on to the next flow. So like say

[00:25:22.240] for example the user asked me to

[00:25:24.480] generate some SQL statements and it

[00:25:27.440] produced a bad SQL statement and then I

[00:25:29.360] errored it out until I got the right SQL

[00:25:31.919] working. Well in that scenario it's

[00:25:34.400] actually better for me to delete all the

[00:25:36.240] old SQL statements and only put the

[00:25:37.760] right one in there or perhaps put a

[00:25:39.600] summary of everything that went wrong so

[00:25:42.000] I can show the best so I can show from

[00:25:44.799] the main agents perspective. All I see

[00:25:46.960] is the user asked to do this and I

[00:25:49.440] generate this SQL statement and I

[00:25:50.799] produce the result. On the other hand,

[00:25:53.279] during the process of actually getting

[00:25:55.200] the error, I probably want to put uh you

[00:25:58.799] want you want you mean result instead of

[00:26:00.480] error at the very bottom.

[00:26:01.600] >> Oh, thank you.

[00:26:02.559] >> Yeah. on on the other end in when I'm

[00:26:06.880] not debug when I'm actually generating

[00:26:08.720] the wrong SQL I probably do want

[00:26:12.880] I probably do want all the errors in

[00:26:14.400] there so it can actually debug itself

[00:26:15.679] and get to the right response and I

[00:26:17.520] would

[00:26:17.760] >> so this is like your error compaction

[00:26:19.520] right what is what some people suggest

[00:26:21.360] is if you run three tool calls and then

[00:26:23.840] you finally get a good one the next time

[00:26:25.600] you send a prompt to the model just do

[00:26:27.360] user message and the SQL and the success

[00:26:29.520] because this is a lot of noise for the

[00:26:31.039] model that isn't like productive to the

[00:26:32.799] conversation

[00:26:33.919] and mana says leave this stuff in

[00:26:35.840] because then the model the next time it

[00:26:37.600] goes to write a SQL query it remembers

[00:26:40.159] oh that table doesn't exist so it learn

[00:26:43.120] it's like it's it can learn from what

[00:26:44.559] was in the context window versus like

[00:26:46.799] basically getting errors again

[00:26:48.480] >> yeah but what's really interesting here

[00:26:50.159] though that you could do is can you go

[00:26:51.840] back to that thing is it's not as

[00:26:53.760] straightforward as what mana says what

[00:26:55.440] mana says is leave it in always what I

[00:26:57.760] I'm going to propose a really quick

[00:26:58.960] algorithm that I think all of us can

[00:27:00.400] understand hopefully which

[00:27:01.919] >> I sent you a link to the board by the

[00:27:03.279] way if you want to write it.

[00:27:04.080] >> That's okay. I'll just draw it on your

[00:27:05.120] I'll just reference it on your screen

[00:27:06.400] which is imagine what I did was I did

[00:27:08.799] this and next time that I got a tool

[00:27:10.799] call for a new SQL I actually injected

[00:27:13.840] the errors in only at that time. So if I

[00:27:17.600] get a tool call for a new generate SQL

[00:27:19.520] or create query plan then I show all the

[00:27:22.080] errors that exist in the past five

[00:27:24.080] queries. But by default I don't. So for

[00:27:27.039] anything that is not a SQL generation

[00:27:28.640] command I hide all the SQL errors. For

[00:27:30.159] anything that is I show the SQL errors.

[00:27:32.000] It doesn't

[00:27:32.640] >> if it's calling the SQL generation tool,

[00:27:35.360] isn't it already too late to like by the

[00:27:37.919] time it's

[00:27:39.120] >> you control the tool. So the SQL

[00:27:41.279] generation tool is going to go ahead and

[00:27:42.799] generate SQL.

[00:27:43.840] >> I guess my point is like if you send

[00:27:45.279] this context window in and the model

[00:27:47.039] says I want to run XYZ query

[00:27:51.440] like

[00:27:51.760] >> I I guess I was describing the model in

[00:27:53.760] some other way where like I would just

[00:27:55.120] want it to indicate that it wants to

[00:27:56.320] generate SQL to me and then I would just

[00:27:57.679] toss in the extra error commands in

[00:27:59.200] there.

[00:28:00.000] >> I see. Okay.

[00:28:00.799] >> Right. That's one thing I can do. I

[00:28:02.399] could also update my base prompt or my

[00:28:04.399] like rag system for whatever I use to

[00:28:06.480] describe the SQL tables better based on

[00:28:08.559] the type of errors I do in like a

[00:28:10.080] post-processing world.

[00:28:11.360] >> So if you separated out the declaration

[00:28:13.600] I want to run a SQL query from the

[00:28:15.679] actual writing of the query itself, then

[00:28:18.080] you can inject the errors in between

[00:28:19.679] here.

[00:28:20.399] >> Exactly. And the or or you can inject it

[00:28:22.799] into the original SQL as well into the

[00:28:25.279] original spot from the previous query.

[00:28:27.200] >> All right. Well, this is about context

[00:28:28.720] engineering. It is incredibly off topic.

[00:28:30.720] So, I'm going to jump over here and read

[00:28:31.840] the research doc. Um, let's have a look.

[00:28:35.440] >> Can you You know what you should do? You

[00:28:36.960] should open this in Obsidian and it'll

[00:28:38.640] be so much cleaner.

[00:28:39.600] >> I don't have Obsidian.

[00:28:40.960] >> Ah, unfortunate.

[00:28:43.360] >> But I can do this.

[00:28:45.360] >> Uh, do you want to open the G-grip

[00:28:47.039] version? But you can open this if you

[00:28:49.120] want.

[00:28:49.919] >> Okay, cool. So, here's our research

[00:28:51.679] question. I think this is fine. So,

[00:28:53.200] let's read the summary. And Vibb I say I

[00:28:55.200] don't know about BAML. And this is like

[00:28:56.559] when you're doing this stuff, you should

[00:28:57.840] always have at least one person that's

[00:28:59.120] an expert in the codebase cuz you need

[00:29:00.559] to be able to read this and make sure

[00:29:01.520] it's right and nothing's missing. So by,

[00:29:03.760] I'm going to ask you to read this and

[00:29:04.799] tell me what's what's missing or what's

[00:29:06.480] wrong.

[00:29:06.960] >> Um, this looks mostly correct. Yeah,

[00:29:10.080] there's a new error. Testing. Okay, go

[00:29:12.720] down. Um, that is the right file. We do

[00:29:16.480] currently have hard-coded timeouts that

[00:29:18.480] need to be plumbed through.

[00:29:19.919] >> Okay, cool.

[00:29:20.399] >> Yeah, that that's what I was expecting

[00:29:21.520] it to find. If it didn't find that, I

[00:29:22.960] knew it would have messed up cuz I know

[00:29:24.320] we have hardcoded timeouts. I don't know

[00:29:25.679] where but I know we have them

[00:29:27.919] >> special AWS client handling

[00:29:30.159] >> because AWS does some weird stuff with

[00:29:32.399] it

[00:29:33.120] >> and then WASM disables timeout. That is

[00:29:35.120] correct.

[00:29:36.399] >> Okay.

[00:29:37.919] >> U Can you go up? Sorry, I can't read

[00:29:39.520] that fast.

[00:29:40.720] >> Publishing API publishes. Yeah,

[00:29:43.600] publishing timeouts. Publishing and

[00:29:45.200] tracing timeouts don't matter for this.

[00:29:46.960] Ignore them. They should not be

[00:29:47.919] configurable.

[00:29:49.120] >> Okay.

[00:29:49.440] >> So, can you just tell the model that?

[00:29:50.880] >> Yep. Yep. So, we're going to start.

[00:29:53.360] Publishing and tracing timeouts do not

[00:29:55.279] matter for this. So you can just ignore

[00:29:57.039] them. Don't include that information in

[00:29:58.559] the document

[00:29:59.440] >> or more likely tell it explicitly they

[00:30:01.440] don't matter. It's better. We we do want

[00:30:03.919] to know that those timeouts exist, but

[00:30:05.360] like

[00:30:06.720] >> instead add a note that the publishing

[00:30:08.960] and tracing timeouts don't matter, but

[00:30:12.240] uh omit the kind of detailed

[00:30:14.240] documentation about what it is. Um yep.

[00:30:17.200] So we're going to launch that one and

[00:30:18.159] then we're going to keep reading. So

[00:30:19.200] this is how you kind of like can keep

[00:30:21.520] keep the model working in the background

[00:30:23.360] as you're continuing to review. So this

[00:30:25.120] doc will update at some point as cloud

[00:30:26.640] makes the changes but um well let's keep

[00:30:28.960] going.

[00:30:29.360] >> Publishing parsing

[00:30:31.840] location property handler. Yep, this is

[00:30:35.200] all correct. Uh time and options blah

[00:30:38.320] blah blah. I believe that visit client.

[00:30:41.039] Yep, that's all correct. Correct.

[00:30:45.520] And just for everyone else, what am I

[00:30:47.440] reading for when I read this code? I'm

[00:30:49.120] actually not reading to like look for

[00:30:50.720] perfect correctness. I'm looking for

[00:30:52.080] approximate fuzzy matching because if

[00:30:54.240] you know, if I was looking for perfect

[00:30:55.360] correctness, I would actually jump to

[00:30:56.480] that line in the codebase and then go

[00:30:57.840] read it.

[00:30:58.559] >> And you can do this if you're really

[00:31:00.000] skeptical. One one advice I give also is

[00:31:02.960] like you should probably

[00:31:06.399] not try to make the research 100%

[00:31:09.039] correct because there's diminishing

[00:31:10.399] returns.

[00:31:11.760] >> Exactly. So like I know what I'm looking

[00:31:13.760] for is I'm like ah this file line is

[00:31:15.360] roughly correct and that's good enough

[00:31:16.880] for me.

[00:31:17.360] >> So yeah line 45. This is Yep.

[00:31:20.080] >> Okay. Request builder provider

[00:31:22.480] implementation. Yep. That's where I call

[00:31:24.480] request. It does the right thing. This

[00:31:26.240] all correct. Go on.

[00:31:27.360] >> Cool.

[00:31:27.840] >> Composite client. No time out at

[00:31:29.760] strategy level. Yep. That's a current

[00:31:31.200] structure. That is correct.

[00:31:33.520] >> Yes, that is correct. No deadline or

[00:31:35.679] timeout. So we will need to go add that

[00:31:37.519] in. And it's found it's found almost all

[00:31:39.200] of them. It has missed orchestrator.rs.

[00:31:43.440] So you probably want to tell it that

[00:31:44.880] >> you missed orchestrator.rs.

[00:31:47.760] Can you add notes about that one as

[00:31:49.360] well?

[00:31:50.880] >> And this is just like where me knowing

[00:31:52.240] the codebase knows that if I don't say

[00:31:54.080] this, it will get it wrong.

[00:31:57.279] >> Um

[00:31:57.919] >> in the which section is this?

[00:32:00.240] >> Out. I don't think you have to tell it

[00:32:01.200] that. It'll figure it out. Oh, sure. You

[00:32:02.480] can say that, too.

[00:32:03.279] >> I just I haven't read the whole thing

[00:32:04.720] yet, so I don't know exactly. Um yeah.

[00:32:08.080] Okay, cool. Cuz there might be Yeah.

[00:32:11.440] Okay, cool. Uh, error handling

[00:32:12.880] infrastructure.

[00:32:14.640] >> Yeah, that's correct. Um,

[00:32:18.240] that is correct.

[00:32:20.080] >> Okay, made our change.

[00:32:21.279] >> Mhm. Go on.

[00:32:23.360] >> How the tests work.

[00:32:24.480] >> I don't actually know if that's how the

[00:32:25.519] test works, but I'm going to ignore that

[00:32:26.880] for now.

[00:32:27.840] >> Can you add inline code examples of uh

[00:32:31.120] the test for each client SDK generation?

[00:32:34.960] That is a bad bet. But sure, we can put

[00:32:36.880] >> You don't think so?

[00:32:38.559] >> Yeah, put it. Put it. It's fine.

[00:32:40.880] >> We'll see how it works. We can always

[00:32:42.080] roll it back.

[00:32:44.399] >> Um, cool. Codegen pipeline. Is this

[00:32:47.519] relevant?

[00:32:48.159] >> No, but it's it probably is actually

[00:32:49.919] because we do have to generate code. I

[00:32:52.080] mean, not really. We don't really have

[00:32:53.440] to generate code. So, maybe not.

[00:32:55.120] >> Okay.

[00:32:56.080] >> Yeah. What's nice about this one is like

[00:32:57.360] the timeouts is already implemented.

[00:32:59.120] It's just not customizable. So, you know

[00:33:00.799] that the flow is actually correct. like

[00:33:03.120] the flow already works.

[00:33:04.799] >> Well, kind of, but it's close. It's good

[00:33:07.039] enough.

[00:33:07.760] >> Yeah, it's a lot easier than the

[00:33:09.360] cancellation one we did.

[00:33:11.039] >> Yes.

[00:33:12.640] >> Um, okay. And then this is code

[00:33:14.000] references. This is just going to repeat

[00:33:15.360] a lot of stuff about what was already

[00:33:17.360] there.

[00:33:18.640] >> Yeah. So, I just want to go read this

[00:33:20.159] though, just so it knows um roughly what

[00:33:23.120] it's doing.

[00:33:24.399] >> So, here's your here's your test

[00:33:26.399] simulation.

[00:33:27.360] >> Nice. Okay. Can I read the test?

[00:33:31.200] >> Yeah. Yeah. Yeah. Let's go back up.

[00:33:33.039] >> Show me the Python one first before I

[00:33:35.200] read anything else.

[00:33:36.480] >> Yeah,

[00:33:36.960] >> a board controller with timeout MS.

[00:33:39.760] >> So, this is just the test for the

[00:33:41.679] cancellation stuff.

[00:33:43.360] >> Yes. So, it did I mean you're

[00:33:45.120] researching so it's not writing new code

[00:33:46.720] probably.

[00:33:47.200] >> Yeah.

[00:33:48.880] >> Um

[00:33:49.279] >> but this is probably actually not

[00:33:50.480] relevant. I'm I was more looking for

[00:33:52.240] like what unit tests are we going to

[00:33:53.760] have to add to um test these new fields.

[00:33:58.960] Yeah, that's you probably should have

[00:34:01.200] phrased it that way.

[00:34:02.080] >> Yeah. Yeah, that's actually wrong. Can

[00:34:04.720] you remove those examples? I'm more

[00:34:06.480] looking for what unit tests would we

[00:34:08.399] have to add to test the new fields that

[00:34:12.159] we want to add here? Um, so can you give

[00:34:14.240] me just one example of uh how and where

[00:34:18.320] there is a test um to test the actual

[00:34:21.040] like BAML syntax? Um, and just one like

[00:34:24.560] tight example and where it lives. Um,

[00:34:26.560] this is going to be helpful for the

[00:34:27.440] planning because we're going to want the

[00:34:29.359] planning agent to Oops. Let's grab this.

[00:34:32.560] Sometimes Super Whisper doesn't paste it

[00:34:34.399] in. Um, cuz we're going to like we're

[00:34:37.440] going to ask the planning agent to build

[00:34:39.119] a test for us. So, um,

[00:34:41.359] >> exactly. So, it'll go it'll go write

[00:34:43.679] some stuff out. Um, that is correct

[00:34:45.440] though where it does this. It's really

[00:34:46.720] all in the property handler. There's

[00:34:48.159] nothing else that has to be modified.

[00:34:50.159] >> Okay.

[00:34:51.119] >> Um,

[00:34:53.440] yes. Uh Matt said something great which

[00:34:55.520] is you should be using voice to prompt

[00:34:58.000] uh for coding tasks. If you're not using

[00:34:59.680] voice, you're just slowing yourself

[00:35:00.880] down. Typing the reason and I'll I'll

[00:35:03.520] give people an intuition about why this

[00:35:05.040] is true because I it took me a little

[00:35:06.160] bit to to come to the dark side. Um

[00:35:09.200] which is or which is that when you're

[00:35:11.280] typing, you almost want to think before

[00:35:13.040] you type. And we're almost all

[00:35:14.400] instinctively trained to do that. If you

[00:35:16.240] make a typo, you're going to press

[00:35:17.280] backspace and go write that out. when

[00:35:19.520] you're speaking, you're going to speak a

[00:35:20.720] lot more uh freely and you're just going

[00:35:22.400] to inject more information in there,

[00:35:24.560] which means that you the model will have

[00:35:26.240] better context and the number of tokens

[00:35:28.240] you inject even if you're speaking very

[00:35:29.920] very verbosely is trivial compared to

[00:35:33.200] the amount of context that you will

[00:35:34.560] never get in there uh if you so just

[00:35:37.200] like speak.

[00:35:38.400] >> Yep. Amazing. Um cool. So yeah, we've

[00:35:43.119] gotten it's updated our unit test

[00:35:45.280] example with just this. So this is

[00:35:48.160] integration test for client timeout

[00:35:49.920] config.

[00:35:50.320] >> Ah it got the spec wrong. Why doesn't

[00:35:52.000] have HTTP in terms of the first one?

[00:35:55.920] >> Yeah.

[00:35:57.760] Uh yeah interesting.

[00:35:59.680] >> Yeah I think it thinks it's optional.

[00:36:02.320] >> Why doesn't the first one have the HTTP

[00:36:04.880] nesting? That's incorrect. You need to

[00:36:06.800] reread the spec and then update the unit

[00:36:08.800] test. We're also getting a little high

[00:36:10.720] on I try to keep the context under 40%.

[00:36:13.359] That's when you get 40 to 50 range. If

[00:36:15.920] it's easy and we're almost there, I will

[00:36:17.520] usually keep it. Um, but you always want

[00:36:19.680] to be pretty aggressive about the

[00:36:21.359] context. But I think I'm ready to start

[00:36:23.359] uh doing the plan for this one

[00:36:25.680] >> once almost. I trust me that we should

[00:36:28.240] just make sure it's actually good

[00:36:29.920] >> because otherwise it's going to be a

[00:36:31.040] waste of time.

[00:36:31.920] >> Yep.

[00:36:32.240] >> Um, we should add some caveats in here

[00:36:34.000] that I think are not obvious. Um, and I

[00:36:36.960] think the spec is actually

[00:36:37.760] underspecified. Idle timeout is only

[00:36:40.079] relevant if called during a stream. Time

[00:36:43.200] to first token is only relevant if

[00:36:44.960] called during a stream.

[00:36:46.960] >> Worth noting um idle timeout is only

[00:36:49.680] relevant if called during a stream and

[00:36:52.960] time to first token timeout is also only

[00:36:55.920] relevant if called during a stream. Can

[00:36:58.640] you update the specification with that

[00:37:00.640] note, not the research?

[00:37:02.480] >> And specifically what you want to add in

[00:37:04.000] is orchestrator/call.rs

[00:37:09.670] does not care about it and orchestrator.

[00:37:09.680] RS does care about it. And this is kind

[00:37:12.079] of that nuance of why I know u this is

[00:37:15.280] this is just me knowing the codebase

[00:37:16.880] like times the first token is a feature

[00:37:18.480] that is only relevant if you're calling

[00:37:19.839] it with stream like function b.stream.f

[00:37:22.800] function name instead of b.f function

[00:37:24.320] name

[00:37:24.960] >> and and this is why we say is like this

[00:37:26.960] is this is real engineering like the

[00:37:29.200] people other people who say like work a

[00:37:30.720] lot with coding agents is the the idea

[00:37:32.480] that like the best engineers have the

[00:37:34.480] entire codebase downloaded into their

[00:37:37.040] brain or whatever you want to call it

[00:37:38.720] like that is still super valuable. the

[00:37:41.119] same way it's valuable if you're

[00:37:42.320] navigating in an IDE and and writing

[00:37:44.240] code by hand.

[00:37:45.040] >> Yeah. Cool. Let's go read let's go read

[00:37:47.280] this now from the top down so then we

[00:37:48.880] can like make sure that we actually

[00:37:50.079] understood it. And you probably need to

[00:37:51.280] refresh, right?

[00:37:52.560] >> Yep. And we're refreshed.

[00:37:54.880] >> Okay. Perfect. Okay.

[00:37:56.079] >> So here's our mod. RS special client

[00:37:59.599] handling

[00:38:01.200] note on the tracing timeouts. Perfect.

[00:38:04.720] >> Um

[00:38:05.839] >> that's just where the data is. It's in

[00:38:07.440] property val

[00:38:08.000] >> property parsing. Yep.

[00:38:10.720] parser database provider for specific

[00:38:12.880] parsing athropic vertex composite

[00:38:16.320] clients. No time out. No time out.

[00:38:19.440] >> Can you scroll up? I want to read the

[00:38:20.640] composite clients uh carefully.

[00:38:23.359] >> Yep.

[00:38:24.320] >> Yep. Okay. Go down. Okay, that's good. I

[00:38:27.520] read that.

[00:38:27.839] >> This is the interesting part. Yeah.

[00:38:29.839] >> Would need total timeout implementation

[00:38:32.000] only. Correct. Um

[00:38:35.760] yes, I think that is correct. Line 221.

[00:38:38.400] Um, it may not be in stream.rs. That's

[00:38:41.280] probably the easiest place to put it

[00:38:42.400] actually. Can we just open that file and

[00:38:43.760] look at it?

[00:38:44.400] >> Yeah. Yeah. Yeah.

[00:38:45.760] >> And this is kind of where it starts to

[00:38:47.200] be like really relevant because like if

[00:38:49.119] I were trying to do this myself, I would

[00:38:51.440] have to think really really hard.

[00:38:53.599] >> Yeah. And when we say like, hey, we

[00:38:55.280] don't we don't edit files and cursor,

[00:38:57.680] you still probably will end up reading

[00:38:59.680] quite a bit of code. God, why? Who did

[00:39:02.400] this?

[00:39:04.000] Why is uh Oh, sorry. We need stream. RS

[00:39:07.520] >> down. Yeah. And what line number?

[00:39:10.079] >> There we go.

[00:39:10.480] >> 21.

[00:39:11.119] >> Um, go down. Okay, I'm good. This looks

[00:39:14.480] correct.

[00:39:14.960] >> You're happy with this is where you

[00:39:16.000] would want that stuff implemented,

[00:39:17.200] right?

[00:39:17.440] >> This is where I would want this

[00:39:18.320] implemented. So, I agree.

[00:39:20.079] >> Yeah. So, this really serves not only as

[00:39:22.160] like documentation, but also like very

[00:39:24.880] subtle steering to where you want your

[00:39:26.880] changes implemented.

[00:39:28.000] >> Yeah. And can you go up really fast?

[00:39:31.359] >> This is where total idle timeout would

[00:39:33.280] be and where um time to first token. And

[00:39:36.400] it's really interesting that this doc

[00:39:37.680] captures all that because like now I'm

[00:39:39.040] like, "Okay, cool. I feel confident that

[00:39:41.119] whatever thing is going to work on this,

[00:39:42.640] we'll have some context that is really,

[00:39:44.240] really relevant."

[00:39:45.599] >> Yep. And just as a fun exercise, I'm

[00:39:48.320] going to go kick off the plan now.

[00:39:50.880] >> Yeah. Yeah. One other 16:30.

[00:39:54.560] >> Yep. Read the spec in spec.md

[00:39:59.119] and the research. Um, actually, I'm

[00:40:02.640] going to show you a cool trick. I'm just

[00:40:04.000] going to run create plan because if you

[00:40:05.839] run it with no arguments, it will um

[00:40:09.359] just ask you what do you want to plan?

[00:40:11.440] >> But isn't that extra context?

[00:40:13.599] >> Extra context, but it's also the right

[00:40:16.400] trajectory. So the planning prompt

[00:40:18.320] actually is like a threephase back and

[00:40:20.640] forth with the user. And sometimes if

[00:40:23.520] you just run create plan and tell it

[00:40:24.960] what to do, it kind of there's a chance

[00:40:27.599] that it skips those interactive steps.

[00:40:30.160] And so by doing by doing create plan and

[00:40:32.800] then this back and forth, hold on, this

[00:40:34.320] is a really important concept. By doing

[00:40:36.160] create plan and then having it answer me

[00:40:37.599] and then I say the next thing, you're

[00:40:39.359] setting the trajectory to be a little

[00:40:41.359] bit more towards your fot prompting the

[00:40:43.680] model that it's often like checking back

[00:40:45.920] with the user and that this is a back

[00:40:47.520] and forth, not a just go call tools

[00:40:49.359] until the thing is solved. You I'll I'll

[00:40:51.200] show you what this means.

[00:40:52.800] >> I I believe you. But for for this

[00:40:54.880] personally, I would just run it cuz I'm

[00:40:56.160] just lazy. Like I'm not I'm not this

[00:40:58.240] would feel like a micro optimization for

[00:40:59.760] myself, but I might be wrong.

[00:41:01.680] >> Uh if you work with these prompts a bit,

[00:41:03.760] you will you will you will uh you will

[00:41:05.760] agree with me.

[00:41:07.359] >> Um where is this thing? You got too many

[00:41:09.119] files in your repo. You're breaking my

[00:41:10.960] uh fuzzy finder.

[00:41:12.800] >> Bro, I have a big code base.

[00:41:16.000] >> Yeah, once I kick this off, we're also

[00:41:17.760] going to run clock. We're going to do

[00:41:19.200] this. Let's work back and forth to uh

[00:41:24.400] outline the phases. Start with your open

[00:41:26.720] questions for me and then give me a

[00:41:28.319] phase outline before writing the plan.

[00:41:31.440] We're just going to give it as much

[00:41:32.720] extra steering as possible to um

[00:41:37.280] >> for this problem. Given how detailed the

[00:41:39.040] research was, I would have actually just

[00:41:40.319] let it rip.

[00:41:42.160] >> Uh you can, but I'm also like want to

[00:41:45.359] kind of show more generally, right?

[00:41:47.680] We're not just solving the problem.

[00:41:48.960] We're But like that's fair. So the

[00:41:50.720] research prompt is actually going to go

[00:41:52.079] do some of its the plan prompt is going

[00:41:53.920] to go do some of its own research. Say

[00:41:55.599] what?

[00:41:56.079] >> You want to auto approve everything?

[00:41:57.760] >> Oh yeah. I'm also going to kick off a

[00:41:59.440] clock which is uh count lines of code

[00:42:02.480] just just for audience context on how

[00:42:04.800] much code is in this codebase.

[00:42:07.680] >> That's a I don't know man.

[00:42:10.560] >> You don't want to see it. Let's see.

[00:42:14.240] Script 200,000 Rust 200,000. Go 130,000.

[00:42:18.560] This is more than last time, dude. This

[00:42:20.319] is crazy.

[00:42:21.119] >> Yeah.

[00:42:22.960] Yeah. I know a lot of this is generated

[00:42:24.960] though.

[00:42:25.359] >> Can you ignore intact test when you run

[00:42:27.839] this? Just ignore the int test folder or

[00:42:30.079] go into Yeah, if there's a way to ignore

[00:42:33.280] ignore BML client basically. Uh BML

[00:42:36.000] client. Yeah, just enter if it'll finds

[00:42:39.119] that. It's like BML client anywhere in

[00:42:40.720] the path.

[00:42:42.560] Oh,

[00:42:43.359] >> we'll do this later.

[00:42:44.319] >> Oh, you need to use Do you not use warp?

[00:42:46.240] >> No, I don't use warp. I use cloud.

[00:42:49.760] >> Interesting.

[00:42:51.359] ignoring also uh star. Uh oh yeah, maybe

[00:42:55.440] that'll work. That'll probably do

[00:42:56.720] something

[00:42:58.960] interesting. I just use warp and I found

[00:43:00.480] it to be pretty good for this stuff.

[00:43:02.720] Works pretty good if you want to just do

[00:43:03.920] it on the CLI. Um I just do everything

[00:43:06.800] in here now. So this thing is

[00:43:08.240] researching again like even though the

[00:43:10.240] research is pretty succinct, um the

[00:43:12.240] planning planning code is designed to do

[00:43:14.400] a little bit of research up front as

[00:43:15.920] well. This is also so that if your

[00:43:18.079] problem is really simple, you can go

[00:43:19.680] straight to planning and you don't have

[00:43:20.960] to do the full research, especially if

[00:43:22.480] you have a smaller codebase. You can

[00:43:23.760] just do the plan and get get better

[00:43:25.359] results.

[00:43:26.319] >> What do we get in clock while it's

[00:43:28.480] running?

[00:43:29.040] >> Let's see.

[00:43:29.760] >> Let's see what we got. There we go. That

[00:43:32.160] looks more appropriate.

[00:43:33.839] >> Okay. Yeah, now it's all rust. And do

[00:43:35.760] you have decode in there? What is that?

[00:43:37.440] >> I don't know what decode. It's reading

[00:43:39.119] something as decode. That's probably

[00:43:40.240] just like config files we have.

[00:43:42.000] >> I mean, clock is a old janky tool. So um

[00:43:45.359] >> yeah this looks about right. Okay cool.

[00:43:47.440] >> Um okay cool. So open questions. Timeout

[00:43:50.319] interaction hierarchy when multiple

[00:43:52.400] timeout mechanisms are active user

[00:43:54.079] configured abort signal retry policy.

[00:43:56.079] What's the priority order?

[00:43:57.359] >> Um what wait

[00:44:00.240] >> should an abort signal immediately

[00:44:01.839] cancel regardless of timeout settings?

[00:44:03.599] >> Yes. Abort should immediately cancel.

[00:44:06.640] >> Should retry attempts each get a fresh

[00:44:08.319] timeout duration?

[00:44:10.400] >> Yes. attempts should each get a fresh

[00:44:12.800] timeout set duration. Cool.

[00:44:16.400] Um it's like as the spec suggests. So

[00:44:18.720] it's like it's gonna it's gonna always

[00:44:20.000] try to come up with some open questions.

[00:44:21.680] Um some of them are just like softballs

[00:44:23.839] of like you want me to do what it said

[00:44:24.880] in the spec. Um should it trigger

[00:44:27.920] between any SSE events including PE keep

[00:44:30.400] alive pings or is it only chunks?

[00:44:33.200] >> Um

[00:44:34.800] only chunks.

[00:44:36.160] >> Only chunks.

[00:44:38.560] Keep alive do not reset the timer. Okay.

[00:44:43.680] Question three.

[00:44:45.839] HTB block structure. Yes. Enforce the

[00:44:49.040] structure not allowed at the top left.

[00:44:51.760] Composite climate should only accept

[00:44:53.839] total timeout.

[00:44:54.960] >> Dude, you got to switch to whisper

[00:44:57.280] floats. A lot more accurate.

[00:44:59.440] >> I just downloaded the biggest model on

[00:45:01.440] Super Whisper to test with it. But

[00:45:04.880] um default timeout values. I'm also

[00:45:06.560] going to have to go get a charger in a

[00:45:07.920] sec.

[00:45:09.359] >> Should we maintain the current

[00:45:10.640] hard-coded defaults? 10-second connect,

[00:45:12.480] 30 second read as fallbacks when no

[00:45:14.480] configuration provider.

[00:45:16.319] >> Yes, keep the default.

[00:45:17.280] >> Yes.

[00:45:19.920] >> Five. Error information granularity.

[00:45:23.520] Yeah. How do you want to display errors

[00:45:25.440] to the user?

[00:45:26.560] >> That was underspecified. Um,

[00:45:31.359] tracked elapse time.

[00:45:33.920] Uh,

[00:45:36.480] just BAML timeout error uh with uh no

[00:45:41.839] data for now. Oh

[00:45:45.599] yeah, it should it should be a subset of

[00:45:48.560] uh BMA client error. Uh it should be a

[00:45:51.040] it should be a child of BMA client error

[00:45:54.079] subclass subclass subasses

[00:45:56.560] >> was environment

[00:45:57.599] >> silent degrade if unsupported.

[00:46:01.119] >> Okay. And then let's look at the phases.

[00:46:05.200] So phase one, and when we're designing

[00:46:07.440] phases, what I really like to do is um

[00:46:10.240] really focus on what is the

[00:46:12.480] incrementably testable thing. I don't

[00:46:15.680] know if that's actually going to be

[00:46:17.119] relevant since you have such good unit

[00:46:19.040] integration test coverage, but if you're

[00:46:20.560] building like a full stack application,

[00:46:22.160] I kind of like if I'm not going to

[00:46:24.319] actually be able to look at it and

[00:46:25.520] verify it until the end of phase three,

[00:46:27.760] I'll just have it combine all three of

[00:46:29.119] those into one phase. Um, there's some

[00:46:31.760] art and science to this, but what do you

[00:46:33.839] think about this?

[00:46:34.960] >> Excuse me. Um, let me take a look and

[00:46:37.520] think about this more.

[00:46:40.000] >> I think this is uh yeah, that's probably

[00:46:43.359] a good phase one.

[00:46:45.119] >> So, we we're skipping the streaming

[00:46:46.560] stuff. We're just doing the the the core

[00:46:49.359] client and basic time.

[00:46:50.240] >> It's really just like parsing clients is

[00:46:52.560] what I would describe that as.

[00:46:54.079] >> Yeah.

[00:46:54.480] >> As like parsing stuff.

[00:46:56.160] >> Yep. Then we add in the BAML timeout

[00:46:58.960] error. Yeah, that makes sense.

[00:47:01.280] >> Create those errors in the SDKs.

[00:47:04.720] >> Yeah.

[00:47:05.680] >> Yep.

[00:47:06.560] >> Then do this. I would probably move

[00:47:08.960] phase 4 right with phase one personally.

[00:47:12.800] >> Okay.

[00:47:14.960] For phases, let's do phase 4 right after

[00:47:19.280] phase.

[00:47:19.680] >> No, right with right as a part of phase

[00:47:21.520] one.

[00:47:21.920] >> Phase one.

[00:47:23.119] >> Yeah. Uh because it's the same parsing.

[00:47:25.599] You can even tell that since it's the

[00:47:26.800] same parsing logic. since it's the same

[00:47:29.920] parsing logic file.

[00:47:33.839] Um, okay. Phase five, testing and

[00:47:36.160] documentation.

[00:47:38.000] Don't do tests at the end. Add tests as

[00:47:42.800] >> No, no, don't do that. Don't do that.

[00:47:44.079] Don't do that. Don't do No,

[00:47:45.599] >> really.

[00:47:46.240] >> Leave that for now. The code base is

[00:47:48.240] [ __ ] So, that's not how I would tell

[00:47:49.920] it.

[00:47:50.960] >> I'll tell you.

[00:47:51.440] >> What do you want to do? You want to just

[00:47:52.240] leave this as like we'll write the test

[00:47:53.440] at the end?

[00:47:53.920] >> Just back backspace all that so far and

[00:47:55.839] just run all the commands you have so

[00:47:57.359] far. Give me like one second to think

[00:47:58.880] about how to tell it that.

[00:48:00.480] >> Okay, I'm gonna hit this. I'm gonna go

[00:48:02.079] grab a charger. Um

[00:48:04.640] and then

[00:48:05.839] >> Yeah, let I'm not gonna hit

[00:48:07.680] >> let it create the plan. Hit enter, let

[00:48:09.359] it create the plan, and then we'll come

[00:48:10.400] back to that testing thing in a second.

[00:48:11.839] >> Yeah. And then we'll read the created

[00:48:13.040] plan and we can iterate from there.

[00:48:14.319] >> Yeah, exactly. Cuz I want to read the

[00:48:15.520] actual plan. Um and then I think I'm

[00:48:18.000] good. Uh but you should fire it off to

[00:48:19.760] let it run the plan.

[00:48:21.760] >> So for context for everyone else, what

[00:48:23.119] have we done so far? In about an hour,

[00:48:24.640] we've gone through where we had this

[00:48:26.240] spec that we wrote that like roughly

[00:48:28.240] outlines new syntax that we have. We

[00:48:31.119] took that spec, we asked an LLM to go

[00:48:33.440] modify it to some more updates. We then

[00:48:35.920] told the LM to go research the BAML

[00:48:37.599] codebase to go and understand exactly

[00:48:40.240] what the codebase is doing and like what

[00:48:42.960] parts are relevant to make that change.

[00:48:45.200] And by the end of this hour, we now have

[00:48:47.280] even an implementation plan of like

[00:48:48.960] here's how we would go implement this by

[00:48:50.720] step by step. And hopefully in the next

[00:48:52.880] 10 to 15 minutes, we'll have the full

[00:48:54.559] implementation plan ready to go. And

[00:48:57.119] once we have the implementation plan,

[00:48:58.559] the rest of this is actually really,

[00:49:00.160] really, really fast because once a plan

[00:49:03.280] is approved, letting a model rip and run

[00:49:05.440] is so fast.

[00:49:07.760] But the key part is having really,

[00:49:09.119] really good documentation there. For

[00:49:10.559] example, if you go back and look at this

[00:49:12.480] earlier, some of you may have seen that

[00:49:15.040] uh one of the things that we did was we

[00:49:17.280] added streaming as an early part of the

[00:49:19.520] stream to the actual spec. And because

[00:49:21.760] the research did not pick that out as

[00:49:23.119] unique,

[00:49:24.640] >> that was an important

[00:49:26.480] >> super high leverage. And this is again

[00:49:28.400] this was the whole point of like a bad

[00:49:31.280] line of code is a bad line of code. A

[00:49:33.280] bad part of a plan is a is a is a 100

[00:49:35.599] bad lines of code. And a like

[00:49:37.280] misunderstanding of which parts of the

[00:49:39.119] system are relevant can tank your entire

[00:49:42.000] project.

[00:49:43.040] >> Exactly. So like because we knew that

[00:49:45.200] that information is relevant, we added

[00:49:46.720] that in and that was actually why the

[00:49:48.559] model realized that hey idle idle time

[00:49:51.200] is only relevant during streaming and so

[00:49:52.960] and that's what I realized too while

[00:49:54.319] doing that. Idle time is only relevant

[00:49:56.160] during streaming and like time to first

[00:49:58.800] token is only relevant during streaming.

[00:50:00.319] We don't want to like error out in the

[00:50:02.000] normal in the normal call pattern when

[00:50:04.400] you're not streaming for time to first

[00:50:06.720] token. Um so while this is almost done,

[00:50:08.800] it's going to go and implement all this

[00:50:10.079] stuff and it's going to write the plan

[00:50:11.599] and then we'll go read the detail plan.

[00:50:13.200] Dextra, while we do this, I want to

[00:50:15.440] >> go download Obsidian.

[00:50:17.040] >> I want to make you download this.

[00:50:18.240] >> Yeah, I actually would love to see your

[00:50:19.760] Obsidian workflow.

[00:50:21.119] >> Just You can't homebrew it. Just

[00:50:22.880] download it.

[00:50:23.680] >> Yes, I can.

[00:50:24.160] >> Oh, maybe you can,

[00:50:25.520] >> bro. You can homebrew anything, man.

[00:50:28.319] >> Okay. Yeah, cuz you've been talking a

[00:50:29.920] lot about how you use this. And actually

[00:50:31.040] one thing I think that is interesting

[00:50:32.319] that is like a thing that I find when I

[00:50:34.800] work with people on these kind of

[00:50:35.839] projects is like and what works when

[00:50:37.200] we're sitting together is like I think

[00:50:39.760] instead of me listening to you and then

[00:50:42.480] translating it into feedback, I can just

[00:50:44.319] hand you the mic and you can talk at the

[00:50:46.079] model. And that's that's like a thing

[00:50:47.520] where it's like when there's two people

[00:50:48.800] working, it's really helpful to be able

[00:50:50.880] to switch back and forth between who's

[00:50:52.400] prompting quickly. And we don't have

[00:50:54.720] that today cuz we're live on a stream

[00:50:56.319] and we're not doing a screen share or

[00:50:57.680] whatever it is, but like being able to

[00:51:00.160] This is running. Can you hold Super

[00:51:01.839] Whisper and I'll talk and we'll just see

[00:51:03.280] if it pulls it up and listen.

[00:51:04.559] >> I don't think it can pull my computer

[00:51:06.319] audio.

[00:51:07.040] >> Wait, are you you have uh Wait, do you

[00:51:08.800] have uh headphones on?

[00:51:11.359] >> If you take off your headphones, it will

[00:51:12.720] listen to me and it'll plug it in.

[00:51:15.440] >> All right, let's try it.

[00:51:17.520] >> Let's see if this works virtually.

[00:51:20.240] >> All right, let's go.

[00:51:22.559] >> Okay, so we can do that. Uh I'm going to

[00:51:25.680] go back to headphones just for the audio

[00:51:27.040] quality, but that's good to know. Um the

[00:51:29.599] the point I was making about like

[00:51:30.720] obsidian and stuff is basically

[00:51:33.440] uh this creates one of the workflows

[00:51:35.839] that you may want that is helpful for um

[00:51:39.920] collaborating with your team, right?

[00:51:41.359] Because like what makes this workflow

[00:51:42.880] really shine is the um open folder.

[00:51:46.160] >> Just open a folder as a vault. Yeah.

[00:51:47.839] Plans and put in reader view. So why do

[00:51:50.720] I why do I personally like this work?

[00:51:52.640] Can you zoom in a bit more?

[00:51:54.319] >> Yep.

[00:51:55.440] Why do I personally like this workflow

[00:51:57.119] where using bare markdown files? Well,

[00:51:59.280] one is I can switch between reader mode

[00:52:01.119] and writer mode. Two, you saw earlier,

[00:52:03.280] one of the things that we were doing is

[00:52:04.640] we were actually asking the model to go

[00:52:06.559] make every edit. Some edits are just

[00:52:08.400] easier to make manually and not have to

[00:52:09.920] go back and forth between the model. And

[00:52:11.839] two, I find reading this to just be

[00:52:13.520] prettier.

[00:52:14.319] >> It's just for me personally, I find this

[00:52:17.040] view to be much much better.

[00:52:18.400] >> Okay,

[00:52:18.640] >> I like it.

[00:52:19.599] >> So, desired ends. This is our this is

[00:52:21.680] our like concise spec. Let's read the

[00:52:24.000] first first few lines. And I apologize

[00:52:26.400] to everyone on the stream that's

[00:52:27.359] watching me and Dexter read a bunch of

[00:52:28.720] stuff. Um,

[00:52:31.440] sadly, this is just what we have to do.

[00:52:33.680] >> This is worth it, too. Like, this is the

[00:52:35.599] part you want to be doing and spending

[00:52:37.359] time on. I I talked to a lot of people

[00:52:38.960] who are uh they get to this and they're

[00:52:41.040] like, "Okay, cool. So, like we can use

[00:52:42.720] the model to write the plans and we can

[00:52:44.000] use the model to write the research.

[00:52:45.359] Like, what if we had the model write the

[00:52:46.720] specs, too, and we can the model write a

[00:52:48.160] really good spec?" And it's like, the

[00:52:50.240] plan gives you 10x leverage. The

[00:52:52.000] research gives you a 100x leverage.

[00:52:54.400] Times you just have to learn to be happy

[00:52:56.319] with being a 100x faster and not try to

[00:52:58.880] get to a thousand because then it things

[00:53:01.119] become hard in a weird way. And there's

[00:53:02.800] sometimes the things that you want to do

[00:53:04.240] manually whether it's reading or

[00:53:05.680] manually pruning these specs that is

[00:53:07.920] still worth doing even though like

[00:53:10.000] you've been told that like if if you if

[00:53:12.800] you're doing something AI should be able

[00:53:14.319] to do it. There's like a there's like a

[00:53:15.680] top out where it's like diminishing

[00:53:17.200] returns. Does that make sense by does

[00:53:19.280] that track?

[00:53:19.680] >> That's right.

[00:53:20.319] >> Yep. Um, so let's go on. This looks

[00:53:24.240] correct. You're right. The um, as the

[00:53:27.599] model will say, you're absolutely

[00:53:28.960] correct.

[00:53:30.079] >> Yeah, we don't say we don't say that

[00:53:31.440] other thing here on stream.

[00:53:32.880] >> Okay, that looks correct. Let's go down.

[00:53:35.280] Fall back and only support this.

[00:53:37.680] >> We're not doing go down.

[00:53:40.480] Um,

[00:53:41.680] >> be an HTTP block. Not adding detailed

[00:53:44.720] metadata to the error objects yet.

[00:53:47.520] >> Yes. Not impossing time out in any WASM

[00:53:50.800] environments.

[00:53:52.800] Not changing default time up behavior.

[00:53:55.440] One second. Not implementing complex

[00:53:57.839] timeout inheritance between composite

[00:53:59.440] and underlying clients.

[00:54:01.440] >> Great.

[00:54:03.200] >> Yes. We're not inheriting time. Every

[00:54:05.680] client is independent.

[00:54:06.960] >> Yep.

[00:54:07.359] >> Implementation approach. H. Okay. Cool.

[00:54:10.319] >> Um, cool. Okay. So, phase one, we are

[00:54:12.800] going to update the helpers to add the

[00:54:15.520] HTTP block.

[00:54:16.559] >> Can you go up? I want to read this a

[00:54:17.920] little bit better. And for context for

[00:54:20.319] everyone else, it's like what are we

[00:54:21.680] doing here? Well, we're going to read

[00:54:23.440] the code. We're notice normally you

[00:54:25.599] don't read all the AI generated code.

[00:54:27.040] I'm going to read this code because this

[00:54:28.240] is relevant. So, I will spend time

[00:54:30.079] reading this

[00:54:31.200] >> and and this is like

[00:54:34.079] the idea is that this is higher leverage

[00:54:35.920] than actually reading the code the model

[00:54:37.599] wrote because it's more of an outline.

[00:54:39.440] Like this is actually not going to

[00:54:40.559] include every single line of code, but

[00:54:42.559] it's going to be the directionally like

[00:54:44.720] like important parts and it's going to

[00:54:46.480] be line by line.

[00:54:47.839] >> We don't have good errors here. So, we

[00:54:49.200] should give the tell the model that you

[00:54:50.480] didn't add good errors for this phase of

[00:54:51.839] the plan.

[00:54:52.800] >> Go down. I don't think it did. I'll just

[00:54:55.119] let's just read the plan a little bit

[00:54:56.160] better.

[00:54:56.480] >> Yeah, let's let's finish reading phase

[00:54:57.839] one and then we'll we'll give it our

[00:54:59.359] feedback.

[00:55:00.240] >> Ignore for now. Okay. Okay, that's fine.

[00:55:03.280] It has some bail is bad. We really want

[00:55:05.760] errors. I think we do want an error

[00:55:07.920] actually because I mean that was the

[00:55:10.079] other issue we fixed is like someone had

[00:55:11.839] they misspelled this and they didn't get

[00:55:13.680] an error.

[00:55:14.240] >> Yeah, exactly. So tell it that we want

[00:55:15.680] good errors here.

[00:55:17.520] >> We want good errors for unrecognized

[00:55:19.520] fields in the HTTP block because the

[00:55:21.520] user needs feedback to know that they

[00:55:23.280] have typed something wrong or

[00:55:24.559] unsupported.

[00:55:25.359] >> Enter. While that runs, we can keep

[00:55:26.960] going.

[00:55:27.920] >> Yep.

[00:55:28.319] >> Yep.

[00:55:29.440] >> This is so fun. I love I love this [ __ ]

[00:55:33.280] >> Let's go on.

[00:55:35.440] Okay, that's perfect. Um,

[00:55:38.960] >> so this is the config.

[00:55:40.960] >> Okay, cool. This part I have no idea

[00:55:42.720] what it does. So to be honest, I'm like

[00:55:44.400] whatever. This is going to figure.

[00:55:45.280] >> So we're going to use the users config

[00:55:46.960] and then we're going to map it from

[00:55:48.240] milliseconds and then we're going to

[00:55:49.839] unwrap it or use the default.

[00:55:51.839] >> We should probably have a way to define

[00:55:53.599] infinite infinite in some way. That's

[00:55:56.079] underspecified in this doc.

[00:55:58.640] >> Um, what is infinite? Minus one.

[00:56:01.280] >> Yeah.

[00:56:01.680] >> Whoops. Let's go. Uh, no. Let's use zero

[00:56:04.160] for infinite.

[00:56:05.040] >> If a user puts zero as the timeout, that

[00:56:07.520] should mean infinite timeout and

[00:56:09.119] override the default.

[00:56:10.240] >> Oh, why zero as a timeout?

[00:56:11.520] >> I upgraded to the super ultra model from

[00:56:14.400] Super Whisper and it's not very good.

[00:56:17.520] >> And I don't know if zero is the right

[00:56:18.960] thing, but like we can use zero for now.

[00:56:21.920] Um, we could also make the user write

[00:56:24.160] in, but that's okay. Let's just do this

[00:56:25.760] for now.

[00:56:26.559] >> Okay, cool. I'm going to just stash that

[00:56:28.480] because it's still working and I don't

[00:56:29.599] want to interrupt it.

[00:56:32.079] Um okay, cool. So now we have um

[00:56:36.880] >> I believe the errors here are fine.

[00:56:39.200] >> Okay.

[00:56:39.599] >> Um uh

[00:56:42.400] >> unrecognized fields not as empty bail.

[00:56:45.599] >> Wait, go up. What did it say about

[00:56:47.280] providers?

[00:56:49.760] >> Go up. It said something about providers

[00:56:52.720] >> is composite fallback or round robin. Is

[00:56:55.040] there any other providers?

[00:56:56.480] >> Round-roin.

[00:57:02.390] Okay.

[00:57:02.400] In the provider check block, it's round

[00:57:06.880] dashroin.

[00:57:08.480] >> There you go.

[00:57:09.119] >> Um, and we're almost getting to 40%. So,

[00:57:11.839] I depending on where we're at after this

[00:57:13.839] round of feedback, I will probably start

[00:57:15.599] a new context window and just be like,

[00:57:17.440] "Hey, we're working on this plan."

[00:57:19.920] >> Cool. We'll figure out the error

[00:57:22.160] checking here. I think the error

[00:57:23.040] checking can be much better. So, we'll

[00:57:24.400] deal with that later.

[00:57:25.280] >> Yep.

[00:57:25.839] >> Yeah. This is going to change, but um

[00:57:27.920] Okay.

[00:57:28.720] >> Cool. It's cool that the model inferred

[00:57:30.480] that zero is a error.

[00:57:32.960] >> It's an infinite. Oh,

[00:57:34.720] >> it did.

[00:57:35.440] >> Yeah. Zero. Oh, this just changed after

[00:57:38.079] I put the feedback in.

[00:57:39.760] >> Oh,

[00:57:40.799] >> do you want to have a 10-minute max?

[00:57:44.000] >> You can just delete that. Just delete

[00:57:45.680] that. And this is what I mean. Like this

[00:57:47.520] is like where we don't have to think

[00:57:48.480] about this. Maybe. Yeah.

[00:57:52.079] Yeah. I don't want to put a max on

[00:57:53.680] there. Screw it. Who knows how good

[00:57:54.880] models get. Maybe we do have 10-minute

[00:57:56.559] long HTB requests that we run.

[00:57:58.960] Do you want to leave this in? This is

[00:58:00.720] validator. Like I think this is the only

[00:58:02.559] one.

[00:58:03.040] >> Um, no. What What does the other one do?

[00:58:06.319] >> It's literally This is just validating

[00:58:08.160] the timeout. So it's like these mean the

[00:58:10.400] same thing.

[00:58:12.640] Okay,

[00:58:14.480] cool. Um, all right. Let's get to the

[00:58:18.079] end of phase one and then we can

[00:58:19.680] actually Well, let's keep going. Does

[00:58:21.680] this look right?

[00:58:23.440] >> Yeah, this looks about right. This is

[00:58:25.839] just passing it through to the HTTP

[00:58:27.920] client.

[00:58:29.440] >> Makes sense. One thing I don't like

[00:58:31.040] about this. Can you go up?

[00:58:32.240] >> Yeah. Yep.

[00:58:33.920] >> I don't like that this stuff is done

[00:58:35.520] over here. I feel like this stuff should

[00:58:37.040] actually be done in the constructor. So

[00:58:38.319] like the defaults should actually be

[00:58:39.599] configured in the parsing

[00:58:41.760] like for all these timeouts we have the

[00:58:43.440] defaults right there.

[00:58:44.799] >> So we should just like the default

[00:58:46.319] should be con in as a part of the

[00:58:48.240] previous section, not as part of this

[00:58:49.839] section.

[00:58:50.799] >> So that way we don't have to reduplicate

[00:58:52.319] the defaults like in five places.

[00:58:54.480] >> Okay. So basically the default should

[00:58:56.319] happen in in this section, not the other

[00:58:58.640] one.

[00:58:59.920] >> Uh yeah.

[00:59:01.440] >> Yeah. Okay. So now we're at 63%. So I'm

[00:59:03.920] going to make a new one.

[00:59:05.599] >> Oh.

[00:59:06.480] >> No, we're going to make a new one.

[00:59:07.760] Sorry, bud.

[00:59:09.440] >> Okay.

[00:59:10.000] >> We're not creating a new plan. We're

[00:59:12.480] updating an existing plan. I'll give you

[00:59:14.240] the path below. Um so don't need to kick

[00:59:17.040] off any research to start. Just use the

[00:59:19.440] guidelines to update the plan. I'm going

[00:59:21.680] to give you the path and some feedback

[00:59:23.440] below. You need better fuzzy match.

[00:59:25.440] >> I know something's going on.

[00:59:26.319] >> You can just right click. You can right

[00:59:27.599] click on that one. The one above. Just

[00:59:30.799] right click on the right click on the

[00:59:32.240] file on Obsidian and it'll give it to

[00:59:33.599] you.

[00:59:34.160] >> Okay. Oh, yeah. Yeah. Copy. Copy path.

[00:59:37.440] >> Yeah.

[00:59:38.400] >> Copy.

[00:59:39.520] >> There we go.

[00:59:40.000] >> You need to put thoughts in front of it.

[00:59:41.520] >> Yeah.

[00:59:42.000] >> I would actually let it read the plan

[00:59:43.200] and then give it feedback after.

[00:59:44.960] >> Yeah.

[00:59:45.359] >> Cuz then that's going to become like

[00:59:47.359] >> in phase one part three, we configured

[00:59:49.760] the defaults. I'd like to instead uh set

[00:59:53.119] up the defaults in part two where we

[00:59:55.520] create the client. Is that is that

[00:59:57.040] right?

[00:59:57.520] >> Yeah.

[00:59:59.280] Or where I parse the client in part one

[01:00:01.839] I think where I parse the PL client.

[01:00:03.599] Yeah. There you go.

[01:00:06.640] >> Cool. Let's keep on going. Can you make

[01:00:09.440] it wider again?

[01:00:10.720] >> Yep.

[01:00:11.119] >> Yeah.

[01:00:11.599] >> This stuff looks really good. It's

[01:00:12.720] actually really simple because it seems

[01:00:14.079] like so straightforward in terms of how

[01:00:15.520] it would implement it. That's fantastic.

[01:00:18.400] >> Um okay, so zero. No timeout, none, use

[01:00:21.599] the default. We're going to move the

[01:00:23.119] default up, but

[01:00:24.880] >> yeah.

[01:00:25.839] >> Okay.

[01:00:26.559] >> Yeah. So then we'll always have it. And

[01:00:27.920] if it says none and zero should really

[01:00:30.160] be none, I think this will do the right

[01:00:33.040] thing. Zero and none should behave the

[01:00:34.960] same.

[01:00:35.200] >> Are you sure? Isn't none use the default

[01:00:37.119] timeout, but zero is explicitly set?

[01:00:39.599] >> No, because it'll be set now in the

[01:00:41.119] other code. Uh yeah, there you go. See,

[01:00:44.240] it changed it automatically to reflect

[01:00:45.920] that behavior.

[01:00:47.280] >> Perfect.

[01:00:47.839] >> This is a lot easier to think about.

[01:00:49.280] Cool. Do you want to skim the change it

[01:00:50.960] made or you trust it?

[01:00:51.920] >> Yeah, I do want to skim the change it

[01:00:53.200] made.

[01:00:54.880] Um, ensure uh I don't like this

[01:00:57.520] happening here. This should happen as a

[01:00:59.040] part of HTTP config. Like as a part of

[01:01:01.119] insure http config.

[01:01:02.960] >> This should happen as a part of ensure

[01:01:04.720] HTTP config. Oops.

[01:01:06.559] >> Uh, so it actually

[01:01:08.960] >> what happened? Yeah.

[01:01:11.760] >> So it'll do the defaults there.

[01:01:13.599] >> Okay, cool.

[01:01:14.079] >> And once it's done, I hate that you're

[01:01:16.640] absolutely right. It's so frustrating to

[01:01:18.319] see.

[01:01:18.960] >> Yeah.

[01:01:19.280] >> Um Okay.

[01:01:21.119] >> It's frustrating to see this early in a

[01:01:23.040] context window.

[01:01:25.040] >> It's fine.

[01:01:26.160] >> Um Okay.

[01:01:27.599] >> And then composite client total timeout.

[01:01:30.000] >> Make it wider again.

[01:01:31.040] >> Yep.

[01:01:31.440] >> Okay. Let's keep reading.

[01:01:34.079] >> Let's Well, it just made a change. Let's

[01:01:35.599] go check the change.

[01:01:36.720] >> What? Why didn't it make the change in

[01:01:38.319] the right place?

[01:01:40.640] Go up.

[01:01:42.799] Okay. So, it did do this here.

[01:01:45.839] If it's not a composite, it adds some

[01:01:47.760] default in there. That's good. That is

[01:01:51.599] correct.

[01:01:52.480] >> Um, it also rolled. I don't know. I

[01:01:54.319] edited this in Obsidian. I don't know if

[01:01:55.680] it actually saved.

[01:01:57.920] >> It does save. You just have to hit

[01:01:59.359] command S, but that's fine.

[01:02:00.640] >> Just going to remove this stuff.

[01:02:01.760] >> Yeah, you're done.

[01:02:02.799] >> Since I don't trust it.

[01:02:05.359] >> Um,

[01:02:06.880] you can go confirm. Just less than zero.

[01:02:10.400] >> This is the research. That's why. Okay,

[01:02:12.079] good. Yeah, cool. Command S works. Yeah.

[01:02:16.720] >> Okay. This looks good.

[01:02:19.280] This looks good.

[01:02:21.760] >> Wait, can you

[01:02:23.200] >> Why is it doing this twice?

[01:02:24.720] >> That's fine.

[01:02:25.920] >> Connect timeout. Request timeout. Okay.

[01:02:28.400] The two different timeouts.

[01:02:30.960] >> Composite time. Total timeout. That's

[01:02:34.160] fine. Does this work? Can I see this one

[01:02:36.400] more time?

[01:02:37.200] >> Yep.

[01:02:38.000] >> Yeah. Orchestrate.

[01:02:40.079] >> I want to look at how orchestrate works.

[01:02:42.079] Total timeout. Okay. Yep.

[01:02:45.280] Yeah, that's correct.

[01:02:46.559] >> Board signal is already there. Existing

[01:02:48.559] retry logic with fresh timeout per

[01:02:50.319] attempt.

[01:02:50.799] >> Yep, that's correct. Okay,

[01:02:52.720] >> that's good.

[01:02:54.799] Does this need to be a special error or

[01:02:56.240] is this right?

[01:02:58.640] >> That probably should be a special error,

[01:03:00.000] but I think that's okay because we

[01:03:00.960] haven't implemented the error yet.

[01:03:02.559] >> Yeah. Okay. And then for streaming,

[01:03:04.480] we're going to do basically the same

[01:03:05.680] thing. So, this is the like compaction

[01:03:07.440] part, right? We're not writing every

[01:03:08.559] single line of code, but it's like,

[01:03:09.680] okay, we did this and this is going to

[01:03:11.280] be about the same.

[01:03:13.119] Yeah, I think the only difference is we

[01:03:14.559] should use Tokyo Select here, but that's

[01:03:16.240] a separate problem. I'll deal with that

[01:03:17.839] later.

[01:03:18.480] >> Are you sure you don't want to change

[01:03:19.520] that?

[01:03:20.640] >> Yeah, you should tell it that. You

[01:03:22.240] should tell it code later. Like we

[01:03:23.760] should use Let's use Tokyo Select. It'll

[01:03:26.400] it'll know what I want.

[01:03:27.280] >> Probably should have told it phase one,

[01:03:28.720] but okay.

[01:03:29.680] >> Figured out.

[01:03:30.559] >> There are examples for user feedback.

[01:03:32.480] >> Yeah. Can you make it read only view

[01:03:33.920] again?

[01:03:34.799] >> Yeah. Connect timeout. Yeah, that's

[01:03:38.400] >> unrecognized fields. supported timeout

[01:03:40.079] fields

[01:03:41.680] not allowed for composite

[01:03:44.720] composite clients only support connect

[01:03:47.039] must be non- negative zero valid means

[01:03:50.000] no timeout yeah these are all our like

[01:03:51.680] test cases basically

[01:03:52.880] >> yeah um and you should I think there's

[01:03:55.119] something in the doc that's somehow

[01:03:56.480] telling it that uh there's yeah there

[01:03:58.960] you go you got that right

[01:04:00.559] >> the select stuff this is right

[01:04:02.640] >> yeah it looks more correct than before

[01:04:05.039] >> here we go okay cool um cool

[01:04:07.760] >> okay um That phase looks correct.

[01:04:10.799] >> Uh that is not the right that is we

[01:04:12.559] don't have make files.

[01:04:14.000] >> Yeah, that's actually I have a global

[01:04:15.440] clot ND that steers it to make and I'm

[01:04:17.440] going to have to get rid of that.

[01:04:19.599] >> Um those are the wrong testing commands

[01:04:22.480] at the end of phase one. Um what should

[01:04:25.200] I tell it to?

[01:04:26.480] >> Yeah. Yeah.

[01:04:27.280] >> I'm also like I'm a little bit worried

[01:04:29.599] this isn't actually telling it to add

[01:04:31.119] unit tests.

[01:04:32.240] >> Um

[01:04:34.559] there are no unit tests here, but that's

[01:04:36.079] okay. Uh well I I'll talk about testing

[01:04:38.640] in a second with BAML.

[01:04:40.000] >> Okay, cool.

[01:04:43.359] >> Um I would probably say is it's it's

[01:04:45.680] kind of meaty for phase one. It should

[01:04:47.359] really just get all the configs right.

[01:04:49.599] That's what I would call all of phase

[01:04:50.880] one. All of phase one is just

[01:04:54.799] configs right. And and

[01:04:56.000] >> so what do you want to take out?

[01:04:57.760] >> I would just split out phase one to the

[01:04:59.359] parsing and actually adding the timeouts

[01:05:01.280] as phase two.

[01:05:02.720] >> Cool. Yeah, this is like a thing in

[01:05:04.799] phase design, right? is you want to it's

[01:05:07.280] like it's how how would you build this

[01:05:09.440] right? How would how much code would you

[01:05:11.200] write before you pause to like run

[01:05:12.640] something?

[01:05:13.440] >> Yeah. And the reason by the way I say

[01:05:14.960] this is because I know that we can add

[01:05:16.720] tests at at the parsing layer first

[01:05:19.280] before we add tests for the rest of it.

[01:05:20.960] >> And I might honestly just say like

[01:05:22.880] everything cargo test passes.

[01:05:25.680] >> Uh I'll tell I'll give you specific

[01:05:27.440] tests to run actually after this.

[01:05:30.000] >> Um or the model can do it.

[01:05:32.160] >> Yeah, I know. But I I'll tell you what

[01:05:33.599] to run and then you can just tell it

[01:05:34.799] that it's not actually cargo test. We'll

[01:05:36.640] have to if you edit this here, it's

[01:05:38.319] going to edit it again. You're going to

[01:05:39.359] get screwed. So you can't you can't

[01:05:40.880] multi hop.

[01:05:42.000] >> Yep. Okay,

[01:05:43.119] >> cool. Let's keep reading though. Um

[01:05:44.799] because even if it renames the phases,

[01:05:46.319] that's fine.

[01:05:47.119] >> Yep. Okay. Um error handling

[01:05:49.680] enhancement.

[01:05:50.319] >> Yep. This is correct.

[01:05:51.520] >> Python SDK error. TypeScript SDK error.

[01:05:54.720] Go SDK error.

[01:05:56.240] >> Cool. Looks good.

[01:05:56.880] >> Well, Go SDK doesn't have errors yet.

[01:05:58.559] >> Oh, really? Pretty sure that doesn't

[01:06:00.799] exist. I'm like 85% sure that that does

[01:06:03.520] not exist.

[01:06:04.319] >> Just want to see what is it doing here.

[01:06:07.039] >> While we're doing this um and while Dex

[01:06:08.880] is running this question, feel free to

[01:06:11.440] keep firing them off while this is

[01:06:12.720] executing because like we have a lot of

[01:06:13.920] downtime while this runs.

[01:06:16.000] >> Yeah. And this is why actually I think

[01:06:17.200] pair programming is really good for this

[01:06:18.880] kind of work because there is a little

[01:06:20.640] bit of downtime. And if you're doing it

[01:06:22.079] solo, I would just go check Twitter or

[01:06:23.920] something. But when you're sitting with

[01:06:25.119] another engineer building stuff, you can

[01:06:27.599] actually take the downtime to like

[01:06:29.039] engage on the problem, think about

[01:06:30.640] what's next, talk about some of the

[01:06:32.480] things that we haven't figured out yet.

[01:06:34.000] Do we have more questions?

[01:06:36.319] >> Keep on going. I'll let them know what's

[01:06:37.839] the questions coming. I'm watching the

[01:06:39.119] chat.

[01:06:39.680] >> Cool. Thanks.

[01:06:42.319] >> Okay, so phase one is parsing and

[01:06:44.400] validation.

[01:06:46.400] >> This is insure HTTP config. And then

[01:06:49.359] phase two should be. And so

[01:06:52.400] >> now what I want to cargo test is not

[01:06:54.480] enough. Now what I'll tell you is I'll

[01:06:55.920] actually show you how to add tests. The

[01:06:57.440] way that you add test is you go into our

[01:06:59.680] repo. Open our repo really fast just so

[01:07:01.440] you know what I'm pointing to in cursor.

[01:07:03.680] >> Yep.

[01:07:04.079] >> Open that and then go to engine

[01:07:08.160] slashablam

[01:07:19.670] test. Yeah. and then do command B so I

[01:07:19.680] can see the sidebar and then uh scroll

[01:07:22.079] up uh it may not it's in validation

[01:07:25.599] files.

[01:07:26.880] >> Oh here we go.

[01:07:28.240] >> So this is where new thing in client

[01:07:31.359] open client and we like boom be like hey

[01:07:34.000] add new tests to this file. These are

[01:07:36.480] all incorrect but there's a mechanism to

[01:07:38.480] run them. Copy path.

[01:07:41.119] Yep. And just tell it to add test for

[01:07:44.079] phase one. You can add test to this

[01:07:45.680] file. Yeah. And then the way that you

[01:07:47.920] run them is cargo test from within that

[01:07:51.280] within um no no not to the whole patch

[01:07:54.400] just engine baml libbaml.

[01:07:56.400] >> So yeah one thing I will say is um this

[01:07:59.200] is the kind of thing that you're not

[01:08:00.480] going to want to tell it manually for

[01:08:01.760] every plan. And so this is the kind of

[01:08:03.440] thing where you could go update your

[01:08:04.799] create plan command to say to give a

[01:08:07.680] guidance around how the tests work for

[01:08:09.599] different parts of the codebase. We're

[01:08:10.880] not going to do that today but that's

[01:08:12.079] like room for improvement. Specifically

[01:08:14.240] what you want to tell the system is this

[01:08:15.760] is how you run parser tests like uh

[01:08:20.319] th this is how you run like parsing

[01:08:22.000] tests or like a validation test.

[01:08:25.199] read a few other files in there to get a

[01:08:28.640] sense how it works

[01:08:30.480] >> and also tell it that the comments

[01:08:32.239] automatically get updated um with the

[01:08:36.640] comments automatically get updated

[01:08:40.319] the er the error comments

[01:08:44.400] if when you run

[01:08:48.400] update_exect equals 1 all caps uh cargo

[01:08:53.199] test dot dot dot Yeah, there you go. So

[01:08:56.080] like that's just like a mechanism that

[01:08:57.440] we have. Yeah, cool. That's it. Tell

[01:08:59.520] that now it should be able now it should

[01:09:00.880] be able to go good test. That's why I

[01:09:02.080] didn't want to do testing stuff earlier

[01:09:03.359] because I wanted to have some context

[01:09:04.799] here. I was like there's just no way

[01:09:06.480] that we'll get this right in that part

[01:09:08.000] of the

[01:09:09.359] >> Well, you want you want to kind of read

[01:09:10.719] the plan and you know what it already

[01:09:12.080] knows and that gives it enough context

[01:09:14.080] to actually go put in the right unit

[01:09:15.520] test.

[01:09:16.239] >> Exactly.

[01:09:17.279] >> Cool.

[01:09:17.520] >> And rep are we using obsidian as a

[01:09:19.440] knowledge base or just as temp for

[01:09:20.960] creating your prompts or context? I

[01:09:23.199] actually I personally never save my

[01:09:25.279] prompts and my repo my research and

[01:09:27.759] plans in my codebase permanently. It's

[01:09:30.159] like a separate artifact that lives

[01:09:31.600] independent of it. And Obsidian is just

[01:09:33.040] a really good markdown viewer and

[01:09:34.480] reader. So that's what I read.

[01:09:37.040] >> Yeah. And also like I think we found a

[01:09:39.040] lot is like we in the past have like

[01:09:41.120] kept all historical research and plans

[01:09:43.359] and given the model access to like

[01:09:44.960] review them for historical context. And

[01:09:47.759] what I'm finding more and more is like

[01:09:49.359] you almost never want that. And so what

[01:09:51.440] you want is you want the model to have

[01:09:53.040] access to all of the research and plans

[01:09:55.920] and specs for a specific project. And I

[01:09:59.120] say project, I mean like this issue that

[01:10:00.800] we're solving and then when you move on

[01:10:02.800] to another project, all that stuff is

[01:10:04.480] becomes not by default visible. Um

[01:10:07.440] unless you ask the model to like go

[01:10:08.880] search for specific things. We do have a

[01:10:10.800] couple files that I call like golden

[01:10:12.480] research which are just like the model

[01:10:14.560] should probably always be able to find

[01:10:15.840] this stuff because it's like here's how

[01:10:17.360] the tests work. like this kind of

[01:10:18.880] information could get put into a

[01:10:20.400] research file that is always available

[01:10:21.920] to the model, but you'd want it to like

[01:10:24.000] be kind of like hand hand manicured and

[01:10:26.400] really really cuz that's a high leverage

[01:10:28.000] thing.

[01:10:29.520] >> Can I read the plan?

[01:10:30.800] >> Yeah, let's see what it did.

[01:10:31.679] >> Okay, cool.

[01:10:32.239] >> Yep.

[01:10:33.040] >> Add validation test. Okay, go on. So, go

[01:10:35.760] down. So, it just shows you error

[01:10:38.159] examples, but then it actually starts

[01:10:39.600] adding validation tests. That's great.

[01:10:42.239] That's great. That's great. That's

[01:10:43.600] great.

[01:10:45.360] And then it will tell you how to go do

[01:10:47.280] this in it. Now tells you invalid tests,

[01:10:50.080] what are happening. Cool. That's fine.

[01:10:52.560] Like all these errors and stuff are

[01:10:54.000] totally fine.

[01:10:55.280] >> Cool.

[01:10:57.520] >> Adds a bunch of tests and then it should

[01:10:59.280] make them pass and some of them won't

[01:11:00.719] pass. So then it'll just like run the

[01:11:02.320] diff themselves.

[01:11:03.600] >> Messages.

[01:11:04.000] >> Uh let's I would actually run phase one.

[01:11:06.640] I would just let let it run phase one.

[01:11:09.120] >> Cool. And then we'll go back and fix the

[01:11:11.199] rest of the plan once we know what's up.

[01:11:13.040] >> Exactly. So while while we're waiting

[01:11:14.880] and reading the rest of it, I would let

[01:11:16.159] it run on phase one.

[01:11:17.679] >> So will you would you actually run every

[01:11:20.480] single one of these commands?

[01:11:22.239] >> Yes, that is how I would run this.

[01:11:25.679] >> Um,

[01:11:26.480] >> yes, that is correct.

[01:11:28.239] >> Make sure this passes. So it's it's it

[01:11:30.400] does have the same thing.

[01:11:31.600] >> I I would get rid of I would I would get

[01:11:33.600] rid of default. Defaults are applied for

[01:11:35.679] non-composite clients. Yes. Um,

[01:11:38.960] >> yeah, I would get rid of that. Yeah,

[01:11:41.040] we're just testing the parser stuff.

[01:11:43.280] >> Yep, there we go. That's all fine. You

[01:11:45.520] can leave that there.

[01:11:46.400] >> It'll probably only run it once.

[01:11:48.239] >> Yeah, it'll figure it out.

[01:11:49.679] >> And then we're just going to not do

[01:11:51.199] manual verification here, right? H

[01:11:53.760] >> It's fine. Let let it be there. I would

[01:11:57.120] let it run. And I would just let it run

[01:11:58.960] on um And the only reason I'm I'm um the

[01:12:04.239] I would just tell it to only run phase

[01:12:06.080] one. I And you're going to start.

[01:12:08.159] >> I will. Yeah. Yeah. Yeah. But I also put

[01:12:09.600] that in there just to over steer it a

[01:12:11.760] little bit.

[01:12:12.400] >> Create plan.

[01:12:12.960] >> Um, cool.

[01:12:14.719] >> Yeah. Implement. Yep. And just let it

[01:12:16.800] rip. And now let's go back to reading

[01:12:18.000] the plan while this is running.

[01:12:19.760] >> And this is something that I I have

[01:12:21.360] often done because we've already read

[01:12:22.960] phase one and we kind of split it into

[01:12:24.560] two separate plans. I'm okay letting

[01:12:26.880] this happen. I I am not at all worried

[01:12:30.080] about like it messing up at this phase.

[01:12:33.040] So I will let it go do that and it'll

[01:12:35.120] make some progress and at some point the

[01:12:36.320] code will be done. Probably in a couple

[01:12:37.440] minutes to be honest. Cool. So, I'm

[01:12:39.280] going to kick off since this one was

[01:12:40.640] getting fairly high. I'm just going to

[01:12:42.960] close this one out and I'm going to use

[01:12:44.400] the same prompt. I literally copied the

[01:12:46.159] same prompt, which is like create plan,

[01:12:48.000] read the file, and then wait for my

[01:12:49.440] feedback.

[01:12:50.560] >> Cool. Let's keep on reading.

[01:12:52.560] >> Cool. Timeout implementation. So, this

[01:12:55.280] is the stuff we moved out of phase one.

[01:12:57.360] >> Yep. So, it's now actually going to

[01:12:58.800] create the client. So, this is this is

[01:13:00.400] much better than before.

[01:13:02.159] >> Yep.

[01:13:03.600] >> Cool. And then this is our applying the

[01:13:06.080] actual timeout to the sync stuff

[01:13:08.640] >> in the each client. And then the

[01:13:11.280] composite client total.

[01:13:13.440] >> Um we have our Tokyo pin. We have our

[01:13:16.080] Tokyo select. So I think this all looks

[01:13:18.800] right. I don't

[01:13:20.159] >> error is out there. I agree with this. I

[01:13:22.320] think we should move the error

[01:13:23.360] definitions up before this happens. Like

[01:13:26.480] we should expose error will need to be

[01:13:28.560] implemented and it's not done yet. So

[01:13:30.239] like

[01:13:31.280] >> in phase two, let's move the exposed

[01:13:33.920] error up and implement it before the

[01:13:36.800] >> I would just move error definitions

[01:13:38.480] before I would just move error. I would

[01:13:40.320] delete that and let's tell it to move

[01:13:42.000] move the phase of defining errors before

[01:13:44.159] we actually do uh the request

[01:13:46.640] definition.

[01:13:47.199] >> So in phase two, let's just define all

[01:13:49.280] the errors first before we go in and do

[01:13:51.520] the request definition stuff.

[01:13:53.120] >> Then let's split out the phases. It

[01:13:54.480] might that might interpret it as do it

[01:13:56.000] in phase two.

[01:13:56.800] >> Do you want to do it instead of phase

[01:13:58.320] two? I want to do it in Yeah, I want to

[01:14:00.400] do it before phase two. Like I want

[01:14:01.920] phase two to move down one more step.

[01:14:03.679] >> Make that into phase three and then add

[01:14:07.120] a phase 2 that is just define all the

[01:14:11.840] errors first.

[01:14:13.920] >> Cool.

[01:14:14.400] >> Exactly.

[01:14:15.040] >> And again, it's all about breaking down

[01:14:16.480] the problem into smaller and smaller

[01:14:17.920] components that are all going to

[01:14:18.960] individually compile because like this

[01:14:21.280] is a huge compilation task. So my whole

[01:14:23.679] goal is compile as much as possible

[01:14:26.400] ahead of time. And one of the benefits,

[01:14:28.239] for example, of using Rust is if it

[01:14:29.679] compiles, it probably works.

[01:14:32.159] >> Rust.

[01:14:32.800] >> This somehow got our stupid value

[01:14:35.760] greater than 10 minutes

[01:14:36.640] >> cuz there's a line somewhere in there

[01:14:37.920] that says like look up 10 minutes. I bet

[01:14:39.840] you there's a thing in there in one of

[01:14:41.520] the things that says like 10-minute max.

[01:14:44.000] >> It just rewrote this again. I tried to

[01:14:45.760] edit it.

[01:14:46.159] >> Yeah, but go look up in the other Go

[01:14:48.000] look up in the other one.

[01:14:50.239] Go look up in the research.

[01:14:51.920] >> Didn't read the research though.

[01:14:53.760] >> It did.

[01:14:55.679] Not in the imp. This is the implementer.

[01:14:57.520] This is the thing actually going to like

[01:14:59.440] do the code.

[01:15:00.080] >> What file calls did it make?

[01:15:01.440] >> It read the plan. My point is like the

[01:15:03.120] plan we we edited that plan to remove it

[01:15:05.440] and it got put back in. So

[01:15:07.520] >> this is why I don't this is why this is

[01:15:09.280] why I don't manually edit sometimes

[01:15:11.440] because the model will just keep

[01:15:12.880] rewriting it with the new stuff.

[01:15:15.199] >> I think I have a separate prompt that I

[01:15:16.960] use that tells it that sometimes I make

[01:15:18.719] edits that you don't have.

[01:15:21.120] >> I see.

[01:15:22.239] >> Um it's fine if it has that. We can just

[01:15:24.640] remember that. Like honestly, a

[01:15:26.239] 10-minute max is fine.

[01:15:27.440] >> No, we're going to fix this.

[01:15:28.640] >> Oh, it actually completed phase

[01:15:30.880] implement. Well, this Are you? No, the

[01:15:33.520] implement plan doesn't need it.

[01:15:35.120] >> I want to update the plan cuz every

[01:15:36.880] every model from here on out is going to

[01:15:38.640] see that in the plan, and it's going to

[01:15:40.239] be like, oh, that's wrong. I'm going to

[01:15:41.760] go fix that, too.

[01:15:43.199] >> Yeah, but then then we should be an

[01:15:44.480] implement plan. We should do this in

[01:15:45.600] create plan. Fire it off. Okay, let's

[01:15:47.920] keep on reading it. Did

[01:15:49.280] >> Hold on. Hold on. No, because I want to

[01:15:51.120] make sure that the actual implementer

[01:15:52.640] also has that. Updated the plan for

[01:15:55.440] validation to simplify the logic. Read

[01:16:00.239] the file again and update the

[01:16:03.040] validation. I'm just going to stage

[01:16:04.560] that. I'm not going to send it.

[01:16:05.760] >> All right. Cool.

[01:16:08.320] Um,

[01:16:10.480] cool. Let me go read this really fast.

[01:16:12.400] Let me read the plan while it's working.

[01:16:14.400] >> Yep.

[01:16:15.360] >> Um, we just want I want to read the next

[01:16:16.800] phase because this part is done. Phase

[01:16:18.400] one should be done. Cool. Error type

[01:16:21.199] definition.

[01:16:22.640] >> Cool. That was correct. Correct. Go up.

[01:16:26.000] No, you're going too fast. My brain

[01:16:27.520] doesn't read that fast.

[01:16:29.920] >> And I do want to read everything else.

[01:16:31.920] >> Yep.

[01:16:32.719] >> Yes. Damn. Time out error. It comes from

[01:16:34.880] a client. So, we actually have all the

[01:16:36.239] client metadata for free. Yes.

[01:16:38.800] >> Yep. Correct.

[01:16:44.709] >> You said this doesn't exist yet.

[01:16:44.719] >> I'm pretty sure. I mean, just go check

[01:16:46.080] that file. Yeah, it's I don't see it.

[01:16:49.920] >> Cool. That's what I thought. Um, so Go

[01:16:52.480] doesn't have errors. Just like delete.

[01:16:53.840] >> Should we just skip this?

[01:16:56.000] >> Just delete it. Delete. Delete it and

[01:16:57.840] just say like doesn't have errors. And

[01:16:59.360] you can tell if you want.

[01:17:00.640] >> The Go SDK doesn't have support for

[01:17:02.719] errors. So remove step four from that

[01:17:05.199] phase entirely. We'll just skip that for

[01:17:07.120] now.

[01:17:07.920] >> And same with Ruby.

[01:17:09.600] >> Same with Ruby. Same with Ruby.

[01:17:11.920] >> Technically, we do have errors. I just

[01:17:13.199] don't want to deal with it right now.

[01:17:16.000] Uh,

[01:17:18.159] and you should say focus only in Python.

[01:17:20.080] Oh, whatever. It's fine.

[01:17:22.560] That's good enough. Let's go back and

[01:17:23.679] read.

[01:17:24.239] >> Okay,

[01:17:25.840] >> this thing is still implementing.

[01:17:28.640] It's doing its thing. And a large part

[01:17:30.719] of actually using AI models is really

[01:17:32.560] about just like moving fast and

[01:17:35.440] paralyzing. So that's why we're

[01:17:36.560] implementing phase one without having to

[01:17:38.400] go through all of it.

[01:17:39.520] >> It's just not worth the time.

[01:17:41.199] >> So now we just have Python and

[01:17:42.400] Typescript. And here's the mapping. And

[01:17:44.400] that's the end of the phase. Is this

[01:17:46.159] right? Like string contains timeout.

[01:17:48.960] >> No, we will eis connect. I don't know

[01:17:51.679] what that E is. Can you go to that file?

[01:17:54.400] Just like look up what that file reads

[01:17:55.920] like. I have no idea. And again, this is

[01:17:57.760] just another benefit of having like the

[01:17:59.199] actual file references. Like we can just

[01:18:00.640] like read this stuff. Just go back and

[01:18:02.960] read. Um, no, it's somewhere down below

[01:18:06.560] >> line in execute request or error

[01:18:09.040] handling. So here we look at the status.

[01:18:13.440] No, this won't be in here. This is

[01:18:15.120] incorrect. This will only ever be in the

[01:18:18.239] I don't know where the error will come.

[01:18:19.600] I mean, maybe where's execute request

[01:18:21.840] match.

[01:18:24.000] >> So, what here's a good example of like

[01:18:26.960] um

[01:18:27.280] >> I have no idea what Russ does here to

[01:18:28.960] actually see where it happens.

[01:18:30.800] >> Like,

[01:18:31.280] >> so this is

[01:18:32.480] >> this is what I'm going to do. I'm going

[01:18:33.840] to show you a cool trick that shouldn't

[01:18:36.560] happen here. Use codebase pattern finder

[01:18:40.560] to see how errors from HTTP clients are

[01:18:45.199] handled.

[01:18:46.000] >> I'm pretty sure it does happen there, by

[01:18:47.440] the way. Oh,

[01:18:50.159] anyway, that's fine.

[01:18:51.280] >> Okay. Uh, close enough. We'll figure it

[01:18:53.199] out.

[01:18:54.239] >> It's somewhere in there. Um, is the

[01:18:56.159] other one done yet?

[01:18:58.320] >> The implement.

[01:18:59.920] >> Why is it running make? It's running

[01:19:02.000] make.

[01:19:02.239] >> It's my global cloud MD. Read the damn

[01:19:04.640] plan, you nerd.

[01:19:05.920] >> Cool. And then I think what what should

[01:19:07.600] end up happening here is once phase one

[01:19:09.199] is done, then we should be able to get

[01:19:10.320] phase two to compile. Once phase two

[01:19:12.080] compiles, then we can actually go

[01:19:13.600] implement it.

[01:19:14.640] >> Yeah.

[01:19:16.800] Um

[01:19:18.880] I'm actually going to stop this cuz the

[01:19:20.480] context's getting quite high.

[01:19:21.679] >> It should be fine. Trust me, I've run it

[01:19:23.840] to like 80% for these guys, especially

[01:19:25.679] during the last part of running tests.

[01:19:27.280] >> But we also have to update this all this

[01:19:29.360] logic. All the unit tests are wrong

[01:19:30.960] because we updated the plan to remove

[01:19:32.400] that timeout max. So, like we have to

[01:19:34.080] fix that and then we have to get the

[01:19:35.360] test passing.

[01:19:36.560] >> It will matter because it's going to fix

[01:19:38.159] and get all the tests passing and then

[01:19:39.360] it's going to have to make a bunch of

[01:19:40.320] changes and fix the tests again. Trust

[01:19:42.159] me.

[01:19:42.480] >> Okay,

[01:19:42.880] >> we're working on the plan. Um, we're

[01:19:45.360] only doing phase one. Um, I did one

[01:19:48.080] small update to the plan. So, um, check

[01:19:50.719] what's been done and then, um, update

[01:19:53.840] the validation logic and then just run

[01:19:56.719] the automated verification steps from

[01:19:58.960] the plan. Don't use make. Don't read the

[01:20:00.960] make file. Just run the cargo test

[01:20:02.880] commands as documented.

[01:20:04.560] >> H interesting. Send it.

[01:20:07.679] >> I got to give it the plan path.

[01:20:10.560] >> Did you stop the other one? Oh,

[01:20:12.080] >> so we're paraly Yeah, we're paralyzing

[01:20:14.640] here, but we're paralyzing between phase

[01:20:17.120] one and also iterating on phase two.

[01:20:19.440] >> Cool. So, it's going to run. I guess

[01:20:21.199] it's going to run stuff, I guess. Auto

[01:20:22.880] approve everything. Okay, cool. Let me

[01:20:24.960] keep reading. I know why this error

[01:20:27.199] handling is happening incorrectly.

[01:20:29.679] The reason that this is happening is

[01:20:30.880] this should actually be done in phase

[01:20:33.360] that should be handled in phase three

[01:20:35.199] later, not in phase one. So we don't

[01:20:37.760] actually have to use exposed error yet.

[01:20:39.600] >> We're already in we're already in phase

[01:20:41.040] three here.

[01:20:42.480] >> No, in the implementation that's phase

[01:20:45.280] two. Yeah, like the error go down.

[01:20:48.320] >> Yeah,

[01:20:48.800] >> go down a little bit more. Go down a

[01:20:51.280] little bit more. Oh, go down. Oh, it's

[01:20:54.640] during time implementation. Okay,

[01:20:56.000] >> I think it's decided that there's no

[01:20:57.520] extra stuff to do. It's already It's

[01:20:59.280] already done.

[01:21:00.480] >> All right, cool. Let's go down.

[01:21:02.239] >> You want to look at timeout

[01:21:03.520] implementation?

[01:21:04.320] >> Yes. Cool. That's correct. Don't set a

[01:21:07.440] timeout. Okay, that's correct. Um, don't

[01:21:10.400] do any of the WAMOM stuff. Tell it tell

[01:21:13.440] ignore WASOM

[01:21:15.520] in phase three.

[01:21:16.800] >> Well, now this is trying to do a bunch

[01:21:19.360] of stuff in phase. Which phase is this?

[01:21:24.239] In phase three.

[01:21:25.840] >> Uh, let's just see what it did.

[01:21:28.400] And then I think so we're what? We're in

[01:21:30.719] uh 11:42. So it's been about an hour and

[01:21:33.040] 45 minutes

[01:21:34.880] >> since we've been doing this.

[01:21:36.239] >> Um okay. So this is the actual error

[01:21:38.320] detection happening here. Um

[01:21:41.760] where we're like updating the enum.

[01:21:43.760] Basically, we're adding timeout to the

[01:21:45.199] error code. Even this seems correct

[01:21:48.159] because we're going to like emit this

[01:21:49.520] from inside the actual like client

[01:21:51.679] handling.

[01:21:52.400] >> Okay, I'm down for that.

[01:21:54.080] >> Okay, so yeah, if we Yeah. Okay,

[01:21:56.719] >> cool. That makes sense.

[01:21:57.920] >> Use the message. Otherwise, we parse the

[01:22:00.320] HTTP error.

[01:22:01.280] >> We go up.

[01:22:02.239] >> Yep.

[01:22:02.719] >> I want to read a couple more things.

[01:22:04.239] >> Yeah,

[01:22:05.120] >> the timeout error will need to have uh

[01:22:08.000] the client name as well.

[01:22:10.560] >> Which phase is this? I missed the

[01:22:12.400] outline. Can I get an outline?

[01:22:13.760] >> No, you can just get an outline. It's on

[01:22:14.960] the right side. Uh it's one of those it

[01:22:18.239] is that one. Click on that the right

[01:22:20.159] side. That icon that you had the

[01:22:21.440] sidebar.

[01:22:23.040] Nope. And then at the top. Yeah, that

[01:22:24.880] one.

[01:22:25.360] >> Yeah. Okay, cool. Oh, that's so much

[01:22:26.880] better. Okay, cool. So, in phase three,

[01:22:31.280] sorry, it was the

[01:22:33.040] >> section four.

[01:22:35.280] >> Phase 3.4.

[01:22:37.120] >> Uh, section five.

[01:22:40.719] >> Oh, that one.

[01:22:41.760] >> This one.

[01:22:42.800] >> The create errors. This part needs the

[01:22:45.520] client name as well.

[01:22:46.719] >> It needs the client information as well.

[01:22:48.480] Since uh specifically you can tell it

[01:22:50.639] since timeout error extends from client

[01:22:54.239] http client error.

[01:22:56.639] >> Cool. Let's go on. Um yeah, I'm just

[01:22:59.679] going to check on this one.

[01:23:01.920] Okay, that looks good. It's running the

[01:23:03.199] test. It's making some

[01:23:05.760] some fixes based on some parsing errors.

[01:23:08.880] So this is the other thing that's really

[01:23:10.000] important is like the better your test,

[01:23:11.280] the more you can give the model an

[01:23:12.639] objective measure of whether it's

[01:23:14.480] correct or not. A lot of people talk

[01:23:15.760] about like LM as judge or code review

[01:23:17.760] agents and it's like the LMS are bad at

[01:23:20.880] judging things if you ask me, but they

[01:23:22.719] are good at reading errors and fixing

[01:23:24.480] them. Um, and this is also why like you

[01:23:26.880] don't necessarily always want to obsess

[01:23:28.719] over getting the plan perfect. Um, you

[01:23:32.080] just you just need to be get be good

[01:23:33.920] enough to get the LM into this state

[01:23:35.520] where it's it has structuring the right

[01:23:37.120] code. It's putting the right things in

[01:23:38.320] the right places. It's using the right

[01:23:39.600] libraries and the right implementations.

[01:23:41.920] And then if there's syntax errors or the

[01:23:44.239] wrong method is used here, it's not

[01:23:46.080] cloned properly, then then the model can

[01:23:48.159] fix all that.

[01:23:49.199] >> Yes.

[01:23:49.760] >> Yes.

[01:23:50.080] >> Cool.

[01:23:50.800] >> Let's keep reading.

[01:23:51.360] >> Um, we'll let that one keep running.

[01:23:53.040] We'll go back to our plan iteration

[01:23:55.199] session. Um, looks like that did it

[01:23:59.040] correctly.

[01:24:00.880] Um, let's find that clone.

[01:24:04.639] >> Yeah.

[01:24:04.880] >> Um, yeah. Client name client.clone. That

[01:24:07.120] looks right.

[01:24:07.840] >> Yes, that looks correct.

[01:24:09.120] >> Cool. And then the composite client

[01:24:11.679] total timeout.

[01:24:13.440] >> Um, this part is the part that scares

[01:24:15.280] me. So, honestly, part of me is like

[01:24:17.840] because I actually don't know how to

[01:24:18.960] implement this. So, let me just um look

[01:24:21.600] at this. Um, go down.

[01:24:24.800] Okay, I guess sleep until deadline.

[01:24:26.480] That's great. Never completes if no

[01:24:28.320] deadline. I mean, this will probably

[01:24:30.719] work. I think this will probably work.

[01:24:33.920] >> This is all existing code pretty much,

[01:24:35.600] right?

[01:24:37.360] >> Yes.

[01:24:39.120] says or however client name is accessed.

[01:24:42.560] Should we have it go put that make that

[01:24:44.159] correct or you fine to have it fix that

[01:24:46.800] during the test cycle?

[01:24:48.320] >> Um I think that that's actually correct.

[01:24:51.840] >> Okay, cool.

[01:24:52.639] >> I'm trying to remember in my code.

[01:24:54.239] >> Yeah, if you're like I'm not sure then

[01:24:55.760] we can have it go do a little bit more

[01:24:57.199] research on the side and figure that

[01:24:58.639] out. Um but that's like yeah for

[01:25:00.639] pinpoint research then you can just

[01:25:02.400] steer to the sub agents. You don't have

[01:25:03.840] to go create a new research document.

[01:25:05.360] Part of me is also thinking that we

[01:25:07.040] should actually ignore composite uh

[01:25:09.120] composite clients for now.

[01:25:10.960] >> For now, just to simplify the plan.

[01:25:12.960] >> Just to simplify the plan like uh like

[01:25:15.040] for now let's just make sure that the

[01:25:16.400] actual errors work for like primitive

[01:25:18.560] clients.

[01:25:19.440] >> Okay. So let's move the composite client

[01:25:23.120] timeouts implementation

[01:25:25.679] >> retry

[01:25:26.639] >> timeout retry implementation into its

[01:25:29.760] own phase after phase three.

[01:25:33.040] >> Yes.

[01:25:33.440] >> Yeah.

[01:25:34.080] >> Yes. I feel way better about that. Um,

[01:25:36.080] just because like I'm like I don't know

[01:25:37.280] how the stuff is going to work. I want

[01:25:38.960] to be able to get errors fully working

[01:25:40.560] for like perfect timeouts.

[01:25:42.639] >> And when you start building like the

[01:25:44.639] other thing is too is you're going to

[01:25:45.760] learn things as you do the

[01:25:46.719] implementation plan. And so like the

[01:25:49.120] smaller you can make your phases the

[01:25:50.639] more you can be like cool we're going to

[01:25:51.679] implement phase one and get that working

[01:25:53.199] and then we're going to go from there.

[01:25:55.199] And um

[01:25:57.440] >> how do I say it?

[01:25:59.040] You may have learnings that cause you to

[01:26:00.639] change the rest of your plan in in the

[01:26:02.320] in the earlier in the earlier phases.

[01:26:04.480] >> Can we go see the other one? See if it's

[01:26:06.080] done.

[01:26:06.480] >> Yeah, let's take a look.

[01:26:07.840] >> It is.

[01:26:09.199] >> Says it's done.

[01:26:10.480] >> Okay. So, here's here's how I know what

[01:26:12.400] to do now. What I know now is I want to

[01:26:14.480] go look at the validation files that it

[01:26:15.920] created. I'm actually not even going to

[01:26:18.159] look at the diff. Let's just look at the

[01:26:19.280] validation file.

[01:26:20.000] >> This is the thing is like yeah, if you

[01:26:21.280] can if you can read the tests and you

[01:26:23.199] know they work, then you don't actually

[01:26:24.560] have to read every line of code. This is

[01:26:26.159] the really powerful bit. It's in uh it's

[01:26:28.639] in Baml. It's on BAML runtime. It's in

[01:26:30.560] BAML lib

[01:26:33.040] uh client. Yeah. So, it made some of

[01:26:34.800] these. I don't know which ones it made,

[01:26:36.000] but it made some.

[01:26:38.639] >> It should have. If it didn't make these,

[01:26:40.239] we know we're here. Here we go.

[01:26:42.000] >> Here's the new ones.

[01:26:43.520] >> Okay. Can you Can you disable the syntax

[01:26:46.400] here?

[01:26:46.639] >> I don't know how to do that.

[01:26:47.760] >> Okay. Well, I don't know either. That

[01:26:49.520] won't do it either. Um Oh, just select a

[01:26:53.440] different file extension like text. The

[01:26:55.760] LSP is always going to pick it. Okay.

[01:26:57.360] Well, command. Never mind.

[01:27:00.000] >> There we go. LSP still serves it. It's

[01:27:02.320] good.

[01:27:03.120] >> Oh, no.

[01:27:03.679] >> It's fine. It's fine. I'll just ignore

[01:27:04.960] it regardless. Um, yeah, there's one

[01:27:08.480] pain point that we have to deal with in

[01:27:09.679] our repo and we've got configurations

[01:27:11.280] set up.

[01:27:12.239] >> But let's just go read this. So, we have

[01:27:13.600] a client. We do this and then we do

[01:27:15.280] this. Cool. It says what? What's the

[01:27:18.000] error? Unsupported property http. That

[01:27:20.960] looks like a bad error.

[01:27:22.400] >> Yeah, that looks wrong. It didn't

[01:27:23.840] actually pull it in.

[01:27:25.520] Yes. Unsupported property HTTP. Go on.

[01:27:28.080] Let's read the next one. What does that

[01:27:29.520] say?

[01:27:31.040] >> Unrecognized fields and configuration

[01:27:32.800] block connect time. This is for the

[01:27:34.320] typo.

[01:27:35.199] >> Yes. Um uh can you can you actually tell

[01:27:38.880] it to s make a recommendation for what

[01:27:41.520] thing to make? I don't like this error.

[01:27:43.520] >> Um

[01:27:44.080] >> it should recommend a we

[01:27:47.440] always like Yeah, you should paste just

[01:27:49.520] paste the error.

[01:27:50.239] >> Yeah. Yeah.

[01:27:50.719] >> And just say I prefer Yeah. and just say

[01:27:52.719] I prefer a error that recommends

[01:27:55.679] >> Here it is.

[01:27:56.239] >> Wait, why did that not work?

[01:27:58.320] >> It's here. It's just I was wrapped.

[01:27:59.920] >> Wait, what does it say? First token

[01:28:01.199] connect timeout. MS. Wait, why does it

[01:28:03.760] say connect timeout? That is valid.

[01:28:05.120] >> There's a timeout. There's a typo here.

[01:28:08.400] >> What's a typo?

[01:28:09.920] >> Typo is there's only one N in connect.

[01:28:12.239] >> Oh, okay.

[01:28:14.719] Can you actually tell it though? Give a

[01:28:16.400] recommendation on best match. Yes. And

[01:28:18.480] we have some functions to already do

[01:28:20.159] that. Um, can you do me a favor? Um,

[01:28:23.760] it's fine.

[01:28:25.360] >> I'm I'm uh giving you the gift of gift

[01:28:27.840] of taste.

[01:28:29.199] >> Okay. Well, go back.

[01:28:30.639] >> Okay. You want to read some more?

[01:28:31.920] >> Yep.

[01:28:32.480] >> That looks good. And again, these

[01:28:33.840] examples execute, right? When you run

[01:28:35.440] cargo test, it actually like makes sure

[01:28:37.360] these errors match.

[01:28:38.480] >> This is good. This should be a map. This

[01:28:40.320] is fantastic.

[01:28:42.480] Error for Oh, what does it say?

[01:28:46.639] >> Total timeout is not supported in like

[01:28:49.040] lowle. This is only for composite

[01:28:50.719] clients.

[01:28:51.840] >> Yes.

[01:28:53.520] Cool. Unsupported property http. We

[01:28:55.840] should

[01:28:56.080] >> So some of these didn't work.

[01:28:58.560] >> Yes. So we should figure out why. Oh,

[01:29:00.880] it's because validation for uh those

[01:29:03.600] clients are different. So we should tell

[01:29:04.880] it that.

[01:29:05.440] >> Okay. So the error in this file is

[01:29:09.760] incorrect. Um the validation for the

[01:29:13.040] orchestrator clients is different. Um,

[01:29:16.000] and so we need to make sure that HTTP is

[01:29:18.000] supported in those as well.

[01:29:20.239] >> It's for fallback. It's just a composite

[01:29:22.239] clients and like this is just like if

[01:29:24.800] you have a good testing framework, this

[01:29:26.239] is much faster to test because I know

[01:29:27.840] for sure that the code is running and

[01:29:29.360] parsing everything accordingly.

[01:29:31.360] >> Yep. Okay. We're getting high in context

[01:29:34.159] as well. So, um, I am

[01:29:36.719] >> This takes a while to run the test. I'm

[01:29:38.400] going to have to restart it. It's still

[01:29:40.560] it's still doing the previous thing, so

[01:29:41.679] I don't I don't want to interrupt it.

[01:29:43.600] >> Cool.

[01:29:45.040] So at this point what we have is we kind

[01:29:47.040] of have we have the parsing working. We

[01:29:49.280] have the data plumbed through the right

[01:29:50.639] classes probably and I say probably

[01:29:52.880] because I haven't actually looked at the

[01:29:53.920] code but I do know the parsing is

[01:29:55.280] working and like we've plumbed through

[01:29:56.480] the most important part which is like

[01:29:58.080] user syntax into the data model.

[01:30:01.360] >> Yep. Can kind of skim through here.

[01:30:04.320] Cool. Building programming languages is

[01:30:06.719] fun.

[01:30:07.280] >> Yeah. It's interesting at the very

[01:30:08.800] least.

[01:30:09.840] >> Is it normal for this to have no output?

[01:30:12.239] >> Yeah.

[01:30:12.719] >> Because we did a grab. Yeah. Okay.

[01:30:14.480] >> Yeah. Yeah.

[01:30:15.520] >> Cool. Our new er Yeah, the tests are

[01:30:17.040] failing because our new error messages

[01:30:18.320] are different. So, it's going to run it

[01:30:19.440] with update expect. Let's see what the

[01:30:21.280] new error messages look like.

[01:30:23.840] Yeah. Look at that. We got our fuzzy

[01:30:26.560] finding working.

[01:30:28.000] >> Yeah, it

[01:30:30.719] >> this looks better, right?

[01:30:32.159] >> It's slightly better. There's still

[01:30:33.360] better things I would do, but I'm okay

[01:30:34.560] with this for now.

[01:30:35.679] >> Okay. I mean, that that's the kind of

[01:30:36.960] thing that's probably We've seen that

[01:30:38.159] it's easy to polish that part. Cool. I

[01:30:40.880] just I would just let the last I would

[01:30:42.400] just let the last thing rip even though

[01:30:43.920] I

[01:30:44.480] >> Yeah. Yeah. No, I I sent it.

[01:30:46.400] >> Okay, cool. Just going to go work on

[01:30:48.960] that. Um here's our planeration.

[01:30:51.840] >> So, new structure, parse and validate,

[01:30:53.679] define error types, implement basic

[01:30:55.199] timeouts, implement composite timeouts,

[01:30:57.040] implement streaming timeouts, testing

[01:30:58.719] and documentation, runtime

[01:31:00.000] configuration.

[01:31:01.199] >> Yes, good.

[01:31:02.159] >> I actually will probably do streaming

[01:31:04.159] phase five before phase four. That's

[01:31:06.000] actually the only difference I'd make.

[01:31:07.040] And the idea is like I want to get the

[01:31:08.400] primitive clients fully working end to

[01:31:10.480] end

[01:31:11.199] >> before I touch anything about the

[01:31:12.239] composite client. This also makes

[01:31:13.600] testing a lot easier.

[01:31:15.040] >> So that's another guideline. Um changing

[01:31:18.159] spec. Um we'll have it like guidelines

[01:31:23.040] to add to create plan.md. This is the

[01:31:26.560] thing you should always be doing when

[01:31:27.600] you're working with this and you find a

[01:31:28.639] thing like oh I always want the model to

[01:31:30.239] do things X way. Then you want to move

[01:31:31.760] it into your infrastructure which is

[01:31:33.120] your your commands and your agents. Um

[01:31:36.080] so number one was

[01:31:38.480] guidance on cargo test generating new

[01:31:43.520] error messages

[01:31:46.639] tests etc. And then the other one was

[01:31:49.600] always implement basic HTTP then

[01:31:53.760] streaming then composite clients in that

[01:31:57.280] order.

[01:31:58.719] >> Yep.

[01:31:59.679] >> But I I I personally probably wouldn't

[01:32:01.440] put this in cloud MD because it's so

[01:32:03.120] specific to this thing.

[01:32:05.199] Yeah, there's some there's somewhere

[01:32:06.639] where you might want to write this down

[01:32:07.760] or keep it handy. We're also like you

[01:32:09.440] may have like prompt snippets that you

[01:32:10.880] store and that's just a thing whenever

[01:32:12.480] you're changing the HTTP client logic.

[01:32:15.199] Okay. So, yeah. Okay. Basic timeout,

[01:32:18.000] streaming timeouts, composite client,

[01:32:19.440] testing and docs, runtime configuration.

[01:32:21.280] I don't know what phase 7 is, but we'll

[01:32:22.800] get there. All right. You want to read

[01:32:25.280] phase four then?

[01:32:26.480] >> Yes, please.

[01:32:27.600] >> Cool. Time to first token and idle

[01:32:29.440] timeout. Here we go.

[01:32:30.560] >> Okay, this looks pretty good. H. Okay, I

[01:32:33.360] see. Okay. Yep, that looks good.

[01:32:35.760] >> Literally counting clocks. Clocks are

[01:32:39.120] hard. Okay. So, if this resolves and we

[01:32:41.280] haven't gotten a token, then we go.

[01:32:43.520] Otherwise, it's the other one.

[01:32:46.159] >> Yep.

[01:32:47.520] >> Cool.

[01:32:47.920] >> Otherwise, we just get the next token.

[01:32:49.360] We just keep alive.

[01:32:50.480] >> Yeah. Okay. So, then we set this, then

[01:32:52.239] we have to keep alive.

[01:32:54.560] >> Cool.

[01:32:54.880] >> Yep.

[01:32:55.360] >> Cool. And yeah, look, I like how it's

[01:32:57.440] staying brief here. Cool. And then in

[01:33:01.040] each client we have to pass in the HTTP

[01:33:03.520] config to the stream handler.

[01:33:06.000] Okay,

[01:33:07.600] sounds good.

[01:33:08.480] >> This looks good to me.

[01:33:09.840] >> Okay, I think we're still on phase one

[01:33:12.239] over here, but I'm just going to do

[01:33:14.560] infinite bypass.

[01:33:16.480] >> Yeah. And then there is a technical

[01:33:18.159] design thing that I need to think about

[01:33:19.360] which is how do what do we want

[01:33:20.719] fallbacks to do on certain types of

[01:33:22.639] errors? And I think we want the

[01:33:24.800] fallbacks to treat like time to first

[01:33:27.199] token errors like errors that it just

[01:33:28.719] like timeout errors are like things that

[01:33:30.719] fallbacks consume and don't forward up.

[01:33:33.600] You just get told that a timeout happens

[01:33:35.280] and then you just move forward. So I

[01:33:36.719] need to think about how composits will

[01:33:38.080] play into that. But I think this will

[01:33:39.360] just work as is right now.

[01:33:42.080] >> Um sorry. So it's like how do composite

[01:33:46.400] clients happen handle timeouts from

[01:33:51.199] children?

[01:33:52.320] >> Exact. And it's not just composit, it's

[01:33:53.679] like retry policies as well. Cuz one

[01:33:55.440] thing you could say is we want to error

[01:33:56.800] out completely

[01:33:59.840] on this. But I think what we're going to

[01:34:01.199] do with timeout errors is uh is not what

[01:34:03.440] we do with abort. On abort

[01:34:06.159] we want to exit fully.

[01:34:08.719] >> Yeah.

[01:34:09.520] >> Timeouts we don't.

[01:34:10.719] >> Yeah. I think a timeout Well, so

[01:34:12.159] sometimes a timeout is like I want to

[01:34:13.600] guarantee that I actually get a response

[01:34:15.360] to the user in some amount of time. But

[01:34:17.679] I think in general, yeah, timeouts are

[01:34:19.920] retriable if it's if you're dealing with

[01:34:21.679] like shoddy upstream infrastructure.

[01:34:24.080] >> Yeah, exactly. Um, and then this should

[01:34:26.719] almost be done.

[01:34:28.480] >> So, let's see. It's doing the

[01:34:30.639] expectations now.

[01:34:32.719] >> Yeah, it's doing the other one where

[01:34:34.000] it's actually running like the HTTP one

[01:34:36.480] >> generated two warnings.

[01:34:37.360] >> Problem with Rust, honestly, is the

[01:34:39.040] worst part about Rust is yes, while it

[01:34:40.560] compiles, it does work.

[01:34:42.320] >> Uh, it is kind of slow to compile. Not

[01:34:44.880] allowed for composite unsupported

[01:34:47.120] property. Yeah, this one's still wrong.

[01:34:49.280] Unsupported property. Yeah, it's still

[01:34:51.840] not figuring this out. So, we've given

[01:34:53.760] it feedback and it hasn't figured it

[01:34:55.920] out. And so, my take here is we actually

[01:34:57.920] need to go update the plan more

[01:35:01.040] um or add like a phase 1B that is like

[01:35:04.080] fix this thing before we move on.

[01:35:06.320] >> Yeah.

[01:35:07.679] >> You see what I mean? Like the composite

[01:35:09.040] clients are still not able to fix this.

[01:35:11.199] Yes,

[01:35:11.520] >> this is correct. But this one on

[01:35:14.719] supported property is still the error.

[01:35:16.560] It looks like something actually died

[01:35:18.239] and it didn't make the updates.

[01:35:20.320] >> Okay. Well, while this is running, we'll

[01:35:21.840] see how this runs.

[01:35:23.040] >> Yep. Most tests are passing. All

[01:35:25.040] validation tests are now passing. Oh,

[01:35:27.360] this is valid. Great. Type field name

[01:35:30.080] not allowed for composite. Okay, this is

[01:35:32.800] better. This is the right error. This is

[01:35:34.480] not failing on HTTP now. So, it did fix

[01:35:36.320] it.

[01:35:36.880] >> Exactly.

[01:35:38.000] >> Okay, cool.

[01:35:39.760] >> Um,

[01:35:40.320] >> amazing. I'm going to commit this. do

[01:35:42.639] it. And that's good. That's a good thing

[01:35:44.080] to commit. So, like now we're done.

[01:35:45.360] We're phase one.

[01:35:46.400] >> Yep. And I will leave the I will leave

[01:35:48.400] all the files and specs and stuff in

[01:35:50.800] there. You can go clean them out of the

[01:35:52.080] PR if you want to.

[01:35:52.960] >> Yeah, I will do that. Can you can you

[01:35:55.280] show the phase one so people can see

[01:35:56.800] what the what the check boxes did?

[01:35:59.600] >> Yeah.

[01:36:00.080] >> Yep. And so it actually will check the

[01:36:02.080] system will actually automatically check

[01:36:03.280] off these stuff for you so you actually

[01:36:04.560] know what you're done.

[01:36:05.679] >> I actually just I Go ahead. I was going

[01:36:08.239] to say and the the implement plan prompt

[01:36:11.280] has a little bit of extra steering in it

[01:36:13.360] to basically like make it able to

[01:36:15.920] resume. So it's like if it has existing

[01:36:17.600] check marks, trust that that's done,

[01:36:19.280] pick up from the first unchecked item

[01:36:20.719] and verify previous work only if

[01:36:22.400] something seems off.

[01:36:23.440] >> Yeah, exactly. So if we go back and take

[01:36:25.120] a look at this, uh we can remove the

[01:36:26.639] manual manual verification. We're done.

[01:36:28.719] Or check it off yourself and probably

[01:36:30.239] want to delete stop here for human

[01:36:31.840] input.

[01:36:34.639] >> Yeah. Okay, let's go compile the rest of

[01:36:36.719] this. Can we look at the compilation

[01:36:38.400] steps in error type definitions?

[01:36:42.159] >> The Oh, the verification steps. It's

[01:36:44.400] going to try to run this with make

[01:36:45.679] again.

[01:36:46.960] >> Yes. So, you should tell it how to do

[01:36:49.440] this.

[01:36:51.199] >> Sorry. I'm just going to do this.

[01:36:53.520] >> Okay. Yeah. I didn't know that you make

[01:36:56.560] so aggressively in your code.

[01:36:58.159] >> I like make because it's language

[01:37:00.000] independent and we use a lot of

[01:37:01.199] different languages.

[01:37:02.880] >> We do too, but it's interesting. I wish

[01:37:05.600] there was a way to just not load

[01:37:09.040] this because now your make file is going

[01:37:10.480] to be not have all your stuff that you

[01:37:12.400] need.

[01:37:12.960] >> That's fine. I'm going to keep this one

[01:37:14.400] in. Yeah, this this shouldn't be in my

[01:37:16.400] global thing anyways. That's better.

[01:37:19.119] Cool. There's your secret alpha for the

[01:37:21.679] day is snippets of my claw MD.

[01:37:24.239] >> There you go. Um, cool.

[01:37:27.920] >> All right. So, uh, we use this commit

[01:37:29.760] command that kind of splits things out

[01:37:31.280] into logical files.

[01:37:34.000] It's fine. I probably could have just

[01:37:35.360] told it to just make one commit, but um

[01:37:37.280] are you ready to jump to phase two?

[01:37:39.280] >> I am. So, we just phase two.

[01:37:41.840] >> Let's do it. Um we haven't read the

[01:37:44.639] later phases, but we'll kick that off

[01:37:46.000] and then we'll go back and read the f

[01:37:47.440] the later phases of the plan. Cool. So,

[01:37:51.520] um

[01:37:53.440] BAML 1630 phase 2

[01:37:57.600] only doing phase two. I guess that's

[01:38:00.159] fine.

[01:38:01.600] >> That's probably good. Let's rip, baby.

[01:38:03.920] You got this.

[01:38:05.760] >> Um, you might also want to tell it

[01:38:07.760] something else. Um, yep. Which is the

[01:38:10.159] way that you we run tests. So, let me

[01:38:12.159] send that to you in Slack. So, that way

[01:38:13.760] you have that for Python.

[01:38:15.920] >> Um, yeah. Actually, we should up before

[01:38:18.320] we start this, we should update the plan

[01:38:19.840] to have that. You want to slack it to

[01:38:21.520] me?

[01:38:21.840] >> Yes. Um, I will give this to you. I'm

[01:38:23.679] giving it to you. One second,

[01:38:26.239] >> Elder. For your question about Sonnet 45

[01:38:28.480] versus Opus. Sonet45 writes good code,

[01:38:31.600] but when you want to reason over a long

[01:38:33.440] complex codebase, you really want to be

[01:38:35.199] using Opus most most of the time.

[01:38:36.719] >> All right, I sent it to you. This is how

[01:38:37.840] we run uh let me let tell you how we run

[01:38:41.840] then uh and just tell it to not run the

[01:38:44.800] typescript test. It'll just take too

[01:38:46.480] long.

[01:38:46.880] >> Are we also doing cargo test?

[01:38:49.199] >> Yes.

[01:38:49.760] >> Yes. Uh we don't really Yeah, probably

[01:38:52.400] to just compile check like the previous

[01:38:54.560] test should still pass.

[01:38:56.239] >> Yep. Okay, cool. Cool. Yeah. So, we'll

[01:38:58.880] update that in the plan and then we have

[01:39:00.719] a look.

[01:39:02.719] Cargo build, cargo test,

[01:39:05.440] do this, do this, do this.

[01:39:10.400] Do you want to do the rough check?

[01:39:12.400] >> Yeah.

[01:39:13.119] >> Okay.

[01:39:13.600] >> That's how you check that everything is

[01:39:14.880] compile time working.

[01:39:16.320] >> Do you want to do the build here or skip

[01:39:18.239] all Typescript?

[01:39:19.920] >> Just skip all Typescript. Uh, yeah,

[01:39:22.800] exactly.

[01:39:24.159] >> I assume if we weren't on a stream, you

[01:39:25.840] would run the TypeScript tests.

[01:39:27.920] No, I'd probably not. If it it's like if

[01:39:30.880] Python compiles and TypeScript doesn't

[01:39:32.639] compile, it's really rare. It's probably

[01:39:34.080] good enough. I'd run it at the very end

[01:39:36.080] because again, my most my most important

[01:39:38.159] resource is my time. So like I'm

[01:39:40.320] optimizing for my time here. So like I

[01:39:42.560] have a pretty good proxy that the test

[01:39:44.000] will probably pass. And I know I'm going

[01:39:45.119] to run.

[01:39:45.360] >> If the Python's good, then you know the

[01:39:46.719] TypeScript's good.

[01:39:47.760] >> Yeah. And I know I'm going to run the

[01:39:49.040] test eventually. So it's like it's not

[01:39:50.480] like I'm not going to do it.

[01:39:52.400] >> Cool.

[01:39:54.080] Amazing. No, I run cloud code directly

[01:39:56.400] on my machine. And the reason is like

[01:39:58.719] honestly even if I'm using Opus, I am

[01:40:01.760] still restricted to the directory I'm

[01:40:03.520] operating in. So it's okay. If the model

[01:40:05.920] does end up doing something really

[01:40:06.960] malicious, I think you could just like

[01:40:08.480] prevent certain you could just like

[01:40:10.080] blacklist certain commands.

[01:40:12.320] So like for example, I know Dexter did

[01:40:14.239] something interesting. You type Python

[01:40:15.360] into your shell, Dexter.

[01:40:17.679] >> Uh oh, I had to get rid of that.

[01:40:20.159] >> Okay. Uh, but yeah, I had a

[01:40:23.440] >> Dexter had a command where if you typed

[01:40:24.800] in Python directly into your shell, it

[01:40:26.639] would it would shim it. Um, it would

[01:40:31.520] shim Python to say echo use uh UV

[01:40:35.440] instead to make sure that the model

[01:40:37.280] could never do anything wrong.

[01:40:40.080] Um, and that helped a lot

[01:40:42.239] >> because there's Python in the cloud

[01:40:44.159] default system prompt.

[01:40:46.159] >> Yes.

[01:40:46.480] >> But now if I run Python,

[01:40:47.840] >> get the reload source.

[01:40:50.159] >> It's in there. It's because the first

[01:40:51.440] one isn't found. It's not a real thing.

[01:40:52.719] You have double slash that goes to root.

[01:40:56.000] >> Ah, all right. Well, I'm not going to go

[01:40:58.080] messing around with my files. But yes,

[01:40:59.760] there that's that's the basic idea is

[01:41:01.600] you just replace Python. The first thing

[01:41:03.440] in your path should be something else.

[01:41:05.600] >> Yeah, that way if the model does it just

[01:41:07.440] will not trigger the wrong Python. So I

[01:41:09.280] think it's the same for all cloud code

[01:41:10.880] stuff.

[01:41:11.760] >> Yep.

[01:41:13.360] Okay. So this one is ripping. That said,

[01:41:15.199] I have had a friend who actually had

[01:41:18.000] claude code or cur I think cursor

[01:41:19.600] actually not cla code

[01:41:21.119] >> run rm-rf

[01:41:23.679] >> uh in a very scary scary directory in

[01:41:25.600] the home directory tilda slash.

[01:41:28.159] >> Yeah, you shouldn't do that.

[01:41:30.080] >> And it did that because it actually made

[01:41:31.760] a directory called tilda by accident in

[01:41:34.159] the local folder and then it started

[01:41:36.480] running that as a shell command to

[01:41:37.840] delete that directory and that is um not

[01:41:40.159] good.

[01:41:41.679] >> Do not want that. Yes. Internal

[01:41:43.679] monkeypatch.py.

[01:41:46.080] >> Yeah, we've done some interesting stuff.

[01:41:49.280] >> Does look right.

[01:41:50.159] >> Yeah, I mean that stuff looks right.

[01:41:51.920] >> Yeah. Okay. Um, cool. We are at hour two

[01:41:56.639] and we're getting through it. Um,

[01:41:59.760] we should think about what's next.

[01:42:03.199] >> I think what's going to end up happening

[01:42:04.239] is we'll get the timeout implementation.

[01:42:06.080] Um, and I think it should work for the

[01:42:07.920] connect and request timeout.

[01:42:09.920] >> Mhm. Um

[01:42:12.080] like as long as time out can if you can

[01:42:14.159] you can you go back let's just make sure

[01:42:15.440] timeout request is actually

[01:42:18.480] >> this base three stuff

[01:42:19.840] >> is only doing the basic stuff. Yeah.

[01:42:21.840] >> Yeah.

[01:42:23.440] So here's our HTTP client. We've read

[01:42:25.199] that a bunch. Here's our request

[01:42:27.440] implementation

[01:42:29.679] and then we do that for all the

[01:42:30.800] providers

[01:42:32.880] and then we detect timeout errors in the

[01:42:35.520] execution.

[01:42:36.159] >> Yeah. Cool. That's correct. We should

[01:42:37.679] get rid of the was on the stuff there.

[01:42:40.639] Get rid of the wom stuff.

[01:42:42.000] >> Yeah, we don't need it. It'll just work.

[01:42:43.520] >> Let's remove the wom stuff from phase

[01:42:47.360] three. Just leave it out of

[01:42:50.159] >> Yep.

[01:42:51.679] >> This is crazy.

[01:42:52.800] >> It's going to distract it.

[01:42:54.560] >> Um,

[01:42:55.679] >> can you go up really fast? I want to see

[01:42:57.280] a couple more things. I want to read

[01:42:58.480] this error code. Detecting timeouts. Go

[01:43:00.320] down. I want to read this.

[01:43:02.480] >> Um,

[01:43:04.239] request timeout. Error code timeout.

[01:43:06.239] That's good.

[01:43:07.199] >> Okay.

[01:43:08.400] >> Yep. Okay. Otherwise, we just do one

[01:43:11.199] from the status.

[01:43:12.239] >> Oh [ __ ] What was the code there before?

[01:43:15.040] Can you command Z this? I might have

[01:43:17.199] messed up. Maybe we did one.

[01:43:18.800] >> Uh, we can go see what the diff was.

[01:43:20.719] >> Oh, no. We do want that WASM stuff. I

[01:43:22.639] was wrong. Oh, this is undo. That was

[01:43:26.080] the original code in there. I thought it

[01:43:27.520] added for this spec, but that's actually

[01:43:28.880] the original code in there.

[01:43:30.159] >> Yeah, sometimes it's not 100% clear what

[01:43:32.239] it's it's like. It'll reproduce large

[01:43:34.480] blocks of the code. It's not always

[01:43:36.080] clear. I think this is the only thing

[01:43:37.840] that's added. Is this it? Let else.

[01:43:40.400] >> Yes, exactly.

[01:43:42.400] >> Um, cool. And then is fine.

[01:43:44.960] >> Yeah, that's fine.

[01:43:47.040] >> Um,

[01:43:48.880] okay. Let's scroll down.

[01:43:51.520] This looks good. Timeout error code, I

[01:43:54.400] guess. 408. I don't know what's a what's

[01:43:56.320] a timeout error code. Is that 408? HTB

[01:43:58.320] request timeout, I guess. So,

[01:44:00.000] >> I don't think it's an HTB code. Is it?

[01:44:03.760] >> I don't know. I'm going to Google that.

[01:44:05.440] >> There you go.

[01:44:06.000] >> Hey. Yeah. Request timeout.

[01:44:08.239] >> Okay. I've never seen this code before.

[01:44:10.880] It's one of those

[01:44:11.679] >> Well, HTV codes are very fascinating. I

[01:44:14.159] don't know what they have.

[01:44:14.880] >> Yeah.

[01:44:16.000] >> Let's see the

[01:44:16.880] >> one

[01:44:17.520] >> handle time orchestrator.

[01:44:20.239] All right. So, we get the response.

[01:44:22.960] If we get a timeout response, then we

[01:44:24.880] expose it as a client as a timeout.

[01:44:27.440] >> Timeout error.

[01:44:28.320] >> Perfect.

[01:44:29.840] Otherwise, we do that. Otherwise, we do

[01:44:31.440] that, which is perfect.

[01:44:33.840] >> Cool.

[01:44:34.960] >> Yeah. Does this look right?

[01:44:37.040] >> Um,

[01:44:39.440] I would add some more tests. I want

[01:44:42.080] phase before we do streaming timeouts

[01:44:43.840] like phase 3B

[01:44:45.360] >> almost

[01:44:46.320] >> should be add end to and a add a pi test

[01:44:49.040] inside of intest Python. Well, I would

[01:44:51.840] do phase 3B.

[01:44:53.760] I would make a separate phase a integy

[01:45:04.149] inside of in Yeah. Python test.

[01:45:04.159] >> Yeah.

[01:45:05.920] uh to validate the time matter at error.

[01:45:08.080] >> Uh yeah, use a pattern finder agent to

[01:45:12.400] see how this works

[01:45:14.639] >> and then yeah and then also give it the

[01:45:16.159] UV command that I gave you earlier to

[01:45:18.800] actually run how uh yeah there you go.

[01:45:21.600] >> Amazing. Um great I can see HTTP config

[01:45:24.960] as a default. I'm wondering

[01:45:27.679] okay yeah so we have done some tests now

[01:45:30.000] and finding a bunch of issues that we're

[01:45:31.679] going to go start. Wow, 300 lines of

[01:45:33.760] errors.

[01:45:35.280] >> Uh, this is the problem with Ross.

[01:45:36.639] They'll figure it out.

[01:45:37.760] >> Yeah. Okay, we're already very high in

[01:45:40.000] the context window, so I might actually

[01:45:42.400] stop it. There's a command I use called

[01:45:44.800] slash continue.

[01:45:46.800] >> I would let it I would let it go on for

[01:45:50.159] for a little bit longer.

[01:45:51.840] >> Nope, I'm not because they changed the

[01:45:53.440] the compaction window. This is going to

[01:45:55.199] compact in like the next two seconds.

[01:45:57.040] So, we're going to do a manual

[01:45:58.000] compaction.

[01:46:00.159] um create a handoff prompt about where

[01:46:02.000] we are and it should start with

[01:46:05.440] slashimplement plan and include a ref to

[01:46:09.679] the plan file. Fortunately, we might

[01:46:13.040] compact as part of this, which would be

[01:46:15.199] frustrating, but let's see if the

[01:46:17.280] context goes back down. Yeah, see it

[01:46:19.679] already compacted itself. [ __ ] Oh, I

[01:46:22.480] hate it. We're still going to do a

[01:46:24.000] handoff and start over.

[01:46:25.840] >> Okay,

[01:46:26.480] >> so this is the prompt it's going to use.

[01:46:28.159] Current status is mostly complete. Needs

[01:46:30.080] final testing and verification. We did

[01:46:31.600] all the stuff. Yes. Okay. Yes. So, we

[01:46:34.960] have a CLI to code layer that I use that

[01:46:37.040] basically lets you have human in loop

[01:46:39.119] for your compaction because it's going

[01:46:40.719] to run the CLI to launch the next

[01:46:42.480] session.

[01:46:43.040] >> So, Oh, it's just going to launch that

[01:46:44.480] for you.

[01:46:45.920] >> Exactly. Um, so you let the model create

[01:46:48.080] the prompt and then it's going to use

[01:46:49.760] the CLI to do it. Um, this is kind of a

[01:46:52.320] thing I've been playing with recently

[01:46:53.440] that I've been enjoying. It's kind of

[01:46:55.520] somewhere in between clear and compact.

[01:46:58.800] Um, but it's a nice form factor. So,

[01:47:00.480] yeah, this launched another one. And now

[01:47:02.880] we should have there's a state thing

[01:47:05.440] here, but it created this new one.

[01:47:09.760] >> That's cool.

[01:47:10.800] >> Um, yeah. So, here's the prompt that the

[01:47:12.639] other model generated. We're using

[01:47:14.080] implement plan. Here's the plan. And

[01:47:15.679] then, yeah, we go from there.

[01:47:17.520] >> Nice.

[01:47:18.800] >> Um, cool. Okay. So, phase two is

[01:47:21.440] rocking. This one we're going to we're

[01:47:23.280] going to we're going to axe.

[01:47:25.679] Um, and this one is looking for Python

[01:47:27.920] test patterns. So, I think it should

[01:47:29.280] have found them. Oh, opus. Come on.

[01:47:33.600] >> Are you out of opus?

[01:47:35.199] >> No, they're API erroring. This is why

[01:47:39.840] can't have nice things.

[01:47:42.800] Let's see.

[01:47:43.280] >> This is actually why I really like uh uh

[01:47:47.360] uh codeex. So, it actually does not go

[01:47:49.119] down as much.

[01:47:50.320] >> Let's see.

[01:47:52.159] Yeah. Okay, it's back. It's just a

[01:47:54.000] little spotty. I am hoping that the

[01:47:56.880] context from this agent from that took 3

[01:47:59.840] minutes searching for patterns is going

[01:48:01.440] to be available in our context window.

[01:48:03.040] Yeah. Okay, cool. It says based on the

[01:48:04.480] patterns I found. So, I think it did

[01:48:05.760] find things.

[01:48:07.679] That's good. Just going to tee up

[01:48:09.040] another one in case we need to make more

[01:48:10.800] changes. Oops. Yeah. Okay, that's fine.

[01:48:16.080] Nope, it's not. I didn't mean to send

[01:48:17.840] it. Front ends are hard. This one's

[01:48:20.480] still cooking.

[01:48:22.639] This one's

[01:48:24.400] ready. Okay. So, major updates. So,

[01:48:26.800] phase 3B integration testing for timeout

[01:48:29.360] errors. How's this look?

[01:48:31.199] >> Okay, that looks correct.

[01:48:34.639] That looks correct. 50 m timeout. That

[01:48:38.800] looks correct.

[01:48:39.520] >> A 500word essay. Cool.

[01:48:42.239] >> Um, and that should fail.

[01:48:45.360] Uh, go down.

[01:48:46.000] >> That's right. Provider open AI. Should

[01:48:47.600] this be

[01:48:48.400] >> That's fine. Okay.

[01:48:49.920] >> Um, let's read this.

[01:48:52.320] >> Yep. That should read time at Perfect.

[01:48:55.040] Um,

[01:48:55.440] >> nice.

[01:48:56.320] >> You're going too fast. I was sorry

[01:48:59.840] >> that one. Yes. Fails. Yep. Accounting

[01:49:02.239] for overhead of any kind. Why not? That

[01:49:04.560] makes sense.

[01:49:05.840] >> Abort after delay. Abort should still um

[01:49:09.920] >> should not be a timeout error. This is

[01:49:11.679] abort takes precedence.

[01:49:13.280] >> Yes.

[01:49:15.199] AB uh because when does a timeout error

[01:49:17.440] happen?

[01:49:19.520] Oh yeah. Yeah.

[01:49:20.400] >> Looks like 100 millconds takes a board

[01:49:22.239] takes precedence. That's amazing. Yeah,

[01:49:23.840] that's really good.

[01:49:26.639] >> Gone. Synchronous. Yep.

[01:49:29.920] We also time out in synchronous clients.

[01:49:32.080] That's perfect.

[01:49:34.800] Streaming. Streaming should also time

[01:49:36.480] out. That is perfect. Um

[01:49:39.840] >> and then we haven't implemented this.

[01:49:41.280] >> Yep. That's correct. That's correct.

[01:49:44.880] Include. This is the power of the

[01:49:46.400] codebase pattern finder.

[01:49:48.080] >> Yes.

[01:49:48.400] >> Is like if you're like I need to do this

[01:49:50.000] thing and I know it wasn't in the

[01:49:51.199] research, you can just steer it, go find

[01:49:52.639] the pattern and then use that.

[01:49:55.440] >> Yes, that is correct.

[01:49:57.199] >> Okay. Um and then updating the BAML

[01:49:59.840] config for tests. So this is timeout

[01:50:02.320] test clients. This is what gets used by

[01:50:04.880] the Python test.

[01:50:05.920] >> Yes,

[01:50:07.920] that this part it'll figure out that

[01:50:09.119] that part looks about right. Uh yeah,

[01:50:10.719] there you go. It figured it out.

[01:50:12.639] >> Cool. Sick.

[01:50:15.040] All right. Um,

[01:50:16.320] >> and I think this is kind of the point,

[01:50:17.600] like if I didn't know that we needed

[01:50:19.119] these phases, we could be endlessly

[01:50:21.199] spinning for a while, but I'm like, "Oh,

[01:50:22.800] I want the Rust code to compile, then I

[01:50:24.239] want the Python test to compile."

[01:50:26.159] >> It's the same way you would engineer if

[01:50:27.600] you were writing the code yourself.

[01:50:29.199] >> Exactly.

[01:50:30.880] >> Um, I think phase two is done. What do

[01:50:33.199] you want to look at to verify it

[01:50:34.400] manually?

[01:50:35.280] >> Um, just look at the diff in VS Code.

[01:50:38.000] Please don't show me the git diff here.

[01:50:40.000] I want to see what files changed. Show

[01:50:41.840] me the tree version.

[01:50:43.360] >> This? No. How do I show you the tree

[01:50:45.520] version? View is tree. Okay, cool. So,

[01:50:48.960] we got this. We got this.

[01:50:51.600] >> Okay. Yeah, it's just doing some like

[01:50:53.760] Oh, you didn't get the commit from last

[01:50:55.280] time. Interesting. Okay, that's fine.

[01:50:57.600] >> Looks like it didn't do all the

[01:50:59.679] providers, but maybe is OpenAI is like

[01:51:01.679] the base for everything.

[01:51:02.960] >> Um, I think this just mixed it from last

[01:51:05.199] time. It just fixed some compile bugs

[01:51:06.719] that your git commit didn't get.

[01:51:09.840] >> Yeah. Okay, this looks about right.

[01:51:12.239] >> Patch. Yeah, here we go. Typescript

[01:51:15.600] errors.

[01:51:18.080] >> Silent so you guys don't see my hear my

[01:51:20.080] text notifications all the time.

[01:51:23.600] Um, okay. Cool. Cool. Uh, all right.

[01:51:26.880] Let's start phase three.

[01:51:29.520] >> Cool. And I think the really nice thing

[01:51:31.119] that a lot of people underestimate in

[01:51:32.400] this workflow is just like how how like

[01:51:35.600] independent each step is. And like for

[01:51:37.840] context, this input this feature as you

[01:51:40.080] guys can tell is very nuanced. There's a

[01:51:42.000] lot of stages to it and it would have

[01:51:44.000] taken forever to implement this

[01:51:46.080] >> and by forever I mean like it probably

[01:51:47.599] would have taken an engineer on my team.

[01:51:49.760] >> A couple days.

[01:51:51.520] >> Yeah. One day maybe two days of time and

[01:51:54.719] that would be like a good implement. I I

[01:51:56.480] would be like very like I personally

[01:51:58.960] would be satisfied if it took me two

[01:52:00.159] days to go from like nothing to it

[01:52:01.599] working end to end. If we can get this

[01:52:03.360] thing working with me and Dex spending

[01:52:04.800] three hours here, this is clearly a win.

[01:52:07.760] And this is like while we're live

[01:52:08.960] streaming and also like not even trying

[01:52:10.239] to do other things and be super

[01:52:11.520] optimized here.

[01:52:13.040] >> I think it was just you and me and there

[01:52:14.560] was no stream. We weren't taking

[01:52:15.679] questions and trying to like talk

[01:52:17.199] through the thought process. We could

[01:52:19.040] use the downtime instead of explaining

[01:52:20.560] what we're doing. We would use the

[01:52:21.599] downtime to go like work a sec a

[01:52:23.360] separate feature in parallel. Phase

[01:52:24.880] three is about implementing the actual

[01:52:26.480] timeout functionality.

[01:52:28.480] Um and then timing wise I have this on

[01:52:30.159] till 1. Um I'm having to like commit and

[01:52:33.040] push what we get. We can either do a

[01:52:34.400] part two next week or we you can pick

[01:52:36.639] this and run with it yourself. I don't

[01:52:38.159] know. I don't know what you want to do.

[01:52:39.440] >> I think if we get this working end to

[01:52:40.880] end Python, I'm actually very happy. If

[01:52:43.119] this works, this means that

[01:52:45.599] >> like the re other reason I broke this

[01:52:47.280] out.

[01:52:48.080] >> Yeah.

[01:52:48.480] >> Is that I can actually ship this and

[01:52:49.920] make it usable by users very early on

[01:52:51.920] without putting the whole composite

[01:52:53.199] features and everything else in there.

[01:52:55.360] >> You would you would ship these new

[01:52:56.639] fields even if they didn't work for

[01:52:58.480] streaming and composite.

[01:53:00.080] >> Well, the

[01:53:00.719] >> I guess it's two separate features.

[01:53:02.960] Exactly. So composite, it comes to a

[01:53:05.040] separate feature. Exactly.

[01:53:06.960] >> But I would actually ship it for

[01:53:08.800] individual clients because that's still

[01:53:10.320] worth it.

[01:53:11.119] >> But you need language support for every

[01:53:13.040] language and you'd need those fields to

[01:53:15.040] work on every all three of those fields

[01:53:16.480] to work in every in every path so that

[01:53:18.400] you could document it.

[01:53:19.679] >> So I would do I would do phase 3B phase

[01:53:22.719] 4 with the streaming support and then

[01:53:24.560] I'd merge

[01:53:25.199] >> and then you chip it.

[01:53:26.560] >> Yes, that'd be enough. I don't need

[01:53:28.320] everything all the way end to end

[01:53:29.760] working. I don't need composite features

[01:53:31.119] to work. What is this? Runtime

[01:53:33.280] configuration and advanced features. Is

[01:53:34.880] this nonsense?

[01:53:35.840] >> No, this is correct.

[01:53:37.760] >> Ah, okay. This is like the dynamic

[01:53:39.599] client registry stuff.

[01:53:41.119] >> Yeah, exactly.

[01:53:42.320] >> Oh, it's very

[01:53:43.199] >> I would I would do this stuff. It's It

[01:53:44.719] is very fast. It just plugs into our

[01:53:46.080] codebase.

[01:53:47.119] >> Um, most of what we have is actually

[01:53:48.800] works really really simply with the

[01:53:50.320] whole system. It's designed in that way

[01:53:51.679] where it should be easy for AI to add

[01:53:53.199] these features or humans to add these

[01:53:54.320] features, which is why most sections you

[01:53:56.320] see are very short. We spend a lot of

[01:53:58.239] time on architecting our codebase. Like

[01:54:00.400] there's I I would say if you're vibe

[01:54:02.000] coding from scratch, this this approach

[01:54:04.320] will probably not work as well because

[01:54:06.639] your codebase has no like concrete

[01:54:08.480] architecture. Like for example, you know

[01:54:10.960] the place where it picked out the wrong

[01:54:12.480] error

[01:54:13.520] >> for the property types where it was

[01:54:14.800] recommending messages.

[01:54:16.400] >> Yeah.

[01:54:16.880] >> I that's actually incorrect the way it's

[01:54:18.639] done. We actually have a different way

[01:54:20.000] of doing it that will actually give you

[01:54:21.520] recommendations that we that's a

[01:54:23.040] standard format that we have that says

[01:54:24.400] here are all the options. Here's the

[01:54:25.599] thing the user typed in. Pass in the

[01:54:27.520] error. I don't want it to use a new

[01:54:29.199] method. I wanted to use that original

[01:54:30.560] method. I just don't want to side rail

[01:54:32.159] the whole conversation to fix that.

[01:54:35.280] >> Well, we got there eventually anyways.

[01:54:37.360] >> No, it didn't because it didn't use the

[01:54:38.800] original method. There's a method that

[01:54:40.239] we have that you have to use that

[01:54:42.000] actually does the formatting for you for

[01:54:43.599] that kind of stuff.

[01:54:44.320] >> Okay. But the actual error messages we

[01:54:45.920] got are correct. So, you're saying it

[01:54:47.119] just rewrote that logic itself

[01:54:48.560] somewhere?

[01:54:48.960] >> It rewrote the logic with a shittier

[01:54:50.480] version of that logic.

[01:54:51.920] >> Interesting.

[01:54:52.400] >> I have good logic that is actually like

[01:54:54.880] way more battle tested for a lot more

[01:54:56.719] edge cases.

[01:54:57.920] >> Okay.

[01:54:59.440] So, that's kind of how I would that's

[01:55:01.119] kind of how I would think about it

[01:55:02.159] because it does a whole bunch of stuff

[01:55:03.199] around preference and ordering and stuff

[01:55:04.880] there.

[01:55:05.760] >> Yeah.

[01:55:06.239] >> Um, and I don't want that to be the

[01:55:08.239] case.

[01:55:09.040] >> Okay. But that's that's the kind of

[01:55:10.400] thing that is like, okay, once we got

[01:55:11.599] the whole thing plumbed in to end,

[01:55:12.960] that's a really easy refactor.

[01:55:14.719] >> Exactly. It's not even a refactor. It's

[01:55:16.480] actually like I I will use AI to solve

[01:55:18.400] that problem, too. But I just don't want

[01:55:20.320] to lose what I don't want to do here is

[01:55:22.560] I don't want to lose a train of thought

[01:55:24.159] over the details that I know don't

[01:55:25.679] really matter.

[01:55:26.239] >> So, we're at 60 again. I'm starting to

[01:55:28.159] get a little again context anxious.

[01:55:30.719] >> Yeah, the problem with our codebase like

[01:55:31.920] I said is massive.

[01:55:33.840] >> Well, also this plan file is getting

[01:55:35.760] quite long and so it's reading the

[01:55:37.199] entire plan file to only like a lot of

[01:55:40.880] this is like stuff that's already done

[01:55:42.320] and working and it may even be worth

[01:55:44.080] compacting the plan file.

[01:55:46.719] >> I have found that that has led to worse

[01:55:48.560] results than letting the context window

[01:55:50.080] with autocompact personally.

[01:55:52.000] >> Okay. Um, and like what I would really

[01:55:54.800] do here is I'd probably do all the

[01:55:56.560] request timeout with every single client

[01:55:59.360] with um with sub agents. That's what I

[01:56:02.960] probably would have done.

[01:56:04.320] >> I'll have it actually go do the

[01:56:05.520] implementation with sub agents and do

[01:56:07.040] the testing with sub agents.

[01:56:09.360] >> Yeah, that's probably what I would have

[01:56:10.880] suggested is like better if you really

[01:56:12.159] care about compaction. Like honestly, I

[01:56:13.679] probably wouldn't even do compaction

[01:56:15.440] here. I would just let it rip.

[01:56:17.760] >> I'm going to compact cuz we got pretty

[01:56:19.679] See, it already auto compact.

[01:56:20.880] >> All right, we got 30 more minutes. I

[01:56:21.920] think my goal is by the end of this 30

[01:56:23.360] minutes it should fully run. I think

[01:56:25.760] it's good to give it the other phases

[01:56:27.520] because then if it has that it knows

[01:56:29.119] what context it can do personally. Let's

[01:56:31.920] keep running this thing.

[01:56:33.520] >> Yeah, we'll just let this run. Um

[01:56:37.920] it actually the only reason you can't

[01:56:39.679] use sub agents here is very sad because

[01:56:41.280] the sub agents are sadly uh cargo does a

[01:56:44.880] lock on the system.

[01:56:48.480] Can't lock. It's actually really

[01:56:51.520] annoying. And also when you're updating

[01:56:53.599] a codebase individually, it's very

[01:56:55.280] annoying unless you have like separate

[01:56:56.480] packages that you're testing in because

[01:56:58.000] it's all within the same package. You

[01:56:59.280] can't really do it in any more parallel

[01:57:01.360] sadly.

[01:57:03.280] And incremental compilation is not a

[01:57:05.040] thing that Rust really has in a great

[01:57:06.880] way sadly. Yeah, but I don't know how if

[01:57:09.599] they'll be able to do it sadly.

[01:57:11.599] Honestly, I actually spend very little

[01:57:14.000] time thinking about what model to use

[01:57:15.520] and I just let it rip and then if I run

[01:57:18.239] into problems, then I will deal with it.

[01:57:20.800] Well, Sonnet 4.5 is supposed to be good,

[01:57:22.560] so it's I think it's worth it. I

[01:57:23.760] actually think people underestimate how

[01:57:25.119] important speed is. I think most models

[01:57:27.360] can write code pretty well. So, like I

[01:57:29.119] probably would use Sonnet 45 or even the

[01:57:31.040] smaller. I actually use the uh the

[01:57:33.679] shittier Sonnet models all the time.

[01:57:35.119] They're good enough. your your

[01:57:37.280] philosophy of you use opus always like

[01:57:39.280] personally I have a pretty good proxy of

[01:57:40.560] when to use and when not to and I get

[01:57:42.320] really results without using opus I

[01:57:44.080] think it can do way harder problems than

[01:57:45.520] that too personally yeah I don't know

[01:57:47.520] that's just my personal take though like

[01:57:49.280] I found it to be fine even for really

[01:57:50.960] hard problems like super long

[01:57:55.520] it is all vibes too no

[01:57:59.760] it's I think most prompting in my honest

[01:58:03.119] opinion most prompting whether it be at

[01:58:04.719] the application layer or using coding

[01:58:06.000] agents is all vibes. And the best thing

[01:58:08.480] you can do is build a really really good

[01:58:10.080] vibe checker in your own brain of

[01:58:12.239] whether or not it's working or not. And

[01:58:14.320] if you can do that, you that will likely

[01:58:16.639] be better than any system you build

[01:58:18.880] because there's this infinite there's

[01:58:20.400] always this joke of like I spent I spent

[01:58:22.239] four hours automating a 10-minute task.

[01:58:24.159] I think the same with prompting for most

[01:58:25.840] tasks. You're going to spend weeks

[01:58:28.159] setting up an eval system for what was a

[01:58:30.080] one day prompting problem. And the

[01:58:31.760] infrastructure is not worth it most of

[01:58:33.599] the time.

[01:58:34.239] >> Well, no screen share. Yeah, because

[01:58:36.719] there's literally just nothing to do. It

[01:58:38.400] just you just have to wait through the

[01:58:39.679] code.

[01:58:40.800] >> Yeah. So, I'll tell you like my take on

[01:58:42.639] this. So, like I've tried showing my

[01:58:44.159] team the prompts and usually what I find

[01:58:45.760] is any workflow that I give to my whole

[01:58:47.679] team, engineering is such a diverse

[01:58:50.000] medium that you usually don't have one

[01:58:52.560] thing that fits all. Um, and like for

[01:58:55.599] example, we all use VS Code. We all use

[01:58:57.679] VS Code in totally different ways. We

[01:58:59.840] all have terminals. We all use terminals

[01:59:01.119] in totally different ways. Then the

[01:59:02.560] reason VS code and terminals I think

[01:59:04.000] work really simply is because like

[01:59:05.520] there's one medium that they have which

[01:59:06.880] is like reading and editing files which

[01:59:08.320] is a really really common pattern but

[01:59:09.840] the actual mechanism that you use to

[01:59:11.280] read and edit files is varies

[01:59:13.040] dramatically between every single

[01:59:15.119] engineer I've ever met. So like or just

[01:59:17.119] like for example you use Vim keybindings

[01:59:18.800] I use I use regular keyboard key

[01:59:20.480] bindings like engineering is such a

[01:59:22.639] dynamic discipline that there's no one

[01:59:24.560] homogeneous way to do things for almost

[01:59:26.639] every task. uh we have workflows like

[01:59:29.520] system workflows like GitHub pull

[01:59:31.360] requests and everything that we do

[01:59:32.560] clearly have more systematic ways of

[01:59:34.400] doing things usually but even then every

[01:59:36.560] team has different ways of doing this

[01:59:37.760] and it's not really prescriptive but

[01:59:39.920] it's usually just like hey thou thou

[01:59:41.679] shalt code review thou shalt do certain

[01:59:43.760] things but not really how the how is

[01:59:45.599] very loosely defined

[01:59:47.760] and I think for prompting and everything

[01:59:49.199] else like as hard as I tried to get my

[01:59:51.440] engineers to do all be do the same exact

[01:59:53.440] thing actually turns out that they're

[01:59:55.520] better when they're doing the thing that

[01:59:56.639] is like kind of like a an offshoot off

[02:00:00.239] of the golden path that works for them

[02:00:02.159] and makes them happy and enjoy the work.

[02:00:06.400] >> And then same with prompts like I think

[02:00:07.840] there are prompts that certain engineers

[02:00:09.119] like because their workflow is better.

[02:00:10.960] It works with their personal style of

[02:00:12.800] workflow better. So that was like I

[02:00:14.560] think one of the key learnings that I've

[02:00:16.719] had which is like and if I press one

[02:00:18.560] workflow on one uh on people too much

[02:00:20.719] then they won't really have fun anymore.

[02:00:22.560] And part of software is not just like

[02:00:24.159] being a machine that spits out code.

[02:00:25.360] It's actually like enjoying the work.

[02:00:26.800] And that's almost like Yeah, it's like

[02:00:28.560] coming to the conclusion yourself rather

[02:00:30.320] than being told what to do. You made two

[02:00:32.239] plans.

[02:00:33.599] >> Okay, let's keep on going on the Let's

[02:00:35.760] see where the implementation's at. Let's

[02:00:37.199] see what it gets.

[02:00:38.719] >> Yeah. Now, now it literally should just

[02:00:40.719] do like a quick compilation step and

[02:00:42.480] then we should read write some pi test.

[02:00:44.159] And like honestly, if all the pi tests

[02:00:45.840] pass, I'd be surprised. I'd probably run

[02:00:47.599] it manually myself because I don't

[02:00:48.880] really trust it. Once it tells me that

[02:00:50.800] it passed, then I would just like see if

[02:00:52.080] it actually passed. Just as a quick

[02:00:53.760] sanity check, you know, I don't want I

[02:00:55.040] don't want to be I don't want to be a

[02:00:56.080] schmuck that just like is like, "Ah, the

[02:00:57.440] AI told me it didn't." Like, while I do

[02:00:59.440] kind of believe it, it's like uh for

[02:01:01.360] really serious stuff, even if my

[02:01:02.719] engineers say the code works, uh or any

[02:01:05.280] team I've ever worked on, if someone

[02:01:06.400] that I'm code reviewing said the code

[02:01:07.599] works, for really serious stuff, I will

[02:01:09.040] go validate it myself.

[02:01:10.800] >> Exactly. Because I'm in the end, I'm

[02:01:12.880] still on the hook for the code working

[02:01:15.599] like regardless of like whether I wrote

[02:01:17.440] the code or not. And like this is and I

[02:01:19.679] didn't notice I didn't do it before for

[02:01:21.199] the previous test because I trusted that

[02:01:23.280] system a lot more than this one. This is

[02:01:25.360] like an end toend test. I'm like ah I

[02:01:27.599] don't want to think about it. Let's

[02:01:28.960] really make sure that this works. But

[02:01:30.480] sadly we just have to wait. I really

[02:01:31.840] wish there was a better thing to do than

[02:01:33.040] just wait. Um no I don't know that I

[02:01:35.920] need to think about this more. That's

[02:01:37.040] why also it's like there's a deeper

[02:01:38.800] problem here that I need to think about

[02:01:39.840] how to do. Um don't update greet plan. I

[02:01:43.920] would Oh yeah. Okay. Oh, so you're not

[02:01:46.480] going to auto approve. Interesting. But

[02:01:48.639] yeah, I mean, you told it the wrong

[02:01:49.760] thing, so it makes sense. It'll fix

[02:01:52.159] them.

[02:01:53.679] It's going to run. No, this is going to

[02:01:55.360] run. I'm like, it's so close. As soon as

[02:01:56.800] a pi test command runs, I trust me, I

[02:01:58.719] think it's going to work. Uh, that part

[02:02:00.560] is fast. It'll just compile. Once this

[02:02:02.239] compiles, the Python test should just

[02:02:03.760] work. It's going to be better than you

[02:02:05.360] think. Um, so I'll stick on a little bit

[02:02:07.599] longer just until we get the Python test

[02:02:09.440] running. If we don't get the Python test

[02:02:11.440] running on like within the first uh

[02:02:14.320] three to four minutes of it executing

[02:02:16.000] that space then we can call it. But I

[02:02:18.719] think it will run. I'm very optimistic

[02:02:20.480] actually. I think this workflow has

[02:02:21.840] worked for me really really well.

[02:02:24.560] Um and I think what's cool for everyone

[02:02:26.400] here is like look I I know BAML. Dexter

[02:02:30.080] doesn't like the BML codebase. And

[02:02:33.040] really all we're doing here is I'm just

[02:02:34.239] reading the plan. He's writing all the

[02:02:35.360] code. I haven't I haven't touched a

[02:02:36.639] single prompt. And like Dexter's

[02:02:38.800] basically like paraphrase some of the

[02:02:39.840] stuff that I've done, but in reality I

[02:02:41.360] haven't done most of it. It's

[02:02:42.800] >> Yeah.

[02:02:43.840] >> Yeah, it's fine. So why why do you do

[02:02:46.400] the continue all the time?

[02:02:48.080] >> Is that actually true? Are you sure it

[02:02:49.840] deletes all the prompts and not just

[02:02:51.199] like summarizes the last few messages in

[02:02:53.119] some interesting way? Okay. Yeah, I

[02:02:54.480] would just double check. I I suspect

[02:02:56.159] that they they probably do something a

[02:02:59.520] little bit more clever than just like

[02:03:01.360] summarize everything here.

[02:03:02.639] >> I think that's the one other thing that

[02:03:03.760] I've learned about myself. Um, wait, why

[02:03:06.239] does it say about Ruby FI? I mean, I

[02:03:08.400] just don't care about compiling Ruby.

[02:03:10.719] The autoco compact generates a summary

[02:03:12.719] of about 3500 words. You can ask the new

[02:03:14.880] agent what is the Damon fetched in

[02:03:17.520] fetched in to write word for word the

[02:03:20.320] transcript provide as file.

[02:03:22.960] Uh, yeah, then you can see the autoco

[02:03:24.880] compact. Yeah, I think it's because it's

[02:03:27.199] just trying to do compilation stuff.

[02:03:28.880] Yeah. Okay, now it's reading the plan.

[02:03:30.880] That's good enough to be honest. That is

[02:03:32.560] the core packet. If that packet passes,

[02:03:34.320] then the rest of it will Yeah. Yeah.

[02:03:36.080] Exactly. Yes. I'm very excited for this.

[02:03:39.199] If this works, it's gonna be super

[02:03:41.199] exciting. And again, I think what's

[02:03:43.360] really fascinating about this whole

[02:03:44.480] thing is like this is

[02:03:48.719] so so so

[02:03:50.800] much faster than the old workflow. Like

[02:03:54.000] what like all this is going to do is

[02:03:55.440] literally write the Python in tech test

[02:03:56.800] and verify that the inte pass. Um, and

[02:04:00.320] like if this works that means the whole

[02:04:02.159] pipeline worked and now we now have like

[02:04:03.679] timeouts at least for part of the

[02:04:04.960] codebase like for primitive clients we

[02:04:07.280] now have support for connection and uh

[02:04:09.840] idle timeouts which are huge like

[02:04:12.719] connection request timeouts. Yeah, the

[02:04:14.960] built-in timeouts are whatever but like

[02:04:16.239] this part I think is the most

[02:04:17.119] fascinating like how does how well does

[02:04:18.719] this work and if this works and like

[02:04:20.480] it's it's golden in terms of like

[02:04:22.239] outputs like this will work

[02:04:23.599] fantastically. I don't know if it ran

[02:04:25.119] the matcher command. Did it? Can you

[02:04:27.520] scroll up and see?

[02:04:29.760] It did. Oh, it did not go up.

[02:04:33.840] Uh, tell you need to run the matchin

[02:04:35.920] command. Matcher command. Just say

[02:04:38.239] matcher. M a tu. Yeah, that one. Just

[02:04:42.000] tell it. It'll figure it out. And then

[02:04:43.599] you do need openi API key. Uh,

[02:04:47.360] you do? I think so. So, you might want

[02:04:49.360] to probably want to stop screen sharing.

[02:04:51.760] Yeah,

[02:04:52.239] >> because that's going to fail for a

[02:04:53.440] variety of different reasons.

[02:04:55.520] >> I have not.

[02:04:56.719] >> Yeah. Nice. So this will

[02:05:00.719] >> Yeah, we're actually working on fixing

[02:05:02.159] this. So this is um much faster because

[02:05:04.880] like pio3 and matcherin are just like

[02:05:07.119] too slow. Yeah, exactly. So it'll fix

[02:05:09.360] itself. I think we're going to be done

[02:05:10.639] soon. I'm very optimistic. We'll see if

[02:05:12.560] it pans out. Yep. Exactly. Yeah, the

[02:05:15.040] diff. That's correct now. Yeah, it it'll

[02:05:18.080] figure it out. This part I feel really

[02:05:20.239] confident about. It probably had to read

[02:05:21.760] the file and be like, "Oh yeah, exactly.

[02:05:23.199] It got the better version of it." Yep.

[02:05:25.760] Now that Python compiles, so we know

[02:05:27.199] that the compilation works end to end.

[02:05:28.880] Yep, I think all things should be in in

[02:05:30.719] Rust. All dev tools should be built in

[02:05:32.560] Rust. I have a strong opinion on that.

[02:05:34.639] Well, dev tools application code write

[02:05:37.040] in whatever you want, but like where

[02:05:38.639] develop.

[02:05:40.639] There we go.

[02:05:43.199] That works. Run it yourself. Yeah. I

[02:05:45.040] want to go run the test and I want to go

[02:05:46.400] Oh, I mean, I guess we can just look. I

[02:05:47.840] want to run the test with like a with

[02:05:50.080] like a with a t thing.

[02:05:52.880] Uh, do- Yeah.

[02:05:56.159] Oh, it is dashv dash dash VVV. Oh, it

[02:06:00.560] responded too fast.

[02:06:03.840] Oh, I think so. What's the assertion

[02:06:06.320] error that you got? Oh, it didn't. The

[02:06:09.119] model just responded poorly. Uh, the

[02:06:12.080] assert is bad. We should get rid of that

[02:06:13.520] assert in that test

[02:06:16.239] cuz the model is responding with like a

[02:06:17.760] string by just knowing it's a string

[02:06:20.000] more than 10 characters and that we

[02:06:21.760] didn't fire an exception.

[02:06:23.599] >> That's it. Like this works. There we

[02:06:25.920] have it. Like end to end Python asserts

[02:06:28.880] definitely work. We're getting time. If

[02:06:30.320] we go look at the actual Can you open up

[02:06:32.880] the thing for me really fast? The the

[02:06:34.880] codebase so we can show the commits

[02:06:38.079] uh the Python code. I want to show the

[02:06:39.360] Python test file test. Yeah. Test

[02:06:41.360] timeouts. Like we're definitely firing

[02:06:43.520] these tests and we're definitely

[02:06:44.400] capturing these exceptions. Now, it's

[02:06:45.760] possible that there's still a bug here.

[02:06:47.119] So I would have to go and like read this

[02:06:48.320] code in really good detail, but just

[02:06:50.960] statistically based on everything that

[02:06:52.159] we have compiled and looking at the diff

[02:06:53.599] of everything so far where the only

[02:06:54.960] difference is really the client that

[02:06:56.079] we're passing in. I find that hard to

[02:06:58.079] believe.

[02:06:58.639] >> So um maybe after I validate that it's

[02:07:01.920] actually good myself. Cool. So Dex, if

[02:07:04.079] you can take all the thoughts, take all

[02:07:05.520] the research, take all of his stuff and

[02:07:07.520] put it as a PR up uh if to the repo. Uh

[02:07:10.880] we'll take it from here.

[02:07:13.280] Um yeah, so this was like I said a

[02:07:15.599] longer form episode compared to what we

[02:07:16.960] normally do. Uh and what we will be

[02:07:20.480] doing in back in the future is we'll go

[02:07:22.000] back to writing more code. But today we

[02:07:24.079] wrote a lot of code using AI and

[02:07:25.760] hopefully the lessons that we shared

[02:07:27.360] around here are going to be helpful to

[02:07:28.880] all of you. With that, we're going to

[02:07:31.760] peace out and let Dexter get the stuff

[02:07:34.560] up and running. Thank you guys for

[02:07:36.880] making all the time and tuning in. Uh

[02:07:38.880] Dexter, until next time.

[02:07:41.360] See you.
