# Claude for Non-Code Tasks



Source: YouTube captions (automatic:en)



[00:00:05.750] All right, everyone. I'm Bav Offs. This

[00:00:05.760] is Dexter.

[00:00:07.400] >> Hi.

[00:00:08.680] >> I work on Baml on I make programming

[00:00:11.080] language, Dexter.

[00:00:12.720] >> Uh I'm Dex. I'm the founder of Human

[00:00:14.840] Layer and I make tools to make agentic

[00:00:17.760] coding easier and better. And this is

[00:00:20.560] the AI at Work Show where we give you

[00:00:23.640] about an hour a week of practical coding

[00:00:26.240] tips for advanced usage and to improve

[00:00:28.920] your use of AI.

[00:00:32.240] >> Exactly.

[00:00:33.480] Um and then our whole goal here is

[00:00:36.200] always um

[00:00:37.840] Sorry, one second.

[00:00:45.590] I apologize for that. Uh I'm working

[00:00:45.600] from home today cuz the internet at our

[00:00:47.000] office is dead.

[00:00:48.520] Uh so sadly, I was stuck here and our

[00:00:50.520] cleaners were around. So I was like, let

[00:00:51.880] me go tell them not to do the top floor.

[00:00:54.440] Um but

[00:00:56.360] one of the things that Dexter and I

[00:00:57.560] always talk about is context

[00:00:58.920] engineering. We talk about how to go and

[00:01:00.000] build these systems.

[00:01:01.760] And I think a lot of people forget that

[00:01:04.480] all these AI applications that we are

[00:01:06.240] all building,

[00:01:07.600] whether we're the user or the engineer

[00:01:09.520] building them,

[00:01:11.080] every single one of us has to think

[00:01:12.600] about context engineering along that

[00:01:14.120] loop.

[00:01:15.320] You have to as a user of an application,

[00:01:16.960] you have to be like, how can I context

[00:01:18.280] engineer Claude the best to make it

[00:01:20.160] generate the code I want? As a builder

[00:01:22.400] of Claude uh Claude code, I need to go

[00:01:24.720] ahead and think about how can I make it

[00:01:26.320] so that the agent will do what the user

[00:01:27.680] wants more of the time. And that it's

[00:01:29.320] that symbiosis of both systems

[00:01:32.000] that it actually makes a really

[00:01:33.480] beautiful experience that makes us be

[00:01:34.880] like, wow, and blows our minds away and

[00:01:37.280] says these AI agents are actually really

[00:01:39.360] good.

[00:01:40.440] And well, normally a lot of our past

[00:01:42.920] episodes have been talking about how to

[00:01:44.160] be actually write some of these agents.

[00:01:46.360] Today, I think there's some real magic

[00:01:48.800] in really thinking about how we're going

[00:01:51.240] to go ahead and almost

[00:01:54.160] be the users.

[00:01:55.600] And think about how can we as users our

[00:01:57.600] best efforts

[00:01:59.240] to go and make these agents work the way

[00:02:00.560] that make them work the way that we

[00:02:02.720] really want them to work.

[00:02:04.520] And one really interesting insight that

[00:02:06.360] I have personally learned

[00:02:08.039] uh working with Dex on these kind of

[00:02:09.600] things and I've been learning from him a

[00:02:10.720] lot actually on these topics.

[00:02:12.920] >> Sorry.

[00:02:13.680] >> Um

[00:02:14.480] comes down to the fact of like

[00:02:17.640] I actually become a better agent builder

[00:02:20.480] by becoming a better agent user.

[00:02:22.920] Cuz it helps me think about like what

[00:02:24.120] are the UX patterns that I wish existed

[00:02:25.959] in these apps. What are the mistakes

[00:02:27.680] that the agent was making and how do I

[00:02:28.959] actually want to interface with them?

[00:02:30.480] For example, last week's episode was

[00:02:32.200] about how to build agents that you can

[00:02:33.520] interrupt.

[00:02:35.120] Why does it Why does that matter? Well,

[00:02:37.480] the most frustrating thing is when I'm

[00:02:39.080] in ChatGPT and I tell it to do something

[00:02:40.840] and it starts spitting out text and

[00:02:42.280] halfway through I'm like, "No, no, no,

[00:02:43.360] go in that direction." What I have to do

[00:02:45.440] there is I have to hit cancel, edit my

[00:02:47.240] previous message, and then press enter.

[00:02:50.200] I wish I could just send a message.

[00:02:53.160] And there's small things like that that

[00:02:54.959] help us think about the design patterns

[00:02:56.560] that we need to do when we build these

[00:02:57.640] agents.

[00:02:59.160] And so today we're going to do something

[00:03:00.840] really exciting

[00:03:02.400] which is

[00:03:03.720] be users of Claude Code.

[00:03:06.760] Dex, you want to

[00:03:08.280] take it away?

[00:03:09.519] >> I would love to, yeah. Um

[00:03:11.720] so yeah, I think um just kind of

[00:03:13.600] hammering that down a little bit. Like

[00:03:15.200] one of the things we say a lot in

[00:03:16.920] context engineering

[00:03:18.800] is um you know, LLMs are stateless

[00:03:21.440] functions, right? So you have your LLM

[00:03:23.720] like the LLM outputs some kind of tokens

[00:03:26.400] and that's like, you know,

[00:03:28.160] you have your answer

[00:03:29.600] and this answer has a spectrum of

[00:03:31.160] quality from like, you know,

[00:03:33.680] it's slop

[00:03:43.390] Um and the only thing that kind of

[00:03:43.400] affects the quality of this answer, if

[00:03:44.880] you're using a fixed LLM and kind of

[00:03:46.320] fixed parameters, is the quality of the

[00:03:48.959] tokens you put in.

[00:03:50.600] And the tokens you put in is essentially

[00:03:52.400] going to be a context window, right? You

[00:03:54.920] could think people talk about prompt

[00:03:56.480] engineering and a prompt, but at the end

[00:03:58.080] of the day, you're going to have a bunch

[00:03:59.160] of different components of what you put

[00:04:00.560] in. You're going to have your system

[00:04:01.560] message.

[00:04:03.120] You're going to have some, you know,

[00:04:05.360] maybe if you did some rag or injected

[00:04:07.600] stuff, um you may like pull some data

[00:04:10.080] from somewhere else.

[00:04:11.760] You're going to have actually If you're

[00:04:12.920] building an AI application, right? Then

[00:04:15.240] you may pull in the user message, um

[00:04:19.000] and then you may put in some like, you

[00:04:20.840] know, instructions.

[00:04:23.880] And then you may also put in some like

[00:04:25.400] memories, right? There's There's all

[00:04:26.640] kinds of stuff you could put in this

[00:04:27.480] context window, and you can shuffle

[00:04:29.120] We've done a lot of episodes on like

[00:04:30.200] shuffling the order of these things and

[00:04:31.720] figuring out how to make them more

[00:04:32.720] concise and more optimized for the LLM.

[00:04:34.760] And so that's If you're writing the code

[00:04:36.480] and you're just structuring everything

[00:04:37.800] around this LLM call, then um

[00:04:41.200] you have a lot of um

[00:04:42.680] like levers you can pull to improve the

[00:04:44.800] performance of this answer that your

[00:04:46.720] system gets or that your user gets.

[00:04:49.200] Um but today we're going to talk And And

[00:04:51.200] And 2 weeks ago we talked about like

[00:04:52.360] just If you are not the agent builder

[00:04:54.160] and you're just the agent user, and the

[00:04:56.120] only thing you control is the user

[00:04:57.760] message, why it's so important to

[00:05:00.240] understand um actually We'll change this

[00:05:02.760] to tools cuz that's more relevant. Um

[00:05:05.840] why it's so important to understand the

[00:05:07.560] other parts of the prompt and where your

[00:05:10.919] message gets injected, because at the

[00:05:13.080] end of the day, you're just one step

[00:05:14.880] removed, but you're still doing context

[00:05:17.440] engineering. You just have less control.

[00:05:19.040] The agent builder owns these parts, and

[00:05:20.960] you only own your user message.

[00:05:23.360] Does that make sense?

[00:05:24.400] >> Exactly. And like one important thing to

[00:05:26.280] think about as an agent builder here is

[00:05:29.080] while we all aspire to almost hide all

[00:05:32.120] these parts purely from our users and

[00:05:33.760] hope that they're purely implementation

[00:05:35.640] details,

[00:05:36.800] in practice,

[00:05:39.200] you actually make it harder for the

[00:05:41.200] users of your app to go do something

[00:05:43.280] better when you make it totally

[00:05:44.800] abstracted. It's important

[00:05:47.320] I would say it's almost your obligation

[00:05:49.720] as an agent builder to at least have

[00:05:51.640] some provide some insight to your users

[00:05:54.120] about how things work.

[00:05:55.800] It's kind of like if you ever use like

[00:05:57.800] any sort of like um

[00:06:00.400] like social media, there's some feedback

[00:06:02.440] loop that you get from like Twitter or

[00:06:04.040] LinkedIn about like what content is

[00:06:05.520] doing well and you're able to navigate

[00:06:07.480] that yourself. Even if you don't know

[00:06:08.520] exactly what's going on, there's some

[00:06:10.040] feedback loop that's available to you

[00:06:11.880] that you can iterate. Some people become

[00:06:14.520] amazing content creators because they

[00:06:16.280] learn how to grasp that signal way

[00:06:17.520] better than other people do.

[00:06:19.400] Same thing here.

[00:06:20.600] But if you're building a tool and you

[00:06:21.960] make it too hard for most users to

[00:06:24.400] understand how to min-max your tool,

[00:06:26.560] they're just not going to use it because

[00:06:27.600] it'll it'll end up more on the slop side

[00:06:29.400] than the really good side.

[00:06:31.800] >> Yeah, and this is expected from there,

[00:06:32.880] right? Like some users, sometimes you

[00:06:34.320] want to make an AI for users that are

[00:06:35.800] not very sophisticated and don't

[00:06:37.440] understand the tool calls or just JSON

[00:06:39.280] objects that get injected in with a

[00:06:40.560] schema and things like that. And then in

[00:06:42.520] that case it's like may if you're

[00:06:44.040] building like an AI for uh people to

[00:06:46.880] get, you know,

[00:06:48.880] uh

[00:06:49.760] you know, let's say medical advice an AI

[00:06:51.680] veterinarian that's going to help people

[00:06:53.200] like figure out what's going on with

[00:06:54.120] their pets, it's like unlikely those

[00:06:55.919] people are very thoughtful context

[00:06:58.080] engineers. Some of them maybe, but then

[00:06:59.880] when you're building a coding agent

[00:07:01.000] that's going to be used by really

[00:07:02.000] technical people, then this becomes a

[00:07:03.800] lot more important.

[00:07:05.000] >> Yeah, exactly.

[00:07:06.840] >> Um two quick like kind of throwbacks. Um

[00:07:12.000] I think it's here. Yeah, so we did this

[00:07:14.360] episode about um Claude code and and

[00:07:17.280] using like kind of like

[00:07:19.440] context engineering and applying it to

[00:07:21.200] how you use coding agents.

[00:07:23.400] Um we're not actually going to talk much

[00:07:25.080] about that today, although some of the

[00:07:26.760] same concepts are going to be in there.

[00:07:28.240] I think we get asked about a lot and a

[00:07:29.600] thing that I've been doing a lot and

[00:07:30.520] really enjoying that I thought I would

[00:07:31.480] share some some experiences on is how to

[00:07:33.800] use Claude code to do things that are

[00:07:35.200] not writing code.

[00:07:37.280] Um because it's actually just a very

[00:07:39.080] good general purpose agent and the fact

[00:07:41.040] that it can write code is really

[00:07:42.120] interesting because instead of instead

[00:07:43.880] of having to find MCP tools for

[00:07:45.240] everything, Claude can kind of just

[00:07:46.960] write its own scripts. So, I'm going to

[00:07:48.840] walk through a couple concepts that I

[00:07:51.200] think are really important to understand

[00:07:52.360] here and then we'll demo I have a demo

[00:07:54.880] set of code in the repo about um

[00:07:58.440] kind of how we use this. And Andrew,

[00:08:00.280] yes, the Claude code system prompt is

[00:08:01.920] all about code, but it still works

[00:08:04.280] pretty well for other things as well.

[00:08:06.760] Oops.

[00:08:07.840] Um

[00:08:09.280] so this is um I've set up

[00:08:13.200] a little

[00:08:14.000] >> Brian uh

[00:08:15.520] while you pull that up, Tess. Brian,

[00:08:16.760] that's a question. Isn't there a

[00:08:18.040] spectrum of like novice users to power

[00:08:19.680] users? There completely is, but that's

[00:08:22.280] kind of why it's important for you as an

[00:08:24.960] agent builder to think really carefully

[00:08:26.960] about what that spectrum is for your

[00:08:29.000] users and where they fall on. If your

[00:08:31.000] users fall more towards the novice side,

[00:08:33.039] like they're not going to go do it, it's

[00:08:34.840] not just about exposing user messages,

[00:08:37.200] it's actually about building really

[00:08:38.520] interesting UI paradigms so that a thing

[00:08:40.880] that is typically viewed as a user

[00:08:43.800] message

[00:08:45.120] is actually going to be act have like

[00:08:48.000] some additional metadata. For example,

[00:08:50.880] let's say you're building a rag system

[00:08:52.400] that's going to go at answer questions

[00:08:54.080] about it.

[00:08:55.680] Um can I draw on your screen, Tess?

[00:08:57.839] >> Go for it. Um oh, let me share the link

[00:08:59.760] so you can actually draw on the

[00:09:00.960] whiteboard itself.

[00:09:02.480] >> That would actually be much better.

[00:09:04.240] Um

[00:09:08.670] and then we'll go back to this really

[00:09:08.680] fast. And then um uh

[00:09:10.760] Amo, yes, all the recordings are shared.

[00:09:12.600] If you've signed up on um

[00:09:14.880] if you signed up on the Luma link, you

[00:09:16.520] will get

[00:09:17.960] an email automatically at the end of

[00:09:19.800] either tomorrow or uh by the end of this

[00:09:21.880] week at the latest.

[00:09:23.520] >> And they're also all here in the repo.

[00:09:25.760] If you go to the AI that works repo,

[00:09:27.120] there is an index of all of the past

[00:09:29.480] episodes. So, if you want to go binge

[00:09:31.160] them, um

[00:09:32.440] please go go do that and have fun.

[00:09:36.040] >> So, just to be really concrete, really

[00:09:37.800] first on this like one way to build a

[00:09:39.240] search box is to just say search box and

[00:09:41.360] now I'll magically do rag under the

[00:09:42.960] hood. Another way to build a search box

[00:09:45.120] is just to say like here's a rag I'm

[00:09:47.320] pulling from under the hood and I will

[00:09:49.760] actually like what cursor does and you

[00:09:51.320] can use the at symbol to refer to other

[00:09:53.160] documents.

[00:09:55.240] And whether it's a word doc or something

[00:09:56.640] else or Google Docs doesn't really

[00:09:57.920] matter, but it allows the user to have

[00:10:00.040] some UX that basically intervenes into

[00:10:03.120] the context building without even

[00:10:05.040] feeling like it's intervening into the

[00:10:06.560] context when

[00:10:07.840] context um

[00:10:09.560] building. And you can do this with

[00:10:10.680] tools, you can do this with rags, you

[00:10:12.120] can do this with almost anything.

[00:10:13.920] But and it doesn't even have to be pure

[00:10:15.920] green. It could be half user, half

[00:10:18.600] >> blend, right?

[00:10:19.560] >> Exactly. You can have a blend.

[00:10:20.960] But this is going to where you can think

[00:10:22.640] about how you like how how easy and hard

[00:10:25.680] something feels is purely based on the

[00:10:27.840] amount of developer experience that you

[00:10:30.080] are willing to

[00:10:31.840] impose on your end users based on the

[00:10:34.080] amount of engineering work that you're

[00:10:35.160] willing to do. If you're willing to do

[00:10:36.600] more engineering work, you can basically

[00:10:38.520] give your users full control of

[00:10:39.720] everything. If you're really good at UX,

[00:10:41.800] it won't even feel bad.

[00:10:43.560] If you're really bad at UX, you'll

[00:10:44.720] basically make them reinvent context

[00:10:46.400] engineering from scratch and then you

[00:10:48.320] better hope your users are extremely

[00:10:50.720] extremely technical.

[00:10:53.280] >> Yeah, I love it.

[00:10:55.880] Um great. So um one thing that we've

[00:10:58.400] been doing is essentially we create a

[00:11:01.640] uh

[00:11:02.800] we've created a a Git repo that we use

[00:11:05.320] to do all of our non-technical things.

[00:11:07.760] And so I'll walk through kind of one

[00:11:09.280] example, which is a CRM. Um we don't use

[00:11:12.360] a CRM anymore. Um Claude Code runs our

[00:11:14.839] CRM.

[00:11:16.000] And while you could have Claude Code

[00:11:17.680] have an MCP tool that talks to

[00:11:18.920] Salesforce or Linear or Airtable or

[00:11:21.640] whatever you're using for your CRM,

[00:11:23.360] we've actually just found this works

[00:11:24.520] really well with Markdown documents. And

[00:11:27.240] so um I have um I'll push all this code.

[00:11:30.040] I haven't pushed it yet. Um but we have

[00:11:31.680] kind of a core structure of a fictional

[00:11:34.680] company that is a on-demand burrito

[00:11:36.880] delivery platform. Um, I also have a

[00:11:39.760] couple real examples from our internal

[00:11:41.960] stuff that I will not be sharing. Uh,

[00:11:45.200] but I will show them to you here. Um, so

[00:11:47.720] I've cleaned this up a little bit. But

[00:11:49.720] this is uh, let's just delete this

[00:11:52.080] folder just in case there's still stuff

[00:11:53.720] in it.

[00:11:55.440] Um, this is like um, reveals another

[00:11:58.760] company in our YC batch. They do really

[00:12:01.280] cool stuff. Um, but you'll see a couple

[00:12:03.040] things here is like this is a markdown

[00:12:04.520] document that explains the people we're

[00:12:06.440] talking to and what's happened so far.

[00:12:09.000] Um, we also have contacts for all of

[00:12:10.920] these people.

[00:12:12.160] Um,

[00:12:13.640] and then we have events. So like this is

[00:12:15.520] an event of And so like these are all

[00:12:17.760] things that you could imagine being

[00:12:19.560] sequel objects in a database. But what's

[00:12:22.240] been working really well is like if you

[00:12:24.080] keep them as markdown then there's no

[00:12:25.320] tool calls required other than just

[00:12:26.680] reading and writing files.

[00:12:28.400] And what you have is you start to build

[00:12:30.240] out basically rather than like a

[00:12:31.520] relationship graph that we would use

[00:12:33.080] with a sequel database, we're kind of

[00:12:35.120] faking it with building a knowledge

[00:12:36.960] graph as markdown files that kind of

[00:12:39.200] just point to each other. And it's a lot

[00:12:40.640] more freeform and it's a lot more

[00:12:42.520] structureless.

[00:12:44.080] Um, but that gives you a lot of

[00:12:45.640] flexibility in terms of And like Claude

[00:12:47.560] can rewrite any of this stuff. You can

[00:12:48.880] fire off about If you decide you don't

[00:12:50.120] like the structure, you can do something

[00:12:51.240] else. But it's basically the combination

[00:12:52.760] of like front matter for deterministic

[00:12:55.720] things.

[00:12:56.760] Um, so you could feed this part to code

[00:12:58.960] and it's metadata about the document and

[00:13:00.720] then Claude can read the document and

[00:13:02.280] the front matter, but like read the

[00:13:03.680] document and understand how it's going.

[00:13:06.200] >> And I want to I want to call out a

[00:13:07.560] couple things really fast. The reason

[00:13:09.720] that this works now and it didn't used

[00:13:11.600] to work before is cuz the models are

[00:13:13.960] getting better.

[00:13:15.360] So and this is just an emergent

[00:13:17.160] capability that we'll all discover over

[00:13:19.280] time

[00:13:20.640] of exactly what's going on. But if you

[00:13:23.440] go ahead and assume that that model can

[00:13:25.480] never do something, you won't be able to

[00:13:27.000] push it to the limit of what it's

[00:13:28.200] actually able to do.

[00:13:29.800] >> Yeah. And this isn't perfect yet. And

[00:13:31.640] it's it's not just the models, too. I

[00:13:32.960] would say it's also the agents

[00:13:35.000] themselves.

[00:13:36.480] >> Yes.

[00:13:36.720] >> Um and so here's like a here's our

[00:13:39.000] engagement history, right? So and I'll

[00:13:40.840] show you how this data gets in, but it's

[00:13:42.320] like it's not just the models

[00:13:43.240] themselves. It's like the agent harness,

[00:13:44.880] right? Claude code is not just Claude's

[00:13:46.720] a great model and it's really, really

[00:13:48.640] well trained and tuned for doing this

[00:13:50.160] kind of work, but it's also that the

[00:13:53.200] harness around it is really, really

[00:13:54.800] tailored to modifying files in a repo.

[00:13:59.880] Um

[00:14:01.280] and so oh, we got a lot of notes in the

[00:14:03.160] chat. Uh Tyler, the way you So, this is

[00:14:06.480] a great question. So, it's like do would

[00:14:08.000] this scale over thousands of contacts?

[00:14:11.080] Um and so the way that we scale this

[00:14:13.520] across thousands of contacts is

[00:14:15.040] basically by doing deterministic

[00:14:16.840] contacts packing, basically. And so what

[00:14:20.000] what we have in here is we have a

[00:14:22.680] makefile

[00:14:24.680] that essentially um

[00:14:27.560] is ways to kind of deterministically

[00:14:29.560] build up your context. And so rather

[00:14:31.760] than having the agent go This is one's

[00:14:34.200] very specific to like, "Hey, let's just

[00:14:36.600] show the first 100 lines of of a couple

[00:14:39.960] different files."

[00:14:41.720] Oh god.

[00:14:43.440] Uh sorry, I was doing some last minute

[00:14:45.040] prep here. So, uh excuse my uh insane

[00:14:48.320] cursor stuff.

[00:14:50.000] Um and I know I said I don't really use

[00:14:51.839] editors anymore, but I do use cursor

[00:14:53.480] when I'm in a hurry and I procrastinated

[00:14:55.480] on the episode prep.

[00:14:57.800] Um

[00:14:59.520] So, here's the one that we had for human

[00:15:01.400] layer, basically, which is, you know,

[00:15:03.440] um our company, everything we have, our

[00:15:05.680] read me, our bi-weekly meeting notes,

[00:15:07.560] our weekly updates, our monthly investor

[00:15:09.200] updates, and just kind of passing in

[00:15:10.760] certain bits of context. And so you can

[00:15:12.800] imagine doing this similarly with a file

[00:15:16.440] that um

[00:15:18.000] basically traverses this knowledge graph

[00:15:20.760] or slices and dices by tags and things

[00:15:23.280] like this. And so, um we build tools for

[00:15:27.360] this. Let's see. I actually don't have

[00:15:29.360] one right now.

[00:15:30.760] Um but let's see if we can make one. Um

[00:15:35.040] >> You want to show the full match result

[00:15:36.120] TS?

[00:15:37.600] >> Um yeah, so this is this is another like

[00:15:40.040] SO So So the other part of this is SOPs.

[00:15:43.520] So you have sort of like

[00:15:45.760] markdown

[00:15:47.760] as database.

[00:15:50.600] And you have kind of two sections,

[00:15:52.400] right? You have your front matter.

[00:16:04.470] And then you have your actual document,

[00:16:04.480] which is like mostly for models.

[00:16:11.910] Um

[00:16:11.920] So that's

[00:16:12.480] >> And And when Dash says the word front

[00:16:13.920] matter, can you pull up the code really

[00:16:15.200] fast, Dash? The front matter.

[00:16:17.120] I want to be a little bit more explicit

[00:16:18.320] about what he means by this. Front

[00:16:20.040] matter is this part.

[00:16:22.440] >> Is the Yeah, the So So markdown docs

[00:16:24.880] support this format.

[00:16:26.400] >> Yeah. And the And what you can think of

[00:16:27.920] this as is we all know, if you ever have

[00:16:30.480] seen cloud code, and this is just

[00:16:32.080] intuitive knowledge that Dash is using

[00:16:33.800] based on how he has seen cloud code

[00:16:35.480] work. It might change if cloud code does

[00:16:37.680] something different. But cloud code,

[00:16:39.360] when it does when you first refers to a

[00:16:41.080] file that's really long, it actually

[00:16:42.760] just dumps out the first 100 or 100

[00:16:44.760] lines or so of it. Just see what it does

[00:16:46.280] approximately.

[00:16:47.760] >> Yeah.

[00:16:48.200] >> What that means is if you're an engineer

[00:16:50.280] and you're not running docstrings at the

[00:16:51.760] top of a file explaining what it does,

[00:16:54.040] you're just hurting your ability for

[00:16:55.320] super long files to be super useful.

[00:16:57.800] Similarly, in markdown files,

[00:17:00.120] can you go back?

[00:17:01.120] >> Um Yep.

[00:17:02.640] >> In markdown files, Dash is doing the

[00:17:03.880] same thing by saying like, "Hey, if I

[00:17:05.319] want to deal with a month, what is the

[00:17:08.079] a num sorry a num a num The most

[00:17:10.040] important thing that I have to deal with

[00:17:11.720] is I really want to know like recent

[00:17:13.839] information that is super super

[00:17:16.360] uh important for me to know. I probably

[00:17:18.040] want to have contacts and phone and

[00:17:19.040] everything else on there and I probably

[00:17:20.120] want to know like

[00:17:21.680] any relevant files that I might want to

[00:17:23.439] look into in case I I want to have like

[00:17:25.880] quick jumps.

[00:17:27.880] And what that does for the model is any

[00:17:29.960] agent that's using this has really quick

[00:17:32.560] interaction. Like, is this relevant? Is

[00:17:34.600] this not relevant? And it can make a

[00:17:35.800] decision for that without having to go

[00:17:37.840] ahead and

[00:17:39.800] actually

[00:17:41.240] um

[00:17:42.600] without having to go ahead and actually

[00:17:43.880] like uh read the entire file. What that

[00:17:46.120] means is if we go back to how context

[00:17:48.240] engineering works,

[00:17:50.120] the best thing you can do in forms of

[00:17:52.440] context engineering, whether as a user

[00:17:54.040] or as a developer, is give the answer to

[00:17:56.520] the model and that's it. If you give it

[00:17:59.360] the exact answer you want to put out, it

[00:18:01.000] will spit it out for you.

[00:18:02.560] The second best thing you can do is give

[00:18:04.880] it as much data that is related to the

[00:18:06.920] actual answer without having to actually

[00:18:09.320] think about it.

[00:18:10.720] However,

[00:18:13.240] that is also really hard. So, the next

[00:18:14.760] best thing you can do is give it as

[00:18:16.480] little noise about what isn't relevant

[00:18:19.160] so that it can actually do the right

[00:18:20.320] thing. So, in this scenario, by only

[00:18:22.640] pruning it to the most relevant sections

[00:18:24.400] at the top, Dexter can effectively give

[00:18:26.800] the model the least amount of noise, and

[00:18:28.800] the noise being all the other noise on

[00:18:30.560] in every single file,

[00:18:32.440] without having to think about it.

[00:18:36.430] So,

[00:18:36.440] >> Yes.

[00:18:38.040] >> There you go. We muted.

[00:18:39.120] >> Um yeah, that makes a lot of sense. Um

[00:18:41.200] yeah, I muted them. Uh

[00:18:42.760] this is in Git Ignore, so Claude can't

[00:18:44.680] find it. Um but what we have, I will

[00:18:47.920] show you um

[00:18:55.150] there's a couple fun things you can do.

[00:18:55.160] So, like I want to talk about kind of

[00:18:56.240] like deterministic context backing, and

[00:18:58.200] this is like a really really

[00:18:59.720] >> $2 just to run a make command?

[00:19:03.480] >> Is it $2? Where does it say $2?

[00:19:05.560] >> Or like at least a dollar, cuz you're

[00:19:07.000] running Opus.

[00:19:08.240] >> Yeah. Oh, yeah. We use Opus for

[00:19:09.640] everything.

[00:19:16.390] Um so, yeah, this thing is going to

[00:19:16.400] Okay, there's a typo.

[00:19:17.880] So anyways, you can use Claude to build

[00:19:19.520] out these systems and you can tell

[00:19:20.880] Claude like, "Hey, I want a script."

[00:19:22.640] Let's make another one.

[00:19:24.040] I need a script that only fetches files

[00:19:29.320] modified the last day.

[00:19:33.120] Read some files for examples and put it

[00:19:38.200] in a TS file I can run with fun and

[00:19:42.000] tools.

[00:19:43.120] So you can start to build out kind of

[00:19:44.880] programmatic ways to work with this

[00:19:46.720] information and then hand those tools

[00:19:49.000] back to Claude. And one of the things we

[00:19:50.480] do a lot is um we use slash commands to

[00:19:52.640] kind of automate some of this stuff.

[00:19:54.720] Um so this is like

[00:20:04.390] and run the daily review SOP. So we have

[00:20:04.400] um

[00:20:05.520] things called SOPs and this is what I

[00:20:07.360] spend most of my time doing is like,

[00:20:09.160] "Okay, you're you're running a company.

[00:20:10.440] What are all these things you're doing

[00:20:11.360] manually?" Okay, check my email, I got

[00:20:12.760] to do this. Okay, I got to go check this

[00:20:14.400] thing once a week. Okay, I got to pull

[00:20:15.680] these metrics. And so you can start

[00:20:17.400] building these into SOPs. This is kind

[00:20:20.240] of a redacted version of what we what we

[00:20:23.800] use at Human Layer. So every day there's

[00:20:25.640] kind of like, "Hey, you're going to

[00:20:26.600] output a comprehensive markdown file."

[00:20:28.880] This is actually related also to how we

[00:20:30.440] do compaction. Um so I turn this on

[00:20:33.240] every morning and I just brain dump into

[00:20:36.320] it everything that's going on. I read my

[00:20:37.640] calendar, I read a couple other things.

[00:20:39.320] Um the one we use is also has a bunch of

[00:20:40.760] tools to like check email and check

[00:20:42.000] calendar and stuff like that which I

[00:20:43.440] haven't included yet, but you can

[00:20:44.560] imagine how those would fit. Um but we

[00:20:47.040] say, you know, do a brain dump, um do a

[00:20:50.440] metrics review. So let me see if I can

[00:20:52.080] actually kick this off.

[00:20:54.280] Um

[00:21:01.510] See how this goes.

[00:21:01.520] I haven't tested this. Um but we have

[00:21:03.480] another one for our investor updates. So

[00:21:05.400] I have fake investor updates for the uh

[00:21:09.120] Burrito now monthly. And so, the idea

[00:21:11.480] would be every day you log in or every

[00:21:12.960] couple days you log in and you generate

[00:21:14.360] a daily review. And then, once a month,

[00:21:17.320] I just compact all the daily reviews and

[00:21:19.760] then have some tools to do things like

[00:21:21.280] pull metrics or pull PR links or pull

[00:21:24.120] product updates from other systems and

[00:21:26.400] compact them into a really nice investor

[00:21:28.320] update. And you can write basically the

[00:21:30.160] the SOPs become your prompts and your

[00:21:32.040] commands.

[00:21:33.480] Um and then they

[00:21:35.640] Yeah.

[00:21:36.400] >> So, one really tangible example for

[00:21:38.120] everyone here is that a lot of people

[00:21:39.200] are engineers. All of us probably

[00:21:41.480] execute some team that does some stupid

[00:21:43.840] amount of stand-up.

[00:21:45.320] And most stand-ups, while stand-up is a

[00:21:47.320] great ritual to actually have a forcing

[00:21:49.280] function for everyone to connect, the

[00:21:50.960] actual content of the update

[00:21:53.480] is

[00:21:55.280] um

[00:21:56.680] is actually very hard.

[00:21:58.680] Uh and very useless for a lot of people

[00:22:00.720] to have. So, what we can do is you could

[00:22:02.600] imagine running a stand-up where instead

[00:22:04.560] of actually having everyone go do it,

[00:22:06.080] you just look at the PRs that happened,

[00:22:07.600] look at all the Git commits, expect

[00:22:09.280] everyone to just like regularly be

[00:22:10.520] pushing feature incomplete branches,

[00:22:13.200] and just run a system that's going to

[00:22:14.480] Git clone every single branch that

[00:22:15.840] everyone is actively working on or

[00:22:17.080] pushed in the last 2 days,

[00:22:19.680] get a summary of it, get the person, get

[00:22:21.960] the system, and then just write it down.

[00:22:24.360] And then boom, you now have stand-up

[00:22:25.680] updates for free backed by sources of

[00:22:27.360] truth.

[00:22:28.600] Uh and you can actually make sure your

[00:22:30.120] stand-up is under 5 minutes, guaranteed.

[00:22:32.560] >> Yep.

[00:22:33.040] >> It's a really fancy thing that you can

[00:22:34.360] do. But, this requires you, as whoever's

[00:22:36.680] running this, to actually have access to

[00:22:38.160] the GitHub repos and be able to write

[00:22:40.040] some amount of knowledge about how uh

[00:22:42.240] how it's going to work, but it doesn't

[00:22:43.160] really have to be that good.

[00:22:46.800] Claude, go and say you got the rest.

[00:22:49.400] >> Yeah. So, usually I would come in here

[00:22:50.880] and do like a big long rambling brain

[00:22:52.720] dump of like, "Okay, I had these

[00:22:53.920] meetings yesterday and we got these new

[00:22:55.360] clients signed and I need to I need to

[00:22:57.480] follow up with these six people because"

[00:22:59.160] and it's like brain dump of what's on

[00:23:00.680] your mind.

[00:23:02.440] And then you would paste that in here.

[00:23:04.520] Um

[00:23:05.480] So, uh in this case, I'm not going to

[00:23:08.120] send that. I'm just going to say, "Hey,

[00:23:09.440] we sold a lot of burritos yesterday."

[00:23:10.800] And then it's going to go through and

[00:23:12.120] run through this SOP. So, it's going to

[00:23:14.200] review yesterday's work, which like in

[00:23:15.800] our in our in our in our repo, we have a

[00:23:17.520] journal file, so the model kind of

[00:23:19.160] tracks like all these different ways of

[00:23:21.160] doing memory. And right now, I'm like

[00:23:22.720] kind of in prototype mode. And so, we

[00:23:24.720] write There's a lot of duplicated data.

[00:23:27.320] And then as we refine the process and

[00:23:28.960] figure out what works, we're getting

[00:23:30.280] more and more concise. Like the CRM

[00:23:31.960] stuff is actually pretty baked and

[00:23:33.360] concise, but the some of the more like

[00:23:35.360] journaling and memory and like update

[00:23:37.080] stuff is still we're still figuring out

[00:23:38.920] how we want that to all work.

[00:23:41.360] >> Tyler asked a really interesting

[00:23:42.480] question. How do you think about agents

[00:23:44.040] versus workflows when automating these

[00:23:45.720] non-coding tasks? I think my perspective

[00:23:49.160] on all this is like I think the word

[00:23:50.480] agent or workflow doesn't really matter.

[00:23:52.520] What I always think about is just like

[00:23:54.680] how much automation are you actually

[00:23:56.000] getting and how clean is the result that

[00:23:57.840] you need? If you need it to be perfect,

[00:24:00.000] then like write the code. Just write the

[00:24:01.440] tool that pulls the data that you want

[00:24:03.120] and then have Cloud Code format into

[00:24:04.480] human-readable format.

[00:24:06.280] If you're okay with loosey-goosey stuff

[00:24:07.880] like stand-up updates, honestly, I'll

[00:24:09.360] just tell Cloud Code to get clone every

[00:24:11.800] single um

[00:24:13.320] get clone the repos, look at all the

[00:24:14.480] branches that are modified in the last

[00:24:16.440] 48 hours,

[00:24:18.320] give a summary of every single diff

[00:24:19.720] against the main branch.

[00:24:21.520] And I don't need it to be perfect and I

[00:24:22.920] just I would just tell it to go do that.

[00:24:24.320] I'd say, "Use sub-agents for every

[00:24:25.680] single branch."

[00:24:26.920] >> So, we actually do this. Um

[00:24:28.720] because I'm not exactly sure what the

[00:24:30.440] workflow is and I'm a little less like

[00:24:32.400] concerned about like exactly what

[00:24:33.920] happens here, we built this release

[00:24:36.200] notes SOP as a prompt, not as a

[00:24:38.960] workflow. But you could easily see how

[00:24:41.600] you could be like, "Okay, fetch the last

[00:24:43.360] things with an API call and then grab

[00:24:45.600] the body of each one and then send that

[00:24:48.680] to an LLM to format into an update um

[00:24:51.280] where it's like, "Okay, use it use it

[00:24:52.880] use a baml call to extract two sentences

[00:24:54.960] about the release and then extract each

[00:24:57.160] feature and then like the deterministic

[00:24:59.160] code builds the markdown file and we may

[00:25:01.680] actually do that someday but what this

[00:25:03.640] becomes is a really nice way to do

[00:25:06.640] prototyping. And so this thing like now

[00:25:09.000] that I have this workflow I'm changing

[00:25:10.520] it every day and that I can just change

[00:25:12.680] the prompt and I get the results that I

[00:25:14.280] want because the stuff that is like

[00:25:15.760] deterministic which is like using the GH

[00:25:17.640] CLI is pretty straightforward and Claude

[00:25:20.120] is really good at doing these kinds of

[00:25:21.400] things. If I have Claude write a tool

[00:25:22.760] that check my email that's pretty easy

[00:25:24.560] for it to like run and then change the

[00:25:27.560] kind of like how the workflow is

[00:25:28.800] supposed to work. And I'll show you

[00:25:30.800] actually the trace of one of these

[00:25:32.040] conversations that we had

[00:25:34.120] but I use this every morning to go fetch

[00:25:36.120] the PRs we merged last night and write

[00:25:37.920] release notes for the latest nightly

[00:25:39.560] build.

[00:25:41.080] And so

[00:25:42.880] we'll come back to this daily review one

[00:25:44.200] but I'm going to show you the

[00:25:47.160] Let's see is there release notes? I

[00:25:49.120] think I archived it.

[00:25:55.990] Oh here we go. This is it. So this is

[00:25:56.000] our release notes from this morning. So

[00:25:58.000] it ran our print context which is

[00:26:00.000] showing the company identity and some of

[00:26:03.000] the other examples and you know how to

[00:26:05.160] get help from humans and like the people

[00:26:07.600] on the team and all this stuff.

[00:26:10.080] And then it does a make print index. So

[00:26:12.720] this is like rather than this is the

[00:26:14.040] context packing thing right? Rather than

[00:26:16.160] having it go like agentically search or

[00:26:18.360] use the built-in LS tool I know that

[00:26:21.000] I'll get more of like context efficiency

[00:26:24.040] by just having it look at every single

[00:26:26.200] like markdown file. And as this gets

[00:26:27.800] really really big I will probably have

[00:26:31.440] it only look at recent projects and

[00:26:33.000] stuff but the nice thing is is like this

[00:26:34.520] becomes really easy to tune and because

[00:26:36.640] it's so interactive and human in the

[00:26:37.880] loop you can kind of just keep updating

[00:26:39.320] it every day as you go.

[00:26:41.360] >> Yeah.

[00:26:41.720] >> Um but what this did was it found

[00:26:45.040] it listed out the PRs and saw the merged

[00:26:46.800] PRs that we had from last night. It did

[00:26:49.600] the JSON body stuff. So like this is all

[00:26:51.600] stuff that could be programming and

[00:26:52.920] scripting, but it's all meta work. It's

[00:26:54.280] all things that are like tedious back

[00:26:56.040] office things that I would usually just

[00:26:57.840] spend time going and compiling release

[00:26:59.680] notes every day.

[00:27:01.160] Um and like yes, there are tools that

[00:27:03.880] will do this for you, but they're kind

[00:27:05.080] of hard to customize. But, you know what

[00:27:07.000] can customize text really, really well

[00:27:08.800] is like a prompt in an LLM. And so, this

[00:27:11.280] went through and it edited the release

[00:27:13.200] and it created this um release tag for

[00:27:15.840] Code Layer last night.

[00:27:17.880] And here's what it looks like. So, I I I

[00:27:20.720] literally did this this morning.

[00:27:22.520] And then when it was done, I went and

[00:27:23.720] made a video demoing it. And then it

[00:27:25.600] even made me a like Slack We have a

[00:27:27.600] couple like Slack channels, private

[00:27:29.000] channels of like our kind of I call it

[00:27:30.840] trusted testers.

[00:27:32.520] Um I think some of y'all are in here.

[00:27:34.720] Um but then it just made the

[00:27:35.600] announcement post. So, I've given it the

[00:27:37.200] format and the SOP of how to do this and

[00:27:39.280] all of the steps including like hey,

[00:27:41.760] when you're done, like prompt me and I

[00:27:44.400] will give you a video demo. And then you

[00:27:46.320] go put that in the release notes.

[00:27:47.960] >> Yeah. I think the mental model that I

[00:27:49.920] have found worked really well here is um

[00:27:53.120] can you go back to the whiteboard?

[00:27:54.880] >> Yeah.

[00:27:57.280] >> This is at least the mental model that I

[00:27:58.720] use. Uh where did it go?

[00:28:00.680] It hid in front of you.

[00:28:02.280] >> Sorry, I'm pulling it up again.

[00:28:04.800] Yeah.

[00:28:05.560] Um the mental model that I have found

[00:28:07.200] worked really, really well I'm going to

[00:28:08.160] be at the bottom decks. Is I think we're

[00:28:10.520] entering like an kind of a

[00:28:12.480] I think our property said this really

[00:28:13.720] interestingly, which was like you have

[00:28:15.480] software and then you have like software

[00:28:16.720] 1.0, which is like pure code.

[00:28:23.750] And then you have like traditional

[00:28:23.760] machine learning,

[00:28:26.200] which is all about uh like writing uh

[00:28:29.440] writing actual training writing training

[00:28:30.880] models, collecting data, all that stuff.

[00:28:32.600] And like now we have this like new box

[00:28:34.080] that somehow like sits in the middle of

[00:28:35.480] this stuff.

[00:28:37.680] That's like

[00:28:38.920] LLM stuff

[00:28:40.640] is kind of what I would put it as.

[00:28:43.000] And now all of a sudden a lot of the the

[00:28:45.320] stuff that we used to do How do I get

[00:28:46.560] rid of arrow?

[00:28:48.360] I don't know how to get rid of arrow.

[00:28:49.960] Okay, well, I'll figure that out later.

[00:28:51.960] Um a lot of the stuff that we used to do

[00:28:53.760] with uh like pure code can now just be

[00:28:56.000] done by an LLM.

[00:28:57.640] The only caveat is that some of the

[00:28:59.040] stuff that now happens in this box is

[00:29:01.480] just going to break some of the time,

[00:29:03.520] but you can the trade-off is well, it

[00:29:05.640] breaks all the time, it also can be a

[00:29:07.200] lot more flexible and adaptable.

[00:29:09.760] So, when you think about engineering, I

[00:29:11.160] think people there's a discussion thread

[00:29:12.760] going on about like agents versus

[00:29:14.240] workflows all this other stuff.

[00:29:16.120] I think the easiest way to think about

[00:29:17.320] this is it's not actually about like

[00:29:18.960] agents or workflows.

[00:29:20.760] Agents and workflows don't really

[00:29:21.800] matter. You can use agents as tools, you

[00:29:22.920] can use workflows as tools. Agents can

[00:29:24.880] have workflows, workflows can have

[00:29:26.040] agents.

[00:29:27.000] It It's really just the matter of like

[00:29:29.520] whether it's a sequence of stuff or

[00:29:30.720] whether you have a while loop. But, what

[00:29:32.240] I find the easiest way to think about

[00:29:33.400] this is

[00:29:34.480] how much tolerance do I have for my

[00:29:36.280] software not being 100% correct like

[00:29:39.200] consistent.

[00:29:41.600] Generating

[00:29:42.760] Generating notes, I have a lot of

[00:29:44.720] tolerance. If I make something, it's

[00:29:46.920] still That's okay.

[00:29:48.840] I probably trust if I add something

[00:29:51.000] that's not there, also okay cuz I can go

[00:29:52.840] back and edit it if it's not there.

[00:29:55.320] And then it's really just a mental model

[00:29:56.920] of like how much trust can I build in

[00:29:58.400] the model to go and go do this. Turns

[00:30:00.400] out I have a lot of trust in the model

[00:30:01.600] to go and look at a bunch of Git logs

[00:30:03.200] and like summarize what actually

[00:30:04.440] happened based on that system.

[00:30:06.920] >> Yeah.

[00:30:07.000] >> Therefore, it becomes a great task

[00:30:09.480] actually do LLM stuff in it.

[00:30:11.640] And I think another analogy that really

[00:30:13.840] breaks this down like whether or this is

[00:30:15.320] like

[00:30:16.120] coding or not coding, whether you're

[00:30:17.680] putting in that's coding or not, is just

[00:30:20.000] this analogy of like

[00:30:21.720] think about how Python, you we had used

[00:30:23.720] to have Python, then we had C++ then we

[00:30:25.320] had C, then we used to have assembly,

[00:30:27.080] and even before that we had like machine

[00:30:28.680] code.

[00:30:30.480] And if you go to the era in which each

[00:30:32.760] of these is invented and you ask like a

[00:30:34.640] C dev in like 1990s if Python is a real

[00:30:37.760] language, they'd say no. You have to

[00:30:39.640] know garbage collection and memory

[00:30:41.480] management to be able to write code.

[00:30:43.840] Turns out in 2025 that's not true. You

[00:30:46.240] can write a lot of good code by just

[00:30:47.560] writing Python.

[00:30:49.440] And it's very possible

[00:30:51.440] that the world that we live in is

[00:30:53.240] whatever is going to happen here

[00:30:55.920] is the same thing. You used to have to

[00:30:57.880] write Python code to be able to be

[00:30:59.000] called yourself an engineer and the

[00:31:00.120] definition of it just changes. So, the

[00:31:01.640] thing we're doing that Dex is showing

[00:31:03.080] you may very well be exactly what

[00:31:05.200] engineering is 5 years from now.

[00:31:07.680] There's no reason that it doesn't have

[00:31:09.560] to be. So, thinking of it as like kind

[00:31:11.800] of almost like an extension to what

[00:31:14.200] you're doing today and being like, "Oh,

[00:31:16.680] for some stuff I have to write C. If I

[00:31:18.400] want to invent NumPy even in Python, I

[00:31:20.200] have to write C. I might even have to

[00:31:21.560] write some assembly."

[00:31:23.480] But for most stuff I can write Python.

[00:31:25.160] Similarly, the stuff from here is for

[00:31:26.880] coding tasks or non-coding tasks

[00:31:29.240] you're really engineering whether you

[00:31:31.200] whether you call it that today or not.

[00:31:33.680] It's just what level of engineering are

[00:31:35.320] you doing?

[00:31:37.080] >> Yeah, and it's the conversation might

[00:31:38.520] not be like, "Hey, I'm going to go write

[00:31:40.480] C cuz the Python's." It's going to be

[00:31:41.760] like, "Okay, cool. Like, the LLM is not

[00:31:43.960] quite getting it right. I'm going to go

[00:31:45.520] write Python code because I need I need

[00:31:47.560] a certain level of quality or

[00:31:49.000] performance or accuracy for this one

[00:31:51.280] little part." And so, for that part we

[00:31:53.080] drop down out of the specifications and

[00:31:55.280] the words and the prompts and it's like,

[00:31:57.000] "Okay, this part I'm just going to do by

[00:31:58.120] hand cuz it has to be very very It's

[00:32:00.480] super imp- The leverage is like super

[00:32:02.320] impactful.

[00:32:04.720] Um but I will say on this like workflows

[00:32:06.520] versus agent stuff like what I will

[00:32:08.600] probably do once I get this to a

[00:32:10.320] satisfactory place, this workflow, is

[00:32:13.000] I'll probably just pop open and be like,

[00:32:15.040] "Great, turn this whole workflow into a

[00:32:18.680] TS script and tools/releases."

[00:32:27.070] Um and basically like once you figure

[00:32:27.080] out like tuning exactly and you get kind

[00:32:29.280] of the flow you want, you can have the

[00:32:31.680] model bake it as a workflow and then it

[00:32:33.520] becomes faster, more reliable, and it

[00:32:36.760] just is kind of like doing the so I

[00:32:38.560] mean, who knows how it's going to use

[00:32:40.360] the tools to do the summary? Like I

[00:32:42.400] probably have to prompt it to say like,

[00:32:43.800] "Okay, use my Anthropic API key and call

[00:32:45.800] Anthropic for these phases."

[00:32:48.120] Um but in general, if you can figure out

[00:32:50.080] the workflow and then you can pinpoint

[00:32:51.520] which parts of this are AI-driven, then

[00:32:53.840] you can make the deterministic parts

[00:32:55.320] deterministic, faster, don't spend

[00:32:57.000] tokens on them, don't wait for the model

[00:32:58.560] to figure it out because it's the same

[00:33:00.160] every single time.

[00:33:01.480] >> Can I show something related to that,

[00:33:03.520] Dexter?

[00:33:04.000] >> yeah. Go for it.

[00:33:05.120] >> Okay.

[00:33:05.800] So, this is again inspired heavily by

[00:33:08.240] what Dexter does. Let me just make sure

[00:33:09.880] that I'm

[00:33:11.240] Okay, I'll share my Obsidian cuz I can

[00:33:12.760] do that the safely. Um I wasn't sure

[00:33:15.040] what's on my desktop right now. So, I

[00:33:16.400] was like, "Let me Let me make sure it's

[00:33:17.720] safe." Um

[00:33:20.680] Um so, when you think about this stuff,

[00:33:22.920] for example, like one of the things that

[00:33:24.120] we do is we think really hard about

[00:33:27.080] We've been doing a new thing where we

[00:33:28.120] write design docs heavily using Claude,

[00:33:30.440] inspired by this thing.

[00:33:31.280] >> your Obsidian thing?

[00:33:32.920] >> Yeah. Um

[00:33:33.680] >> I've been waiting to see this. This is

[00:33:34.800] like, okay.

[00:33:35.520] >> So, we write all our design docs now

[00:33:37.280] through Claude.

[00:33:38.760] And it's very useful. And for example,

[00:33:41.480] one of the stuff that we're

[00:33:42.200] investigating right now is

[00:33:44.520] how is um actually this is a bad design

[00:33:47.600] doc cuz this is going to have too much

[00:33:49.000] context for people. But I will talk

[00:33:51.280] about this.

[00:33:52.920] Cool. So, one of the things that we'd

[00:33:54.480] love to add into BAML is discriminated

[00:33:56.280] unions. I would love for people to be

[00:33:58.160] able to write things like this so then

[00:33:59.600] they can actually get like really

[00:34:00.880] beautiful TypeScript classes that look

[00:34:02.320] like this automatically

[00:34:04.200] that actually have state and stuff

[00:34:05.840] attached to them. It's really hard to do

[00:34:07.440] naming

[00:34:08.480] for some reason.

[00:34:09.679] But part of doing this discriminated

[00:34:11.639] union stuff is sometimes at the top of

[00:34:14.520] every doc, I want it to go ahead and

[00:34:15.840] have like links to files and everything.

[00:34:17.360] And this is super abstract so I don't

[00:34:18.919] actually restrict it too much.

[00:34:20.760] But a lot more of the design docs I have

[00:34:22.360] I have a new prompt actually that I'm

[00:34:23.440] using. I actually want a summary

[00:34:26.240] of everything in here so I can quickly

[00:34:27.919] find stuff about like what branch was I

[00:34:29.440] working on, what was the date on this,

[00:34:31.440] who's the person that worked on this?

[00:34:33.080] And I don't do something very smart

[00:34:34.520] here. This is actually seven different

[00:34:36.280] API calls to Claude code cuz it runs

[00:34:38.080] like seven different commands to go

[00:34:39.200] assemble this.

[00:34:41.320] What I should be doing is I should have

[00:34:42.960] a script.

[00:34:44.320] >> Make a script that gets the metadata.

[00:34:45.639] Yeah, we did that. So we used to have it

[00:34:47.480] be four calls to Claude code and then

[00:34:48.840] we're like, "Okay, this is the same

[00:34:50.320] every time." And actually like the way

[00:34:52.000] that the bash works is that you have to

[00:34:53.760] pull in like you can't white list it in

[00:34:56.040] permissions because of how the high

[00:34:57.360] queue call evaluates your allowed

[00:34:59.080] policy. And so we were just like, "Okay,

[00:35:01.120] cool. We'll make a script and we'll

[00:35:02.440] allow this the script."

[00:35:05.200] >> Exactly. And by doing this, you can one,

[00:35:08.360] not only have your agents work faster

[00:35:09.880] cuz now instead of waiting for four

[00:35:11.040] calls to get this happen before all this

[00:35:13.240] dumps out.

[00:35:14.760] You used to one call.

[00:35:16.160] Um and it just pulls out all the data

[00:35:17.760] and go dumps it out immediately to the

[00:35:19.160] file.

[00:35:20.240] So one, you get expediency. One, you

[00:35:21.920] save a lot of money cuz remember the way

[00:35:23.600] that these the way that you get charged

[00:35:25.400] for all this stuff is by

[00:35:27.960] your context window. And if you're

[00:35:29.360] running four scripts with the same

[00:35:30.720] context window before writing the final

[00:35:32.240] document, one, two, three, four, your

[00:35:36.640] context window is being built to you

[00:35:38.040] four times to collect this data.

[00:35:39.920] So if you spend Well, part of it is

[00:35:40.960] cached, but

[00:35:43.080] it's still being built to you four times

[00:35:44.920] to build this data. Um and the way

[00:35:46.960] Claude code does the caching from what I

[00:35:48.480] understand is Claude has at most four

[00:35:50.360] caching segments built in.

[00:35:52.480] So at best you're getting a 4x uh

[00:35:54.480] reduction on parts of the window, but

[00:35:56.120] for really really large segments, you're

[00:35:57.440] not getting that much.

[00:35:58.880] >> And you're you're still always paying

[00:36:00.560] for the generation, right? The model has

[00:36:02.320] to say bash this, bash that, bash this

[00:36:05.080] thing over here. And so each one of

[00:36:07.040] those you're still paying for output

[00:36:08.440] tokens.

[00:36:09.440] >> Exactly. And this was if you go back and

[00:36:11.240] look at the Sorry. If you go back and

[00:36:13.000] look at the Now I'm going to throw out a

[00:36:14.040] different thing. Sweet agent tool chain,

[00:36:15.800] one of the best innovations they had was

[00:36:17.240] instead of giving the model super

[00:36:18.440] high-level tools like just bash. So for

[00:36:21.160] example, we could take Claude code's

[00:36:22.480] only tool is just bash.

[00:36:24.560] And it can do everything through your

[00:36:26.600] Problem is the model just works better

[00:36:28.640] if it can just run like read file

[00:36:32.280] instead of having to write the bash

[00:36:33.520] command for reading a file,

[00:36:35.640] read file with this line number instead

[00:36:37.480] of having to go write the bash command

[00:36:39.000] for reading this file with the line

[00:36:40.080] number or range.

[00:36:41.480] It just like reduces the amount of

[00:36:43.200] effort the model has to do and it can

[00:36:44.600] think at a higher level. And it's kind

[00:36:46.600] of like how when you do a design doc, if

[00:36:49.240] in the process of writing this design

[00:36:50.880] doc, I have to be like, here's the exact

[00:36:52.520] implementation of this at the same time

[00:36:54.280] of designing the system,

[00:36:56.320] my brain can't operate in that way. So,

[00:36:58.800] it's really useful for me to actually

[00:37:00.600] just write the design doc like, what is

[00:37:01.920] the end user going to see? What is the

[00:37:03.320] end user going to interface with? And

[00:37:05.400] only after that,

[00:37:07.160] go forward and then

[00:37:09.600] work on the implementation plan in some

[00:37:11.440] way or another.

[00:37:12.760] But it's

[00:37:13.560] the idea is you can break down the

[00:37:14.960] problem and similarly when you go do

[00:37:17.000] non-coding tasks, you want to think

[00:37:18.640] about it in the same way.

[00:37:20.160] What are the systems of the prompt that

[00:37:22.560] I can do in the very beginning that are

[00:37:24.520] super, super verbose and repetitive and

[00:37:27.400] perhaps have some ambiguity to them?

[00:37:30.680] And then eventually, I can apply an

[00:37:32.360] optimization function like if you were

[00:37:34.560] to optimize code, you'd make it faster

[00:37:36.320] and more reliable.

[00:37:37.960] Same thing. I can say, "Hey, I'm doing

[00:37:39.280] the same thing four times. This thing is

[00:37:40.880] very deterministic. Let's move to

[00:37:42.440] software 1.0 and write regular code to

[00:37:44.760] go solve this problem."

[00:37:46.400] And the rest of my system will still be

[00:37:47.680] software 3.0 which is more about LLM

[00:37:49.560] driven

[00:37:50.720] software.

[00:37:58.550] >> Super dope. Um

[00:37:58.560] should we see if our script I have a

[00:38:00.680] couple other things I can show off, but

[00:38:02.120] any questions so far? I really like

[00:38:03.640] Kyle's point on like Master has a good

[00:38:04.920] take on this. Agents and workflows need

[00:38:06.400] to be composable, right? A workflow can

[00:38:08.400] call agents, agents can call workflows.

[00:38:10.360] They're just kind of these different

[00:38:11.240] building blocks that can have like

[00:38:13.480] infinite depth if you want them to

[00:38:15.200] depending on the complexity of your

[00:38:16.400] problem.

[00:38:18.200] >> Um John asked the question of like has

[00:38:20.160] this been able to keep the code base

[00:38:21.320] consistent, coherent, and um coherent

[00:38:24.000] and consistent?

[00:38:25.240] Um

[00:38:27.040] I will not share with you what I said.

[00:38:29.720] I'll actually share with you what one of

[00:38:31.320] my engineers said because obviously I'm

[00:38:32.960] going to be biased in many different

[00:38:34.240] ways. Um

[00:38:36.280] So, I will share with you general

[00:38:38.840] And then that's going to And this

[00:38:39.840] technique, by the way, really, really

[00:38:41.120] inspired by

[00:38:42.680] actually I just showed you the DM.

[00:38:44.880] Um

[00:38:46.800] So, firstly, first thing while he's been

[00:38:49.240] doing this is Claude code doesn't read

[00:38:51.240] really large files. We have some really,

[00:38:52.640] really large files in our code base.

[00:38:54.560] His response

[00:38:55.880] immediately

[00:38:57.840] we need to optimize for this.

[00:38:59.840] So, he's like we should not have large

[00:39:01.360] files anymore. So, we'll probably add a

[00:39:02.880] linting rule in our code base to go

[00:39:04.240] solve this.

[00:39:05.720] Um

[00:39:07.840] Like it's just that good. And our code

[00:39:10.480] base is complex. We're building a

[00:39:11.600] compiler in Rust. It's not the easiest

[00:39:14.320] task for a language to go do.

[00:39:16.400] Um the model is really surprised at the

[00:39:18.000] fact that it works, but the most

[00:39:19.800] important part is actually

[00:39:22.000] I don't know if it's in here. We're

[00:39:23.600] discussing this for a while. The hardest

[00:39:25.080] part that actually turns out to be is

[00:39:27.240] 80% of it is just using it efficiently.

[00:39:29.520] The whole planning phase that we do, the

[00:39:31.000] research phase, that was heavily,

[00:39:32.400] heavily inspired by Dexter. I would have

[00:39:33.600] never thought about it. I didn't believe

[00:39:35.520] in Claude code to that degree. Like it

[00:39:37.520] works, but I didn't think it could do

[00:39:38.920] hard things.

[00:39:40.400] >> We just merged the PR today. Last

[00:39:42.400] Saturday, me and Vibhav sat down and I

[00:39:44.040] was trying to teach him this stuff and I

[00:39:45.720] was like, "Here's the prompts. Go try

[00:39:46.800] them for a thing." And after about 45

[00:39:48.600] minutes, I think Vibhav said, "I don't

[00:39:50.880] know if this is going to work for our

[00:39:51.640] code base. Like I already knew where

[00:39:52.920] this was. This would have taken me 15

[00:39:54.440] minutes. Like I don't think this is for

[00:39:56.360] us."

[00:39:57.400] And I said, "Okay, what do you want to

[00:39:58.320] do?" He's like, "Dex, how about you

[00:40:00.040] drive?" And And I was like, "Cool, I'll

[00:40:02.400] drive, but I want you to pick a really

[00:40:03.960] big, complex thing that we're going to

[00:40:06.160] work on cuz I want to prove to you that

[00:40:07.800] this works in big code bases." And we

[00:40:10.040] sat there for 7 hours

[00:40:12.600] and we coded two features. We added WASM

[00:40:14.760] support to BAML. So, now you can run it

[00:40:16.880] in the browser.

[00:40:17.680] >> Be very transparent. That one is not

[00:40:18.960] merged yet.

[00:40:19.840] >> I know. Well, yeah, neither of them got

[00:40:21.640] merged that day.

[00:40:22.400] >> No. The abort one

[00:40:24.560] >> The abortion one, the the abort

[00:40:26.280] controller one, uh adding cancellation

[00:40:28.600] to BAML got merged.

[00:40:30.600] Um which is like I think it was what,

[00:40:32.640] like 35,000 lines of code? And a lot of

[00:40:34.440] it was generated, but it was like a a

[00:40:36.720] crap ton of code that we wrote.

[00:40:38.520] >> Yeah. Um to give you context here, this

[00:40:41.120] whole process that we built, this

[00:40:43.280] problem was a very, very hard problem.

[00:40:45.760] We've had three people on our team

[00:40:47.040] trying to attempt it. They've spent four

[00:40:49.080] days each individually at different time

[00:40:50.960] periods of the BAML project.

[00:40:52.800] No one merged it. And there's reasons

[00:40:54.480] why it didn't merge or no one was able

[00:40:56.000] to solve it.

[00:40:57.480] But, what's interesting is that this

[00:40:59.320] technique allowed us to go and build

[00:41:00.760] this out and get it working demo in

[00:41:03.160] about 7 hours while in parallel doing

[00:41:06.320] some other really hard thing, which is

[00:41:07.920] web assembly support.

[00:41:09.600] And then we were actually able to go

[00:41:10.720] ahead and actually build playground

[00:41:12.520] support in our VS Code extension that

[00:41:14.720] actually allows you to cancel something

[00:41:15.960] while running. So, not only did we add

[00:41:17.640] it to the core runtime, so you as a

[00:41:19.040] TypeScript dev can just like abort a

[00:41:21.360] method that's running under the hood,

[00:41:23.560] but you can also cancel it in web

[00:41:24.760] assembly.

[00:41:25.960] And this project would have just never

[00:41:27.200] happened

[00:41:28.400] uh if it wasn't for Viper coding. So, it

[00:41:30.240] does work. That said,

[00:41:33.280] while it did produce almost the right

[00:41:35.080] code, it didn't produce what we call

[00:41:37.120] like clean code.

[00:41:39.040] So, while once we got it working, we had

[00:41:41.200] to go do something, which is we had to

[00:41:42.680] go ahead and issue some sort of react um

[00:41:46.960] uh some sort of

[00:41:48.400] um

[00:41:49.560] cleaning, I would say, along the hood,

[00:41:52.000] where we had to go and say like, "Hey,

[00:41:53.360] here you created some methods that don't

[00:41:55.040] need to exist. Use the existing methods

[00:41:56.680] instead."

[00:41:57.880] And don't extend the API interface. But,

[00:42:00.120] that was much, much easier to do

[00:42:02.600] once we had a working example and it

[00:42:04.600] worked end-to-end and it actually had

[00:42:06.200] unit tests and testability to just

[00:42:08.040] change the internal mechanisms to be

[00:42:10.120] more along the design we had.

[00:42:12.480] It's definitely 80% less work than it

[00:42:15.720] would have been otherwise. Like no doubt

[00:42:17.680] in my mind.

[00:42:19.000] >> Anyways, we're not here to talk about

[00:42:20.760] Claude for coding, but that was a great

[00:42:22.800] like little side tangent.

[00:42:24.920] Um

[00:42:25.800] What else do you think would be useful

[00:42:26.920] to talk about? I mean, I have more demos

[00:42:28.280] we can look at this daily review thing

[00:42:30.360] and see if it's running. So, it's like

[00:42:32.280] running our pull metrics script, which

[00:42:34.440] >> Yeah.

[00:42:34.880] >> is a thing.

[00:42:35.720] >> is running, I'll take a couple more

[00:42:37.120] questions. Someone Slava asked like, why

[00:42:38.760] not use a local database? I see one set

[00:42:40.320] of MD files. Well, Slava, the question

[00:42:43.040] is really just the same thing that we've

[00:42:44.080] talked about the whole time, which is

[00:42:45.200] it's an optimization spectrum.

[00:42:47.520] The V0, the most lossy form of this

[00:42:49.880] data, is a markdown file. If you find

[00:42:52.280] that, hey, we are scaling to thousands

[00:42:53.840] of people, you can optimize it to use a

[00:42:57.000] SQL database over time. But, the whole

[00:42:59.440] point of this is you don't have to on

[00:43:00.960] day one.

[00:43:05.310] Uh

[00:43:05.320] is it running yet, Dex?

[00:43:06.640] >> Yeah, so these are some of our tools.

[00:43:07.840] So, I showed the like make print context

[00:43:10.440] command, which shows, you know, the

[00:43:12.600] company overview, the recent investor

[00:43:14.520] updates. This is how you can kind of

[00:43:15.960] deterministically pack your context

[00:43:18.360] without Claude needing to go to Again,

[00:43:19.840] the same thing that you mentioned about

[00:43:21.000] like, hey, rather than like doing this,

[00:43:23.640] we just do it all as a script. Same

[00:43:25.200] idea. It's like if I know that every

[00:43:26.680] time this thing runs, I want it to have

[00:43:28.720] all this context, and I don't want to

[00:43:30.120] put it all in Claude.md for whatever

[00:43:31.600] reason, because sometimes I might not.

[00:43:33.040] But, it's like 90% of workflows I'm

[00:43:34.880] going to tell it to call the like make

[00:43:36.680] print context print index things. And

[00:43:39.480] then we actually use something called

[00:43:40.760] like ctx.md,

[00:43:42.680] which is like run make print context

[00:43:51.590] make run make print index

[00:43:51.600] follow the user's ask.

[00:43:54.400] And so, now I can say,

[00:43:56.800] um

[00:44:01.870] /ctx

[00:44:01.880] what's the last investor update? And it

[00:44:06.080] will get all this context automatically

[00:44:09.320] without having to go read a bunch of

[00:44:11.320] files. So if there's stuff you always

[00:44:12.680] want to know and this gets back into

[00:44:13.720] context engineering, right? Because if

[00:44:14.880] you just put everything in, then you

[00:44:17.080] were going to take up too much of the

[00:44:18.080] context window and you're going to

[00:44:19.200] distract it and there's going to be

[00:44:20.480] flows and things like this. But this is

[00:44:22.400] kind of a hopefully this technique is

[00:44:24.480] clear of how you could basically give

[00:44:27.080] the model access to or you can kind of

[00:44:29.240] like streamline your workflows and just

[00:44:30.840] kind of guarantee that the model will

[00:44:32.320] always

[00:44:34.120] have kind of the core base context. And

[00:44:36.840] the reason why we don't use Claude MD

[00:44:37.880] for this is because what we talked about

[00:44:39.080] 2 weeks ago is if you look in the Claude

[00:44:41.240] code system prompt, it does inject

[00:44:42.920] Claude MD, but it says a system

[00:44:46.320] instruction at the end because most

[00:44:47.760] people don't know how to write a good

[00:44:48.840] Claude MD because they're not context

[00:44:50.160] engineers. They or they're they're

[00:44:52.360] they're aspiring context engineers. They

[00:44:54.080] got to they got to figure figure out

[00:44:55.720] like learn this stuff is it says this

[00:44:57.960] may not be relevant. Only consider this

[00:45:00.040] advice if it's highly relevant to what

[00:45:01.600] you're working on. And so if you want to

[00:45:03.240] guarantee stuff ends up in the context

[00:45:05.080] window in a way that is sort of

[00:45:07.320] will get more attention from the model,

[00:45:10.880] then you can be a little bit more

[00:45:12.040] deterministic about how this works.

[00:45:14.280] >> Yeah. And I think you asked interesting

[00:45:16.360] question of like how do you deal with it

[00:45:17.560] if you have a long-running task that

[00:45:19.280] Claude needs to go run

[00:45:21.360] and you want to take a dependency on it

[00:45:22.600] in a future task. Well, this really goes

[00:45:25.040] back to like you as a user need to

[00:45:27.320] understand the restrictions of the agent

[00:45:29.400] that you are using.

[00:45:30.840] Claude code doesn't really have a way to

[00:45:32.520] add dependencies on background tasks.

[00:45:34.680] There's nothing you as a user can do

[00:45:37.360] to really make that work super super

[00:45:39.520] reliably. Claude code lets you run a

[00:45:41.640] background task but it doesn't let you

[00:45:42.800] depend on that background task for some

[00:45:44.320] other task.

[00:45:45.640] So until the agent builder enables that

[00:45:47.480] capability, you can't do it.

[00:45:49.360] So

[00:45:50.400] sadly, that's just like understanding

[00:45:52.120] what the limits and stuff are. And if

[00:45:54.040] you really need that because your

[00:45:55.240] workflow is constantly like that, well

[00:45:56.960] then

[00:45:58.000] you'll have to build your own agent

[00:45:59.040] loop. And that actually builds that in

[00:46:02.160] as a mechanism for what the system does.

[00:46:05.640] And the reason for that is because if

[00:46:07.040] you're running a background task and you

[00:46:08.080] want to put the pency on it, then

[00:46:09.360] whatever system task you're using has to

[00:46:11.360] have context on here's all the

[00:46:12.880] background task that I'm currently

[00:46:13.960] running.

[00:46:15.320] And therefore, here's how you go build

[00:46:17.680] this out.

[00:46:19.120] Under the hood.

[00:46:19.640] >> Um, lot of questions about the Claude

[00:46:21.720] code system prompt. We did uh, I think

[00:46:25.040] we dropped a snippet of it in the last

[00:46:28.000] AI that works.

[00:46:30.160] Or the one where we talked about Claude.

[00:46:31.920] Oh, not that.

[00:46:39.390] Let's just have a look at the whole

[00:46:39.400] repo. So,

[00:46:41.400] context engineering for coding agents, I

[00:46:43.960] believe it was.

[00:46:46.520] Eh, no, that's context engineering.

[00:46:53.030] There is

[00:46:53.040] >> Um, you can definitely see the system

[00:46:54.560] prompt of Claude code because under the

[00:46:56.040] hood it's just making a network call.

[00:46:58.000] Uh, and you can just like proxy it and

[00:46:59.680] then you can see the prompt.

[00:47:01.840] >> Um,

[00:47:03.000] >> You have it somewhere right here.

[00:47:04.440] >> Yeah, here's the trace. So, this is you

[00:47:06.160] can literally just point Claude at a

[00:47:07.440] proxy and have it log everything out and

[00:47:09.200] then send this the the the request

[00:47:11.080] upstream to Anthropic. This is what a

[00:47:13.120] lot of people doing. But like, yeah,

[00:47:15.040] here's our user message.

[00:47:17.200] As you answer the user's questions, you

[00:47:18.480] can kind of see all of this and it says

[00:47:22.160] Here it is. Important, this context may

[00:47:24.080] or may not be relevant to your task. You

[00:47:25.600] should not respond to this context or

[00:47:26.920] otherwise consider it in your response

[00:47:28.680] unless it is highly relevant to your

[00:47:29.960] task. So, every time you put something

[00:47:31.520] in Claude MD, it gets suffixed with

[00:47:34.040] this. Most of the time it is not

[00:47:35.880] relevant.

[00:47:37.240] >> So, that means if you are trying to tell

[00:47:39.360] it to do something in Claude MD, like

[00:47:40.800] this is really important,

[00:47:42.520] and

[00:47:43.360] it my model might decide that it's not

[00:47:45.360] important because this is just part of

[00:47:47.200] the context window that the Claude agent

[00:47:49.360] does no matter what you do. And there's

[00:47:50.840] nothing you can do to edit this except

[00:47:52.760] have a proxy and remove that manually

[00:47:55.120] from the prompt in your proxy layer.

[00:47:58.080] >> And this is the engineering part, right?

[00:47:59.240] This is about if you don't know exactly

[00:48:01.400] what's put in, if you don't know the

[00:48:03.480] tool descriptions, if you don't know

[00:48:06.000] kind of how Claude is being talked So,

[00:48:07.960] here's the raw body, but we can actually

[00:48:09.360] go get the JSON.

[00:48:11.200] Um so, here's yeah, here's the system

[00:48:12.960] message. Here's the

[00:48:15.640] um

[00:48:17.400] Here's the tool. So, here's the task

[00:48:18.760] tool. People talk about sub-agents.

[00:48:19.840] Here's the prompt for the sub-agent.

[00:48:22.000] Launch a new agent that has access to

[00:48:23.280] all the tools when you're searching for

[00:48:25.040] a keyword that you're not confident. So,

[00:48:26.720] this is like understanding how this the

[00:48:29.680] tool the task tool is exposed to Claude

[00:48:32.880] is really important for when you're

[00:48:34.680] prompting it. And so, I don't say launch

[00:48:36.040] a sub-agent, I say launch a task because

[00:48:37.960] that's more likely to have the right

[00:48:39.000] effect. And when I tell it to launch a

[00:48:40.760] task, I tell it to put in the dis- in

[00:48:43.360] the prompt how to prompt the agent

[00:48:46.280] because I want to get more clear

[00:48:48.400] specific things out of that sub-agent.

[00:48:52.040] I don't know if that answers the

[00:48:52.760] question.

[00:48:59.390] >> No, I think that does that.

[00:48:59.400] Um Richard asked a really interesting

[00:49:00.880] question about hey, makes me think that

[00:49:02.400] an IDE had a window for

[00:49:03.920] deterministically managing context

[00:49:05.360] windows, that'd be super useful.

[00:49:07.320] I think today that would probably be

[00:49:09.600] true. I think tomorrow it won't matter.

[00:49:12.320] And the same realization I think is with

[00:49:14.560] Python. I think a lot of people used to

[00:49:16.360] say that in Python if you if you're not

[00:49:18.440] garbage collecting automatically or at

[00:49:20.280] the right time and you can't manually

[00:49:21.840] control it, you can't write good code.

[00:49:24.320] Doesn't matter today.

[00:49:25.960] And I think as the models get better,

[00:49:28.000] like deterministically managing every

[00:49:29.840] single word matters less and less. If

[00:49:31.680] you're using a 1B model, it does matter.

[00:49:33.200] You do really need to manage every

[00:49:34.600] single word that goes in.

[00:49:36.600] But if you're not, it honestly, if

[00:49:38.680] you're using the latest models today,

[00:49:40.640] I suspect what you need as a user need

[00:49:42.160] to do is just like manage the sections

[00:49:44.080] of context, not necessarily every single

[00:49:45.920] word to that degree.

[00:49:48.800] Um and there's probably some usefulness

[00:49:51.120] because even as an agent developer,

[00:49:53.600] like

[00:49:54.680] I would have never I have never actually

[00:49:56.600] read the research and um

[00:50:00.120] I've never actually read the research

[00:50:01.640] prompts that Dasha gave me. I've never

[00:50:03.160] read the create plan prompts that Dasha

[00:50:04.640] gave me. I've never read the ones it

[00:50:05.960] gave me. And they work. And the whole

[00:50:08.320] point here is that if they didn't work,

[00:50:10.800] I would go read the prompt.

[00:50:13.080] And you can think of it like how you

[00:50:14.600] would debug as an engineer.

[00:50:16.640] Like if something works, you don't

[00:50:18.040] really care what the API does under the

[00:50:19.400] hood. You don't care how much of a black

[00:50:20.960] box it is. Same with context

[00:50:22.720] engineering. Thing is working, don't

[00:50:24.440] bother understanding it. The model's

[00:50:25.800] good enough, it's working. The minute it

[00:50:27.520] stops working, go figure out why.

[00:50:30.440] >> Yeah, I've never read the source code of

[00:50:31.960] the cat command and I have no no reason

[00:50:35.320] to or desire to, cuz the API is clean

[00:50:37.440] and it always does what it says.

[00:50:39.320] >> Exactly.

[00:50:40.640] And I think that's really what context

[00:50:42.240] engineering is about is like you don't

[00:50:43.840] you can when we did the performance

[00:50:45.480] engineering for last 10 years, whenever

[00:50:46.800] I did that,

[00:50:48.160] every line of code that you write, I

[00:50:49.520] promise you there's some way to make it

[00:50:51.240] faster. Almost definitely. There's

[00:50:53.400] something you can do to make it faster.

[00:50:56.440] You don't need to.

[00:50:57.720] The value of performance engineering is

[00:50:59.200] not about making every line of code

[00:51:00.960] faster. It's actually about knowing what

[00:51:02.760] lines of code to spend your effort on,

[00:51:04.160] so you can make that part of the system

[00:51:05.560] faster. Same with context engineering.

[00:51:08.240] Don't make every single system perfectly

[00:51:10.520] engineered. Focus on the parts of the

[00:51:12.400] system that actually need to be

[00:51:13.680] perfectly engineered. So in this

[00:51:15.280] workflow that we did today,

[00:51:17.320] Dasha really didn't have to optimize a

[00:51:18.760] lot of this stuff.

[00:51:20.160] Because

[00:51:21.400] like it works. It does the thing it

[00:51:23.000] wants. Doesn't matter how expensive it

[00:51:24.520] is. And most of the stuff that he's

[00:51:26.080] doing is

[00:51:27.240] allowed to be lossy.

[00:51:29.440] >> It's allowed to be lossy and it's the

[00:51:30.560] kind of thing that like without a lot of

[00:51:31.880] prompting, the model can still get it

[00:51:33.280] right.

[00:51:34.000] >> Yeah, or at least 85% right. And for the

[00:51:36.240] task that you're doing, it doesn't

[00:51:37.280] matter if it's 100% right. It just needs

[00:51:38.720] to be

[00:51:39.840] directionally correct. Like change logs

[00:51:42.400] or contact conversations. Like here's

[00:51:44.560] the last thing you talked about, and bye

[00:51:45.680] bye.

[00:51:46.640] Like none of that stuff needs to be

[00:51:48.080] perfect or capture every single word of

[00:51:49.800] it.

[00:51:54.670] >> Yeah. And and the the reason why it

[00:51:54.680] doesn't have to be perfect is like when

[00:51:55.960] I build this stuff, I work backwards

[00:51:57.320] from the workflows, which is like what's

[00:51:58.840] the end goal is like I want to send my

[00:52:01.480] team an update every week. I want to

[00:52:03.280] send my investors an update every month.

[00:52:05.320] I want to send a public update to our

[00:52:07.000] mailing list every month. And I want to

[00:52:08.840] send our like trusted testers good

[00:52:10.480] release notes that are high signal and

[00:52:12.120] high quality every morning. Um or every

[00:52:14.480] couple days. But mostly every morning

[00:52:16.280] cuz we're shipping too much to do two

[00:52:17.720] releases in a day.

[00:52:19.920] >> Yeah.

[00:52:21.320] Um

[00:52:22.440] we'll take a couple questions and then

[00:52:24.480] I've got a flight to Amsterdam. So we're

[00:52:25.920] going to we're going to probably cut it

[00:52:28.240] a little bit shorter than normal. If you

[00:52:30.040] guys haven't seen the Code Lair tool, um

[00:52:32.800] that sure will drop a link.

[00:52:34.520] It is the coolest thing that I have used

[00:52:37.400] for paralyzing how much code I can get

[00:52:40.040] done

[00:52:41.120] at any given time. I have I consider

[00:52:43.400] myself a pretty good engineer, but I

[00:52:45.240] realized that I was a novice before I

[00:52:46.800] used this thing and now I use it and I'm

[00:52:48.360] so much better than I used to be. And I

[00:52:49.840] think I aspire to be as good as Dexter.

[00:52:52.160] Uh

[00:52:52.640] >> Thanks, buddy.

[00:52:54.120] >> Uh check it out. If you're not using it,

[00:52:56.200] uh definitely check it out. Give Dexter

[00:52:57.520] some feedback.

[00:52:58.680] >> Yep. There's a wait list there. I just

[00:52:59.960] put the link in. We'll put it in the

[00:53:01.040] show notes. Um

[00:53:03.000] uh you can go find it on GitHub and use

[00:53:05.760] the brew install command. I am asking

[00:53:08.320] early users to jump on the wait list so

[00:53:11.000] that I can watch you use it for the

[00:53:12.240] first time and get your feedback and get

[00:53:14.160] you added to some of our like private

[00:53:15.920] testing channels.

[00:53:17.320] That'll probably be true for another

[00:53:18.480] couple weeks as we iron out the last of

[00:53:20.240] the stability things and really pull in

[00:53:22.200] user feedback. So yes, technically you

[00:53:24.320] can go find it, but I would prefer to

[00:53:26.480] onboard you uh directly. And so we're

[00:53:28.760] going to start letting people in off the

[00:53:29.720] wait list pretty soon. Uh so uh I can't

[00:53:32.840] stop you cuz it's free and open source

[00:53:34.360] forever and you can just go find the

[00:53:35.760] release, but if you want to help out,

[00:53:39.000] you can join the wait list and you can

[00:53:40.360] get added to the group DMs with Vybhav

[00:53:42.880] and some of the cool people who are

[00:53:44.400] early testers.

[00:53:45.560] >> And definitely just like if you really

[00:53:47.320] want to skip the list, just like add us

[00:53:49.240] a DM on Discord or something and you'll

[00:53:52.560] get through much faster.

[00:53:54.640] Um and that'll be the easiest way.

[00:53:57.800] >> Cool. Questions?

[00:54:04.350] >> Would be

[00:54:04.360] That's would have same sense of

[00:54:09.120] >> Any other questions right now, everyone?

[00:54:10.760] Uh it sounds like

[00:54:12.120] not too many.

[00:54:19.350] >> Uh do you think the domain of tasks that

[00:54:19.360] can be achieved with this approach is

[00:54:20.640] going to keep growing? Will we hit some

[00:54:21.960] point where humans don't even determine

[00:54:23.480] the SOPs and communication strategies?

[00:54:27.200] >> Um

[00:54:28.880] My opinion is honestly, I think it's

[00:54:30.520] like software. Yes, like yes.

[00:54:33.640] Inevitably so. And not just because the

[00:54:35.200] models will get better. I think even if

[00:54:36.480] the models don't get better, like the

[00:54:38.320] agentic loops that we write write you

[00:54:40.680] that we use to leverage the models will

[00:54:42.320] get better and the tooling around them

[00:54:44.000] will get better. So like it's an

[00:54:45.480] inevitability. Like even if Python

[00:54:47.800] doesn't like change fundamentally

[00:54:49.680] architecturally,

[00:54:51.280] the libraries people build make it more

[00:54:53.320] usable every week, every day.

[00:54:55.680] Um when we built Bammel like part of

[00:54:57.840] Bammel on day one was definitely worse,

[00:54:59.320] but like we just add more stuff into it

[00:55:01.000] so people can build more complicated

[00:55:02.480] things. Like that's just the way

[00:55:03.920] software works. So anything that is pure

[00:55:06.240] bits on a machine, generally bits moving

[00:55:08.200] around on a machine generally gets

[00:55:09.280] better over time and the capabilities

[00:55:11.360] over time. As long as people give great

[00:55:12.720] feedback

[00:55:13.840] and leverage it further.

[00:55:16.560] >> Uh Richard, great question. Is project

[00:55:18.400] management software going away? Project

[00:55:20.600] management software is the only SaaS we

[00:55:22.560] still use every day. Um that's funny.

[00:55:25.920] That and Superhuman. Uh so it's things

[00:55:28.800] like GitHub and Linear we still use

[00:55:30.400] because it provides a nice collaboration

[00:55:32.160] space and shared artifacts. It's a

[00:55:34.240] little bit harder to do with just like

[00:55:37.120] markdown files in GitHub when you want

[00:55:38.760] to have lots of comments and multiplayer

[00:55:40.480] and attach assets and things like that.

[00:55:42.080] Although Vibhav, I don't know, I have to

[00:55:43.440] try your Obsidian workflow cuz if you

[00:55:45.040] could create a shared Obsidian space,

[00:55:46.520] maybe you can just drop everything in

[00:55:47.840] markdown and it's not that much more

[00:55:49.760] efficient than having the model fetch

[00:55:51.040] the stuff, but like

[00:55:52.760] I don't like the linear MCP because it

[00:55:54.760] dumps a bunch of JSON into my context

[00:55:56.480] window. So we wrote a script that wraps

[00:55:58.040] it and pulls all the comments in one go.

[00:56:00.360] >> Yeah, exactly. And that's again because

[00:56:01.640] the linear team doesn't understand

[00:56:02.600] context engineering, so they're doing

[00:56:03.800] dumb things with it. And they're just

[00:56:05.600] giving you stuff in a way that doesn't

[00:56:07.160] make sense that you know how to do

[00:56:08.600] better.

[00:56:09.760] So you're like, I can get way better

[00:56:11.120] juice if I don't use it directly.

[00:56:13.160] Um I also agree with like I think people

[00:56:15.040] always are like, "Ah, cloud code is

[00:56:16.360] going to do everything." I actually

[00:56:17.120] think that's wrong. Um I think the best

[00:56:19.600] way to think about it is like we don't

[00:56:20.800] have one website to rule them all.

[00:56:22.920] We have a ton of different websites that

[00:56:24.240] we all go to that do slightly different

[00:56:25.560] things.

[00:56:26.560] Uh and I don't see that ever really

[00:56:28.560] changing. We'll have different tools

[00:56:29.600] that we use all the time.

[00:56:31.560] Uh

[00:56:32.240] tools are just a natural way of humans

[00:56:35.280] interfacing data and people have

[00:56:36.880] different patterns and different UIs

[00:56:38.120] that they like.

[00:56:40.400] Um

[00:56:41.920] Yeah, Dexter's comment about what

[00:56:43.280] strategies you use to keep keep context

[00:56:44.760] from getting uh too big.

[00:56:47.160] Always be compacting. Whether you're

[00:56:48.720] using {slash} compact in cloud code,

[00:56:50.480] whether you're using manual compactions

[00:56:52.120] like what Dexter and I do with research

[00:56:53.600] and planning, the idea is you want to

[00:56:55.440] have some sort of state system that

[00:56:57.040] isn't the chat log itself.

[00:56:59.280] And you want to be able to review that,

[00:57:00.920] read that, understand that, which is why

[00:57:02.640] I personally have found Dexter's way of

[00:57:04.520] having a file as a source of truth that

[00:57:07.480] I can just go read at any point to be

[00:57:09.320] extremely powerful because whenever the

[00:57:11.360] agent does steer off, I can restart the

[00:57:13.480] context, feed in that file, and then

[00:57:15.920] boom, I'm done.

[00:57:17.480] >> Yeah, I actually almost wrote always be

[00:57:19.120] clearing because clear is actually what

[00:57:21.120] we use. We don't use the {slash}

[00:57:22.400] compact. So when I say compact, it's

[00:57:24.120] little C compact, which is like find

[00:57:26.520] your own way to squeeze down the context

[00:57:28.720] into the things that are important to

[00:57:30.200] you. Not And whether the cloud way works

[00:57:32.600] well for you, that's great, but what we

[00:57:34.320] have is kind of custom prompts that are

[00:57:35.720] like, "Cool, make a list of every file

[00:57:37.880] you touched and snippets of all the

[00:57:39.320] changes you made and what you were

[00:57:40.680] working on and what's currently broken

[00:57:42.080] and what are the next steps." And that

[00:57:43.440] works. Having that write that to a

[00:57:44.640] markdown file, then you can edit it, you

[00:57:46.360] can see it, you can control it, you can

[00:57:47.920] learn how to get better at that

[00:57:48.840] prompting.

[00:57:50.240] Um is a really powerful skill and is

[00:57:51.960] again, it's all about context

[00:57:52.960] engineering. How do you take a bunch of

[00:57:55.000] information and distill it down into

[00:57:56.640] fewer tokens that are just as valuable

[00:57:58.440] to the model.

[00:57:59.600] >> Um you asked a question, what do you

[00:58:01.000] think about the role of MCP over time? I

[00:58:02.640] think we just stated it with Dexter

[00:58:04.280] being like the linear MCP does a dumb

[00:58:06.120] thing, so I just wrapped it and actually

[00:58:07.440] made it do the right thing. MCPs are

[00:58:09.360] just API calls.

[00:58:11.480] If the API caller knows what they're

[00:58:13.640] doing, it's a

[00:58:14.960] API calls are good to use.

[00:58:16.600] If you're using it as a dumping ground

[00:58:17.800] to just have it do a lot of things, your

[00:58:19.320] agent probably won't work cuz 90% of the

[00:58:21.040] tools that people build probably are

[00:58:22.720] built incorrectly because most people

[00:58:24.480] are not on the bleeding edge of actually

[00:58:26.400] thinking about context engineering. And

[00:58:27.840] if you are,

[00:58:29.280] you're being held back. It's just where

[00:58:31.040] you think the median is versus where you

[00:58:32.680] are.

[00:58:33.720] And the median right now is pretty bad.

[00:58:36.480] >> Aw.

[00:58:37.520] >> Um

[00:58:38.000] >> Let's make it better. I mean, that's why

[00:58:39.120] we're here, right?

[00:58:39.920] >> why we're here. Yeah, we want to lift it

[00:58:41.360] up.

[00:58:42.440] >> John says, "This is the kind of stuff

[00:58:43.680] people will sell courses on in 18

[00:58:45.120] months. We should get a CC by and A so

[00:58:47.480] that people can't sell our shit."

[00:58:49.560] >> That's right. I don't really care. I

[00:58:52.040] think the best kind of education is

[00:58:53.280] given out for free and that's what all

[00:58:54.640] good content is.

[00:58:56.280] Um why not take over the user's content

[00:58:57.920] completely by dynamically generating

[00:58:59.520] them before each agent

[00:59:01.560] um execution?

[00:59:03.280] I think that's a thing that you can do,

[00:59:04.640] Slava, but really it goes down to again

[00:59:07.080] the same point, which is

[00:59:09.240] if you're going to go ahead and take

[00:59:10.600] over the user's context completely, you

[00:59:12.440] better hope that your users are real

[00:59:14.760] novices cuz they're advanced users, they

[00:59:16.680] will not be okay with that. They'll be

[00:59:18.320] like, "Dexter, I'm like, this thing

[00:59:19.400] isn't working cuz I'm trying to have it

[00:59:20.760] something do something much more

[00:59:22.440] complicated than what you planned to to

[00:59:24.280] have it do."

[00:59:25.200] >> This is something else I'm saying. This

[00:59:26.920] is show me the prompt.

[00:59:28.760] >> Exactly. It says it's show me the

[00:59:30.200] prompt. And the whole point is like by

[00:59:32.400] taking over the user's context

[00:59:34.480] completely, while you do lift the floor

[00:59:36.800] a little bit,

[00:59:38.000] the thing that you don't do is you

[00:59:40.440] actually bring down the ceiling a lot.

[00:59:42.920] >> Yep.

[00:59:43.320] >> So, it's a trade-off of what you're able

[00:59:45.520] to go build. And if you're okay bringing

[00:59:47.960] out the ceiling cuz the usability of

[00:59:49.480] what people want is very low, it's okay.

[00:59:51.800] That's what that's totally useful.

[00:59:53.840] Generating release notes seems like one

[00:59:55.480] of those things where you can bring down

[00:59:56.440] the ceiling a lot and just make your

[00:59:58.120] users' life a lot better by bringing

[00:59:59.480] down the floor bringing up the floor.

[01:00:01.800] But, if it's something like generating

[01:00:03.000] arbitrary code in cloud code, you

[01:00:04.840] probably don't want that. And cloud code

[01:00:06.440] works best because Dexter can put in

[01:00:08.080] whatever he wants into the context and

[01:00:09.560] know what have it do roughly the right

[01:00:10.920] thing.

[01:00:14.350] >> Dex.

[01:00:14.360] >> Um let's take one or two more questions.

[01:00:17.160] Um are those here I mean that Yeah,

[01:00:19.520] we'll push the code out soon. I think we

[01:00:21.240] should Do you want to push the research

[01:00:22.480] and prompts out, too? Or we can do that

[01:00:24.960] in a different episode, actually. We

[01:00:25.920] should do that later. I think that's

[01:00:27.520] >> Yeah, no. I mean, we should do another

[01:00:28.520] episode where you walk through your

[01:00:30.000] Obsidian flow. Like really in practice,

[01:00:32.120] how does it work? How do people interact

[01:00:33.640] with it? What's your workflow? Um I

[01:00:35.680] think that'd be really interesting. Um

[01:00:37.280] >> Yeah, we'll share the prompts out then

[01:00:38.520] once we tune them a little bit. Um and

[01:00:40.960] then let's just see if there's any more

[01:00:42.360] questions.

[01:00:47.910] Um Kyle, the GraphQL will never be the

[01:00:47.920] answer. It never was. It never will be.

[01:00:50.240] Um good try, though. Um

[01:00:53.680] and I think um

[01:00:57.560] I think that is it from questions.

[01:01:00.640] >> Excellent.

[01:01:01.200] >> Um all right. Thank you everyone for

[01:01:03.080] joining. Um we'll see you again next

[01:01:04.960] week. I will be in the middle of the day

[01:01:06.840] at Germany time, so we'll see how well

[01:01:08.640] that goes. Uh but uh we'll have a fun

[01:01:11.360] time and we'll get a couple more bits of

[01:01:13.040] episode out and content out.

[01:01:15.360] >> Awesome. All right. Bye-bye, everyone.

[01:01:17.640] >> Always good seeing you, Dex. All right.

[01:01:19.360] >> all later.
