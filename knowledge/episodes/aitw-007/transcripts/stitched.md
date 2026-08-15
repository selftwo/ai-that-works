# S02E03 – 12-factor agents: selecting from thousands of MCP tools



Source: YouTube captions (automatic:en)



[00:00:03.750] cord later. So, welcome back everyone.

[00:00:03.760] Uh, this is the thing that we have been

[00:00:05.839] doing now for a little bit of time where

[00:00:08.000] our goal is to talk about AI that works,

[00:00:10.160] talk about real code, talk about things

[00:00:11.759] that are going to scale, and also build

[00:00:14.480] reliable systems for different kinds of

[00:00:16.000] use cases. Um, I'm Vibv. I'm one of the

[00:00:18.720] creators of BAML. Uh, but more

[00:00:20.880] importantly, I've been in machine

[00:00:21.840] learning for about 10 years. I've worked

[00:00:23.439] on all sorts of systems from Face ID to

[00:00:25.600] predictive systems at hedge funds all

[00:00:27.199] the way to augmented reality systems

[00:00:28.880] over at Microsoft and unreliability is

[00:00:31.920] the hardest thing to deal with. Uh so we

[00:00:34.320] want to talk about that in different

[00:00:35.520] ways and Dexter. Yep. And I'm I'm Dex.

[00:00:38.559] Um I'm working on a tool called human

[00:00:40.480] layer which again we're not here to

[00:00:41.600] shell anything. We're just here to learn

[00:00:43.040] from each other and build AI that works

[00:00:44.800] and figure out how we can push today's

[00:00:47.280] models to the bleeding edge. But um in

[00:00:50.239] the last year or so, I've talked to

[00:00:52.399] hundreds of founders building agents and

[00:00:54.320] learning what reliability means to them

[00:00:55.920] and what kinds of human in the loop and

[00:00:58.320] all kinds of asynchronous orchestration

[00:01:00.399] and um worked really closely with IBOV

[00:01:03.359] uh for a long time on like what is the

[00:01:05.199] future of agents look like and how can

[00:01:06.880] you build agents where you have a really

[00:01:08.560] high performance ceiling and you're not

[00:01:10.560] locked into kind of the assumptions of

[00:01:12.799] various frameworks and things like that.

[00:01:14.880] So that's that's what that's why I'm

[00:01:16.320] here. That's what I'm passionate about.

[00:01:17.960] Cool. And today's topic is about MCP

[00:01:21.200] texture. Do you want to clue them in on

[00:01:23.759] what we're want to talk about? Yeah. Um,

[00:01:26.159] so the idea is um, we've done a lot of

[00:01:28.960] examples in that video is is one of them

[00:01:30.799] and we've done a couple workshops so far

[00:01:32.640] about um, like tool calling agents in a

[00:01:36.799] world where you want to maintain

[00:01:38.240] complete control over the prompt and the

[00:01:40.000] control flow. Um, but I think one of the

[00:01:43.439] things that has people so excited about

[00:01:44.880] MCP is there's a little bit less. It's

[00:01:47.119] kind of a uniform interface for pulling

[00:01:48.960] additional tools into your system. Um,

[00:01:52.079] and a request we've gotten from a lot of

[00:01:53.600] folks is basically, okay, how do I take

[00:01:55.200] this 12 factor agents methodology and

[00:01:58.640] kind of maybe get to skip some steps or

[00:02:00.880] accelerate my development by not having

[00:02:02.799] to write the tool implement? Like we're

[00:02:05.600] really good. What we care about is like

[00:02:07.360] optimizing the prompt and the structured

[00:02:09.520] output so that when you have a reasoning

[00:02:12.000] trace that's a 100 steps long or

[00:02:13.520] whatever it is that ap the AI can still

[00:02:15.840] reliably select the next tool but once

[00:02:18.319] that tool is selected your code has to

[00:02:20.800] decide what to do with it and that's

[00:02:22.720] both uh incredibly freeing and

[00:02:24.879] incredibly powerful but also puts a

[00:02:26.959] little bit more of the work on you. Um,

[00:02:29.920] and so I had this experience building,

[00:02:31.440] we have a deployment bot that runs in

[00:02:33.360] Slack and we use it to like basically

[00:02:34.879] when a when a dev when a when a branch

[00:02:36.640] is merged, uh, it'll run the dev builds

[00:02:39.040] and stuff and then a human can kind of

[00:02:40.480] at message the bot and say, "Hey,

[00:02:41.840] promote this to production." Uh, that

[00:02:44.480] involves triggering GitHub workflows and

[00:02:46.800] triggering promotion workflows in

[00:02:48.400] Verscell. And it spent we spent way too

[00:02:51.360] much time trying to figure out the exact

[00:02:54.720] API invocations to promote uh a release

[00:02:58.160] in Verscell. And it turned out like the

[00:03:00.160] fastest way to do it was like go into

[00:03:01.519] the Chrome console and like copy the

[00:03:03.760] requests and then paste those into a

[00:03:05.120] model and have it write the code because

[00:03:07.360] of the the point is is like integrating

[00:03:09.440] with external systems is hard and MCP

[00:03:12.400] gives service providers a way to give

[00:03:15.440] users a kind of drop in tool uh set of

[00:03:18.720] tools where all all you have to do is

[00:03:20.400] add this MCP to your system and then you

[00:03:22.640] can expose it to your agent as hey these

[00:03:24.319] are options of the types of JSON you're

[00:03:26.080] allowed to output and then once that

[00:03:28.480] JSON that is output, we can actually

[00:03:29.760] send that to the MCP server. And so the

[00:03:32.239] vendor, whoever's maintaining the

[00:03:33.519] upstream service is providing us with a

[00:03:35.440] toolkit or an SD, it's like SDKs for

[00:03:37.519] agents, right? Where I don't have to

[00:03:38.560] learn how all this stuff works. I just

[00:03:40.400] send the tool call to the MCP server and

[00:03:42.720] that's going to handle talking to the

[00:03:44.080] upstream system or API or whatever it

[00:03:46.000] is. So all that is great, but the

[00:03:48.879] problem is what if we have a thousand

[00:03:50.400] plus MCB tools? What if we had 50,000

[00:03:52.560] MCB tools? What if we have a bazillion

[00:03:54.959] MCB tools? At some point, it's not going

[00:03:57.840] to fit in the context window. At some

[00:03:59.360] point, model performance is going to

[00:04:00.959] drop. At some point, just like we use

[00:04:04.159] databases to save data onto disk and

[00:04:06.000] don't have everything living in memory,

[00:04:07.439] we're going to have to build a system

[00:04:08.480] that can go deal with this because

[00:04:11.040] everything interesting happens at large

[00:04:13.080] scales. And if you have a company with

[00:04:15.280] 10 users, you can live in memory. It's

[00:04:17.840] just not that interesting. Probably

[00:04:19.440] there are some companies with 10 users

[00:04:20.720] that are interesting. Um, and today I

[00:04:24.320] want to, but before we get into MCP, I

[00:04:26.080] just want to get a poll from people

[00:04:27.360] really quickly, um, about what it is.

[00:04:31.040] I'm going to save this as a meeting

[00:04:32.479] poll. And I'm just going to run this.

[00:04:34.479] Um, and just two questions. I just want

[00:04:36.880] to get a feel for where people are at,

[00:04:39.199] uh, about MCP, like who uses MCP? What's

[00:04:42.880] people's long-term view on MCP? I just

[00:04:44.720] want to get the feel for where we're at.

[00:04:55.350] And I'm going to try and uh I'll leave

[00:04:55.360] it on for about like 15 more seconds. Um

[00:04:58.479] so try and answer

[00:05:01.680] uh if you can. Um if you're just here to

[00:05:04.400] sit and listen, that's totally okay as

[00:05:05.919] well. But we got almost everyone

[00:05:07.759] answering. Um and I'm going to share uh

[00:05:10.400] my

[00:05:11.400] screen just so we can share the poll

[00:05:13.840] results. Um I think I can if I end it

[00:05:16.400] will share the poll results. All right,

[00:05:18.000] I'm going to end. It's been 45 seconds.

[00:05:19.919] In three, two, one,

[00:05:22.680] done. All right, I'm going to share the

[00:05:25.680] results in the chat. Uh, can you guys

[00:05:28.160] see the results? I assume you can. Um,

[00:05:30.880] it's out of interesting what we see is

[00:05:33.360] we have some folks about um about 30% of

[00:05:36.560] people use MCP currently. 50% of people

[00:05:39.600] aspirationally want to do it.

[00:05:41.520] Surprisingly, 25% of people will never

[00:05:43.680] do it. Um, and then most people seem to

[00:05:47.360] be bullish on MCP. Uh, a few people

[00:05:50.639] don't seem to like it and uh some people

[00:05:53.199] are like not MCP

[00:05:55.320] exactly. Does anyone that is in the camp

[00:05:58.400] of I currently ship with MCP just want

[00:06:00.400] to share what they do with MCP just to

[00:06:04.400] give everyone else a little bit of

[00:06:05.759] context?

[00:06:13.430] Sure. Uh, I can I can hop in. Um, yeah.

[00:06:13.440] So for me, uh, a lot of what I was

[00:06:15.360] doing, I I took over as like head of

[00:06:16.960] engineering and didn't have a product

[00:06:18.560] manager. And so a lot of the work that I

[00:06:20.400] was doing was basically like, hey, I've

[00:06:21.600] got some loose, uh, assumptions of a

[00:06:24.639] ticket or something that needs to be

[00:06:25.840] done. Um, and I'd like to put that into

[00:06:27.759] like linear or something like that. And

[00:06:29.600] so formatting like a PRD or formatting

[00:06:31.600] something that just quickly kind of

[00:06:33.400] outlines what I needed to do. So I

[00:06:35.840] hooked up NCPs with claude um with

[00:06:38.000] claude desktop specifically and then um

[00:06:40.240] would hook those in uh so that I could

[00:06:42.639] kind of just very quickly scaffold

[00:06:44.560] something out. Um so like that's

[00:06:47.600] something um and I've kind of looked at

[00:06:49.440] different ways of of expanding that.

[00:06:51.360] Like I think MCPs are still pretty early

[00:06:53.360] on so it's been a bit tricky to find a

[00:06:56.479] way to like scale that out. So, a lot of

[00:06:58.080] what I've ended up shipping is like web

[00:07:00.560] hookups to MCPs or custom chat clients

[00:07:03.520] because I want to I want to use it on my

[00:07:05.280] phone. I want to use it on the go like

[00:07:06.720] you know like I can't just tied to my

[00:07:09.680] computer. Uh thanks for sharing. Uh Ben,

[00:07:12.000] right? Sure. Yeah. Thanks for sharing

[00:07:14.160] Ben. I think generally that's what I

[00:07:15.599] have seen for MCPS. I know very few

[00:07:17.440] companies, we've talked to a bunch of YC

[00:07:19.440] companies and I know very very few of

[00:07:21.280] them that actually use MCPs in

[00:07:22.800] production except for enduser things to

[00:07:26.160] get scale out. Um, and I think the magic

[00:07:29.440] of like if you're owning if you're

[00:07:30.960] writing code to own the inner agent

[00:07:32.720] loop, MCP just becomes another layer of

[00:07:34.960] SDK. I think the real magic I was

[00:07:36.800] talking about this on LinkedIn with a

[00:07:37.919] couple folks this week and like the real

[00:07:39.360] magic of MCP is like if you're not

[00:07:41.280] writing code or you don't know how to

[00:07:43.280] write code but you just want to drop a

[00:07:45.120] bunch of integrations into a chatbot

[00:07:46.800] that you already use like claw desktop

[00:07:48.400] or cursor or something like that that's

[00:07:50.720] where it really shines.

[00:07:53.919] Yeah, I agree. And I think but if you're

[00:07:56.319] doing it like for what I've seen it

[00:07:58.560] struggle with is I think the problem

[00:07:59.759] that a lot of people have. So before we

[00:08:00.960] get into this, let's do a whiteboard

[00:08:02.000] really fast like sort of exactly what is

[00:08:03.599] MCP at least from our perspective and

[00:08:06.240] how do we distill it down into the same

[00:08:08.080] systems that we've been used to. So we

[00:08:10.560] do this a lot where like we think of

[00:08:12.080] LLMs as just functions. Functions take

[00:08:14.080] in input parameters and they return a

[00:08:15.599] data type. Let's break down what an MCP

[00:08:17.840] is from a very core principles and then

[00:08:20.240] we can go back and think about the

[00:08:21.520] implementation details of what the exact

[00:08:24.080] implementation spec of what the current

[00:08:26.479] proposal for what MCP is and how that

[00:08:28.639] ends up panning out. Um, and we'll try

[00:08:31.520] and keep this fairly high level. So, let

[00:08:35.039] me open this really fast

[00:08:37.800] slide and I will open the

[00:08:41.719] whiteboard. Um, I'm starting to draw it

[00:08:44.000] up. Yeah.

[00:08:46.080] And I will screen share my whole screen.

[00:08:48.000] So once again, um, if we do see an API

[00:08:50.160] key, try not to copy it.

[00:08:54.040] Um, all right. I think we we are live.

[00:08:58.399] All right. All right. Join the room.

[00:09:01.320] Cool. So MCP servers are just they're

[00:09:05.120] responsible for two things. They expose

[00:09:08.160] two special APIs on top of a standard

[00:09:11.279] what you could imagine as a REST

[00:09:12.800] service. It has one API called list

[00:09:14.959] tools and it has another API called call

[00:09:18.279] tools. That is it. There's nothing else

[00:09:21.040] magical about

[00:09:22.200] MCP. Fundamentally, it's you can view it

[00:09:25.040] effectively as a rest API that has two

[00:09:26.959] special things. And it and like Dexter

[00:09:29.600] wrote tool baked in. It kind of has it

[00:09:32.000] kind of can be. Uh just to challenge

[00:09:34.080] that

[00:09:35.000] Dexter, there's nothing that says I

[00:09:37.360] can't just like put like a database

[00:09:39.120] here,

[00:09:40.880] where I'm loading my tools from. It's

[00:09:43.279] true. Yeah, I I think most

[00:09:44.320] implementations have kind of a static

[00:09:46.000] schema, but but um yeah, technically

[00:09:50.240] every time you call this list tools

[00:09:51.839] endpoint, it could

[00:09:54.560] and every time you call tool, it could

[00:09:56.399] at some point return a say a 404 on a

[00:09:58.880] tool not found. And that is very okay

[00:10:02.160] for the spec of what an MCP has. The

[00:10:05.440] problem that I think a lot of people run

[00:10:06.959] into is when they list out tools, they

[00:10:09.440] do the most simplistic thing. They take

[00:10:11.279] these tools and pass it into the LM and

[00:10:13.519] that works until it doesn't because at

[00:10:17.120] some point if we believe MCP is the

[00:10:19.120] future and I'm I I'll share my personal

[00:10:21.680] view on all that at the end. Uh so it's

[00:10:23.839] not biased in any way. Um the idea is

[00:10:26.079] actually like before you basically

[00:10:27.600] before you send your prompt to the

[00:10:29.200] agent, you would spin up every MCP

[00:10:31.279] server in scope for that query,

[00:10:33.279] everything that's installed, pull all

[00:10:35.040] the tools out and then say like, hey,

[00:10:36.720] here's the user's prompt and here's all

[00:10:38.640] the tools you can call. Exactly. That's

[00:10:41.279] a traditional thing out there. And then

[00:10:43.760] the model will pick a tool call, which

[00:10:45.920] is in our world that we all know is

[00:10:47.600] return a data model. And then we'll call

[00:10:50.480] that data model and then pass it back to

[00:10:53.760] the MCP server.

[00:10:55.519] live

[00:10:57.440] live.

[00:10:59.519] Awesome. So when we are doing this um

[00:11:03.279] the problem with this is a lot of people

[00:11:05.360] call that authorization and all these

[00:11:07.120] security things we have to deal with.

[00:11:08.240] Let's just ignore all that. Let's just

[00:11:09.519] assume at some point we'll be able to

[00:11:10.880] pass in beer tokens of various

[00:11:12.959] permissions authored correctly and we'll

[00:11:15.040] solve all that problem. I don't want to

[00:11:16.800] go into that because that's just a spec

[00:11:18.240] design problem. Um you're talking about

[00:11:20.720] the O questions in the chat. Yeah, I'm

[00:11:22.320] just going to ignore that for now

[00:11:23.600] because I think there's more interesting

[00:11:25.120] problems at hand because fundamentally I

[00:11:27.680] think the first question we should ask

[00:11:29.760] is is it useful to have a system that

[00:11:32.399] returns to us a list of tools? Probably.

[00:11:36.560] Is it useful to have something

[00:11:37.920] standardized that does that? Probably.

[00:11:40.480] Just like it's super useful to websites

[00:11:42.320] for websites to all agree semantically

[00:11:44.160] on a robots.txt file and we all scraper

[00:11:47.279] companies just agree that we're not

[00:11:48.560] going to go scrape robots. We'll scrape

[00:11:50.480] according to robots.txt. txt. It's not

[00:11:52.640] or a website can expose a open API open

[00:11:55.279] API spec that says, "Hey, here's the

[00:11:56.959] methods on this API and here's how you

[00:11:58.560] authenticate to them." Exactly. So,

[00:12:00.560] another equivalent to an MCP equivalent

[00:12:02.800] could just be something that says every

[00:12:05.600] time I go to like uh my

[00:12:13.670] website. It exposes an open API spec

[00:12:13.680] that describes all the ai stuff that is

[00:12:16.560] available to an agent. And there was

[00:12:18.240] another company that was doing this.

[00:12:19.200] They called it like / aagents.j JSON or

[00:12:21.680] something. Yeah. And it was an altern I

[00:12:23.519] think it was almost like an alternative

[00:12:24.800] to MCP and I think now they're just

[00:12:27.360] going all in on MCP just because that's

[00:12:29.200] kind of what's what's become the

[00:12:30.560] standard. It basically is. But like

[00:12:32.560] fundamentally like does this specific

[00:12:34.800] implementation detail where you put it

[00:12:36.399] on a server and everything make sense?

[00:12:38.240] Maybe, but probably not in the sense of

[00:12:40.560] like generality. Like we probably don't

[00:12:42.880] need to require a microser as a bakedin

[00:12:46.160] design concept. But the idea that we

[00:12:47.920] want to list tools makes sense. The idea

[00:12:50.399] that we want to be able to call those

[00:12:51.600] tools dynamically makes sense. So let's

[00:12:54.399] talk about what we could do in the world

[00:12:56.000] of a thousand tools. For those of you

[00:12:57.920] that were here for our very first

[00:12:59.440] episode, classification with a thousand

[00:13:01.360] plus categories, you might find this to

[00:13:03.360] be very very similar. Um, and for those

[00:13:07.200] of you that haven't, I'm going to run

[00:13:08.959] through it very quickly, but you should

[00:13:12.320] watch that full video to get the whole

[00:13:13.839] concept of it so we don't have to spend

[00:13:15.760] too much time on repeating the same

[00:13:17.200] thing because that video goes into much

[00:13:18.720] more detail. I'm going to delete the

[00:13:20.959] word MCP and I'm just going to say I

[00:13:22.480] have a list of tools because what I

[00:13:24.480] fundamentally have is I have a bunch of

[00:13:25.839] tools and I want to go

[00:13:27.880] from one tool or like I want to imagine

[00:13:31.279] each of these are a bucket of like a

[00:13:32.639] hundred tools. What I really

[00:13:35.200] Do do you want to quickly just pull up

[00:13:37.519] the JSON file of like basically we're

[00:13:39.920] not using the MCP servers and um we just

[00:13:42.399] have that like tools.json show people

[00:13:44.079] what it looks like tools.json.

[00:13:47.600] So this is we took there's a there's an

[00:13:49.600] MCP registry called Smithery and so they

[00:13:52.079] have thousands of MCP servers and so

[00:13:54.000] what we did was we b queried the list of

[00:13:57.440] servers and then for each server we

[00:13:58.959] pulled off all of the tools that server

[00:14:01.120] exposes. Right? So now we have like I

[00:14:04.160] think this is like 10,000 something

[00:14:05.600] tools in here or something stupid. It's

[00:14:07.440] like an absurd amount of tools. An agent

[00:14:09.839] should not be able to handle this. So

[00:14:12.000] we're just going to talk about this and

[00:14:14.399] we're going to talk about if we have

[00:14:15.600] these 10,000 tools all from different

[00:14:17.199] servers. How do we go down this? Well,

[00:14:19.360] we need some function. I don't know why

[00:14:21.839] mine is black. What is wrong with

[00:14:28.949] this? I don't understand opacity. Okay.

[00:14:28.959] We need some function that is going to

[00:14:30.399] take us down from a thousand

[00:14:32.199] tools to less. Let's say like whatever

[00:14:36.079] tools we think the model can handle. If

[00:14:38.480] it can handle something like let's

[00:14:41.120] assume we're using GD40. So we can

[00:14:42.959] handle a 100 tools. A model is going to

[00:14:45.199] be pretty good at picking a 100

[00:14:47.240] tools. So Dexter is writing the function

[00:14:49.600] signature given a user query and given a

[00:14:52.639] list of tools which we can just call it

[00:14:54.399] a list of tool. Yeah, exactly.

[00:14:57.120] We're going to return down another list

[00:14:58.800] of tools. That's all we need to go write

[00:15:01.880] out. I'm going to write one thing in

[00:15:03.760] there. There we go. So, this is the goal

[00:15:06.000] for step one. And I'll just call it I

[00:15:08.639] put in query string because this is the

[00:15:10.320] most common in these like raggy type

[00:15:12.320] like retrieval things of like what was

[00:15:14.079] the user's query, but it's actually like

[00:15:15.920] whatever parameters would help our

[00:15:17.920] deterministic code or whatever is inside

[00:15:20.079] this function, which could be more

[00:15:21.639] nondeterministic stuff down the line. It

[00:15:24.079] could be a checkbox in my UI where the

[00:15:25.839] user has explicitly checked off Slack.

[00:15:28.079] It could be a checkbox where they've

[00:15:29.279] explicitly checked off notion or in

[00:15:31.199] addition to the string that comes into

[00:15:32.959] here. Right? So, it's about tying the

[00:15:35.760] system together. But fundamentally, I

[00:15:37.199] just need a function that says given

[00:15:38.560] some query object and a list of tools,

[00:15:40.160] pick a smaller list of tools. Um, and I

[00:15:42.959] can do this could be a random function.

[00:15:45.199] It doesn't matter. That's the point. I

[00:15:47.120] just need something that can go from a

[00:15:48.639] lot to a smaller amount, right? You

[00:15:50.880] could the simplest one would just be

[00:15:52.160] like return tools sub like return the

[00:15:54.880] first 50 tools. Exactly. And a more

[00:15:57.199] complex one is we can use embeddings to

[00:15:59.440] go and pick these tools. And we'll talk

[00:16:01.440] about um how that ends up looking. And

[00:16:04.399] then eventually what I want is now given

[00:16:06.000] this query I want to pick the right

[00:16:11.829] tool. And we all know how to do this as

[00:16:11.839] well which is we have the model go ahead

[00:16:14.079] and say given the user query go pick the

[00:16:16.480] right tool. And that's a simple

[00:16:17.519] prompting problem. Once we have this

[00:16:20.160] calling the tool, it just becomes a

[00:16:21.519] matter of wiring up the right APIs or

[00:16:23.199] calling the right function along the

[00:16:24.560] way. So we don't have to think about

[00:16:26.160] this too much and then we're basically

[00:16:28.240] done. And the real magic here is being

[00:16:30.959] able to have what we call these probes

[00:16:32.639] across the way where we want to be we

[00:16:34.639] want to have probes in two different

[00:16:35.839] sections of the system. We have these

[00:16:38.320] probes over here that

[00:16:40.360] says did the did my system that narrows

[00:16:43.360] a tool narrow to at least one of the

[00:16:45.600] right tools that I need? That's question

[00:16:47.600] number one.

[00:16:48.959] If it did, I'm good. I don't need to

[00:16:50.880] change this part of the system. Then the

[00:16:52.959] next question I ask is now given this

[00:16:54.399] narrower set of tools, did the model

[00:16:56.880] pick the right set of

[00:16:59.079] tools. That's another question I can go

[00:17:01.800] ask. And for both of these systems, I

[00:17:04.559] just ask a simple yes no question. Based

[00:17:06.720] on which one is wrong, I update that

[00:17:08.480] part of the system. And do we want to

[00:17:10.559] just for simplicity assume that the

[00:17:11.919] model's only picking one tool at a time

[00:17:14.000] for now? I know we can support multiple

[00:17:15.839] but yeah for now we can assume that if

[00:17:17.839] we want to support multiple remember we

[00:17:19.360] just use a list you just change the

[00:17:22.000] system to a list and then we kind of

[00:17:23.360] solve the problem

[00:17:28.950] automatically. So now we'll actually go

[00:17:28.960] write the code be before I go into

[00:17:32.840] that. Do people understand does anyone

[00:17:35.919] have follow-up questions on exactly what

[00:17:37.440] MCP is and what we need to be able to do

[00:17:39.360] if we have a thousand plus tools to be

[00:17:41.840] able to leverage that in our

[00:17:48.630] system. I'll pause for like two seconds

[00:17:48.640] and you guys have plenty of time to ask.

[00:17:50.480] This is meant to be interactive because

[00:17:52.400] Dexter and I talk about this stuff all

[00:17:53.919] the time, but if you have questions like

[00:17:55.760] this is the easiest way to get a

[00:17:57.039] real-time answer.

[00:18:02.470] I I have a question I'd like to ask if

[00:18:02.480] that's okay. Yeah. Uh so I just like to

[00:18:05.919] hear if generally this is something we

[00:18:07.840] have people deciding which tool to use

[00:18:09.760] or we basically want to set up LLM so

[00:18:12.559] that they automate it all. So it's like

[00:18:14.880] I'm wondering what the scaling procedure

[00:18:16.799] is like. Is it just all synthetic or do

[00:18:19.039] we have someone actually in a meeting

[00:18:20.880] hashing it out with like domain experts?

[00:18:23.600] Well, that depends on your use case. If

[00:18:26.400] you're in the legal world, you might

[00:18:28.080] want to have some lawyers actually look

[00:18:29.440] and see if the right tools were selected

[00:18:31.200] for each of these use cases. Like, hey,

[00:18:32.960] did the LM were the right narrowed set

[00:18:35.360] of tools selected? Where is the right

[00:18:37.360] tool selected from the smaller set of

[00:18:39.360] tools? Like if I have like tools as much

[00:18:41.440] as like load data from some judicial

[00:18:43.919] record versus like send a message on

[00:18:46.000] Slack like any human can probably look

[00:18:48.480] at say if the query what the query

[00:18:49.919] wanted but there might be more nuances

[00:18:51.840] for two different types of tools in the

[00:18:53.360] judicial record system that call

[00:18:55.120] something evidence like submit evidence

[00:18:57.600] versus like submit like evidentiary

[00:19:00.400] claim. I don't even know what those

[00:19:01.600] words mean but you can assume that those

[00:19:02.960] words mean something specific in that

[00:19:04.840] industry and only a lawyer could discern

[00:19:07.440] that correctness. And again, we have we

[00:19:09.919] have two probes in our system, right? We

[00:19:11.760] have our way we narrow down the tools

[00:19:14.320] and then we have our prompt. And so in

[00:19:16.000] your prompt, you could say things if you

[00:19:18.000] find if you test this and you find, oh,

[00:19:20.000] in this case, it can't tell the

[00:19:21.360] difference between those tools or can't

[00:19:22.720] select them, then maybe you either

[00:19:24.559] update the descriptions of the tools

[00:19:26.799] themselves because that gets injected

[00:19:28.400] into the prompt here or you actually

[00:19:30.400] explicitly put in your prompt like

[00:19:32.240] instructions about like only use this

[00:19:33.760] tool in this case, otherwise use this

[00:19:35.360] tool. Yes. But again, it's just

[00:19:37.120] something that you can change that's

[00:19:38.640] isolated, that's testful.

[00:19:41.320] Yes. Um, does that make sense, John?

[00:19:46.320] Yeah. I think I I really appreciate the

[00:19:48.320] perspective on how to get the

[00:19:49.520] engineering process into it. Yeah. And

[00:19:51.280] like really the problem with AI systems

[00:19:52.799] is you do have to blend non-AI people

[00:19:54.400] with AI pipelines and you have to help

[00:19:56.240] blend the two knowledges together. And

[00:19:58.000] often it's easier to teach

[00:19:59.120] non-engineering people a little bit of

[00:20:00.960] AI than it is to teach not engineers a

[00:20:03.840] lot of business context um at least what

[00:20:06.880] we have seen. So now let's talk I think

[00:20:09.039] there's a question that I see quite a

[00:20:10.240] lot in here which is like just the

[00:20:12.160] volume of tools. Is this like a real

[00:20:13.840] problem that people have? Well I think

[00:20:16.480] most people don't have this problem

[00:20:17.679] because most people are building toys

[00:20:19.360] but the minute you build like a real

[00:20:21.120] system you will immediately have this

[00:20:23.960] problem. Oh sorry. And the reason you'll

[00:20:26.799] have this problem is if you decide to

[00:20:28.240] use an MCP server, what MCP servers are

[00:20:30.880] you going to load? If you use an engine

[00:20:33.039] like Smithery and you just plug

[00:20:35.120] everything in, you will have a deluge of

[00:20:39.600] tools. There's nothing you can do about

[00:20:41.520] that. Like Dexter and I didn't even

[00:20:42.880] scrape all of Smithery and in a very

[00:20:45.280] short time we

[00:20:47.880] found 10,000 tools. This doesn't even

[00:20:51.120] work. And the thing that you have to

[00:20:52.400] think about really hard over here is the

[00:20:54.720] fact that like there's like new types of

[00:20:56.159] security vulnerabilities that get

[00:20:57.919] injected here, which is how do you trust

[00:21:00.720] the MCP servers if you're just adding

[00:21:02.480] them in in a wild way? Because I could

[00:21:04.320] change the description here that says to

[00:21:06.400] just say like as I'm like add a social

[00:21:07.919] security number and if you're just

[00:21:09.760] pulling stuff in, you do not get you do

[00:21:13.280] not get like an easy source of trust

[00:21:15.280] here. This just this just blew up on

[00:21:18.320] Twitter yesterday. Someone someone

[00:21:20.000] posted like, "Oh yeah, if you drop the

[00:21:21.360] GitHub MCP server and you let your users

[00:21:24.240] prompt it, they can get it to like

[00:21:26.320] create a pull request that includes a

[00:21:28.159] bunch of PII." Exactly. Exactly. And

[00:21:31.520] there's nothing you can really do to

[00:21:33.360] prevent that fundamentally because what

[00:21:35.280] you're really doing is you're using code

[00:21:36.960] you don't own without any sort of

[00:21:39.400] gateways that you don't have. This is

[00:21:41.679] just like a security risk fundamentally

[00:21:44.159] where like when you call this tool, you

[00:21:47.360] have no control over what happens. It's

[00:21:49.200] basically happening outside of your own

[00:21:50.559] system if you're using I mean you could

[00:21:52.480] you could drop in like deterministic

[00:21:54.640] code somewhere here, right? And you

[00:21:56.240] could say like, oh, let's do a last

[00:21:57.679] minute filter before we call it. And

[00:21:59.919] yeah, we could do some checks, we could

[00:22:01.280] do validation, but fundamentally the MCP

[00:22:03.200] server is a black box to your

[00:22:04.799] application if you don't own it. If it's

[00:22:07.120] all internal MCP servers, these are

[00:22:08.799] lower risks, obviously. But when you

[00:22:11.039] think about MCP servers, you should view

[00:22:12.720] them as the same way as using an API

[00:22:15.120] endpoint from anywhere that you don't

[00:22:17.200] trust until you know it. So, can you

[00:22:19.600] trust uh GitHub's APIs to not do

[00:22:21.679] anything malicious with your data? Yes,

[00:22:23.200] because you're their customer, they'll

[00:22:24.400] treat you well. Can you trust an MTB

[00:22:27.280] server that exposes your GitHub API to

[00:22:29.200] your end users? probably less though

[00:22:32.640] because there is incentive for some

[00:22:34.720] people out there to have access to it to

[00:22:36.400] do bad

[00:22:37.480] things. So you have to be careful about

[00:22:39.760] what you expose. Exposing a readonly MCP

[00:22:42.320] server definitely okay. Exposing a read

[00:22:44.480] and write you should think about it.

[00:22:46.880] Read and modify probably more dangerous.

[00:22:49.600] Append only actions less risky. So you

[00:22:52.720] need to go and evaluate these systems

[00:22:53.919] from a standard software engineering

[00:22:55.280] principles and not get too excited about

[00:22:57.200] I just added these capabilities because

[00:22:59.280] these capabilities come with an

[00:23:00.799] unbounded amount of risk that you're

[00:23:02.880] adding onto your application. And that

[00:23:05.039] is I think one thing that is way less

[00:23:06.480] talked about in these AI agents because

[00:23:10.080] this is the risk of

[00:23:12.280] MCP. That said, we're here to talk about

[00:23:14.640] how to use MCP, not the risk of MC MCP.

[00:23:17.520] So, we'll talk about how to go do this

[00:23:18.960] because any of the things that you do

[00:23:20.159] here doesn't have to be true with just

[00:23:21.960] MCP. You could have this in your own

[00:23:24.080] app. You could have built 50,000 tools

[00:23:26.880] that you trust that your company

[00:23:28.840] exposes. And now you want to give your

[00:23:30.880] agent those

[00:23:31.960] capabilities. Now, many of you have

[00:23:33.919] probably seen me draw this diagram a few

[00:23:35.760] times at this point where I always draw

[00:23:38.000] like oh my god, not an A. How do I draw?

[00:23:41.520] I want to draw with my pencil. Um, I

[00:23:44.480] always draw these weird things where I

[00:23:45.840] draw this

[00:23:46.760] curve. This curve represents a lot of

[00:23:49.200] software. Uh, so I'm going to draw this

[00:23:51.440] how this talks about MCP and

[00:23:52.960] capabilities. Sorry, what's on the x-

[00:23:54.799] axis here? That's what I want to talk

[00:23:56.080] about. What MCP really does is an MCP

[00:23:59.440] server quickly extends your capabilities

[00:24:02.159] that you're able to cover with better

[00:24:05.000] averageness, but it drops your

[00:24:07.039] reliability in any one service because

[00:24:10.159] what you've done by adding MCP is you

[00:24:14.080] basically taken away more

[00:24:16.120] control away from your control flow

[00:24:18.799] system. So you're not writing if

[00:24:19.919] statements, for loops, all these other

[00:24:21.200] systems around there. You're just saying

[00:24:23.840] pick something, go do it.

[00:24:26.159] And that's like saying, I've hired a

[00:24:28.480] hundred different contractors and I will

[00:24:30.240] just let them shuffle tasks around to go

[00:24:31.840] do it. They'll probably go do something,

[00:24:33.440] especially if they're pretty good. But

[00:24:35.760] yeah, the time classical deterministic

[00:24:38.880] software

[00:24:41.120] versus, you know, here's a hund here's

[00:24:43.200] a, you know, a thousand tools and one

[00:24:46.720] call like the god prompt or whatever.

[00:24:48.799] Exactly. Like, hey, you're an agent. You

[00:24:50.480] can solve every single problem for me.

[00:24:52.880] And this here is like a spectrum. And

[00:24:55.520] so, yeah, more tools is like, cool, I'm

[00:24:58.320] going to write less code and I'm going

[00:25:00.159] to hope the LM can figure it out. But

[00:25:02.240] again, that's what we've always found.

[00:25:03.360] That's what 12 factor agents is all

[00:25:04.799] about is like the less deterministic you

[00:25:07.520] have, the less the less deterministic

[00:25:10.080] your software is. And that's kind of

[00:25:11.200] part of it. And there's always

[00:25:12.159] trade-offs there. And you got to find

[00:25:13.279] your sweet spot. And so what we're going

[00:25:15.279] to talk today is like methods of like,

[00:25:16.640] okay, how can we how can we balance and

[00:25:18.480] how can we find a sweet spot where it's

[00:25:20.000] like, okay, I'm still not writing every

[00:25:21.760] line of code like into classic

[00:25:23.279] deterministic software, but I'm also not

[00:25:25.760] just like handing off the keys and

[00:25:27.520] letting the model go yolo it. Exactly.

[00:25:30.000] Cuz like this line we have here

[00:25:31.919] represents classic deterministic

[00:25:33.360] software. It handles that one scenario

[00:25:35.200] really damn well and nothing else. Then

[00:25:37.360] we add some LMS to it and it becomes

[00:25:39.919] slightly wrong side of the curve. it

[00:25:42.640] becomes slightly worse but it starts to

[00:25:44.240] handle a lot more scenarios and then we

[00:25:46.320] add a bunch of MCP and then like it on

[00:25:50.000] average it might perform worse but it

[00:25:51.760] handles way more scenarios than anything

[00:25:54.480] else that we have done beforehand and

[00:25:56.080] like therefore it's better because co we

[00:25:58.960] care about coverage for our unique

[00:26:00.640] application more than we care about

[00:26:02.799] adding everything else and really it

[00:26:05.200] doesn't have to be an eitheror situation

[00:26:07.520] which is where people get stumped it can

[00:26:09.600] easily just become we will write this

[00:26:11.760] deter deterministics offer for this one

[00:26:13.279] control path we have. We'll write an LM

[00:26:15.520] workflow for this other control set of

[00:26:17.279] control paths. And you know what? For

[00:26:19.120] everything else that we're not going to

[00:26:20.080] cover, we're going to toss it in an MTP

[00:26:22.159] and that will address everything. And we

[00:26:24.720] can just use an LLM to decide which of

[00:26:27.760] these paths we're going to send our user

[00:26:29.919] on based on the current journey that

[00:26:31.440] they're

[00:26:32.360] on. And that is an easy way to think

[00:26:35.279] about these hoppers. It's not an either

[00:26:36.640] or. We can really leverage all of them

[00:26:38.360] together along the way. That said, let's

[00:26:42.559] talk about tools and how we use a

[00:26:44.320] thousand plus tools. And there's another

[00:26:46.880] good question there of like, can we

[00:26:48.080] label tools as critical? I'll add a link

[00:26:50.080] after the session. There's uh there's

[00:26:51.440] some new stuff in the spec where you can

[00:26:52.640] annotate the tools, but it's it doesn't

[00:26:54.159] get sent to the LM. It's kind of

[00:26:55.520] directions to the client. Exactly. Um,

[00:26:58.640] so we'll talk about this a little bit.

[00:27:00.320] So, let's talk about again what is these

[00:27:02.720] tools because I tried to go write this

[00:27:05.320] code and I'm I've I've written as much

[00:27:08.240] of it as I could ahead of time because

[00:27:09.760] most of it's just boilerplate code and

[00:27:11.200] we can just walk through it. It's a lot

[00:27:12.640] easier rather than having to talk about

[00:27:14.200] it. Um, so what I want to do is I want

[00:27:17.440] to open this file and I want to look at

[00:27:19.760] what this looks like. So, what is our

[00:27:22.159] agent loop? As the very first part of

[00:27:24.159] it, our agent loop is going to be this.

[00:27:27.600] We are going to have a function. A

[00:27:29.360] function is going to take a state. And

[00:27:30.799] for now, I'm going to do something

[00:27:31.919] really dumb. I'm going to pass in our

[00:27:33.600] state as purely a string. And Dexter

[00:27:37.679] will probably like this, which is I

[00:27:39.360] added some other other tools. Nice. Um,

[00:27:42.720] our prompt is going to be extremely

[00:27:44.760] simple, which is you are an agent with

[00:27:47.600] access to any number of tools. I'm going

[00:27:50.240] to tell it what it has to do. It's going

[00:27:52.000] to answer with one of those tools and

[00:27:54.559] help that user by picking action from

[00:27:56.559] the following. I should this is bad or

[00:27:59.760] the following and then I'm just going to

[00:28:01.440] write the user I'm just going to dump

[00:28:02.720] the state as a part of the user message

[00:28:04.640] along the

[00:28:05.960] way. Now what are these tools that I

[00:28:08.399] have exposed to the model? I have two

[00:28:09.840] specific tools that I'm going to like

[00:28:11.120] hardcode into my system because I know

[00:28:13.520] MCP servers are just not good enough.

[00:28:15.760] The first one I'm going to add is I want

[00:28:17.200] to have the user have two different

[00:28:18.559] types of messages that I have. One is a

[00:28:21.440] request clarification where I literally

[00:28:23.760] just want the I want to show the user a

[00:28:25.520] different type of message that says I

[00:28:26.799] need your help and I might render that

[00:28:28.399] in the UI separately than a respond to

[00:28:30.720] user message because it's just slightly

[00:28:33.200] different UIs and I just want to have

[00:28:34.640] that differentiated and then the actual

[00:28:37.440] message. So that's my human message. But

[00:28:40.159] then I have a second type of tool that

[00:28:42.320] is all my actions and I'm just going to

[00:28:43.919] mark these dynamically defined. So I

[00:28:46.000] will not define them at runtime. I will

[00:28:47.760] only define them. I will not define them

[00:28:50.240] at compile time. All these actions are

[00:28:52.080] only known at runtime. So this is the

[00:28:55.039] difference between um if you want to I'm

[00:28:57.679] just going to send you one other file.

[00:28:59.039] The uh the kind of like calculator tools

[00:29:02.320] that we brought in that. Okay, cool.

[00:29:05.520] What is it called? Uh tool calculator.

[00:29:08.000] So like this would be like like hard

[00:29:09.840] hard code defining your tools. Exactly.

[00:29:12.640] Uh and then passing those to the model.

[00:29:14.559] And so you could do these all by hand,

[00:29:16.000] but the whole point is in MCP we're

[00:29:17.600] going to do this dynamically. We're

[00:29:18.640] going to fetch something at runtime and

[00:29:20.640] then we're going to feed those into the

[00:29:22.640] model as blend as well. Like you can

[00:29:25.600] say, hey, we have what we'll do is we'll

[00:29:28.880] actually send just like we have like

[00:29:30.559] some statically defined tools like human

[00:29:32.520] messages. We can also just add

[00:29:34.640] calculator tools here. Let's give it the

[00:29:37.039] calculator tools while we're at it.

[00:29:39.919] Like we don't have to it's it's we live

[00:29:42.159] in this hybrid world where some tools

[00:29:43.840] are going to be defined dynamically and

[00:29:45.760] some tools are going to be defined

[00:29:47.240] statically and the static tools are in

[00:29:49.600] general going to have more reliability

[00:29:52.080] more systematic guarantees because we

[00:29:53.919] know about them and the deny tools will

[00:29:56.240] have less guarantees and more less

[00:29:58.080] reliability because we won't really tie

[00:29:59.840] to our UI or end process because we

[00:30:02.080] can't by

[00:30:04.600] definition. Um and then we really just

[00:30:06.960] have this function. So I want to talk

[00:30:09.440] about how we'll end up using this

[00:30:12.600] function. So generally I will try and

[00:30:15.200] write this code by hand. So I'll just go

[00:30:17.200] around it about and go do that. So what

[00:30:20.399] we're going to have is we're going to

[00:30:21.520] have a function that's going to do

[00:30:23.000] something. Now in order to load our

[00:30:25.919] tools from dynamically you have to use

[00:30:28.880] something that can go represent the

[00:30:30.159] tools. So we have a thing called type

[00:30:31.520] builder that does that. And for now

[00:30:33.679] let's just assume that we this will

[00:30:35.679] work. I'll talk about how this does.

[00:30:38.080] Yeah, I might even just put a to-do here

[00:30:40.080] like, hey, look, this is where you would

[00:30:41.760] like dynamically launch your MCP server,

[00:30:44.159] call the list tools, and kind of compact

[00:30:46.159] it into your list of things that you're

[00:30:48.080] going to parse. But we just we did that

[00:30:49.440] ahead of time um and just dropped in a

[00:30:51.840] JSON file. That makes sense. Exactly.

[00:30:53.279] And your your company might do that,

[00:30:54.960] too. You might just cache the tools list

[00:30:56.720] thing so you don't have to call it every

[00:30:58.000] single time you go there. Um because

[00:31:00.399] that file, like we said, could be huge.

[00:31:02.080] like getting 10,000 tools could easily

[00:31:04.240] be I don't know how big this file is,

[00:31:06.159] but like we can just see inspect.

[00:31:10.000] Actually, I think it tells me

[00:31:12.640] um it tell me it's 300,000 lines. Um it

[00:31:17.760] is it

[00:31:19.480] is one it's like 11 megabytes of data

[00:31:23.679] and that may not matter but there's a

[00:31:25.279] point at which like the network does

[00:31:26.720] matter and I don't want to send that to

[00:31:28.000] my client on server all the time. I just

[00:31:29.760] want it cached around. So you as a

[00:31:31.919] developer might also make that choice at

[00:31:33.679] some

[00:31:34.440] point. Then what I have is I'm going to

[00:31:36.480] get these tools. I'm going to send it to

[00:31:37.760] my tool options. Then at runtime, I'm

[00:31:40.799] going to say my actions data model. I'm

[00:31:42.640] going to add a property to it called

[00:31:43.919] tools. And I'm going to add my tools

[00:31:45.919] into this

[00:31:47.000] property. Now, how did I pick how did I

[00:31:50.240] go from a thousand tools to a smaller

[00:31:52.559] amount? Well, in this case, I did the

[00:31:53.840] dumbest possible thing, which is I just

[00:31:55.279] picked the first 50 tools. I did nothing

[00:31:57.519] clever at all. Do you want to pull that

[00:31:59.360] into like a narrow tools function just

[00:32:01.120] to be kind of map it back to the to the

[00:32:03.440] whiteboard

[00:32:09.509] narrow tool and like what is the type of

[00:32:09.519] this thing? This is going to be a list

[00:32:11.360] of field

[00:32:20.389] types. Okay, I have to go import things.

[00:32:20.399] This is probably the only reason I did

[00:32:21.919] not do this.

[00:32:34.470] Um, okay. So, I'm just going to go for

[00:32:34.480] now. I'm going to go do this. I'll pass

[00:32:35.600] in a query stir and pass that in. And

[00:32:39.039] what I will do here is this instead of

[00:32:41.519] this will just be

[00:32:43.720] a narrow tools and I will pass in a

[00:32:47.120] query which is empty stir.

[00:32:51.440] But basically the query would be the

[00:32:53.039] input to your do something method.

[00:32:55.039] Right. Exactly. And then specifically

[00:32:57.760] what I'm saying is hey in this scenario

[00:33:01.919] the tool options is going to be a union

[00:33:05.279] of any of these tools that I passed in

[00:33:08.080] to this uh to this thing. So given a

[00:33:11.120] list of 100 tools I am allowed to pick

[00:33:14.080] any one of those. Now I might say I want

[00:33:16.399] to pick multiple of those and I can just

[00:33:18.519] do list or something. And now I'm

[00:33:21.120] allowed to pick a list of these unions,

[00:33:23.360] but I don't have to pick all of them and

[00:33:24.799] it's up to me to decide. So union is

[00:33:27.440] basically you're going to ask the model

[00:33:29.360] pick one structured object and it to be

[00:33:33.519] valid it has to be one of the 50 types

[00:33:36.240] in this union basically. Exactly.

[00:33:38.320] Exactly. Cool. Um and then what I'm

[00:33:41.519] going to go do is I'm going to do the

[00:33:43.440] next part which is I'm going to write my

[00:33:44.720] chat loop. And many of you have probably

[00:33:46.799] seen this chat loop before. Um, it's

[00:33:50.320] very straightforward. We just put a

[00:33:52.159] while loop true. We have a chat object

[00:33:54.000] that represents our current state. And

[00:33:57.120] we're going to just run this and say I'm

[00:33:59.039] going to pick the action based on

[00:34:00.240] whatever the user based use that LM

[00:34:02.399] function. The action will return one of

[00:34:04.480] my static tools which is a human message

[00:34:07.560] type or and if it is a human message

[00:34:10.159] type, I'll print out the message to the

[00:34:11.760] user. I'll add it to my chat thread that

[00:34:15.200] I have going on over here. And then I'll

[00:34:17.599] take the user's message, I append it on,

[00:34:19.280] and I'll run it again. And this is a

[00:34:21.440] really subtle thing going on here. I

[00:34:22.800] think most people are used to seeing a

[00:34:24.159] big JSON structure here with RO user and

[00:34:26.560] all that stuff. This is actually a great

[00:34:28.480] uh illustration of a concept we talk a

[00:34:30.639] lot about in 12actor agents, which is

[00:34:32.399] like you can tell the model what's

[00:34:34.800] happened so far however you want. You do

[00:34:37.520] not have to use the standard OpenAI JSON

[00:34:40.800] messages format. you could just put the

[00:34:42.720] whole thing in a system message or put

[00:34:44.320] the whole thing in a user message um and

[00:34:46.480] let it work from there. And if you look

[00:34:47.679] at how our prompt works, it's just going

[00:34:49.839] to put all that in. Uh I know models are

[00:34:53.119] like specifically tuned on like user

[00:34:55.520] versus assistant and you could still

[00:34:57.040] implement that, but um it's up to you. I

[00:34:59.440] I think this is worth worth calling out

[00:35:01.040] because it's it's subtle. Exactly. Um so

[00:35:04.640] you can see TypeScript or Riot. Um I'll

[00:35:06.960] do TypeScript next time. It's pretty

[00:35:08.160] much the same thing. You can send all

[00:35:09.359] this stuff to chat and I'll convert it

[00:35:11.359] to TypeScript for you. I was on a stand

[00:35:13.440] up today and my my engineers uh keep

[00:35:16.480] asking to rewrite all our Python and

[00:35:18.320] TypeScript. So I I feel you, Andrew. I

[00:35:20.720] apologize that I have to do the sin of

[00:35:22.400] using Python because we're equal

[00:35:25.359] opportunity builders here. I think

[00:35:27.440] there's a there's plenty of plenty of

[00:35:29.280] reason to use Python and TypeScript. I

[00:35:30.960] honestly think that if you're going to

[00:35:32.000] build things in AI, you should just get

[00:35:33.760] good at both. Uh or just learn BAML and

[00:35:36.800] doesn't anyway. I'm I'm joking. I'll

[00:35:38.480] stop. Um, but I think though when I go

[00:35:41.200] down this road is like I've added this

[00:35:42.800] to my tool and for the other action,

[00:35:44.400] what I'll do is the minute I get an MTB

[00:35:46.079] tool, in this case I'm breaking, but I

[00:35:49.119] don't have to break. I could call the

[00:35:50.320] MCP server and then continue onwards. I

[00:35:53.119] want to pause you one more time. Uh,

[00:35:54.560] your battery's about to die. Oh, shoot.

[00:35:57.119] Yes. Um, shouts out to Remo or sorry,

[00:36:00.640] uh, shouts out to, uh, Shia for calling

[00:36:03.599] that out. Any questions so far? Does

[00:36:06.160] this all make sense?

[00:36:11.990] I mean, shouts out to Remo for saying

[00:36:12.000] Python and Typescript, but

[00:36:22.069] yeah, go ahead, Kashall.

[00:36:22.079] Um yeah, I was just wondering like when

[00:36:24.079] you have like multiple uh functions that

[00:36:26.480] are being run within the MCP server, um

[00:36:29.599] is there have you encountered a

[00:36:31.280] situation where you have to figure out

[00:36:33.440] the right order for the functions to run

[00:36:35.280] and how does the LLM do that? You know,

[00:36:37.680] in some cases the order might be

[00:36:39.119] important.

[00:36:41.280] Yeah. Um yeah, I mean I think the LM's

[00:36:43.839] always going to return tools as a list

[00:36:46.320] and so you could call it in the order

[00:36:47.680] that the LM picked. You can also just

[00:36:49.760] constrain the ln. This prompt that we

[00:36:51.440] have here is constraining it to only do

[00:36:54.640] one action at a time. Um, but you could

[00:36:57.440] just turn this to a list type and then

[00:36:58.800] it could return multiple. Um, I've seen

[00:37:01.280] some interesting stuff where people have

[00:37:02.640] it call it calls the human message tool

[00:37:04.800] and the other tool and that can be used

[00:37:06.720] like depending on how you prompt it like

[00:37:08.240] the prompt is all the like you have

[00:37:10.400] total control over how you ask the model

[00:37:12.079] to talk and so you could say always

[00:37:14.000] output a human message and the tool

[00:37:16.160] you're calling and then we show it to

[00:37:17.359] the user while the tool's being called.

[00:37:19.280] Um, but yeah, for ordering vib you ever

[00:37:21.680] seen anything where like a model picks

[00:37:23.040] multiple tools and you have to decide

[00:37:24.320] what order to call them in? Well, that

[00:37:26.320] I'm gonna I'm gonna do something silly

[00:37:28.400] here, but it's like look, if you care

[00:37:29.760] about ordering and you just

[00:37:37.430] Yeah, but I'm talking more like in a

[00:37:37.440] situation where um I don't know, it's

[00:37:39.680] just imagine like a subject matter

[00:37:41.440] expertise uh subject matter expert who

[00:37:44.480] doesn't really know much coding and

[00:37:45.680] stuff and they're just using this tool

[00:37:47.200] and um the tool is like asking for like

[00:37:51.599] a bunch of websites that have to like uh

[00:37:54.320] go through different things. So, um

[00:37:56.720] there might be a right flow to do do

[00:37:58.960] those operations in your responsibility

[00:38:01.760] as an app developer to determine your

[00:38:04.160] use case. If you're doing a bunch of

[00:38:05.839] stuff in parallel, you're doing that as

[00:38:07.280] an optimization because you just have

[00:38:09.520] the LM do one thing at a time and go do

[00:38:11.040] that. What you've said is I want to go

[00:38:12.640] do things in parallel. Yeah. Just like

[00:38:15.200] if you're doing you have to deal with

[00:38:16.720] race conditions, data races, and atomic

[00:38:18.800] and non-atomic variables. If you're

[00:38:20.000] writing multi-threading code, that's now

[00:38:22.079] your job as an app developer to take on

[00:38:25.119] that burden away from your users. And

[00:38:27.520] how do you do that? You just do this.

[00:38:30.079] You can just say this depends on these

[00:38:31.760] tools as a part of your mort tools.

[00:38:35.280] Yeah. Or you could even take it out of

[00:38:36.400] the LM's hands and you could have

[00:38:37.520] deterministic code that says like hey

[00:38:39.200] for if there are web search tools in the

[00:38:41.359] payload, run all of those in parallel

[00:38:43.760] before running any of the other tools.

[00:38:45.200] But at the end of the day, the model

[00:38:46.560] calls seven tools. The model is asking

[00:38:48.800] you go do all these things and then send

[00:38:51.440] me back the context window once you've

[00:38:53.200] done all the things. So you basically

[00:38:55.119] get to decide and optimize all of that.

[00:38:58.079] Yeah.

[00:39:00.640] Yes. Does that make sense?

[00:39:13.990] Hello.

[00:39:14.000] You know the first step is you have to

[00:39:15.920] find flights that work and only after

[00:39:18.160] you find the flights do you want those

[00:39:20.160] days right you but if you end up booking

[00:39:22.320] the hotels first but your flights are

[00:39:23.839] you know the days are not aligned that's

[00:39:25.839] kind of a situation you don't want so

[00:39:27.680] how can we like you know have the agent

[00:39:29.760] go through those like steps sequentially

[00:39:32.240] is what I'm trying to figure out that's

[00:39:34.160] as a part of your data model your data

[00:39:36.160] model needs to represent the

[00:39:37.720] sequentialness of control flow if you

[00:39:41.040] want to go do that Or you can just embed

[00:39:43.760] that as baked in knowledge like vector

[00:39:45.520] says which is like if you get search

[00:39:47.920] request regardless of what order the LMS

[00:39:49.680] spits out in like um let me let me

[00:39:52.400] change this really fast just to make it

[00:39:54.160] more clear. Let's say I return an array

[00:39:56.720] of tools right over here. I've now

[00:39:58.800] changed my code to

[00:40:01.480] um yeah

[00:40:03.320] exactly exactly said it really well.

[00:40:07.400] Uh so let's say over here I have an

[00:40:09.839] array. I now have a list of actions and

[00:40:11.520] human messages that come

[00:40:13.240] out. It is now up to me to say that this

[00:40:16.000] thing is now going to be what is this?

[00:40:19.839] Oh shoot. I disabled the generator.

[00:40:23.880] Sorry. Sorry. I'm running a dev version

[00:40:26.240] and I need to stop doing

[00:40:32.710] things. All right. Cool. Um this thing

[00:40:32.720] now is going to be a list of actions.

[00:40:34.800] And what I want to do here is I want to

[00:40:36.320] say for action and actions go do the

[00:40:39.200] same thing that I was saying before. Oh,

[00:40:41.760] okay. But now I can I don't have to do

[00:40:44.320] this. I could first say like actions

[00:40:46.720] equal action like sort

[00:40:55.589] actions and I can say I can sort this

[00:40:55.599] now in this way

[00:40:58.880] uh

[00:41:05.109] instance and I can say all human

[00:41:05.119] messages must be processed first before

[00:41:07.680] any other tool that comes out from the

[00:41:09.280] model. Okay, cool. Thank you. Right? So

[00:41:12.000] I can find this bridge and it's up if if

[00:41:14.480] this is important to my application

[00:41:16.000] security development, I can go do this.

[00:41:18.880] Um but this is really really important

[00:41:21.280] that um as a developer we remember what

[00:41:26.079] is something that we can do versus

[00:41:28.160] something that

[00:41:30.760] a versus something that a model has to

[00:41:33.599] go do. And this doesn't have to be a

[00:41:35.760] sort. I could even filter and I could

[00:41:37.440] remove or I could modify actions. I

[00:41:39.680] could say, "Hey, if one of the actions

[00:41:42.480] is going to be like read bank

[00:41:44.760] transaction, insert another action

[00:41:46.960] before that that says show something to

[00:41:48.640] a user that I'm going to read your bank

[00:41:51.200] statement and like send a human message

[00:41:53.119] to confirm before I go do this." Yes.

[00:41:55.440] And Joe started typing something that I

[00:41:57.040] think is really really clear and like

[00:41:58.720] really important is like the first time

[00:42:00.000] I tried to build a tool calling agent

[00:42:01.760] for me for something that I really

[00:42:03.040] wanted. It was like and I've said I

[00:42:04.480] think I said this last week too is like

[00:42:06.000] it was I was building I had a make file

[00:42:07.680] to build my project and it was like

[00:42:08.960] docker build and run tests and all this

[00:42:10.880] stuff and I I started with just like

[00:42:13.200] here's the make file go build the

[00:42:14.800] project and I gave it access to call

[00:42:16.240] bash bash functions and then I kept

[00:42:18.240] doing things out of order and then I

[00:42:19.680] kept making the prompt bigger and more

[00:42:21.359] complicated and I was like first do this

[00:42:23.280] then do this then do this then do this

[00:42:25.280] and I think one of the points we're

[00:42:26.319] going to make on this show all the time

[00:42:27.920] is that there are certain things that

[00:42:29.280] models are really really good at but

[00:42:32.000] like if you already know the order. I

[00:42:33.839] spent like two hours trying to hack on

[00:42:35.200] this thing and get the prompt perfect.

[00:42:36.880] If you already know what the right order

[00:42:38.560] is, you could have just written those

[00:42:40.079] five make commands in a bash script. You

[00:42:41.599] don't need a model to do that. Exactly.

[00:42:44.319] So now I'm going to go run this code

[00:42:46.560] just to give people a little bit of an

[00:42:47.760] idea of what I've been doing. Um over

[00:42:49.839] here um I'm going to stop screen sharing

[00:42:53.119] for half a second while I load my API

[00:42:56.520] keys.

[00:42:58.280] Port. Okay.

[00:43:00.800] And I'm going to be back to screen

[00:43:07.910] sharing. Okay. So, I've loaded my API

[00:43:07.920] keys and hopefully no one will see them,

[00:43:10.560] but if you do, we'll find out. I I have

[00:43:14.000] I have a couple copies of them if anyone

[00:43:15.920] wants them. Yeah. Um, so let's go run

[00:43:20.079] this thing. And I'm going to do a

[00:43:21.359] really, really simple thing. I'm just

[00:43:22.560] going to call it run do something. And

[00:43:24.960] we'll just see what happens.

[00:43:27.359] UV run

[00:43:30.760] tools tool. Oh, I'm not in the right

[00:43:32.960] folder. That's why.

[00:43:46.069] 2025 and CD bonus. What is this?

[00:43:46.079] Workshop

[00:43:47.160] bonus. Clear. Okay. UV runtools.

[00:43:51.560] py. So, I'm going to go send it a bunch

[00:43:53.920] of messages. And this is going to run

[00:43:56.640] some stuff. And the first thing I want

[00:43:58.400] to show people is the message I send is

[00:44:00.960] get pages 1 through three from the

[00:44:03.079] database. So we can I want to spend some

[00:44:05.520] time just reading over this prompt so we

[00:44:07.359] can see what happens. It's the same

[00:44:08.960] prompt that we had before. Um I'm going

[00:44:12.560] to move this over here so we can go see

[00:44:14.119] this which is saying the following. You

[00:44:16.880] are an agent with access to any number

[00:44:18.160] of tools. Answer in JSON with one of

[00:44:19.680] these schemas. And I literally just list

[00:44:21.839] out the tools field like I did over

[00:44:24.960] here. Um, I'm going to show what this

[00:44:27.119] parts tools

[00:44:28.280] does. This thing is going to add a

[00:44:30.640] tools.

[00:44:36.790] Whoops. This thing adds a tool field

[00:44:36.800] which is over here into my action data

[00:44:38.400] model and it lists out all the tool

[00:44:40.160] options that I have. So my tool name is

[00:44:42.000] going to be whatever execute command or

[00:44:44.960] something. It has the command timeout

[00:44:46.480] blah blah blah one read output and a

[00:44:48.880] bunch of other tools. Where are these

[00:44:50.720] coming from? What I did over here is I

[00:44:53.680] simply read the JSON schema and I just

[00:44:55.680] converted to a data model of my choice.

[00:44:58.160] This is the other point. You don't have

[00:45:00.480] to use open API spec. You don't have to

[00:45:02.240] tie yourself down to it. You might find

[00:45:04.160] that hey, the word tool name is fine,

[00:45:07.760] but actually it's going to be way

[00:45:10.520] better to not call it tool name. I just

[00:45:13.440] want to alias it to I want to alias this

[00:45:16.240] to like a function name. Oh, function.

[00:45:18.880] Yeah, exactly. So, we can change this

[00:45:20.800] and now the

[00:45:26.390] LLM will basically now call it function

[00:45:26.400] name. And that's the point. Don't tie

[00:45:28.560] yourself down because different models

[00:45:29.920] will have different behaviors and you

[00:45:31.599] need to be able to change this on the

[00:45:33.119] fly in a really easy way. You likely

[00:45:35.680] want it to be the same thing all the way

[00:45:37.280] down no matter what. Now I did something

[00:45:40.319] very unique which is I actually this is

[00:45:42.240] what I call it for the LLM. What what I

[00:45:44.160] actually call it in my code is like BAML

[00:45:47.839] tool name with dollar signs because I

[00:45:49.760] wanted to find that key and not

[00:45:51.520] accidentally pollute it from all the

[00:45:54.079] other JSON fields that people might

[00:45:55.760] have. Sorry I didn't quite catch the the

[00:45:59.040] the usage of BAML tool key. Can you

[00:46:01.680] Yeah, let me describe that again. Let me

[00:46:03.599] call this let me call a tool really

[00:46:05.280] fast. Let's just call like um add a

[00:46:08.079] we'll do this add a to-do actually. So

[00:46:10.800] we see over here add a to-do over here.

[00:46:12.960] So actually add a to-do to jot to send

[00:46:17.720] Dexter the uh the database

[00:46:22.440] ID and I'll say add a

[00:46:25.400] to-do. Let's just see what this happens.

[00:46:28.319] I have no idea.

[00:46:36.109] Um, I need

[00:46:36.119] it. Oh, and you can see what it actually

[00:46:38.560] did. It actually said right over here,

[00:46:40.319] detailed like due date, priority, and

[00:46:41.839] additional description. Why? Because due

[00:46:44.480] date, priority, and additional

[00:46:45.839] description. It actually pulled it out

[00:46:47.200] from here. I need it by

[00:46:50.920] tomorrow, May

[00:46:54.119] 28th, and it's high pri.

[00:46:59.280] Okay. Okay. So, the model didn't select

[00:47:00.640] the tool, but it knew what the tool

[00:47:02.240] needed because it was in the pro.

[00:47:03.920] Exactly. So, it used the request human

[00:47:06.560] clarification tool and then it returned

[00:47:08.480] this tool back for me. And why is BAML

[00:47:12.079] tool name here? Well, that's because

[00:47:14.000] this is a special thing that I added

[00:47:16.480] that I wanted. So, for the sake of the

[00:47:18.800] prompt, I don't want to call it

[00:47:19.920] something special. I just want to call

[00:47:21.520] it function name because it's easier for

[00:47:22.880] the model. for the sake of my code, I do

[00:47:25.839] want to call it something special

[00:47:27.440] because who knows what MCP server is

[00:47:30.240] doing what under the hood and maybe they

[00:47:32.400] have another property called function

[00:47:33.839] name and I don't want to deal with that.

[00:47:37.119] So what I do is I just say for the LM

[00:47:39.440] we'll call it function name but in my

[00:47:41.359] codebase I'll call it BAML tool name so

[00:47:43.839] I can find it very easily and handle it

[00:47:46.400] in a more deterministic way. Does that

[00:47:48.880] make sense Dexter?

[00:47:51.599] Yeah, I got it. Um, I mean, you're still

[00:47:53.520] passing it into the prompt as function

[00:47:56.000] name. Yes.

[00:47:59.119] So, I don't see how it quite solves that

[00:48:00.960] problem, but I get I get the concept

[00:48:02.160] you're trying to get across, which is

[00:48:03.520] like you want to have kind of special

[00:48:05.200] reserve fields or something. Exact. And

[00:48:06.880] like if I want to call if I accidentally

[00:48:08.640] even if I call this to if I call this in

[00:48:11.280] the model, the model is going to get

[00:48:13.319] confused. Like we know this is going to

[00:48:15.520] hurt the model's performance. So I'm

[00:48:17.839] going to do the thing that's going to

[00:48:18.720] help the model the most and just alias

[00:48:20.560] that in field to whatever I want to call

[00:48:23.760] it. And then when when basically and the

[00:48:25.920] idea is like we haven't implemented the

[00:48:27.359] part of the loop that actually goes and

[00:48:29.040] calls that tool yet. And we're probably

[00:48:30.720] not even going to do that today. Um

[00:48:32.400] maybe if we have time at the end but the

[00:48:34.640] idea here is how do we narrow sorry what

[00:48:36.640] I do here is I say tool equals

[00:48:40.520] action model

[00:48:43.160] extra

[00:48:50.430] tools oh and this

[00:48:50.440] is okay cool tool this is going to be in

[00:48:54.160] any type it always will be in any type

[00:48:56.240] there's nothing you can really do about

[00:48:57.359] that um if because you're doing it

[00:48:59.599] dynamically at runtime exactly because

[00:49:02.000] we can't really help that. So, we'll

[00:49:03.280] just type it as a

[00:49:09.589] dict. And now we'll go do this. And now

[00:49:09.599] we can say like tool name

[00:49:11.720] equals

[00:49:20.630] tool.pop. What do I call that field?

[00:49:20.640] Name

[00:49:27.190] key. And now I have the name of the tool

[00:49:27.200] and then

[00:49:28.200] args are just the rest of it.

[00:49:31.520] And I can even say print.

[00:49:38.630] Yeah, let's let's see that. Let's run

[00:49:38.640] it.

[00:49:40.240] Yeah, cool.

[00:49:49.150] Let's run

[00:49:49.160] this. And

[00:49:55.910] um

[00:49:55.920] you're going to have to go get your

[00:49:56.880] prompt again. If you just copy the list

[00:49:58.880] of user messages out of the top, you can

[00:50:00.800] do it. Oh, wait. Oh, wait. Scroll back

[00:50:03.680] down here. Yeah, get

[00:50:15.910] that. And that's the same thing, which

[00:50:15.920] makes sense because LMS aren't fully

[00:50:19.640] uh Where did it

[00:50:22.040] go? Scrolling is hard. I should have

[00:50:24.400] made this a test case.

[00:50:27.359] And the other thing I noticed is that

[00:50:28.720] I'm actually not injecting the AI

[00:50:30.319] messages in here. So it sounds like

[00:50:32.319] there's a bug somewhere in my code. Oh

[00:50:34.160] yeah, right over here. I only print it

[00:50:35.839] out. Yeah, I think cursor deleted your

[00:50:38.640] AI message. That makes sense. But

[00:50:41.920] honestly, now it says right over here,

[00:50:43.359] I'd like to call the tool notion AI

[00:50:45.440] notion API MCP tool. And I just send

[00:50:47.680] these args in. And now I can just pass

[00:50:49.920] that into the MCP parameter, get the

[00:50:51.599] response, add it to my chat object in

[00:50:54.000] whatever form I wanted. it doesn't

[00:50:55.359] really matter. And then continue on with

[00:50:57.280] my

[00:51:03.430] loop. Um I'm going to pause here and

[00:51:03.440] just say, do people have

[00:51:06.520] questions? I think the biggest question

[00:51:08.720] that was in there was um that Joe was

[00:51:11.760] asking was like, okay, how do we do the

[00:51:13.440] embeddings and the narrowing in a like

[00:51:15.440] smart sophisticated way? Yeah. Um and I

[00:51:18.160] think that's actually more interesting

[00:51:19.119] than actually going and calling the

[00:51:20.400] tool. Although I think probably we can

[00:51:22.079] publish an example afterwards of like

[00:51:23.599] hey we brought in the Python MCP client

[00:51:25.440] and actually ripped it like yeah we can

[00:51:27.359] just call the tool or something. We can

[00:51:28.559] go do that too. Um I think you're right.

[00:51:31.040] I think this is probably the most

[00:51:32.160] interesting part. What I would do if I

[00:51:34.240] were here is I actually wouldn't do this

[00:51:36.240] in this way. The thing we've done here

[00:51:38.319] is not bad but really what I would do is

[00:51:41.440] I'd say narrow tools um list tools dev

[00:51:46.640] load

[00:51:48.599] tools. Um, and what I'm going to do is

[00:51:50.880] like tool file path. And then what I'm

[00:51:54.559] going to return is going to be a

[00:51:58.160] uh type builder

[00:52:00.520] object. I'm just going to call this

[00:52:02.640] right over here every single

[00:52:06.359] time. So I'm going to parse the tools.

[00:52:09.280] I'm going to parse tool path. I'm going

[00:52:11.920] to return this. And specifically I'm

[00:52:13.760] going to have is I'm going to pass in a

[00:52:14.960] query into here.

[00:52:17.680] And given a query, I'm going to narrow

[00:52:19.040] the tool. So everything looks everything

[00:52:20.559] should look almost the

[00:52:34.309] this. And now we basically are going to

[00:52:34.319] load the tools on every single chat all

[00:52:37.200] the time and pass that object

[00:52:40.119] in. Now we don't Yeah, let's see how

[00:52:42.400] that works. You think that's going to

[00:52:43.839] work? Well, well, in this case, no,

[00:52:46.079] because I'm still returning narrow tools

[00:52:47.920] is still returning the 50 p tools. Okay.

[00:52:50.559] Um, like there's nothing that's

[00:52:51.920] happening over here. Um, but like we

[00:52:55.359] could use embeddings to solve the right

[00:52:56.960] tools. The problem again that I think a

[00:52:59.119] lot of people run into is the problem

[00:53:00.800] that we run into when we do

[00:53:02.920] classification. Most people make the

[00:53:05.040] mistake of saying that hey, I'm going to

[00:53:07.520] use this embed this description as the

[00:53:09.920] thing that I pass into LM and also the

[00:53:11.680] thing for embeddings. That is a mistake.

[00:53:14.559] Just like in classification, remember

[00:53:16.319] what we did and when we did a

[00:53:17.599] classification doc and I'll pull up that

[00:53:19.040] doc again.

[00:53:25.349] Um, hello. There's the screenshots are

[00:53:25.359] in the repo. Exactly. That's I'll just

[00:53:27.520] pull it up on here.

[00:53:35.430] Uh, because I think that's going to be a

[00:53:35.440] better way to just look at it. And we

[00:53:37.920] look at classification and we look at

[00:53:39.440] this like we did not send the same

[00:53:42.880] description to the prompt as we did for

[00:53:44.720] the embedding system and we should not

[00:53:47.760] do that because different different

[00:53:50.720] models have different behaviors. So the

[00:53:53.920] fact of being able to go ahead and we

[00:53:56.000] can say that hey the description for

[00:53:57.440] this category for the embedding text is

[00:54:00.000] different than the description that goes

[00:54:01.520] into LM to help select the right

[00:54:03.200] category is also true for LLMs. The

[00:54:06.640] description that I use here for this

[00:54:08.160] tool is likely not the best description

[00:54:10.880] for actually passing into an embedding

[00:54:13.160] model. Maybe I take the whole thing over

[00:54:15.920] here and I send that to an embedding

[00:54:17.520] model. Maybe I send the entire server to

[00:54:20.400] an embedding model all at once and all

[00:54:21.920] the tools under one server. It really is

[00:54:24.240] up to me of how I decide that and I

[00:54:27.680] shouldn't be tied down to go doing that

[00:54:30.079] in some other way. So even like this

[00:54:32.880] thing that we wrote over here of like

[00:54:34.319] picking the right tools, this doesn't

[00:54:36.559] actually have to be as simple as like I

[00:54:38.079] have a list of tools already. Go select

[00:54:39.920] that. I could say I have a list of

[00:54:41.359] servers which contains a list of tools

[00:54:43.440] and now go narrow from there. And that

[00:54:45.520] could both narrow the servers down and

[00:54:48.160] the tools down. So it's important that I

[00:54:51.280] maintain that control at all times of

[00:54:53.599] how I go do this. And one sophisticated

[00:54:56.000] manner is chuck everything in embedding.

[00:54:58.319] use the description of the tool to

[00:54:59.839] decide what you do. But what ends up

[00:55:01.760] happening in practice is like when I

[00:55:04.400] read this, this doesn't actually help me

[00:55:06.559] if I use the description alone. You

[00:55:08.319] could easily imagine having this, this

[00:55:10.319] is the same description for git github

[00:55:12.880] and

[00:55:13.800] bitbucket. That is useless to me as a

[00:55:17.800] developer. Um, you might have that. Hey,

[00:55:20.559] I know that you are logged in as a

[00:55:23.520] company that I you have connected to my

[00:55:25.599] organization. and you've connected

[00:55:27.640] GitHub. Well, then it doesn't matter

[00:55:29.680] what big bucket descriptions are. I just

[00:55:31.359] use a boolean switch that isn't anything

[00:55:33.599] fancy to just say I only enable GitHub

[00:55:36.520] servers and I don't enable uh Bitbucket

[00:55:39.880] servers. And you'll hear DR and I say

[00:55:42.480] the same thing over and over again,

[00:55:43.760] which is like there is no oneshot magic

[00:55:46.640] trick. And I think that's what people

[00:55:48.000] when when we saw the poll today, why

[00:55:49.599] everyone was so optimistic about MCP is

[00:55:51.680] it feels like that magic bullet, but

[00:55:54.400] it's not. you're just adding more

[00:55:56.400] software and like whether you want to

[00:55:57.680] use an API or not is up to you. Like we

[00:56:01.119] use REST APIs all the time. We don't all

[00:56:03.040] reinvent GitHub. We just use it and it's

[00:56:05.000] useful. So like yeah, it might make

[00:56:07.520] sense to use someone else's agentic

[00:56:10.359] system. But how you use it, how you plug

[00:56:13.359] it in is very important to your actual

[00:56:15.839] application and like that is application

[00:56:19.119] specific.

[00:56:25.670] Cool. Are we going to do it? Do you I

[00:56:25.680] mean I can write the embedding thing.

[00:56:26.880] What I will do is I will just go to our

[00:56:29.200] previous code and I will copy and paste

[00:56:31.319] it because we already have it. I don't

[00:56:33.599] have to re reinvent the

[00:56:35.720] wheel. Um

[00:56:38.359] but we had this thing up here which is

[00:56:40.640] narrow down

[00:56:42.359] category. It's literally going to be the

[00:56:45.440] exact same

[00:56:47.079] code. Um where did it go? Yeah. Yeah.

[00:56:50.400] And I think while you're doing that,

[00:56:51.440] like the main the main lesson here is

[00:56:52.640] right you can you can do this in a hund

[00:56:54.000] different ways. You can use embeddings.

[00:56:55.440] You can do this like I feel like I don't

[00:56:57.040] know the word for it. Um it's not rag

[00:57:00.160] but it's like basically like passing

[00:57:02.079] chunks of data into an LLM and having it

[00:57:04.960] like decide whether any of them are

[00:57:06.799] relevant. Passing lists of tools and you

[00:57:10.240] can have a really small LLM decide,

[00:57:12.720] okay, cool. These six tools are relevant

[00:57:14.400] and the rest of them are not. And you

[00:57:15.839] might get zero relevant tools on most of

[00:57:17.920] your queries. Um, but again it's a

[00:57:20.160] smaller, more focused prompt. Yeah, let

[00:57:22.960] me go change this code really fast

[00:57:24.319] because in order to go do this, what I

[00:57:25.920] actually have to do is right now what

[00:57:27.520] I'm returning here for every tool is I'm

[00:57:29.359] returning the name of the server and the

[00:57:30.880] tool and then the actual type that is

[00:57:32.559] associated with it. What I actually need

[00:57:34.559] to return now has changed. What I need

[00:57:36.720] to return now is going to be the entire

[00:57:38.559] tool object and the type of the tool.

[00:57:42.000] It's no longer a simple object because I

[00:57:43.920] need that object to be able to do the

[00:57:45.040] embedding to do the embeddings. Yep.

[00:57:47.280] Exactly. So now what I'm going to have

[00:57:49.280] here is I'm going to load the tools. Um

[00:57:55.000] sorry I'll load the tools. The tools

[00:57:57.599] will be did I change the type?

[00:58:00.359] Toolable. I'm going to load the tools.

[00:58:02.480] Tools will be a type of tools and

[00:58:04.079] values. This will be tool

[00:58:05.960] types. And now I have to go down and

[00:58:08.640] write this code.

[00:58:18.829] I will go do this and

[00:58:18.839] this narrow down my tools. So I will

[00:58:21.760] have a bunch of tools. For every tool,

[00:58:24.319] what I will do is I will

[00:58:27.280] uh find the embedding of every uh so

[00:58:30.799] you're going to use the raw JSON from

[00:58:33.920] the MCP server to generate the embedding

[00:58:36.720] text.

[00:58:39.720] Exactly. Is this correct?

[00:58:42.960] I have to do

[00:58:44.960] you don't have you need to grab the

[00:58:46.079] embed function. Yeah. So, what I'm going

[00:58:48.160] to do is I'm going to do

[00:58:50.119] JSON.dumps. I'm just literally going to

[00:58:52.000] dump that into my category

[00:58:54.960] and I won't think too hard about

[00:59:02.870] it. And we're pulling some language from

[00:59:02.880] the last one of we're using in in this

[00:59:05.280] one it's called categories in this one.

[00:59:08.079] In the uh tools one, it should probably

[00:59:10.000] be called tool, but yeah, we'll deal

[00:59:13.040] with that in a second. Um, I'm gonna

[00:59:15.280] rename this to field

[00:59:24.870] numpy. And most of this should just

[00:59:24.880] work. Oh man, look at auto doing our

[00:59:27.119] homework for us, building the uh summary

[00:59:29.040] of key takeaways for us. Yes, define a

[00:59:31.359] prompt with an action that's dynamic.

[00:59:33.200] List out all your tools. like we'll

[00:59:35.359] increase the matches to like I don't

[00:59:36.880] know like

[00:59:39.400] 100. And now this is going to go return

[00:59:42.000] this. And now we just use this and we

[00:59:43.599] return a union and we're basically done.

[00:59:46.520] Um and that should basically just work.

[00:59:50.400] Uh text. Okay. Blah blah blah. I don't

[00:59:53.680] need that anymore. Let's run this

[00:59:55.200] sucker. This might take a while because

[00:59:56.880] I want to run embeddings on like 10,000

[00:59:58.559] tools. Um so we'll just see what it

[01:00:00.799] does.

[01:00:02.400] Uh, and I'm not running any of it in

[01:00:04.000] parallel because I didn't do it in

[01:00:05.040] async, which I probably should, but

[01:00:06.400] that's okay. Um, actually, get back to

[01:00:09.880] multipprocessing, dude.

[01:00:13.440] Uh,

[01:00:14.280] openi

[01:00:16.680] async async openi. Okay,

[01:00:19.799] cool. Uh, I want to go do this. Does

[01:00:23.440] input actually expect a list of ins? Um,

[01:00:26.319] I don't know how that's going to work if

[01:00:27.520] I send it multiple. So, let's not try

[01:00:28.880] that.

[01:00:42.910] parallel. How do I do this in

[01:00:42.920] asynciogather? Oh, wait. Asyncio.run

[01:00:45.760] async.io.gather.

[01:00:54.309] I am a little stickler for doing this.

[01:00:54.319] So, I will Oh, I see. I will likely

[01:00:57.319] wait. um and editing SQL

[01:01:06.630] and then if you if you wanted to keep

[01:01:06.640] this as synchronous. Okay,

[01:01:14.190] thanks Deborah.

[01:01:14.200] Async. Okay, cool.

[01:01:17.839] Is this working? Oh, and then I have the

[01:01:21.480] embeddings.

[01:01:23.240] Cool. Uh and then I just wait on these,

[01:01:25.599] I guess.

[01:01:27.160] Um, I don't

[01:01:30.119] actually I'm certain that this will get

[01:01:32.559] fixed at some

[01:01:34.760] point.

[01:01:52.069] Okay. I think this will run. Um, you got

[01:01:52.079] to do async io.run run here or make it

[01:01:55.440] async.

[01:01:56.960] Yeah. And then I will have to do async.

[01:02:05.510] Um, we'll do this. And this is doing

[01:02:05.520] something incredibly dumb where I'm

[01:02:06.880] going to call the embed on every single

[01:02:08.400] call to this. So, I have no idea what

[01:02:09.839] this is going to do. Uh, UV add openai.

[01:02:29.589] um and all this seems to be a little bit

[01:02:29.599] I think repetitive from last time but

[01:02:31.119] that's because like the reason I didn't

[01:02:32.319] describe this is you can go learn about

[01:02:33.760] the nuances there very easily but the

[01:02:37.359] whole point of this is that you don't

[01:02:39.040] have to do everything you can just use

[01:02:40.960] the same principles and build them up to

[01:02:42.960] build more complex systems over time

[01:02:45.440] yeah so you could use embeddings to

[01:02:47.040] narrow this

[01:02:49.119] to narrow this down. Oh, sorry, Dexter.

[01:02:51.599] What were you saying? Oh, sorry. Yeah,

[01:02:52.799] there's a little lag. Um, yeah, you can

[01:02:54.240] use embeddings to narrow this down. You

[01:02:56.319] can use um you can use an LM to narrow

[01:02:59.440] this down. You could use some

[01:03:00.720] deterministic code that does someone

[01:03:02.640] mentioned having full text search.

[01:03:05.760] And I'm doing something really really

[01:03:07.280] dumb over here which

[01:03:15.109] is I am if I can I'm basically just

[01:03:15.119] embedding this each JSON blob completely

[01:03:18.160] independently.

[01:03:20.000] So I'm not even embedding the

[01:03:21.119] description. You probably would want to

[01:03:22.079] do like the name and the description or

[01:03:23.920] something, right? Maybe. I don't know. I

[01:03:26.160] I really don't know. The thing is like

[01:03:28.240] for every tool you probably want a

[01:03:29.839] special way to embed it and that thing

[01:03:32.240] is unique to that tool. And in fact, I

[01:03:35.359] mean, so yeah, and this is the point. I

[01:03:36.640] mean, we'll just keep saying every week

[01:03:38.160] is like the idea is not to get this

[01:03:40.240] perfect in an hour. The idea is to build

[01:03:42.640] a system that gives us lots of points

[01:03:45.039] that we can both test, that we can mock,

[01:03:47.280] that we can probe, that we can tweak so

[01:03:49.599] that we can optimize each part of the

[01:03:51.599] pipeline to the point where we can build

[01:03:53.440] a a system that as always gets the most

[01:03:56.480] out of today's LLMs. And this is this is

[01:03:58.880] sort of the approach that we're seeing

[01:04:01.039] both large enterprises and really hot

[01:04:03.039] startups are using all over the place is

[01:04:05.280] like the 100 MCP tools single prompt or

[01:04:08.799] thousand MCP tools sing single prompt

[01:04:10.799] one that that one just breaks down and

[01:04:12.240] like you could just use less tools to

[01:04:14.079] start but eventually you'll actually

[01:04:15.680] want to be able to have an agent that

[01:04:17.359] can do lots and lots of things and this

[01:04:19.599] is kind of step one in doing that. Yeah.

[01:04:21.920] And more importantly, like the fact of

[01:04:23.520] the matter is the actual embedding text

[01:04:25.280] that you're going to go embed is likely

[01:04:27.839] unique to your unique problem. The way

[01:04:30.799] you embed that tool is specific to you.

[01:04:34.240] And any description you use is likely

[01:04:36.799] going to be specific to you. So even if

[01:04:39.039] you have I mean you could even you could

[01:04:40.640] even pre-process and have an LLM read

[01:04:42.480] the JSON and spit out a really wordy

[01:04:44.640] description that then we go use to make

[01:04:46.160] embeddings out of. Yeah. And then I

[01:04:48.559] think you asked the question remod like

[01:04:49.920] could you not fine-tune a small

[01:04:50.960] classification model I mean you could

[01:04:52.559] that becomes another way to build the

[01:04:55.440] same function that we just built over

[01:04:56.880] here which is narrow categories you can

[01:04:59.039] build a classifier that does that you

[01:05:00.880] could build a random algorithm it's it's

[01:05:03.119] based on your use case and how well you

[01:05:04.880] understand your problem and how well you

[01:05:07.359] understand your problem going back to

[01:05:08.559] the eval episode that we did is like you

[01:05:10.880] should have a test suite that's puts a

[01:05:13.760] hundred things in here and gives you a

[01:05:15.119] score out because until you know that a

[01:05:17.520] certain approach is better or worse than

[01:05:19.119] another one, you're just kind of

[01:05:20.720] shooting in the dark.

[01:05:23.520] Exactly. And then like one of the ways

[01:05:25.359] that you see us doing this right now,

[01:05:26.640] we're just like I hardcoded a simple

[01:05:28.400] prompt into my system. I didn't really

[01:05:30.319] think about it and then I put a

[01:05:32.960] um then I just put a while true loop and

[01:05:34.720] I just kept running and typing just to

[01:05:36.160] see if it behaved correctly. Why did I

[01:05:38.839] add this human uh this uh this uh human

[01:05:44.000] message tool? Well, at this point, I've

[01:05:45.280] built a lot of agents, so I kind of just

[01:05:46.640] know that likely the human message is

[01:05:49.039] not going to have enough clarification.

[01:05:50.799] So, I generally will build this in since

[01:05:52.640] I'm building a CLI interactive system

[01:05:54.440] anyway. So, for a CLI interactive

[01:05:56.880] system, I'm just going to default to

[01:05:58.640] this as like good practice that I've

[01:06:00.640] learned. But that just experience of

[01:06:02.960] building these systems. Three minutes

[01:06:04.799] left. Any last takeaways here um before

[01:06:07.760] we jump to questions? I'm hoping this

[01:06:10.000] will run eventually. I forgot to build

[01:06:11.920] the progress bar. This is why I add the

[01:06:13.440] progress bar. It's so nice. TQDM.

[01:06:17.440] Yeah. Uh but no, really the last

[01:06:19.680] takeaway is just like MCP isn't that

[01:06:21.839] hard. It's just an API that does list a

[01:06:24.720] bunch of tools and let you call that

[01:06:26.000] tool. We already have a bunch of other

[01:06:27.760] ways to go do that as well. So you don't

[01:06:29.520] have to tie yourself to

[01:06:30.760] MCP. Calling an MCP server with a

[01:06:33.039] thousand plus tools is just a matter of

[01:06:34.480] being able to narrow down to small

[01:06:35.760] amount of tools correctly. The rest of

[01:06:37.760] this code is easy software and you can

[01:06:39.680] go look at exactly how we did this. Um,

[01:06:42.400] like how we converted that to a type

[01:06:44.319] spec is really easy. You're just

[01:06:45.599] defining open API specs and converting

[01:06:47.599] it to open API says boolean, you make

[01:06:50.079] that a boolean. Open API says string,

[01:06:51.760] you make that a string. Open API says a

[01:06:54.480] these three enums, you make that an

[01:06:55.839] enum. It's a pretty straightforward data

[01:06:57.440] model conversion. So that part isn't

[01:07:00.160] really interesting. Uh, the only part

[01:07:02.400] that is interesting is giving it a tool

[01:07:04.000] name that then you can go call.

[01:07:11.990] And to recap based on what auto said I

[01:07:12.000] think is really good is like basically

[01:07:13.359] define a prompt with a dynamic action

[01:07:15.680] call list tools optionally narrow those

[01:07:18.160] tools um inject those parse into

[01:07:20.880] structured data and inject them into the

[01:07:22.640] BAML prompt at runtime and then handle

[01:07:25.520] the LM response however you would in any

[01:07:27.680] other agentic system. Exactly. That's

[01:07:29.920] it. It's not that hard. It's very few

[01:07:32.720] lines of code. The lines of code get

[01:07:34.640] messy

[01:07:35.720] when when you start doing fancy things

[01:07:38.559] like narrowing down your categories

[01:07:40.240] using embeddings.

[01:07:47.990] Awesome. We had a lot of great questions

[01:07:48.000] during the show. Uh any other questions?

[01:07:50.079] Either drop them in the chat or put a

[01:07:52.000] hand up or just come off mute. What's

[01:07:54.880] been the best performing embedding

[01:07:56.319] model? Uh and what's been the best

[01:07:58.240] performing embedding you've made so far?

[01:08:00.079] How do you implement it? Um, I don't

[01:08:02.400] think there is a best performing. I

[01:08:03.760] think it's very use case uh specific.

[01:08:05.599] But in general, I think it's just

[01:08:07.400] like as long as you can control the text

[01:08:10.079] and the embedding, it becomes really

[01:08:11.359] easy to tweak it when it picks the wrong

[01:08:13.680] thing. So like I think that's the most

[01:08:15.839] important insight is like look, if the

[01:08:18.000] embedding picked the wrong tool, then

[01:08:19.839] there's no way the LM can pick the right

[01:08:21.359] one because it's not even in your input.

[01:08:27.749] So you just have to be able and the

[01:08:27.759] beauty of this system is if as if you

[01:08:30.159] have to tweak your prompt to change your

[01:08:32.159] embedding, you're

[01:08:34.759] stuck. Like that's a bad place to be.

[01:08:38.319] What you really want to be able to do is

[01:08:39.759] you want to be able to tweak your

[01:08:40.719] embeddings completely orthogonal to

[01:08:42.880] changing your prompts. If they're the

[01:08:44.960] one and the same, then changing one

[01:08:46.880] impacts the other. You want to separ you

[01:08:48.880] want a separation of concerns as much as

[01:08:51.480] possible. Is that Dexter? What about

[01:08:53.600] you? Have you seen models that are

[01:08:55.120] strictly better or worse? Um, I've seen

[01:08:59.120] faster embeddings. Yeah, that's pretty

[01:09:01.520] much it. Embeddings really just aren't

[01:09:04.080] that cool. But like there are ways now

[01:09:06.560] where you can make them fast at least.

[01:09:08.640] Yeah,

[01:09:13.590] I think the model is the least important

[01:09:13.600] part of it. The most interesting part is

[01:09:14.960] the content that you're trying to do

[01:09:16.640] things with, and that's what I would

[01:09:17.839] focus on given how good these models

[01:09:19.359] have gotten already.

[01:09:21.839] Yeah, I I agree. I think the the lever

[01:09:23.679] you want to try tweet like it's always

[01:09:25.359] like do the easiest thing first. Like if

[01:09:27.440] you can get to the performance grade

[01:09:29.040] that you need by changing the text that

[01:09:31.199] goes into the embedding, then why on

[01:09:33.040] earth would you go fine-tune an

[01:09:34.400] embedding model or try to use some fancy

[01:09:36.400] one or something like that? And and to

[01:09:38.960] to that point, if you can't do that

[01:09:40.880] level of accuracy, then you should go

[01:09:42.880] fine-tune an embedding model, but try

[01:09:45.120] the easiest thing first.

[01:09:47.920] Yep. And honestly, I would say even like

[01:09:49.440] try a thousand MCP tools in your prompt

[01:09:51.440] first and like see if that works. Why

[01:09:53.040] even filter like who knows maybe 03 will

[01:09:55.520] just do it and you don't your your use

[01:09:57.679] case is not specific to like cost or

[01:09:59.840] latency in any

[01:10:11.510] way up to 70% great then that was a good

[01:10:11.520] change and that was worth it. But if you

[01:10:12.719] had the embedding filtering and it goes

[01:10:14.080] up by 0.01% 01%. You can even say like

[01:10:16.560] is it really worth the extra code and

[01:10:18.320] the time from our team or do we need to

[01:10:19.760] take a step back and do a different

[01:10:21.040] approach? Yeah. Um Tim asked a great

[01:10:23.920] question. How long does it take to take

[01:10:25.199] a symbol embedding? I think it's just

[01:10:26.480] network dependencies sadly. So like I

[01:10:28.400] would just expect anything will take

[01:10:30.080] anywhere from

[01:10:31.320] like 50 milliseconds probably the

[01:10:33.600] fastest you can do and like a second is

[01:10:36.640] probably the worst case outcome. Um,

[01:10:38.960] what I would do is because embedding

[01:10:40.320] should be cheap is I would just deploy a

[01:10:41.600] small embedding model into your own VPC

[01:10:43.280] and just call it a day. Use like Bedrock

[01:10:45.199] or something else to go hosted, Azure,

[01:10:46.960] whatever you want. Um, and that's

[01:10:49.040] probably the best bang for the buck. Um,

[01:10:51.560] because as we're seeing here, processing

[01:10:54.400] of 10,000 embeddings does take a while.

[01:10:57.199] Uh, it's taking a long time for this to

[01:10:59.440] run and I can't really do anything about

[01:11:00.719] that. I just have to let it run.

[01:11:22.870] anyone. Um, can I show the Can you show

[01:11:22.880] the call for narrow down categories

[01:11:24.800] again?

[01:11:26.199] Yeah, it's really right here. What I'm

[01:11:28.880] doing is my system I think he's like

[01:11:31.520] where where are you calling it? Oh,

[01:11:33.440] right here. I'm just saying it's like

[01:11:35.280] the the union of the tool options are

[01:11:37.760] the unions of all the

[01:11:39.719] tools narrow down to some

[01:11:43.480] amount and we'll post all this code

[01:11:45.840] online. So like you'll get access to it.

[01:11:47.520] We'll send the getter rebound

[01:11:49.640] everything so you'll be able to run this

[01:11:51.679] yourself. I'll probably disable the

[01:11:53.280] embedding thing or maybe what I'll do is

[01:11:54.640] I'll just save the embeddings to disk so

[01:11:56.400] you don't have to recomputee it uh

[01:11:58.239] unless you change the raw

[01:12:00.360] string. Um cool. Or you could just test

[01:12:03.199] this with a slice, right? You know, go

[01:12:05.360] edit the JSON file or just slice out the

[01:12:08.400] first 50 and test this. Um, maybe I'll

[01:12:11.360] do that

[01:12:18.149] because I suspect that's what's

[01:12:18.159] happening right now.

[01:12:26.790] Oh, he gave up.

[01:12:26.800] I have no idea how far in I got. There's

[01:12:28.560] 50 cents of open AI credits down the

[01:12:30.480] drain.

[01:12:32.000] Okay, this might be faster. Doing a

[01:12:33.520] thousand network calls. Um, I realized

[01:12:36.080] 10,000 was probably too ambitious. Um,

[01:12:38.239] I'm going to do less. I'm gonna do 100.

[01:12:41.679] Um, I'm going to only select the top

[01:12:43.520] like the 10

[01:12:46.280] matches. This will likely be a lot

[01:12:48.560] faster. Um, and really what I should

[01:12:50.159] have done is hosted a local embedding

[01:12:51.520] model and just run that. And now you can

[01:12:53.199] see exactly what happened. So I said

[01:12:55.360] what? And this is kind of cool. I said

[01:12:56.719] database stuff and it started building

[01:12:57.920] Superbase into my tooling system.

[01:13:01.880] Right. And actually it said notion API

[01:13:04.480] get page which is probably right. It

[01:13:07.280] picked the superbase MCP server uh

[01:13:09.920] restore page database create a new

[01:13:11.840] database archive page and everything

[01:13:13.120] else. You can see that some of these are

[01:13:14.239] totally

[01:13:15.159] wrong. Um but we can go do this. Um and

[01:13:18.800] it actually asked me a really useful

[01:13:20.560] question. Yes. But I want you to

[01:13:25.000] navigate the

[01:13:28.040] browser to

[01:13:30.520] then find the database ID. And now

[01:13:35.040] hopefully it'll come up with browser use

[01:13:36.800] in the prompt when it does this. And

[01:13:38.560] that's exactly what it just picked one.

[01:13:40.400] Yep. Right. Not only did it do that,

[01:13:42.239] actually list it out and picked browser

[01:13:43.679] base as a thing. Can we can we see the

[01:13:45.840] list of tools that made it in like the

[01:13:47.280] top the top 10, top K or whatever? Yeah,

[01:13:49.920] there you go. and it was able to go pick

[01:13:52.080] that through because I'm only passing

[01:13:53.600] the last message and it basically just

[01:13:55.440] works. I think that's the whole point of

[01:13:57.199] these systems. Um, but if they didn't

[01:14:00.800] work, then what I would do is I'd likely

[01:14:02.400] like likely have to somehow modify the

[01:14:04.000] object that I'm embedding in some way so

[01:14:05.679] the right thing did get selected. That

[01:14:08.000] I'm I'm glad I ran that with a shorter

[01:14:09.520] tool because then we actually got to see

[01:14:10.560] it working into I think that was a great

[01:14:12.080] call. Um, sick. But the principles are

[01:14:15.360] all the same.

[01:14:20.870] Cool. All right, folks. Thanks so much

[01:14:20.880] for coming by.

[01:14:23.199] Thanks for coming, everyone. Uh, we'll

[01:14:25.120] see you guys next week. Human in the

[01:14:26.560] loop. We're going to do async. We're

[01:14:27.920] going to do we're going to do autonomous

[01:14:29.760] agents. We're going to do clarifying

[01:14:31.600] with the human for a while. I'm really

[01:14:33.040] excited to show some human in the loop

[01:14:34.480] code.

[01:14:36.080] Awesome. Thanks everyone. Bye folks.

[01:14:39.600] Good luck. Good luck.
