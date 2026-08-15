# Bash vs. MCP - token efficient coding agent tooling



Source: YouTube captions (automatic:en)



[00:00:02.470] You're super echoey.

[00:00:02.480] >> That's cuz you're also on the Zoom, but

[00:00:04.000] we should be live now at this point. Um,

[00:00:06.400] and then I'm going to leave the audio in

[00:00:08.160] the Zoom and we should be live and good

[00:00:10.240] to go. Awesome. And I'm going to post

[00:00:12.000] the link over on our Discord as well.

[00:00:13.920] And then we'll get started right away

[00:00:15.200] with AI that works this topic.

[00:00:18.480] >> Are you ready, Dex?

[00:00:19.920] >> I'm ready. We're live.

[00:00:21.760] >> All right. What's today's topic, Dex?

[00:00:23.840] Give us the rundown. Uh so today's topic

[00:00:26.400] we are going to talk about using coding

[00:00:29.439] agents using bash versus MCP for tools

[00:00:32.960] which has been a debate that's going on

[00:00:35.120] uh a lot in a lot of places and I think

[00:00:38.879] um

[00:00:40.879] I want to just dig under the hood cuz

[00:00:43.040] like most things in AI the answer is

[00:00:45.760] there is no right answer and the correct

[00:00:48.160] answer is to understand how the models

[00:00:50.160] work under the hood understand how the

[00:00:52.800] harnesses work under the hood And of

[00:00:54.800] course do a little bit of context

[00:00:56.000] engineering and really just understand

[00:00:57.920] the tokens you're putting into the model

[00:00:59.359] and taking out of the model model.

[00:01:00.960] >> I think that's one of the topics that I

[00:01:02.640] have been seeing happen more and more

[00:01:05.920] over in um just popping up more and more

[00:01:08.479] everywhere that I see right now. It's

[00:01:10.240] happening over on like Twitter threads

[00:01:11.680] all the time. I was just talking to a

[00:01:13.600] user over on the uh

[00:01:16.400] uh I was just talking to users over on

[00:01:19.920] like the Discord and they were talking

[00:01:20.960] about how UIDs cause like a huge problem

[00:01:23.040] as well.

[00:01:24.720] And it's just like all this stuff is

[00:01:26.720] really just about simplicity. I don't

[00:01:28.320] know if anyone's noticed Claude Code has

[00:01:30.400] actually renamed their bash tool to

[00:01:31.840] general purpose.

[00:01:33.840] Like the words

[00:01:35.040] >> that's the the task tool, right?

[00:01:36.799] >> The general purpose tool that they added

[00:01:39.520] recently and I think

[00:01:40.960] >> I think that's the subtask agent. Yeah,

[00:01:43.520] the word, but they renamed it. And I

[00:01:45.360] think the reason for that is it's just a

[00:01:47.119] better name. And a lot of people

[00:01:48.880] underestimate how important these names

[00:01:50.560] are.

[00:01:52.159] And I think when we talk about MCP

[00:01:54.799] versus Bash, I think that's the first

[00:01:55.920] name we should talk about. Why don't we

[00:01:57.040] why don't we start off with something

[00:01:58.159] really basic, which is when we go start

[00:02:00.159] off with this, I want to start off with

[00:02:01.280] a whiteboard that really outlines how

[00:02:02.960] MCP is actually working

[00:02:05.520] uh under the hood. Yeah, exactly. Off

[00:02:08.000] was me. I was just talking about this

[00:02:09.759] like 60k tokens right in your context

[00:02:12.319] window. I think the best analogy for

[00:02:15.520] this is

[00:02:17.360] um before we go really deep into it is

[00:02:19.280] really going to be package management

[00:02:20.800] software.

[00:02:22.319] If anyone's ever built a website, you've

[00:02:24.239] probably seen the extension that tells

[00:02:25.920] you how big an npm import is that you're

[00:02:28.080] making. And like there's some that are

[00:02:30.160] like 65 megabytes and some that are

[00:02:32.239] really small. And as of right now, I

[00:02:35.760] think no one really cares if you use a

[00:02:37.120] megabyte in your package. I mean, you

[00:02:38.400] shouldn't. Please be nice and don't do

[00:02:40.000] that. But in practicality, it doesn't

[00:02:42.640] really matter uh on today's machines.

[00:02:45.680] But like 12 months ago, uh 12 years ago,

[00:02:48.080] it did matter. And I think that's kind

[00:02:50.480] of the world we live in with MCPs versus

[00:02:54.080] bash is like MCP in theory is really

[00:02:56.879] nice. It's basically a packet man. It

[00:02:58.319] says something for prompts is kind of

[00:02:59.599] how I view it as. But the problem is if

[00:03:02.000] you don't know what prompts are

[00:03:03.360] happening under the hood, you're stuck

[00:03:05.200] in this world where you made your

[00:03:06.959] instead of making your website slower by

[00:03:08.640] having a massive package, you've

[00:03:10.879] accidentally made your um agent less

[00:03:14.480] accurate by having a massive prompt. And

[00:03:17.519] that's really the fundamental issue that

[00:03:19.360] I think people run into. And like

[00:03:21.200] slowness is kind of bad, but like you

[00:03:22.720] can get around it because at least the

[00:03:23.840] website functions the same. But accuracy

[00:03:26.000] is not is is literally a user quality

[00:03:28.319] hit. So I think that's why this

[00:03:30.560] conversation is getting a lot of upbeat

[00:03:33.599] more recently is because the accuracy

[00:03:36.080] problem is effectively unbounded in

[00:03:39.120] terms of difficulty.

[00:03:40.239] >> Um yeah and so I want to jump right in.

[00:03:42.720] Um we have a quick episode here. So, um,

[00:03:45.760] when you launch a coding agent, and

[00:03:47.280] we'll be talking about cloud today

[00:03:48.400] because that's the one that, um, we have

[00:03:50.799] the most experience with, but everything

[00:03:52.319] we're doing is true for codeex, true for

[00:03:53.920] AMP, true for open code, any CLI you

[00:03:55.840] would use. Um, your context window and

[00:03:59.360] your agents ability to do good work in

[00:04:02.080] it. Um, is completely and directly

[00:04:04.560] proportional to the size of your context

[00:04:07.439] window. Um, I think we have Jeff Huntley

[00:04:09.439] on stream today. I think the way he put

[00:04:11.360] it is very clear and succinct. I don't

[00:04:13.200] think anyone will argue with you. The

[00:04:14.799] more context you use, the worse results

[00:04:17.519] you will get across the board no matter

[00:04:19.199] what. Um,

[00:04:20.560] >> obviously having missing information or

[00:04:22.079] incomplete information is bad, but um

[00:04:26.240] the in general the more you can keep it

[00:04:28.320] concise with the right information, the

[00:04:30.160] better. Um, so when you launch a cloud

[00:04:32.400] code prop and I'll show you kind of what

[00:04:33.600] we'll look under the hood here actually.

[00:04:35.120] Um, let's see. I'm actually going to

[00:04:37.199] share my whole desktop. So um, add the

[00:04:41.120] work circle of trust. If you see

[00:04:42.880] something you shouldn't, please unsee it

[00:04:44.880] and tell us.

[00:04:46.560] >> Twitter deck, so we'll

[00:04:47.440] >> Yeah, we're live on Twitter. Yeah.

[00:04:48.960] >> Yeah, I'm not I'm not really I don't

[00:04:50.320] trust any of you anymore. Sorry. We're

[00:04:51.919] big we're big time now.

[00:04:54.160] >> Um

[00:04:56.160] so one thing that you uh that you can do

[00:04:59.440] is you can look at a um you can we we

[00:05:02.320] have this project here on AI that works.

[00:05:04.960] Um, why does

[00:05:07.199] Streamyard insist on hiding the stream

[00:05:10.240] the window when it does full screen? Um,

[00:05:13.600] so we uh all the code for this episode

[00:05:15.759] is here. One of the things we've written

[00:05:17.120] is a small reverse proxy that you can

[00:05:19.440] run in Docker um that will just proxy

[00:05:21.440] all your cloud traffic and then write it

[00:05:23.199] out as log files. Um, I don't have the

[00:05:26.160] log files here. Um,

[00:05:29.199] or directly

[00:05:31.280] and actually

[00:05:33.440] >> you might have one of them over. Uh, I

[00:05:35.440] think I saw you

[00:05:36.240] >> in the other episode. Yeah, I didn't

[00:05:37.680] push them.

[00:05:38.560] >> For those of you that have haven't seen

[00:05:40.320] the cloud code files, like when you

[00:05:41.759] actually go look while Dex pulls it up,

[00:05:43.919] some of the stuff that they add into the

[00:05:45.520] system prompt is actually quite

[00:05:46.720] interesting. For example, uh claude will

[00:05:49.440] actually tell the model to the claw that

[00:05:52.400] MD file should be followed unless it's

[00:05:54.320] not relevant, in which case don't follow

[00:05:55.919] it.

[00:05:56.639] >> Yeah, that was a fun one.

[00:05:58.240] >> Uh is this the one?

[00:05:59.840] >> Sorry. Yeah. So, this is one of the

[00:06:01.120] traces. I have to scroll over cuz I did

[00:06:03.120] a search.

[00:06:03.600] >> Just copy the line and then we can just

[00:06:04.880] JSON format it.

[00:06:06.400] >> Well, so what I wanted to show you is

[00:06:07.919] basically part of what's in your context

[00:06:09.919] window, right? So, the thing is a list

[00:06:11.360] of messages and the tools get listed in

[00:06:13.360] is you have your bash tool, you have

[00:06:14.880] your glob tool, you have your GP tool.

[00:06:16.800] So there's all these built-in tools,

[00:06:18.240] right? And then you'll also have any MCP

[00:06:22.000] tools that you add in. And so let's see

[00:06:24.240] if I have any of these in here. So yeah,

[00:06:26.240] here's the linear MCP tools. So you have

[00:06:28.400] a bunch of JSON and schemas that explain

[00:06:30.720] to the model how to use these different

[00:06:33.039] tools. And so like this doesn't get

[00:06:34.639] injected in the context window.

[00:06:35.919] >> Pause for a second there.

[00:06:36.960] >> Yeah.

[00:06:37.280] >> I want you guys to take a look at this.

[00:06:38.639] See the name? The name is MCP linear

[00:06:40.800] list cycles. Like it's not just that

[00:06:42.960] you're injecting stuff into the model,

[00:06:44.880] you're also injecting random names that

[00:06:46.880] Claude has to use to like differentiate

[00:06:48.639] stuff to pass it into the model. Like

[00:06:50.880] why does a model care that this thing is

[00:06:52.479] called MCP linear list ticket? Like if I

[00:06:55.440] only have one thing for getting

[00:06:56.800] documents and it's purely linear, I

[00:06:58.639] could just call this get document and

[00:07:00.080] it's going to work effectively very very

[00:07:02.639] similarly. In fact, they'll probably

[00:07:04.240] work better because again, it's it's not

[00:07:06.319] about these small naming differences are

[00:07:08.400] exactly why Enthropic had to rename

[00:07:09.840] their tool to general purpose away from

[00:07:13.599] a broader

[00:07:16.080] um away from a broader like subtask

[00:07:18.240] because the names really make a huge

[00:07:19.599] difference in accuracy.

[00:07:21.039] >> Well, and just just to just to like

[00:07:22.800] clear that up also like the the if we

[00:07:25.120] look for we can find the task tool here.

[00:07:28.639] Um, if my search

[00:07:31.599] >> you want to just copy this and paste it

[00:07:33.280] into a JSON prettier.

[00:07:35.599] >> Uh, no. The problem is is that this

[00:07:37.840] proxy logged things with um,

[00:07:41.840] this proxy logged things with a

[00:07:43.599] serialized JSON thing.

[00:07:45.199] >> That's okay. You can just unserialize

[00:07:46.479] the JSON if you copy and paste it. If

[00:07:48.000] you I'll send you the website.

[00:07:51.120] >> No, no, no. Um,

[00:07:53.440] just hang on. There we go. So the task

[00:07:56.000] tool has a prompt and a description

[00:08:00.000] right now, but in a newer version of

[00:08:02.400] Claude, they added like sub agents with

[00:08:04.960] names. And so general purpose is the

[00:08:07.199] default name for the task tool in newer

[00:08:09.599] versions of cloud code. And this this

[00:08:10.879] this shell this um this prompt is a

[00:08:13.280] little old. Um so I just want to clear

[00:08:15.440] that up. There's a general purpose sub

[00:08:16.960] agent that is to differentiate from any

[00:08:19.280] custom sub aents that you might have.

[00:08:21.039] But in the because in the old world

[00:08:22.240] there was just task and there was no a

[00:08:24.080] there was no name parameter in here.

[00:08:27.840] Um but I want to get back on track here.

[00:08:30.000] So we have all the built-in tools like

[00:08:31.759] bash gp glob. Um we have then the uh mcp

[00:08:37.760] tools that you might add right and I'm

[00:08:39.839] just going to go through a couple

[00:08:40.880] examples with claude. So this is like

[00:08:43.200] linear list issues. And we're going to

[00:08:46.080] do a really simple example today, which

[00:08:47.600] is essentially around um let's go find

[00:08:50.320] it. Um what's the difference between

[00:08:53.120] using a CLI to talk to linear to get an

[00:08:56.720] issue versus oh no, this is what I get

[00:08:59.519] for writing my readmemes in in Neovim

[00:09:03.040] and not setting up actually a bunch of

[00:09:04.800] good neoim plugins.

[00:09:07.360] Um, so we're going to look at um just a

[00:09:10.080] really simple cloud command here. Um,

[00:09:12.320] because you can actually without even

[00:09:13.680] doing the proxy stuff.

[00:09:16.320] You can um

[00:09:19.600] you can see the output and the tokens

[00:09:22.320] used and you can use that to count the

[00:09:23.920] tokens. Embedded in these messages is

[00:09:26.959] basically something that looks like

[00:09:28.399] this. And so what we care about the most

[00:09:30.800] is cache creation input tokens. And if

[00:09:32.800] we sum those up over a user uh over a

[00:09:35.200] session, then we can get kind of a clear

[00:09:38.160] picture of how many tokens were used in

[00:09:40.880] that session. There's a little script in

[00:09:43.920] here um that will uh actually parse this

[00:09:48.560] output and make it useful. Um so you can

[00:09:51.200] steal this and use it. It's really quite

[00:09:53.040] simple. Um, but we have our initial our

[00:09:55.440] our assistant message and we created

[00:09:57.519] 6,000 tokens here and then it read that

[00:10:01.360] file and then it's going to write that

[00:10:03.519] file and so each one of these is some n

[00:10:05.519] number of tokens that is the actual like

[00:10:07.519] JSON of the tool call. Does that make

[00:10:09.760] sense? By Bob questions?

[00:10:12.480] Yeah. Okay, cool. So, um, you can also

[00:10:16.480] do something cool where if you run the

[00:10:17.760] exact same thing again, you will

[00:10:19.200] actually see that this is like this is

[00:10:20.640] not an episode about caching. We went

[00:10:22.240] really deep on caching when we went

[00:10:23.680] through the manice paper, but if you use

[00:10:25.519] the exact same user message and the same

[00:10:29.120] set of allowed tools, then you're

[00:10:31.839] actually using the cache the whole way

[00:10:33.839] through. All of these calls are exactly

[00:10:35.680] the same. And so we're not actually

[00:10:37.200] writing any new tokens to the cache,

[00:10:39.120] which is both cheaper and faster. Um,

[00:10:42.320] but if you bust the cache by changing

[00:10:44.240] the user message, you can see a slightly

[00:10:47.040] different output. So, because I changed

[00:10:48.959] it from write food to bar.txt txt to

[00:10:51.279] please write fudabar.txt.

[00:10:53.680] Everything that comes after my user

[00:10:55.200] message is recomputed. And so it didn't

[00:10:57.200] do all 6,000 because the cloud system

[00:10:59.279] message is still the same and the

[00:11:01.920] cloudmd is still the same. But somewhere

[00:11:04.640] in here, I think that what happens is

[00:11:06.079] the user message comes in before the

[00:11:08.399] tools and stuff. I don't know exactly

[00:11:09.839] the mechanics of it. We can go look at

[00:11:11.200] it. But um the idea is if you only

[00:11:13.600] change parts of it, then you get to

[00:11:14.959] reuse parts of the cache. Um cool. Does

[00:11:18.640] that make sense so far? Um, so now what

[00:11:21.360] I'm going to do is I have here um the

[00:11:25.440] MCP linear thing. Um, so this is just a

[00:11:28.800] simple MCP config to add linear to our

[00:11:31.760] app.

[00:11:33.279] Um, and so I'm going to run this one

[00:11:35.040] now, too. Oops, not that. And then I'm

[00:11:37.200] going to pop back to the whiteboard in a

[00:11:38.480] second. Um, but we'll see here is we're

[00:11:41.600] going to add way more tokens to the

[00:11:44.000] context window. Yeah. So there's 18,000.

[00:11:46.480] the difference between linear and

[00:11:48.560] nonlinear is about 12,000 extra tokens.

[00:11:52.640] And so if you think about your total

[00:11:54.160] context window, um

[00:11:57.920] what we talk about a lot is trying to

[00:11:59.680] keep it below like 40% usage. And so

[00:12:02.079] rather than like having Claude work for

[00:12:03.680] a long time back and forth, we just say

[00:12:06.320] like have Claude do one thing, have the

[00:12:08.079] agent do one thing, get it right, and

[00:12:10.639] then start over with a fresh context

[00:12:12.320] window and have it work on the next

[00:12:13.680] thing. Um, and so that means that even

[00:12:16.000] though this entire context window is,

[00:12:19.279] you know, 200k tokens minus 32k input

[00:12:23.200] tokens, which means you get a total of

[00:12:25.519] like

[00:12:27.600] 168k

[00:12:30.240] um to work with. So 12,000 tokens,

[00:12:35.360] let's see, is 7% of your context window.

[00:12:39.440] It's not crazy, but if you go start

[00:12:41.519] putting

[00:12:43.200] like six different MCPs in there,

[00:12:46.639] um, you are eating up, you know, a

[00:12:49.600] fourth of and like you're already

[00:12:51.360] basically like your system prompt and

[00:12:52.959] your cloud MD is

[00:12:55.519] is what? So, we added 12 and then we

[00:12:57.360] have like 6K in the base. That's

[00:12:58.800] assuming you have like a tiny cloud MD,

[00:13:00.880] right?

[00:13:02.720] This is this is very small right now.

[00:13:04.720] Um, and this is telling it to use the

[00:13:06.240] MCP tools for linear. Um, and so when we

[00:13:09.120] I'm gonna skip the CLI part for a sec.

[00:13:11.200] We'll just do this one. Um, so I'm gonna

[00:13:13.839] ask it to fetch an issue

[00:13:17.760] um, from linear and we'll see how many

[00:13:21.279] tokens that count that takes. Actually,

[00:13:24.160] I haven't tested this part. Um,

[00:13:27.440] I'm going to check the Are there any

[00:13:28.639] questions in the chat while we're going

[00:13:29.839] through this?

[00:13:30.639] >> We've got one that I really like.

[00:13:33.279] >> Let's do it.

[00:13:33.760] >> Which is,

[00:13:34.959] >> what are these extra tokens like? where

[00:13:36.720] do these 18,000 tokens come from? And I

[00:13:38.639] think the best way to actually show that

[00:13:39.920] off is can you just pull up the JSON

[00:13:42.720] right there?

[00:13:44.959] Um, can you open the JSON really quick?

[00:13:47.200] The linear JSON, the linear um thing

[00:13:49.839] that you pass in.

[00:13:51.040] >> Yeah. And we'll actually pull it up and

[00:13:52.480] I'll show you how to use the NP MCP

[00:13:54.959] inspector. Let me just because we can

[00:13:57.199] also look here.

[00:13:58.079] >> Yeah, but I want to show just the JSON

[00:14:00.000] really fast. uh if you're able to just

[00:14:05.040] >> So if we look in

[00:14:08.480] you want to see the JSON like the actual

[00:14:10.399] request

[00:14:11.120] >> the No, no, I want to see the linear MCP

[00:14:13.440] file.

[00:14:14.959] >> Oh, okay.

[00:14:15.760] >> Yeah, cool.

[00:14:16.240] >> MCP linear.json. Exactly. Uh and then

[00:14:20.399] can you open that file, the MCP linear

[00:14:23.279] SSC on the browser?

[00:14:24.399] >> Um no, but I can do you one better. Uh

[00:14:27.920] inspector. Let's see what this does. Uh

[00:14:30.800] I assume this is going to have a nice

[00:14:32.000] little UI on top of the

[00:14:34.079] >> Exactly. Yeah. This is how you can So we

[00:14:36.320] can connect here and see.

[00:14:39.120] >> Do you just want to open the browser?

[00:14:40.320] It'll be

[00:14:42.240] just to open it really fast. Yeah.

[00:14:44.240] >> Oh, it's SSE not. There we go. So you

[00:14:47.440] can list out the tools. So there are

[00:14:50.160] names and descriptions and everything

[00:14:52.399] you see here is being passed into the

[00:14:54.800] model to tell it how to use these tools.

[00:14:56.639] So the description of every field, the

[00:14:58.560] description of every method, and the

[00:15:00.079] name of every method. And there's just a

[00:15:02.480] lot of these. And some of them have very

[00:15:04.320] complex um like yeah, list teams has all

[00:15:08.079] of these like sorting and filter params.

[00:15:10.000] So every single word in here is a token.

[00:15:12.240] Is that kind of what you're looking for?

[00:15:13.839] >> Exactly. So like when when we got asked

[00:15:16.480] this question uh about like where what

[00:15:18.639] are all these tools actually coming

[00:15:19.920] from? Like the problem is

[00:15:23.360] unlike unlike a website where like every

[00:15:26.000] single div you put in really doesn't

[00:15:27.680] make it to the user, it does make it to

[00:15:29.440] the browser. And when you render every

[00:15:31.279] div, you could have like five divs le

[00:15:32.959] nested with each other and the browser

[00:15:34.320] will render it and it'll look the same.

[00:15:35.760] If you have a really really really

[00:15:36.880] really old computer, having like 50 divs

[00:15:40.160] nested will be worse than simply having

[00:15:42.320] a single that will be much worse than

[00:15:44.560] having a single div if you don't need

[00:15:46.639] it. That said, from an end user

[00:15:48.480] perspective on today's computers, it

[00:15:49.759] doesn't matter. But today,

[00:15:51.839] when you're doing this with an LLM,

[00:15:53.600] every single word you put into that MCP

[00:15:56.320] server is literally making it to the LM.

[00:15:59.920] And unlike browsers, as of right now,

[00:16:02.560] these models are not good enough. You

[00:16:04.079] got to forget the slashes. This is why

[00:16:05.920] we use text highlighting and why we use

[00:16:07.440] a programming language.

[00:16:08.720] >> No, no, we're using a whiteboard today

[00:16:10.399] by Bob. It's going to be fine.

[00:16:11.920] >> Yeah. But like the point here is like

[00:16:13.680] from a from an end user perspective,

[00:16:15.279] this white this this thing doesn't

[00:16:17.680] matter. Like who cares that this thing

[00:16:19.920] has uh five divs? No one. But in the

[00:16:23.920] world of an MCP where you have five 50

[00:16:25.839] redundant words, it's actually hurting

[00:16:27.839] your performance because the model has

[00:16:29.920] to actually look at it and it has to do

[00:16:31.519] computation to decide what that that

[00:16:33.519] word is actually irrelevant to this

[00:16:35.040] request. It's not merely So if you go

[00:16:38.079] back,

[00:16:39.279] >> you want to go to the inspector.

[00:16:41.040] >> In this case, all I wanted to do was

[00:16:42.639] just get an edge ticket. Why do I have

[00:16:44.639] to know that I have to list teams? It's

[00:16:46.800] totally useless information.

[00:16:49.600] >> And you can you can tune this a little

[00:16:51.519] bit, right? Especially with sub agents,

[00:16:52.959] you can like disallow or allow certain

[00:16:55.120] tools. Um, and then you're going to get

[00:16:57.040] less in the context window. Um,

[00:16:58.800] >> but that's all manual. You can't

[00:17:00.160] actually do it.

[00:17:01.440] >> You can't actually disallow tools.

[00:17:04.240] >> I think in sub agents it will not be

[00:17:06.240] shown to the model if if you put it in

[00:17:09.760] disallow tools.

[00:17:11.039] >> So we can actually test this.

[00:17:12.319] >> You have to pass that in though. That's

[00:17:14.400] a

[00:17:15.679] >> Yeah, you have to you I mean you have to

[00:17:16.959] engineer it. You have to say, okay, like

[00:17:19.439] here's my context window. If I want to

[00:17:21.199] save 1% so I can get, you know, 1%

[00:17:23.760] better performance, then I'm going to

[00:17:26.000] only put in this four MCP tools from

[00:17:28.319] linear that I use and I'm going to like

[00:17:30.080] hide all the other ones. But you have to

[00:17:31.919] understand how context windows work. You

[00:17:33.200] have to end this. This is the

[00:17:34.160] engineering part.

[00:17:35.679] >> Exactly. And I think this is really

[00:17:37.679] where the MCP versus bash debate gets to

[00:17:40.240] really get started, which is that if you

[00:17:43.520] are using MCP, the problem is you don't

[00:17:47.039] get to control exactly what bits make it

[00:17:50.480] into your context window or it is at

[00:17:52.559] least very difficult to control what

[00:17:54.960] bits make it into your context window.

[00:17:56.960] >> Yeah.

[00:17:57.280] >> On the other hand, if you're using bash,

[00:17:59.840] you now live in this world where you

[00:18:00.960] have to kind of reinvent everything or

[00:18:03.440] the model has to reinvent everything. So

[00:18:05.520] like to make to make a linear request,

[00:18:08.000] it has to do a curl on the linear API

[00:18:10.080] and the model is trained on it and it

[00:18:11.760] knows what the linear URLs are, then

[00:18:13.600] great. But if it's not trained on it,

[00:18:15.679] now you live in this world where you

[00:18:16.799] have to run multiple iteration loops to

[00:18:18.320] go figure out what that is. And I think

[00:18:20.720] that's really the duality of this whole

[00:18:22.400] debate of like which side do you prefer

[00:18:24.320] on? Do you prefer on the model becoming

[00:18:26.160] less accurate because you're bloating it

[00:18:27.840] up or do you prefer on the model being

[00:18:29.919] less accurate because it doesn't know

[00:18:31.760] how to use the thing you wanted to use?

[00:18:33.919] And this is kind of the chart you kind

[00:18:36.080] of like to draw a lot, which is like do

[00:18:38.960] you want, you know, the the like curves,

[00:18:41.039] right? Is like how much engineering

[00:18:42.480] effort do you want to put into this? Um,

[00:18:46.880] it's sort of like for low effort, you

[00:18:48.640] can get something like this.

[00:18:51.200] Oh my god, I'm so bad at drawing with a

[00:18:52.960] trackpad. And then if you want to do a

[00:18:55.360] little bit more engineering effort, you

[00:18:56.880] can kind of like collapse this in and

[00:18:59.440] narrow the range of potential outputs or

[00:19:02.240] narrow the range of performance. I don't

[00:19:03.840] know if that's uh that's that's how

[00:19:06.320] you're thinking about it.

[00:19:07.679] >> Yeah. Um the only caveat is you usually

[00:19:10.400] draw it with a slightly higher peak in

[00:19:12.000] the middle because if you're narrowing

[00:19:13.679] it, you're usually doing it because you

[00:19:14.960] want a better outcome. So you're getting

[00:19:16.320] way better outcomes for the care

[00:19:18.240] >> area of the domain you care about versus

[00:19:20.400] more generalized outcome in more

[00:19:21.679] domains. And both can have pros and

[00:19:23.760] cons.

[00:19:25.280] >> Yeah. Exactly. If you take away half the

[00:19:27.039] linear tools, you can't do as much stuff

[00:19:29.120] on linear. But if you only want to do

[00:19:30.640] those things, then yeah, engineer it and

[00:19:32.320] just focus on the things you want to

[00:19:33.440] focus on.

[00:19:34.240] >> Exactly. So it's not so I would say like

[00:19:36.880] the bait and conclusion that I don't

[00:19:38.320] know about your conclusion, Dex, but

[00:19:39.440] like the main conclusion that I've had

[00:19:40.799] about MCP

[00:19:42.000] >> is I am very happy to use MCP stuff that

[00:19:44.799] I have written.

[00:19:46.400] I'm very unhappy to use stuff MCP stuff

[00:19:48.799] that other people have written because

[00:19:50.559] when I write it, I know where it is. I

[00:19:52.400] know where the code lives and I can go

[00:19:53.840] edit it myself to make it actually not

[00:19:56.559] hurt the prompt or not hurt the coding

[00:19:59.039] agent.

[00:20:00.320] >> But if I use someone else's stuff, then

[00:20:01.760] I have like can you pull up the GitHub

[00:20:03.520] MCP just to like really make or like

[00:20:05.919] Joff's uh Jeff's uh blog post on this?

[00:20:09.440] >> Yeah. What was the one? um

[00:20:11.600] >> G Huntley and I think he talks about

[00:20:13.360] like uh email if we can't find it just

[00:20:16.320] pull up the MCP for it. Just

[00:20:18.320] >> put the link in the chat.

[00:20:20.000] >> Yeah, if someone has a chat link, just

[00:20:22.400] post it in there. But like just look up

[00:20:23.840] the GitHub MCP server and

[00:20:25.840] >> drop that one in the inspector.

[00:20:27.679] >> I hate that this thing doesn't tell me

[00:20:29.120] how to use it.

[00:20:30.000] >> So, put that over into the uh inspector

[00:20:32.720] if you have it. And I just want to like

[00:20:34.159] get people an idea for like how insane

[00:20:36.400] this MCP is. And like if anyone's using

[00:20:39.760] MTP with get this GitHub uh I would be

[00:20:42.480] surprised if it worked in in any modly

[00:20:45.600] complex task MCP.

[00:20:48.159] >> Yeah, we'll try this one. This is like

[00:20:49.520] the dynamic client registration thing.

[00:20:51.679] Um we can try just doing this.

[00:20:55.039] >> Does it work? Okay.

[00:20:55.919] >> Does not support I can just look up the

[00:20:58.400] and I think it has like the it has the

[00:21:00.080] actual prompt in here really fast that

[00:21:01.760] you can go see. Um I mean if you just go

[00:21:03.679] down and just let go just go down the

[00:21:05.679] GitHub. You're going to see it right

[00:21:06.799] here. Go to the GitHub. I'll show you

[00:21:08.000] what it is and just scroll down.

[00:21:12.000] >> Just let's just look at these tool

[00:21:13.200] configurations. Let's just look at how

[00:21:14.320] many they have first.

[00:21:15.039] >> God,

[00:21:15.600] >> like look at this stuff.

[00:21:17.600] >> Yeah,

[00:21:18.000] >> we're giving it and this is just the

[00:21:19.919] docs. This isn't even like the MCP

[00:21:21.679] format. I promise you the actual MCP is

[00:21:23.760] not this short.

[00:21:25.360] >> It's going to be longer than this. And

[00:21:26.720] like well, no wonder you just spent 60k

[00:21:28.960] tokens of your context window doing

[00:21:30.400] this. And if you're using 128k to model

[00:21:33.039] by chance and you're not using one of

[00:21:34.480] the 1 million context windows, well,

[00:21:36.640] duh. it's not working. You just use half

[00:21:38.480] your context window just to describe it

[00:21:40.080] how to use the GitHub.

[00:21:41.679] >> So, and it looks like they do have flags

[00:21:43.520] for hiding and removing stuff. So, you

[00:21:45.360] wouldn't even have to wrap this. But,

[00:21:46.480] like if you if you if you care and you

[00:21:48.960] only want to work with issues, then you

[00:21:51.280] can probably trim it down quite a bit.

[00:21:53.840] >> That's if you're running the GitHub MCP

[00:21:55.679] on your own. That's only if you're

[00:21:57.280] running the GitHub MCP server on your

[00:21:58.640] own. If you're using

[00:21:59.919] >> When would you not be When would you not

[00:22:01.520] be running it on your own? or you might

[00:22:02.799] be using like an MCP remote and using

[00:22:04.960] someone else's GitHub server.

[00:22:07.520] And this also requires you to know ahead

[00:22:09.440] of time what your MCP services are. So

[00:22:11.520] like let's let's imagine we're in a

[00:22:13.840] world where

[00:22:15.120] >> I'm jump back to the whiteboard.

[00:22:17.120] >> Yeah, I'm running a bunch of GitHub

[00:22:18.400] commands. Sometimes I get commit,

[00:22:19.679] sometimes I get pull, sometimes I um

[00:22:23.200] sometimes I track issues, I do various

[00:22:25.760] things. Now I have to spin up a

[00:22:27.520] different GitHub MTP for every single

[00:22:29.200] instance that I want to go call the

[00:22:30.799] model on. It basically boils down to

[00:22:33.039] either me prescribing everything ahead

[00:22:34.799] of time or me somehow training the model

[00:22:37.679] to do this. And I think the very

[00:22:39.600] interesting point that Joff made was

[00:22:41.440] like or Jeff made was like instead of um

[00:22:45.120] instead of actually passing in the

[00:22:47.120] GitHub MCP, you can just use the GH CLI

[00:22:50.320] which the model is very very well

[00:22:52.159] trained on. You don't need an MCP in

[00:22:55.039] this scenario because if you ask like I

[00:22:57.360] don't know just ask Claude to like dump

[00:22:58.720] out the GH command for like

[00:23:00.240] >> Yep.

[00:23:00.720] >> getting a specific issue. There you go.

[00:23:02.960] >> Using GH. Yeah.

[00:23:04.080] >> I mean this is going to work. I

[00:23:05.600] guarantee you it's going to oneshot this

[00:23:07.280] on the first try and you're not going to

[00:23:08.640] have any issues.

[00:23:09.760] >> Exactly. And I don't know what model

[00:23:11.039] you're using.

[00:23:11.520] >> It's like cool. Here's this is Opus. But

[00:23:13.440] like it doesn't matter. Sonic canes

[00:23:14.880] one-shot this too. And so

[00:23:18.400] >> so so what I want to get into in the

[00:23:19.520] time we have left and then we'll make

[00:23:20.640] time for questions is basically like how

[00:23:22.559] do you get around this and how do you

[00:23:23.840] engineer around this and basically what

[00:23:25.440] we've done at human layer is we've

[00:23:26.720] written our own kind of wrapper around

[00:23:28.559] the linear CLI that lets us it's not

[00:23:31.200] only that it's not an MCP it's just a

[00:23:32.960] CLI because bash is pretty good when

[00:23:34.640] you're and if you're using a coding

[00:23:35.840] agent you don't really need more um but

[00:23:39.280] basically this lets you control every

[00:23:41.760] token that comes out and so we are using

[00:23:45.440] um

[00:23:46.960] we are using basically like markdown.

[00:23:49.280] We're pulling out the fields that we

[00:23:50.720] care about and then we're just pulling

[00:23:52.559] the markdown. And then if you want to

[00:23:54.720] get the comments, you just have another

[00:23:56.400] flag for getting the comments. And that

[00:23:58.000] all happens outside of the model versus

[00:24:00.799] if uh so yeah, here's a bunch of

[00:24:03.200] comments on this issue. This happens to

[00:24:04.559] have been open for a while, so there's a

[00:24:05.919] lot of comments on it. Um but if you

[00:24:09.120] want to expose this stuff to the model,

[00:24:11.679] I mean, this is pretty this is pretty

[00:24:13.200] dense. And so I might say like, you

[00:24:14.480] know, tell the model to fetch it into

[00:24:15.919] like a ticket.md and then it can read it

[00:24:18.080] incrementally or whatever it is. But

[00:24:19.760] this is so much more flexible because

[00:24:21.760] you're not forced to push the inputs and

[00:24:24.000] outputs through your model's context

[00:24:25.440] window. The model can just use bash and

[00:24:27.760] stream everything into a file and then

[00:24:29.360] read the file incrementally. You have it

[00:24:31.120] there. You don't have to call it again

[00:24:32.960] uh if you don't want to. Um,

[00:24:36.400] and so what this means is like if we go

[00:24:39.120] and we run this with our token counter,

[00:24:41.679] we can kind of compare the like I want

[00:24:44.000] to just see how this works, but is like

[00:24:46.480] um if we ask it to do I'm just going to

[00:24:49.440] do missions cuz I'm not convinced that

[00:24:52.559] the actual uh the white labeling of MCPS

[00:24:56.320] is working as I expect it to. But um we

[00:24:59.120] can grab this one and say fetch the

[00:25:01.760] issue and all comments and we'll see the

[00:25:03.840] the huge difference in token usage

[00:25:06.720] between using the MCPS and going back

[00:25:08.960] and forth versus um versus just uh I'll

[00:25:13.039] run another one over here which is um we

[00:25:16.000] can take there's like another claude MD

[00:25:19.840] linear CLI into cloudMD. And so instead

[00:25:25.520] of having a [ __ ] ton of MCP tools, we

[00:25:27.760] have this really tight, very small, very

[00:25:29.760] token efficient description of like

[00:25:32.080] here's how to fetch an issue, here's how

[00:25:34.080] to fetch it with comments. And instead

[00:25:35.760] of 12,000 tokens, this is probably like

[00:25:37.760] a max 100 tokens of like here's the

[00:25:39.919] tools and here's how to use them. Um,

[00:25:44.159] and so let's see. This was 24,000 tokens

[00:25:47.600] to fetch it. I think it actually

[00:25:49.200] probably used the bash tool. Um, it

[00:25:52.080] didn't even use the linear MCPS. Um,

[00:25:56.240] damn. All right, we'll have to post uh

[00:25:57.919] we'll get the prompt right and we'll

[00:25:59.039] we'll post it up afterwards. Um, but if

[00:26:01.919] we do it this way and we do the same

[00:26:04.000] thing and we just take out the linear

[00:26:06.880] MCPS and we have this new cloud MD that

[00:26:09.200] says use the CLI,

[00:26:11.520] um, we should see far less tokens get

[00:26:14.320] used in the cache creation.

[00:26:18.320] So like uh Dax, what would you say is

[00:26:20.240] like the general summary that you would

[00:26:21.600] tell people here? Like what what is like

[00:26:23.279] the general takeaway is like when should

[00:26:25.039] someone use MCP in your mind? Um it's

[00:26:27.600] again it's like if you don't if you

[00:26:30.000] don't know how to integrate the API or

[00:26:31.919] you don't want to or you don't have the

[00:26:33.520] time or you want to do an experiment

[00:26:35.200] then like yes you can totally just use

[00:26:37.760] the MCP play with it but then if you're

[00:26:39.919] using something all day in your workflow

[00:26:42.240] and like it's the same thing we tal

[00:26:44.799] about we talked about last time in this

[00:26:46.880] like hierarchy of leverage right is like

[00:26:50.320] the more something impacts your workflow

[00:26:53.520] the more you should care about it. And

[00:26:55.840] so like I put your MCP tools somewhere

[00:26:57.919] down here. If everybody on your team is

[00:27:00.000] going to be using something every day as

[00:27:02.000] part of their workflow, then it makes

[00:27:03.919] sense to engineer it because if you make

[00:27:05.840] it 1% better and use, you know, instead

[00:27:08.480] of using 2% of the context window, use

[00:27:10.240] 1% or instead of using 7% of the context

[00:27:12.640] window, you use 1%. Then that's going to

[00:27:15.279] have massive campa cascading impacts

[00:27:17.360] across your whole team. If you're like,

[00:27:19.600] let me play with this and see if this

[00:27:21.039] works, then yeah, just use the MCP

[00:27:23.520] because it's off the shelf and it just

[00:27:24.720] works. It's the same thing as like if

[00:27:26.480] you were going to pull an npm package

[00:27:28.080] for, you know, a sorting algorithm and

[00:27:29.840] then you're like, okay, this is actually

[00:27:30.960] the core most important loop in our

[00:27:32.720] code. So, we need to write our own

[00:27:34.480] version of it because algorithms is a

[00:27:36.320] bad example because there's like a

[00:27:37.679] specific reference implementation, but

[00:27:39.200] something performance sensitive that's

[00:27:40.799] going to be in a really tight loop, then

[00:27:42.880] that's when you need to think about uh

[00:27:45.360] spending more time optimizing it. And

[00:27:46.880] this is what we talk about all the time,

[00:27:47.840] right? Vib, your example is like, yeah,

[00:27:49.679] use 03 to solve the problem until it's

[00:27:51.520] either too slow or too expensive and

[00:27:53.520] then go figure out whatever prompt is

[00:27:55.200] going to help you use GPT 40 mini to do

[00:27:58.320] the same work with almost as good

[00:27:59.919] results, right?

[00:28:01.200] >> Yeah, I think it's the same thing

[00:28:03.600] actually. I echo that 100%. Like, and

[00:28:07.520] for me candidly, I haven't really I

[00:28:09.679] found it more work to go dig into MCPS

[00:28:11.840] than to just like write a bash script

[00:28:14.559] because like cloud code will just turn

[00:28:16.000] out a bash script real fast for almost

[00:28:17.600] everything I want to do

[00:28:19.919] and like the MCP becomes more overhead

[00:28:21.760] because I have to go figure out how to

[00:28:22.640] go set it up and learn it really fast

[00:28:24.480] and when it doesn't work, debugging

[00:28:26.640] becomes a problem for me. Um, so at

[00:28:29.360] least whenever I have tried, I found the

[00:28:31.200] debugging loop is bad enough that I

[00:28:33.279] found it just useful to just start with

[00:28:34.640] bash by default or like custom scripts

[00:28:36.480] whenever I go do this. Um, and I

[00:28:39.360] actually don't have any MCPS installed

[00:28:41.200] on my on any agent that I use

[00:28:43.360] personally.

[00:28:44.640] >> Well, and it it depends what you're

[00:28:46.399] doing, right? If you on the runtime, if

[00:28:47.760] it's a coding assistant and you can

[00:28:49.279] dynamically expand the runtime as you

[00:28:51.039] need new things, then yes, of course,

[00:28:54.240] why would you go use something off the

[00:28:55.679] shelf if you know exactly what you want

[00:28:57.120] and you know enough to review the

[00:28:58.399] scripts and make sure that it's correct.

[00:29:00.159] I think where MCP really really shines

[00:29:02.720] is in allowing people who don't have the

[00:29:05.520] will or the time to extend existing

[00:29:07.919] software. So, if you have like your

[00:29:09.360] cursor window here,

[00:29:11.600] uh, and like I know how to use cursor,

[00:29:13.840] or maybe it's like claw desktop or

[00:29:15.440] whatever it is, um, and I want to just

[00:29:17.760] [ __ ] connect this to all my stuff,

[00:29:19.520] but I'm not, you know, a super I don't

[00:29:21.360] know why I chose to do a dark mode theme

[00:29:23.039] here.

[00:29:23.279] >> If I'm not comfortable in code, then

[00:29:24.559] it's going to be really annoying for me

[00:29:26.240] to go connect that all the way down

[00:29:27.760] through.

[00:29:28.960] >> Uh, exactly. Steve made a good point.

[00:29:30.559] Like if you're APIs that you don't know

[00:29:32.000] very well or like if you're not familiar

[00:29:33.840] if you don't feel comfortable with like

[00:29:35.200] software as much because like AI has

[00:29:37.760] enabled you to go explore software in a

[00:29:39.360] way that you couldn't then it's really

[00:29:40.559] good. Uh the browser use MCP sounds

[00:29:43.919] really interesting. I haven't personally

[00:29:45.600] tried it. Uh people have tried

[00:29:47.520] playright. um John's saying in the chat.

[00:29:50.960] Um so I do like the premise of that and

[00:29:54.640] then like I found that like

[00:29:58.000] personally it's just like

[00:30:01.279] I don't know my opinion is just like all

[00:30:02.640] this stuff while it's nice is just it

[00:30:04.080] slows you down unless you have a good

[00:30:05.840] developer loop. If the thing you're

[00:30:07.760] doing is writing code then the thing

[00:30:09.520] that matters the most is how fast can

[00:30:11.520] you know the code is working or not

[00:30:12.880] working. And if you're stuck debugging

[00:30:14.720] the thing that is generating the code

[00:30:16.080] for you, that is a much slower iteration

[00:30:18.720] loop than actually stuck debugging the

[00:30:20.320] actual code itself.

[00:30:21.360] >> Yeah, I like that. Um, cool. What other

[00:30:25.039] questions?

[00:30:26.559] >> Um, have we got questions for people

[00:30:27.919] today? Dex, what I'd love to do with

[00:30:29.440] like the remainder of the time is

[00:30:30.640] actually like let's look at the plot

[00:30:31.919] system prompt while we go while I pull

[00:30:34.000] up questions. I'm going to show this.

[00:30:36.159] >> We got a question. What are the best

[00:30:37.600] resources to build MCP or something like

[00:30:40.080] uh Zapier?

[00:30:42.480] To be honest, uh that problem is not as

[00:30:45.520] hard as you might suspect. Uh in order

[00:30:47.919] to go build that out, there's actually a

[00:30:50.480] small little piece of code that we have

[00:30:52.159] in our past examples. Let me share my

[00:30:54.480] screen. I'll show you. Um and I'll show

[00:30:57.120] you guys where that example is so you

[00:30:58.720] can take a look at it. Share screen.

[00:31:00.799] Screen. Cool. So, in one of our past uh

[00:31:03.919] episodes, we talked about this

[00:31:06.640] MCP. We talked about Oh. Oh, the like

[00:31:09.919] how to select from a thousand MCP tools.

[00:31:12.559] >> Exactly.

[00:31:14.240] One of these is this one. I don't know

[00:31:15.360] which one it is. Oh, right here.

[00:31:18.640] >> Um, and we actually talked about this

[00:31:19.919] and we actually have code samples of

[00:31:21.120] actually how to go run this. It turns

[00:31:22.559] out writing an MCP loop is actually

[00:31:24.399] pretty straightforward. You just need a

[00:31:25.919] way to turn open API specs into prompts

[00:31:29.039] and then a way to receive those prompts

[00:31:30.799] and feed it back in to the open API

[00:31:32.880] spec. So when Dex was showing the

[00:31:34.960] example where like the linear tool was

[00:31:36.480] named MCP_linear

[00:31:38.720] list uh issues that's simply because a

[00:31:41.679] clawed code CLI needs a way to remap

[00:31:44.480] like when the LM selects that tool they

[00:31:46.480] need a way to remap and pick that tool

[00:31:48.720] and actually execute it through the MCP

[00:31:50.880] agent. So like the code you end up

[00:31:52.880] writing

[00:31:54.960] actually ends up looking something like

[00:31:56.159] this. I'll just write a quick little

[00:31:57.360] pseudo code here. Um, which ends up

[00:31:59.760] being like let agent equals all

[00:32:04.880] >> I think. Do you mean to be sharing your

[00:32:06.960] editor?

[00:32:08.000] >> Oh, I'm not sharing the right screen.

[00:32:10.399] Okay, I'm sharing another screen now.

[00:32:12.640] response equals like call agent user

[00:32:16.080] message tools and tools has to be like

[00:32:21.279] generate uh load mcp file

[00:32:25.919] >> mcp you connect to the server and then

[00:32:28.399] you talk to it and you get its list of

[00:32:30.159] tools and then you pass that into your

[00:32:31.679] call and that's all that's happening

[00:32:33.120] >> it's an open API spec so all you're

[00:32:34.960] doing is parsing that turning into some

[00:32:36.640] data model and most people can read JSON

[00:32:38.559] and turn it from one JSON to another

[00:32:40.159] JSON so you go do that uh and then you

[00:32:43.120] just say like for tool in response

[00:32:48.000] um um if done if uh response

[00:32:52.960] else what you do is like you just say

[00:32:54.720] like

[00:32:56.480] tools do uh tools.lookup lookup tool

[00:33:01.519] name or something and then like run uh

[00:33:05.120] state append

[00:33:07.519] result

[00:33:09.600] and then you just put this in a while.

[00:33:11.360] That's all an MCP tool call is. You load

[00:33:14.080] your tools from an a from a file. You

[00:33:17.440] have some initial state which is a user

[00:33:19.039] message. Then you call the agent with or

[00:33:21.120] call an LM with a bunch of tools and the

[00:33:23.760] state passed in. Then you check if your

[00:33:25.679] tool indicates you're done. Return the

[00:33:27.120] message to the model somehow. Otherwise,

[00:33:29.279] you in your tools registration, you look

[00:33:31.360] up the name that the model selected and

[00:33:33.440] you pass it to the you pass in the

[00:33:35.360] parameters of the model selected and you

[00:33:36.799] run it and then you get the result pass

[00:33:39.679] to the state and keep on running this in

[00:33:41.679] a while loop until you're actually done.

[00:33:44.159] So hopefully harsh that answers your

[00:33:45.600] question of how someone would go and

[00:33:46.960] build this out along the way.

[00:33:49.360] >> Yeah, this is uh this is a good thing to

[00:33:51.679] just kind of jam into your brain is like

[00:33:54.640] >> this is how agents work. If you haven't

[00:33:56.640] written this while loop, write this

[00:33:59.039] while loop. Like literally don't use a

[00:34:01.120] framework. Just like write the while

[00:34:03.120] loop. If you're curious how to do it, we

[00:34:05.200] have a bunch of examples in our podcast

[00:34:07.279] of how to go do it. And but like this is

[00:34:10.079] like the crux of how models agents work.

[00:34:14.560] >> Okay. I have more fun context window

[00:34:16.240] stuff if you want to pop back over.

[00:34:18.079] >> Yeah, I'll stop screen sharing. Uh I'm

[00:34:20.240] going to go catch up with other

[00:34:21.520] questions while you go do that.

[00:34:22.879] >> Cool. Um, so we did someone did share uh

[00:34:25.919] Jeff's article. This is definitely worth

[00:34:27.280] a read. And he just did a talk that I

[00:34:28.720] posted on Twitter recently. Um, but it's

[00:34:30.560] basically like a tool is just a

[00:34:33.440] description of what the fields are and

[00:34:35.359] what they are. Um, and so you can figure

[00:34:37.040] out what the tool is and all the models

[00:34:38.159] have their own way of serializing tools

[00:34:39.679] into the model and especially the closed

[00:34:41.200] platforms, it's kind of like you don't

[00:34:42.480] get good visibility into it, but you can

[00:34:44.480] count the tokens and every single like

[00:34:46.960] word in your tool description or your

[00:34:48.879] argument description uh matters to the

[00:34:51.679] model. And so like when Reddit comes up

[00:34:54.159] and says like, "Hey, we must have these

[00:34:56.159] MCP servers if you're going to work."

[00:34:57.920] And then you can look and you say,

[00:34:58.880] "Okay, the GitHub MCP server 60,000

[00:35:00.960] tokens. Memory MCP 10,000 tokens." Like

[00:35:03.760] you put all these in there and this is

[00:35:05.280] literally straight from Jeff's talk. Uh

[00:35:06.800] but it's like you put all these in there

[00:35:08.240] and you're literally starting at 100,000

[00:35:10.240] context usage. You're using all of your

[00:35:12.240] like useful part of the context window

[00:35:14.400] because again remember like your context

[00:35:17.599] window. This is like the the money

[00:35:19.280] section of your context window. This is

[00:35:20.720] where you're going to get good work

[00:35:21.520] done. Everything goes downhill after

[00:35:23.119] here. And so if you're starting your

[00:35:25.359] work with your first user message at

[00:35:27.680] like 60% context window usage, you are

[00:35:30.560] never ever ever going to get good

[00:35:32.800] results from cloud code. like maybe for

[00:35:35.359] simple stuff, maybe in like really

[00:35:36.960] simple code bases or or like new like

[00:35:39.920] new projects you can get it to do stuff,

[00:35:42.000] but if you load in 50 MCP tools, like

[00:35:44.480] it's all about like yes, cloud makes it

[00:35:46.960] easy to just get going, but if you don't

[00:35:48.960] understand what's happening under the

[00:35:49.920] hood, then you are going to have bad

[00:35:52.160] results. Um, and so understanding this

[00:35:54.640] stuff and understanding like yes, the

[00:35:56.160] long context models can do needle in a

[00:35:57.839] haystack really well, but most of the

[00:36:00.079] general performance drops off pretty

[00:36:01.839] quickly as you add more tokens. Um, oh,

[00:36:04.320] cool. And Een has a spreadsheet of which

[00:36:05.920] of these and how much how many tokens

[00:36:07.680] they put in.

[00:36:08.560] >> They just take a large amount. Um, on a

[00:36:11.119] very actually Alexander asked a great

[00:36:13.359] question. It's it's related but not uh

[00:36:15.760] and I think in a way that Alexander

[00:36:17.200] probably unex did not expect which is

[00:36:20.000] >> how do you deal with thoughts on images

[00:36:22.079] in prompts or other things that are

[00:36:24.079] going on? Um, and I have a lot of

[00:36:27.599] opinions on this person. I'm sure Dex

[00:36:29.280] does too. Um,

[00:36:30.480] >> yeah. But I'm going to take over the

[00:36:32.480] screen decks.

[00:36:34.800] Uh share the screen. And funnily enough,

[00:36:36.880] we actually talked about this in not too

[00:36:38.560] long ago, which is when we talked about

[00:36:41.040] um uh multimodal stuff.

[00:36:44.880] >> Yeah.

[00:36:46.240] >> The fact is like images can sometimes

[00:36:49.359] take up more tokens to describe what you

[00:36:51.119] want and sometimes less tokens to

[00:36:52.560] describe what you want. It really

[00:36:54.640] varies, but sometimes it can be

[00:36:56.560] incredibly powerful. If you're doing web

[00:36:58.720] development, an image is likely going to

[00:37:00.880] help describe the mistake that you made

[00:37:02.720] to the model way better than a visual

[00:37:04.720] will. If it's a very small thing, uh

[00:37:07.440] words will probably just do good enough.

[00:37:08.720] But like if it's a very complex thing

[00:37:09.920] like move this thing over here, the

[00:37:12.160] image will

[00:37:12.720] >> or like

[00:37:14.240] >> if you really don't understand web

[00:37:16.160] development and you can't like if you

[00:37:17.760] know how CSS works and you're like, oh,

[00:37:19.359] we need to add padding to that node,

[00:37:21.440] then you can say that. But if you don't

[00:37:22.880] know how to explain that to a model

[00:37:24.400] because you don't know the difference

[00:37:25.200] between margin and padding, which is me,

[00:37:27.359] then yeah, give it the picture and it'll

[00:37:29.040] be like, "Oh, I need more padding."

[00:37:30.720] >> Exactly. And I think like it it's really

[00:37:33.440] uh a nuance. Uh but honestly,

[00:37:36.480] images work really well. People that

[00:37:38.400] aren't using I I have a I might have

[00:37:41.119] this thing running. It's like check this

[00:37:43.119] out. Like this is a straightup image off

[00:37:45.040] the model. It generally works off the

[00:37:46.960] bat. to like boom phone call extract and

[00:37:52.480] this is straight up live running off the

[00:37:54.720] model and models are really really good

[00:37:58.000] at image processing. All right. And

[00:38:00.240] there you go. And it just pulls stuff

[00:38:02.480] out. Um like if you're not using models

[00:38:05.040] for image processing you're you're

[00:38:06.800] hurting yourself. Go do that.

[00:38:08.880] >> Yeah.

[00:38:09.200] >> Um at least in my opinion.

[00:38:11.839] >> Yeah. Um all right. All right, I got one

[00:38:14.000] more thing on context windows um which

[00:38:16.240] is that cloud system prompt stuff and

[00:38:18.079] this is what you can figure out by

[00:38:19.440] actually like going through the traces

[00:38:21.599] itself because this won't come out in

[00:38:23.200] the claw JSON output lines um but like

[00:38:25.760] you may have stuff that always goes in

[00:38:27.520] your context window like but you should

[00:38:29.920] know that in your cloud MD it is

[00:38:31.920] injected with a very specific message so

[00:38:34.240] whatever you put in your cloud MD it

[00:38:36.320] will be added at the very end you will

[00:38:38.240] get this thing which is basically like

[00:38:40.160] do not pay attention to anything in

[00:38:41.680] clawet MD unless it's super relevant.

[00:38:44.880] And most of the time you should ignore

[00:38:46.480] what's in here, which is why I don't

[00:38:48.400] know if you found you put certain things

[00:38:49.760] in cloud MD like always run the tests

[00:38:51.920] after making a change and it kind of

[00:38:53.599] only does it like 10% of the time. This

[00:38:56.400] is why and I think this is a product

[00:38:58.720] decision from anthropic and I understand

[00:39:00.560] why they did this. It's probably because

[00:39:02.400] most people don't know how to write a

[00:39:04.160] good claude MD and in many cases over

[00:39:07.200] steering the model is actually more

[00:39:09.119] harmful than understeering it because

[00:39:11.200] the model has emergent capabilities and

[00:39:12.960] so like you'd rather deemphasize the

[00:39:15.599] inputs from an unskilled prompter than

[00:39:19.200] like risk that they basically just tank

[00:39:21.680] the performance by having a a rogue

[00:39:23.599] sentence and claw MD that ruins

[00:39:25.040] everything.

[00:39:26.560] >> Exactly. That's why they have this and

[00:39:28.320] it makes sense. But like if you're a

[00:39:29.839] skilled prompter, it's hurting you.

[00:39:31.680] >> Yeah. And so this is why actually like

[00:39:33.200] you should know what's in your context

[00:39:34.320] window. And what I do is I actually

[00:39:35.440] craft the context window. So all of my

[00:39:37.359] instructions, I don't put them in

[00:39:38.800] cloudmd. They're actually dynamic based

[00:39:40.720] on the files in the repo. Um because

[00:39:43.280] context engineering is about blending

[00:39:44.640] deterministic and non-deterministic

[00:39:46.320] code. This is what we always talk about

[00:39:47.680] like where do you use the LMS, where do

[00:39:49.119] you not? And so I actually have a slash

[00:39:51.280] command in one of our repos. I think we

[00:39:52.800] talked about this on the cloud for

[00:39:53.920] non-Cloud like usages, but there's a

[00:39:56.160] /CTX that basically says run this make

[00:39:59.359] task and then run this make task and

[00:40:01.520] then do whatever the user said. And so

[00:40:03.839] it's like if I run /ctx with some

[00:40:06.240] specific instructions, the first thing

[00:40:08.160] it's going to do is run this print

[00:40:10.160] context, which is literally just going

[00:40:11.920] to cat out the contents of a bunch of

[00:40:13.680] files that explains. We use this to like

[00:40:15.440] run the company and run our CRM and

[00:40:16.880] stuff like this. And so it's going to

[00:40:18.400] cat out a bunch of files that show,

[00:40:20.000] okay, here's what we've been talking

[00:40:20.880] about recently. here's our key metrics,

[00:40:22.880] here's the last couple investor updates,

[00:40:24.640] things like this. Um, and so this is

[00:40:26.880] crafting your context window. You're

[00:40:28.160] telling the model the first thing you do

[00:40:29.760] is you like output these things. And

[00:40:32.320] it's dynamic, right? You could put it in

[00:40:33.920] a file and just have it output it. But

[00:40:35.760] what I really want is I just want to

[00:40:37.119] take the top 200 lines of these like

[00:40:38.880] couple files. And then you can also like

[00:40:42.000] write code to generate the tree. And so

[00:40:43.839] like we have a file tree here that is

[00:40:45.520] basically just like here's every single

[00:40:47.440] file that is interesting to you that is

[00:40:49.680] like sliced and filtered based on the

[00:40:51.599] markdown. We use like markdown front

[00:40:53.280] matter a lot. So this is a file in our

[00:40:55.119] CRM. And so it's got a bunch of like

[00:40:56.720] fields at the top that you can parse for

[00:40:58.319] slicing and dicing. Um and then it's and

[00:41:02.079] then we can just like okay the things

[00:41:03.760] that match the filter print the file

[00:41:05.599] name and the summary from the file

[00:41:08.400] itself. And so like this is again like

[00:41:11.599] crafting your context window. This is

[00:41:13.839] the bigger picture and like this is the

[00:41:15.839] thing that even as the models get

[00:41:16.960] smarter, even as the coding agents

[00:41:18.400] change, like as long as we're still on

[00:41:20.240] like transformer-based LLM technology

[00:41:22.240] and we don't have any like huge

[00:41:23.440] breakthroughs, this will matter for a

[00:41:25.520] while.

[00:41:26.319] >> Yeah. That said, I'll I'll push one

[00:41:28.800] counterpoint there uh really fast

[00:41:30.480] because I do agree with everything that

[00:41:31.760] says, which is the models are changing

[00:41:33.440] at a rate that I personally did not

[00:41:35.200] predict. So it's possible that today's

[00:41:36.800] context limit is around like 40 60%

[00:41:38.560] according to Dex in terms of how good it

[00:41:40.000] is. It might be tomorrow's model is like

[00:41:41.599] good at 60% or 80%. So like what I find

[00:41:44.880] is useful is I just try and push the

[00:41:46.319] model like sometimes I'll just toss in a

[00:41:47.839] bunch of context and just see how well

[00:41:49.280] it deals and like sometimes it works,

[00:41:52.079] sometimes it doesn't. So like while it's

[00:41:53.760] good to have a general rule of thumb,

[00:41:55.520] what I find is it is definitely good to

[00:41:59.440] always texture yourself as well. And

[00:42:01.200] thanks for the feed by the way John.

[00:42:03.599] Thanks for the feedback. We'll fix the

[00:42:04.720] audio next time and get it working. Not

[00:42:07.119] sure why my audio is softer than someone

[00:42:08.880] else's, but just like keep on pushing

[00:42:11.200] the model to their limits. Push in 100k

[00:42:13.599] tokens and see if it works and does what

[00:42:15.200] you want. Push in easy tasks, push in

[00:42:17.200] hard tasks, and just see what it works.

[00:42:18.880] >> Talking about models evolving as

[00:42:20.560] rapidly, do you still use SAP in

[00:42:22.640] production instead of function calls?

[00:42:24.960] >> Um, everyone that uses BAML does. Um,

[00:42:27.839] and it works pretty well. It actually we

[00:42:29.760] tested it on GPD5. We have better

[00:42:32.160] performance on tool calling on GT5 as

[00:42:34.000] well. And I think it just go boils down

[00:42:36.400] to the same basics is like

[00:42:39.119] describing the tool to the model just

[00:42:41.839] gives you better results in general and

[00:42:44.560] not requiring JSON will generally always

[00:42:47.119] give you better results.

[00:42:48.240] >> What is SAP?

[00:42:49.280] >> Um little off topic uh but sure

[00:42:54.240] uh what is SAP for those of you that

[00:42:56.800] don't know? Well, I'll show you guys

[00:42:58.079] really fast. um screen. I will share a

[00:43:00.480] browser window or a cursor window.

[00:43:03.200] What's the next question, Dax, while I

[00:43:04.480] pull up this?

[00:43:05.200] >> Um kind of a side note. Is BAML likely

[00:43:08.480] to support hotel at any point? I can

[00:43:10.240] take this one. Uh actually, maybe I

[00:43:13.839] shouldn't.

[00:43:16.560] Uh I have hacked BAML by you could

[00:43:19.440] there's like a modular API where you can

[00:43:21.200] separate the request and response. And

[00:43:23.040] if you hang on to the Bambble Discord,

[00:43:24.400] there's a bunch of people who have

[00:43:25.440] gotten it to go to any because it's just

[00:43:28.000] key value pairs. You can send it

[00:43:29.599] anywhere.

[00:43:30.480] >> Yeah. Um what is what is SAP? Um SAP is

[00:43:34.640] this algorithm that we have that says

[00:43:36.319] when you ask a model, in this case, turn

[00:43:38.160] an image or a string into a ré data

[00:43:40.240] model which is described like this. SAP

[00:43:42.880] is this really really cool algorithm

[00:43:44.319] that we have that says no matter what

[00:43:45.760] the model does, it will work. So in this

[00:43:47.359] case, I put back JSON and we got to

[00:43:49.760] ignore it. But we can go further and say

[00:43:52.400] no quotes around keys. So like my prompt

[00:43:56.000] is literally this really really basic

[00:43:57.839] thing. Add three reasons why this resume

[00:43:59.599] is a good fit. And I just changed the

[00:44:00.880] prompt from the previous. I'm still

[00:44:01.920] using the John Doe example. But now when

[00:44:04.319] I go run it, well the model didn't

[00:44:05.599] listen. I'm using GPT4 mini. But this

[00:44:07.280] thing is not valid JSON at all. It has

[00:44:09.839] no quotation marks. It kind of has

[00:44:11.280] nothing. But we still pulled out the

[00:44:13.119] right data. So, our parser is kind of

[00:44:14.880] like a

[00:44:16.560] uh you can think of it as a um SAP on

[00:44:20.319] steroids or JSON.parse on steroids is

[00:44:23.599] kind of like how I would think about it.

[00:44:25.920] >> Oh, so many DSPI questions. We talked

[00:44:28.319] about this a couple week weeks ago um

[00:44:30.720] about people combining DSP's approach

[00:44:33.680] with BAML's schema line parser approach

[00:44:36.319] and they actually work best when you put

[00:44:38.480] them together which is exciting.

[00:44:41.280] Thanks for the abort controller. Yeah,

[00:44:42.880] that was a fun project we did. Um,

[00:44:46.319] >> as uh it started off as a bit and then

[00:44:48.560] we decided to see how much how much code

[00:44:50.240] we could ship in one day. Uh, and uh, I

[00:44:54.079] actually got to architect the Golang

[00:44:55.520] side of that. Um, because Claude was bad

[00:44:58.079] at fetching data from the internet about

[00:45:00.640] how to do idiomatic cancellation in Go.

[00:45:02.880] So thankfully I spent five years

[00:45:04.400] building that at replicated.

[00:45:06.800] >> Um,

[00:45:07.599] >> sorry, my dog went bonkers cuz uh,

[00:45:09.760] someone came into my house. You are all

[00:45:12.480] good. People are talking about how great

[00:45:13.839] the abort controller is. I think I think

[00:45:16.000] I think uh any final questions otherwise

[00:45:19.200] we will wrap it up and uh as always we

[00:45:22.800] will post the code and the recordings

[00:45:24.960] and uh the next event on Luma within uh

[00:45:27.200] about 24 hours.

[00:45:28.319] >> Um Javier's got a question. Does someone

[00:45:31.280] here know why the Gemini streaming model

[00:45:33.839] outputs sentence chunks uh but word

[00:45:36.880] chunks?

[00:45:38.480] Uh oh. Well, one thing to note about how

[00:45:40.720] to how streaming works under the hood is

[00:45:43.119] the model is always streaming, the model

[00:45:45.040] only generates one token at a time.

[00:45:46.720] There's no way to make the model

[00:45:47.680] generate two tokens or skip towards

[00:45:50.160] that. Um, what ends up happening is

[00:45:54.319] while the model is always streaming, the

[00:45:56.800] API provider that you're using chooses

[00:45:59.440] how many tokens to send you at any given

[00:46:01.280] stream time.

[00:46:02.480] >> Their prerogative.

[00:46:04.880] >> So unless you own the model, you can't

[00:46:06.640] guarantee when you get it. OpenAI may

[00:46:08.960] currently be giving you one token at a

[00:46:10.480] time. I know sometimes they give me two

[00:46:12.160] or three. It really varies. Sometimes

[00:46:15.040] they give you 10. It varies. Like I

[00:46:17.760] would not build any any amount of

[00:46:19.920] reliability ever in your application.

[00:46:21.599] That depends on getting one token at a

[00:46:23.280] time. It would be a bad bet to make.

[00:46:26.640] >> Yep.

[00:46:28.079] >> Sick.

[00:46:29.119] >> I think there's one more a couple more

[00:46:30.880] questions. Do we see any? Uh did you

[00:46:33.200] give your opinions on DS5?

[00:46:35.440] I was talking about we talked about I

[00:46:37.280] forget which episode it is. We will find

[00:46:38.720] it and put it in the show notes, but we

[00:46:40.400] did talk about someone posted a study

[00:46:43.440] where it's actually the the best the

[00:46:45.599] best way to do this is to combine BAML

[00:46:48.160] and DSPI together.

[00:46:49.760] >> Yeah, I think the idea of DSPI

[00:46:51.599] personally is really interesting. I view

[00:46:52.960] DSP as like, oh, we don't actually want

[00:46:54.640] to go write the prompts. Uh maybe we can

[00:46:57.280] have something else autogenerate the

[00:46:58.560] prompts. I think that concept is

[00:47:00.560] actually really fascinating, but I think

[00:47:03.680] we're at depth. I think you made a tweet

[00:47:05.440] about this. It's just like we're in the

[00:47:06.560] early eras of how programming LMS works

[00:47:09.920] and like the early C compilers were just

[00:47:13.119] not that good. Like they they just

[00:47:16.160] weren't that good cuz they didn't know

[00:47:17.839] what kinds of things people wanted to

[00:47:19.119] write in C. So they couldn't possibly

[00:47:20.560] optimize very well. You need some bake

[00:47:22.960] time to make these sort of optimizers

[00:47:24.720] really really good. Um, and sometimes a

[00:47:28.319] lot of this stuff is just like like for

[00:47:31.119] example, MCP is this attempt for for

[00:47:34.880] writing this optimized tech. In theory,

[00:47:38.079] linear could sit down and optimize the

[00:47:39.920] heck out of the linear API for accuracy

[00:47:42.560] and like make it really like make the

[00:47:44.720] words perfect. And in that theoretical

[00:47:47.760] world, we should all use a linear MCP

[00:47:50.319] because it is the best way to interface

[00:47:51.839] with the model because the linear team

[00:47:53.040] owns that responsibility and optimizes

[00:47:54.720] the heck out of it. In practice,

[00:47:58.400] you end up in a world where it's not

[00:48:00.319] that good and that someone just ships

[00:48:02.319] something really really fast and it like

[00:48:04.160] looks like it works but doesn't actually

[00:48:05.760] work.

[00:48:06.400] >> Well, and I don't want to talk about it

[00:48:08.000] in terms of like quality or

[00:48:09.760] craftsmanship even. I think it's the

[00:48:11.359] same as that like system message in

[00:48:12.880] Claude MD where it's like they kind of

[00:48:14.560] have to optimize for like what's what's

[00:48:17.520] 80% of the value for everybody because

[00:48:20.319] they know the people who really care

[00:48:21.680] about every single token can always go

[00:48:23.200] do it themselves but I think the goal is

[00:48:25.359] like how do you give the most value to

[00:48:27.280] the broadest number of people

[00:48:29.520] >> exactly and like when I when I really

[00:48:31.280] think about this it's like I just don't

[00:48:33.760] think prompts per like personally my

[00:48:36.240] opinion is I don't think prompts are in

[00:48:37.839] a world where 80% is good enough

[00:48:40.400] >> because they're running it's like it's

[00:48:42.240] like CSS stuff like no one uses

[00:48:45.280] Bootstrap anymore because Bootstrap was

[00:48:47.359] 80% CSS.

[00:48:49.359] >> It's like it gets you the website but

[00:48:51.440] like you can't ever use Bootstrap as

[00:48:53.119] your design system unless you're Twitter

[00:48:54.559] and that is your actual design system

[00:48:57.119] because it doesn't it's not customizable

[00:48:59.119] enough. It's not maintainable. So then

[00:49:00.480] you end up using Shad CN because Shaden

[00:49:02.960] lets you as a developer have a good

[00:49:05.359] starting point but you get to own

[00:49:06.960] everything and edit it yourself. I think

[00:49:09.280] the premise that you will never want to

[00:49:11.359] read and write the you will never want

[00:49:13.119] to read the prompt and edit the prompt

[00:49:14.400] manually is fundamentally flawed. I

[00:49:17.359] think at least for the at least for the

[00:49:18.880] foreseeable future the next and by that

[00:49:20.480] I mean like the next 12 to 18 months

[00:49:23.680] is the furthest I would say you will

[00:49:26.480] want to see the prompt and you might

[00:49:28.319] want to have something write the first

[00:49:29.760] version of the prompt but likely you'll

[00:49:32.079] want to hand tune it and at to some

[00:49:33.920] degree to some or at least have

[00:49:35.359] visibility into what it is in a useful

[00:49:37.839] and editable way just like we have

[00:49:39.920] wanted that with CSS and it took us

[00:49:42.319] about like 20 years to make that

[00:49:43.520] conclusion about CSS that like hey we

[00:49:46.160] don't want like a framework that lives

[00:49:47.839] somewhere in npm node modules that is

[00:49:49.520] write only uh that is

[00:49:51.280] >> yeah we don't we don't want a component

[00:49:53.359] library we want a a platform for

[00:49:56.240] building component libraries that was

[00:49:58.000] the right level of configurability

[00:49:59.760] >> exactly and I think it's the same with

[00:50:01.440] prompts personally I think like you

[00:50:03.920] don't want a you don't want a prompt

[00:50:05.599] library you want a way to write prompts

[00:50:08.319] that you can edit and modify and do

[00:50:10.720] whatever you want but have really good

[00:50:12.559] jumping off points by default

[00:50:14.960] >> and I talked to really really

[00:50:16.319] opinionated designers. Just to like

[00:50:18.240] continue this analogy a little bit more,

[00:50:19.839] I talked to really good, really

[00:50:21.520] opinionated designers who care about

[00:50:23.760] every single pixel on the page and they

[00:50:26.559] love shad CN because they can apply

[00:50:29.760] every single style they want to every

[00:50:32.240] component and be guaranteed that it's

[00:50:34.000] customized and they don't have to reach

[00:50:36.079] through some like artificial interface

[00:50:38.240] which is like like Bootstrap has an

[00:50:39.760] interface to it. There's things you can

[00:50:41.040] do with Bootstrap and there's things you

[00:50:42.559] can't do. Whereas what Shad Cian gets

[00:50:45.280] you is the entire spectrum, the entire

[00:50:47.599] solution space of every single class you

[00:50:49.920] could apply is available to you. It's

[00:50:52.720] clean and nice via Tailwind and you have

[00:50:55.440] sane defaults. But if you want to change

[00:50:57.440] something, there's no like reading the

[00:50:58.960] docs of like, okay, how do I tell

[00:51:00.960] Bootstrap to apply padding to a

[00:51:03.280] component like this? You just look at it

[00:51:04.800] and you open the box and you set the

[00:51:06.400] padding. And I think the same is true

[00:51:08.079] for prompts right now. And the same is

[00:51:09.280] true for agents. Like a good agent

[00:51:10.800] framework will absolutely

[00:51:13.680] like give you the ability to reach into

[00:51:16.240] the box and customize everything

[00:51:18.319] >> without having to read.

[00:51:19.839] >> I think that point about reading docs is

[00:51:21.119] really important. I think Ariel as a

[00:51:22.800] good question is like oh does that mean

[00:51:24.160] like DSP changed that focus? I think DSP

[00:51:26.079] does a really really good job personally

[00:51:27.680] of getting people to start thinking

[00:51:29.280] about stuff as input output pairs but

[00:51:32.559] like at least when I worked in machine

[00:51:34.319] learning it's really really hard to

[00:51:36.000] actually build a golden eval data set in

[00:51:37.920] practice. I think it's a good jumping

[00:51:40.160] off point, but again, it just goes off

[00:51:41.839] to like it's really good to make an

[00:51:44.240] initial website with cloud code or

[00:51:46.160] something else, but at some point you

[00:51:47.599] always want that flexibility along the

[00:51:49.200] way. In general, I think flexibility has

[00:51:51.040] been really powerful. Um,

[00:51:54.000] exactly. I think John made a good point

[00:51:55.440] like generally frameworks have become

[00:51:57.280] more flexible and opinionate versus

[00:51:59.599] frameworks are becoming opinionated.

[00:52:01.119] Like I I think opinions are like people

[00:52:05.119] want to go in like people are becoming

[00:52:06.800] more people want to build more things

[00:52:08.880] not less things as time is going on.

[00:52:13.040] Um Nathan you asked an interesting

[00:52:14.800] question. What about context 7? I have

[00:52:16.240] no idea what context 7 is so I can't uh

[00:52:18.079] sadly answer that. Uh but um if you have

[00:52:21.520] a tidbit on what it is and we can take a

[00:52:23.280] look for next time. Uh Des is off on a

[00:52:25.359] call. Uh I think he's running late. I

[00:52:28.160] think we're ending the show today on

[00:52:29.760] this. Uh, if someone has a um a couple

[00:52:33.280] more questions, feel free to send them

[00:52:35.760] over on the Discord. Our Discord is

[00:52:37.200] generally open.

[00:52:39.040] If you have um other things that you're

[00:52:41.440] interested in chatting about, definitely

[00:52:43.359] send us links on what we chat about.

[00:52:45.920] This has been AI that works. If you want

[00:52:48.319] to join the next episode, uh you can

[00:52:50.079] subscribe to this calendar over here.

[00:52:52.160] and we'll generally post uh new events

[00:52:54.319] every Tuesday at um uh every Tuesday at

[00:52:58.319] 10 a.m. PST as per usual.

[00:53:00.960] Look forward to the email, guys, and see

[00:53:03.440] everyone
