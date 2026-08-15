# Dynamic Schemas



Source: YouTube captions (automatic:en)



[00:00:01.270] What's up?

[00:00:01.280] >> Hello. Hello. Hello.

[00:00:03.880] Um give me a second. I'm going to do one

[00:00:05.760] last thing and just post it over on

[00:00:07.120] general and then we'll be good good to

[00:00:08.880] go.

[00:00:09.600] >> Will you post it in my Discord, too? I'm

[00:00:11.840] lazy.

[00:00:13.200] >> AI that works today. Dynamic schemas.

[00:00:16.960] Send now and then I'll post a great

[00:00:19.720] thread. Boom. I hope that is the guest

[00:00:21.960] invite link and not the other link. Let

[00:00:24.440] me delete this real fast. Delete.

[00:00:27.120] I think I sent the wrong link.

[00:00:29.000] Uh people and then let me send

[00:00:31.600] invite.

[00:00:33.200] Yep. I definitely sent the wrong link.

[00:00:34.960] Audience copy.

[00:00:39.030] Um

[00:00:39.040] >> Did you invite them all to be co-hosts?

[00:00:41.120] >> Uh I did. I did. I went to

[00:00:46.870] Um do you want to do you want to go post

[00:00:46.880] in your the Human Layer Discord as well?

[00:00:48.880] >> Um yeah. Did you update the link?

[00:00:50.680] >> I did. Um

[00:00:53.160] you should all see it.

[00:00:54.640] All right. Um with that, uh welcome

[00:00:57.040] everyone. Today we are going to do an

[00:00:59.600] episode that I am very very excited to

[00:01:02.360] go do, which is all about how to do

[00:01:05.280] dynamic UIs.

[00:01:07.280] And how do we build dynamic um

[00:01:09.880] systems where we sometimes don't know

[00:01:12.560] what the model is going to go do. So,

[00:01:14.720] we'll give it a couple minutes and then

[00:01:16.360] we'll start in um

[00:01:18.400] we'll start pretty soon.

[00:01:19.640] >> Amazing. We need to get some like filler

[00:01:21.720] like uh background music for the for the

[00:01:24.200] lobby vibes.

[00:01:25.000] >> do. Um yeah. Let me put something up on

[00:01:26.480] up.

[00:01:28.000] Boom.

[00:01:28.440] >> Get Suno to do like a techno Mortal

[00:01:31.280] Kombat theme.

[00:01:33.000] >> Uh dude, I

[00:01:35.360] this is uh music is sadly not my domain.

[00:01:38.080] So, we'll have to figure out how to get

[00:01:39.280] that going for you actually because I I

[00:01:41.600] have no idea how to pick the right songs

[00:01:43.440] or anything.

[00:01:44.560] >> Well, no. You just have AI generate it,

[00:01:46.480] dude.

[00:01:47.440] >> Oh, maybe. When we were making the

[00:01:48.920] YouTube videos at first, um

[00:01:51.480] uh for our team, my team I started

[00:01:53.360] adding music everywhere and my team was

[00:01:54.600] just like, "No. Stop."

[00:01:55.920] >> No. No music.

[00:01:58.440] >> Okay. we got some we got some MK fans.

[00:02:01.280] Oh yeah, we could put on the Skyrim

[00:02:02.560] loading scene. That would actually be uh

[00:02:05.560] Someone was talking, I saw on Twitter

[00:02:06.840] someone was posting like

[00:02:08.520] uh

[00:02:09.640] the uh Claude uh like while it's

[00:02:12.000] thinking or waiting or whatever it is,

[00:02:13.880] just showing the Skyrim loading loading

[00:02:16.000] art while you're waiting for Opus to

[00:02:17.560] load go take a long time to do whatever

[00:02:19.320] it's doing.

[00:02:21.080] I don't want to show this for like a

[00:02:22.040] minute.

[00:02:23.160] Uh 20 seconds.

[00:02:24.720] I mean

[00:02:25.480] >> Yeah, I think one of Also, what's

[00:02:27.200] interesting this week is we didn't send

[00:02:28.440] the Luma out this week uh because I was

[00:02:30.640] slammed for reasons I will say later.

[00:02:33.120] >> But I Bob has some fun news coming.

[00:02:35.400] >> Yeah, but it it'll be interesting to see

[00:02:38.400] how many people actually go with Luma.

[00:02:40.640] It sounds like it's a

[00:02:42.840] uh it sounds like it's definitely a

[00:02:44.360] thing they'll have to do more regularly.

[00:02:46.760] >> Amazing. All right, um we're it's 10:05.

[00:02:49.560] Let's get started. This is AI that

[00:02:51.600] works, the show where we teach you how

[00:02:53.200] to take AI from demo and uh you know,

[00:02:57.440] toy examples and build things that are

[00:02:59.680] actually production grade that work in

[00:03:01.400] the wild. I'm Dex, I'm the founder of a

[00:03:03.120] company called Human Layer and we got

[00:03:05.320] Vibhav here. I'll let him introduce

[00:03:06.640] himself.

[00:03:07.959] >> I'm the founder of a company that builds

[00:03:09.519] Bambo.

[00:03:10.000] >> And today, you want to tell people what

[00:03:11.840] we're talking about today?

[00:03:13.320] >> Yeah, um

[00:03:14.680] I'm going to start off with just showing

[00:03:15.880] a demo that I've shown many, many times

[00:03:17.800] that many of you may have seen before.

[00:03:19.880] But I I think one of the most important

[00:03:22.880] things that becomes possible with LLMs

[00:03:26.040] is something that I find uh personally

[00:03:28.440] very interesting, which is

[00:03:30.360] dynamic UIs. How do we deal with schemas

[00:03:33.360] that are totally dynamic, runtime

[00:03:35.320] defined, and we don't even know the data

[00:03:37.440] that's coming in?

[00:03:38.760] So, many of you have probably seen for

[00:03:41.600] example, this uh invoice processor where

[00:03:44.400] we ask a model to look at this PDF.

[00:03:47.239] And when it looks at the PDF, it just

[00:03:49.280] looks at it, comes up with a schema that

[00:03:51.200] models this PDF. Um if we run that

[00:03:53.760] schema through an LLM, we can even get a

[00:03:56.240] really good response coming out of it in

[00:03:58.560] a way that I think is way more helpful.

[00:04:01.240] Then

[00:04:01.880] >> this is actually generating dynamically,

[00:04:04.080] like creating the React components based

[00:04:06.120] on the structure of the data.

[00:04:07.760] >> Well, the React component is actually

[00:04:09.080] predefined. It's like a JSON. It's a way

[00:04:11.160] to render an arbitrary JSON object. And

[00:04:13.480] we just do a tabular view.

[00:04:15.560] But the steps that it's doing just to

[00:04:17.280] just to prove that it's not recorded. Um

[00:04:19.640] let's cuz I think people don't always

[00:04:22.840] uh they're like, "Oh, maybe it's a

[00:04:24.120] recording." It's like here's like a

[00:04:25.720] quick screenshot of my phone.

[00:04:31.630] And

[00:04:31.640] boom, there we have it. It should pull

[00:04:33.919] out the information right there. Um and

[00:04:36.000] it is And if I zoom in a little bit, it

[00:04:38.360] should be a little bit easier to see.

[00:04:41.520] You can easily see exactly what the

[00:04:43.160] information has. It's 10:07. It's

[00:04:45.680] Tuesday, September 30th. There's a

[00:04:47.120] picture of a person standing on a beach.

[00:04:50.200] And there's some stuff over here about

[00:04:52.800] like notifications that seems to be kind

[00:04:54.880] of made up.

[00:04:56.160] >> Yeah, Joy Chef, I don't have that app.

[00:04:58.480] Is that like a

[00:04:59.480] >> Um so I've no idea where it's coming

[00:05:00.680] from, but I'll have to check it out. But

[00:05:01.800] the point is like the model is able to

[00:05:03.400] go look at this and make some inferences

[00:05:05.919] around what's happening. And this all of

[00:05:08.400] this is happening through a two-step

[00:05:09.960] process.

[00:05:11.680] Um and we'll describe what that two-step

[00:05:13.240] is really fast uh by swapping over to

[00:05:15.880] the whiteboard. This step is really,

[00:05:17.600] really simple.

[00:05:20.160] One second. I'm going to

[00:05:21.840] I'm going to go to Okay. Yeah, the step

[00:05:23.560] is actually quite simple. All we do is

[00:05:26.200] we take in some image that's defined by

[00:05:28.720] uh the model.

[00:05:31.280] And we ask the model, "Given this image,

[00:05:33.760] I want you to uh

[00:05:36.280] model

[00:05:37.880] is

[00:05:38.680] take image

[00:05:40.480] and give me a schema." And we ask it to

[00:05:43.240] model a schema back to us.

[00:05:45.680] And this is literally a prompt that we

[00:05:47.040] will write I'll say, "Hey, given this

[00:05:48.480] image, give me a schema."

[00:05:50.680] Then what we do

[00:05:52.360] is we take that schema and we say,

[00:05:54.920] "Given the image,

[00:05:57.520] please take

[00:05:59.120] image

[00:06:01.560] and output

[00:06:03.880] schema." And I'll put this as variables

[00:06:05.880] so it's a little bit easier to see. And

[00:06:07.520] that's literally all the system is.

[00:06:09.920] You take the same image, you take the

[00:06:11.320] same schema, and then in theory,

[00:06:14.120] you should get out a filled out schema.

[00:06:18.240] >> So that's like a big JSON object,

[00:06:19.720] basically.

[00:06:20.480] >> Of some type, exactly. And ideally the

[00:06:22.680] type is defined over here. And I think

[00:06:25.040] this

[00:06:26.160] while this concept is really simple,

[00:06:28.760] I think it's one of the most powerful

[00:06:30.040] concepts that becomes possible in the

[00:06:31.720] world of GenAI in a way that very, very,

[00:06:34.680] very few things can do. Specifically, um

[00:06:39.880] specifically when I go look at it,

[00:06:42.320] this sort of concept, what it can do for

[00:06:45.040] us,

[00:06:45.919] is it can really and give me a second,

[00:06:48.280] let me just like

[00:06:49.400] put this out here so that we have

[00:06:50.520] another screenshot to have. What it can

[00:06:52.640] do for us is it can and I'll give you

[00:06:54.720] the screenshot of well, the schema as

[00:06:56.480] well that comes out of it.

[00:06:58.640] >> Yeah, if you can if you can pull the

[00:07:00.360] schema and also like can we get the JSON

[00:07:02.600] object that is being used to render that

[00:07:04.600] thing?

[00:07:05.760] >> Um I don't know. Let me see if that

[00:07:07.640] button works. No, it does not work so I

[00:07:09.400] cannot give you that, sorry.

[00:07:10.840] >> Can you get it from the Chrome console

[00:07:12.200] or something or not?

[00:07:13.080] >> Uh it's fine. Keep going.

[00:07:14.480] >> Okay.

[00:07:15.120] >> But I think the whole point is if you

[00:07:16.360] can define the schema really well,

[00:07:18.600] then you can actually have the model go

[00:07:20.200] output this stuff for you. I think the

[00:07:22.160] reason that this is such a foreign

[00:07:23.400] concept is most people have never done

[00:07:25.200] this in regular software, but if you've

[00:07:27.800] ever built some sort of like if you've

[00:07:29.840] ever built like, let's say, a form

[00:07:31.480] builder or if you've ever built a um

[00:07:36.040] or if you've ever built like a uh

[00:07:37.960] templating engine of some kind, you've

[00:07:40.080] done this. This is basically just meta

[00:07:41.800] programming.

[00:07:43.120] You're having the LM do some of the

[00:07:44.440] program you're trying to have the LM do

[00:07:46.360] the programming so you can program you

[00:07:48.560] can run that program later.

[00:07:51.760] >> It's like

[00:07:53.280] list list for reader macros all over

[00:07:55.280] again.

[00:07:56.440] >> I am actually have no have no idea about

[00:07:58.920] list so I can't actually

[00:08:01.080] comment on that. But I think the premise

[00:08:03.520] here is if you can go do something like

[00:08:05.200] this

[00:08:06.120] you can then take this to the next level

[00:08:08.600] and say that

[00:08:10.400] what you could do is give me the schema

[00:08:12.360] I want to build

[00:08:14.240] a third component here.

[00:08:16.919] Which is

[00:08:19.000] I can ask a different question which is

[00:08:20.680] which is given the schema

[00:08:23.080] give me a react component

[00:08:27.040] to render it.

[00:08:31.070] >> Wow.

[00:08:31.080] >> take the thing as an input over here and

[00:08:33.719] that actually can make this component

[00:08:35.360] and now you can take this plus this and

[00:08:38.200] now you have a pretty render you could

[00:08:40.120] theoretically have a pretty rendered

[00:08:41.440] view

[00:08:42.400] of the schema as well that isn't like a

[00:08:44.280] hard coded view like the one I'm showing

[00:08:45.720] you right over here. So I think the

[00:08:47.440] whole premise of meta programming here

[00:08:49.440] just opens a world in general to a whole

[00:08:52.000] new set of possibilities that were never

[00:08:54.320] going to be possible for most

[00:08:55.760] applications. We just saw Anthropic

[00:08:58.280] release something like this

[00:08:59.960] in their most recent application where

[00:09:01.680] they said hey you can just press the

[00:09:03.760] button

[00:09:04.920] and if you press the button then um it

[00:09:07.640] will work.

[00:09:08.880] And you can actually go see

[00:09:11.400] you can actually go see a custom UI for

[00:09:13.120] their new application.

[00:09:14.960] This is basically what they're roughly

[00:09:16.680] what they're doing.

[00:09:18.240] You take a schema you ask the model to

[00:09:20.760] render the schema and now you have a

[00:09:22.240] really pretty view of the schema.

[00:09:24.839] And if you do this way you can build

[00:09:26.240] dynamic interactions on top of it you

[00:09:29.080] can build more data like data legibility

[00:09:33.520] in general because rendering is just

[00:09:35.480] going to be prettier than

[00:09:37.160] this arbitrary JSON blob.

[00:09:40.440] But, you can also do other things. Like,

[00:09:42.480] you could give

[00:09:43.720] a person a human loop step that says,

[00:09:48.160] "When I'm doing the schema right over

[00:09:49.760] here, before I do anything else,

[00:09:52.800] I can just do a really quick human

[00:09:54.520] review.

[00:09:55.880] Where before I actually do anything with

[00:09:57.280] the schema, I can do a quick little loop

[00:10:00.000] to make sure that this thing is actually

[00:10:01.280] good.

[00:10:01.800] >> Okay, so that would be basically taking

[00:10:03.360] the human feedback and like if we were

[00:10:05.640] going to extend this out, you can just

[00:10:07.280] get the schema

[00:10:08.800] or you can take the schema, send it to a

[00:10:10.480] human,

[00:10:11.880] and then basically pipe that back into

[00:10:14.040] the same prompt again with the human

[00:10:15.640] feedback until it's basically approved.

[00:10:18.600] >> Or just let the human edit it

[00:10:19.840] themselves.

[00:10:21.600] >> Okay.

[00:10:22.520] >> Right? So, there's so much you can do

[00:10:24.320] here that I think makes it really just

[00:10:26.680] makes this whole domain of like dynamic

[00:10:29.240] schema generation so fascinating.

[00:10:32.120] I mean, Typeform, if you've ever seen

[00:10:33.760] Typeform,

[00:10:34.960] uh which is like basically a form

[00:10:36.040] builder app,

[00:10:37.640] makes so much money because of how

[00:10:39.520] pretty they made making schemas.

[00:10:41.680] That's all they did under the hood. They

[00:10:43.440] I mean, they do obviously do a lot of

[00:10:44.600] stuff and I'm oversimplifying.

[00:10:46.520] But, one of the things that they

[00:10:47.560] definitely did in the very, very

[00:10:48.839] beginning is they made it stupid easy

[00:10:52.760] to build a lot of um

[00:10:56.080] to build a lot of schemas on the fly.

[00:10:58.720] So, that what you can end up doing is

[00:11:01.440] you can just have really pretty forms

[00:11:02.760] without having to do any of the mockery

[00:11:04.280] around it.

[00:11:05.839] And I think with the world of LLMs, you

[00:11:07.080] can now do this for any problem

[00:11:09.160] all the time. Let's talk about a

[00:11:11.640] First of all, I I'll talk about a little

[00:11:13.000] bit more complexity we can add in a

[00:11:14.160] second. But, what's your first thoughts,

[00:11:15.600] Stacks?

[00:11:16.440] >> Type- Typeform's a really interesting

[00:11:17.960] example. I'm I'm curious what you're

[00:11:19.480] going to use to demo this. But, I mean,

[00:11:21.080] I I like the way this builds

[00:11:24.320] incrementally of like, "Look, you can

[00:11:26.280] just do the schema and then you can look

[00:11:28.160] at that and you can do something with

[00:11:29.200] it." And then you can say, "Cool, here's

[00:11:30.320] the schema and the image. Give me the

[00:11:31.480] JSON." And then you can write your own

[00:11:33.320] react component to render it. Or you can

[00:11:35.560] say like, "Okay, cool. Look at the

[00:11:36.760] thing, get the schema, build a react

[00:11:38.520] component for the schema, do the

[00:11:40.000] extraction, and then do a custom

[00:11:41.960] rendering." And what's nice about this

[00:11:43.360] is these are all kind of well modeled as

[00:11:45.640] individual parts of the workflow that

[00:11:48.640] could be tested independently. You can

[00:11:50.960] get the first part working and and

[00:11:52.680] verify that on 5s or like actually like

[00:11:55.440] spot checking or writing real tests. And

[00:11:57.080] then you can slowly build up to

[00:11:58.880] something really, really cool. think is

[00:12:00.800] especially if you're newer to and doing

[00:12:02.840] AI engineering and doing context

[00:12:04.200] engineering, I think um is a really,

[00:12:06.800] really valuable pattern to think about

[00:12:09.240] when you're building, right? Like if you

[00:12:10.360] showed me that webcam demo of like,

[00:12:12.560] "Hey, here's here's my phone, build me a

[00:12:14.480] dynamic table." I'm like, "I have no

[00:12:16.920] idea how the heck to build that." So, I

[00:12:18.800] like I like the way this is laid out. Um

[00:12:21.200] what were you thinking about kind of

[00:12:22.760] like as a demo use case today? Cuz

[00:12:24.720] obviously we already have the

[00:12:26.320] the extractor thing working. But like

[00:12:28.480] what Have you Have you thought about

[00:12:29.720] like what would be the best way to like

[00:12:31.000] demonstrate this live?

[00:12:32.920] >> Yeah, I have been. Um let me just put

[00:12:34.760] this over here by the way, just so

[00:12:35.720] people know what phone what photo we

[00:12:37.360] used

[00:12:38.080] >> Yeah, you can put that over my shitty

[00:12:39.960] hand-drawn image of a sun and a cloud.

[00:12:42.800] >> Um let's put it over here.

[00:12:44.280] Uh maybe. I think I want to I want to

[00:12:45.920] talk about a couple of things. I think

[00:12:47.240] what I'm going to do is probably walk

[00:12:49.360] through this actual code.

[00:12:51.800] Um and just show people what this code

[00:12:53.920] ends up looking like.

[00:12:55.520] Uh firstly, like even the most basic

[00:12:57.480] part of like how do you even go from

[00:12:58.680] like ask the model to generate a schema?

[00:13:00.640] What kinds of schemas work well? What

[00:13:02.400] kinds of schemas work poorly?

[00:13:04.520] Talk about how to do actual streaming

[00:13:07.200] over here.

[00:13:08.320] And like how how do I get it to stream?

[00:13:10.000] Cuz that's a whole different problem.

[00:13:12.080] Talk about what it takes to render the

[00:13:13.440] schemas in different ways of doing that.

[00:13:15.560] And then I think if we get to it, I'd

[00:13:16.880] love to do the react component stuff as

[00:13:18.400] well and show how to go do that.

[00:13:20.400] >> Okay, awesome.

[00:13:21.680] Even in the rendered UI, there's so much

[00:13:23.880] capability that can go into this

[00:13:26.600] of how to make this possible.

[00:13:28.720] So, I'm going to try and take it step by

[00:13:30.480] step and make sure that we're really

[00:13:31.880] detailed in this walk-through cuz like

[00:13:34.720] the fundamental building block of hey

[00:13:37.200] model design me a schema and then what

[00:13:38.960] can I do with the schema is super

[00:13:41.200] powerful.

[00:13:41.840] >> Uh there's a question real quick. What

[00:13:42.960] do you mean What do you guys mean by

[00:13:44.000] getting a schema from the image? It's

[00:13:45.800] It's a good question um that we should

[00:13:47.480] probably make sure is super clear before

[00:13:49.200] we

[00:13:49.840] >> this really fast. I'll use a different

[00:13:51.280] example that we've been using uh that

[00:13:53.200] I've been working on.

[00:13:58.430] I'll I'll use um like over here I'll

[00:13:58.440] just start an app. So, over here let's

[00:13:59.840] say I have an app. I'm going to upload a

[00:14:01.160] file.

[00:14:03.280] I will upload a

[00:14:05.800] file that's like um

[00:14:07.520] mean.txt like this one.

[00:14:11.080] Uh why not? Let's do some meta um meta

[00:14:13.960] theming here.

[00:14:15.560] And what I'm going to have the LLM to

[00:14:17.120] do. Go ahead, Dex.

[00:14:18.600] >> No, I was just going to say so when we

[00:14:19.600] say generate a schema from the image,

[00:14:21.400] it's not hey AI turn this image into

[00:14:23.920] data or turn this into text. It's a

[00:14:25.640] little more meta. It's saying, hey AI,

[00:14:27.680] can you tell me if you were going to

[00:14:30.760] extract data from this, what would the

[00:14:33.440] schema for that be? And this is like a

[00:14:35.880] really interesting flavor of of context

[00:14:38.160] engineering where you're using AI to

[00:14:40.080] generate something that goes into that a

[00:14:42.040] downstream prompt. People have been

[00:14:43.960] doing this for years. The original agent

[00:14:45.640] was like use one LLM call to make a plan

[00:14:47.920] and then use another LLM call to execute

[00:14:50.040] it, right? This has been around since

[00:14:51.320] 2023 in the early days of ChatGPT. Um

[00:14:54.720] this is a lot more kind of like

[00:14:56.839] structured and and

[00:14:59.400] you know, you're but

[00:15:01.240] how do I say it? I don't know. Help me

[00:15:02.880] out here.

[00:15:03.400] >> Um Eugene has actually got a couple

[00:15:05.120] questions. I'm going to let Eugene in uh

[00:15:06.880] really fast.

[00:15:08.480] Um hey Eugene. Come on in. What uh and

[00:15:11.839] while while Eugene loads in I'll just

[00:15:14.400] I'll just articulate what I think Dex

[00:15:15.640] was saying.

[00:15:16.960] >> Thanks, Dex.

[00:15:17.400] >> It's exactly

[00:15:18.960] It's

[00:15:20.080] >> Oh, sorry, Eugene. Uh can you not screen

[00:15:22.360] share really fast? I'm going to have to

[00:15:23.640] turn this off.

[00:15:24.200] >> Of course.

[00:15:24.920] >> All right.

[00:15:26.440] Uh, do you have a

[00:15:28.200] I'm going to go back to screen sharing

[00:15:29.520] the screen.

[00:15:30.040] >> Yeah, let's let's let's let's double

[00:15:31.480] down on kind of like how Yeah, what how

[00:15:32.920] do you get a schema from an image? Um,

[00:15:35.080] and yeah, what's what what makes this

[00:15:36.680] more advanced than the, you know, make a

[00:15:38.720] plan and then execute it is that we're

[00:15:40.640] not passing something into the prompt

[00:15:42.520] and

[00:15:42.720] >> Of course. Of course. Um, I'll let you

[00:15:44.600] guys finish. Sorry.

[00:15:45.520] >> Okay, seems like there's a little lag.

[00:15:47.240] >> I'll call him in a second. Let me I

[00:15:48.360] think there's a I'm we're probably not

[00:15:50.040] very good at this.

[00:15:51.400] Um, I'll kick you out for a second. I'll

[00:15:52.520] invite you maybe in a bit when we're uh

[00:15:54.760] when we're back. Sorry, Dex. I don't

[00:15:56.600] know how to get someone out of here. Um,

[00:15:58.240] if you can do that.

[00:15:59.000] >> All right, I'll leave.

[00:16:00.360] We auto-generate

[00:16:01.640] >> Sorry about that. Um,

[00:16:03.160] but let me describe the schema thing

[00:16:04.320] really fast.

[00:16:05.440] So, in the schema thing what we did is

[00:16:07.120] we asked the LM to say, "Hey, given this

[00:16:09.120] image that I have over here,

[00:16:11.360] define a schema." And the model said,

[00:16:13.080] "Okay, well, here's the schema that I

[00:16:14.440] have associated with this. Class dog,

[00:16:16.480] there's a banana in there." So, I

[00:16:17.720] modeled a banana. I'll model some socks.

[00:16:20.600] I'll say that there's a background over

[00:16:22.120] here. There's an image description of

[00:16:24.360] some kind. And then the thing that I

[00:16:26.000] want to give back. Because defining

[00:16:28.040] schemas is not sufficient. Not only do I

[00:16:30.440] have to define a schema, I also have to

[00:16:31.920] tell you what about the schema do I want

[00:16:33.600] back. I want an image description back.

[00:16:36.839] So, there's basically a two-party

[00:16:38.839] problem here when I generate schemas of

[00:16:40.400] any kind. One, I have to model every

[00:16:41.920] single schema. And then I also have to

[00:16:43.760] give me the type of the thing I want

[00:16:45.360] back.

[00:16:46.440] So, in this case, I just asked the LM to

[00:16:48.000] go and do that for me. And once it does

[00:16:50.000] that, what I can do is I can just say,

[00:16:51.760] "Okay, now given this image, run this

[00:16:54.839] code and and uh return this type back to

[00:16:57.760] me, image description," which is

[00:16:58.920] described down here.

[00:17:00.240] >> So, instead of the model having to think

[00:17:02.280] about one, what data is interesting and

[00:17:05.160] what shape should it have, and also what

[00:17:06.959] are the values for that data, you're

[00:17:08.439] kind of separating the work into two

[00:17:10.439] separate tasks, basically.

[00:17:12.720] >> Exactly. And now, when I go run this,

[00:17:16.920] what I can do is can run this code that

[00:17:18.600] I generated, and the model should in

[00:17:20.600] theory uh it's always in theory because

[00:17:22.680] it's AI.

[00:17:23.800] Um but it should in theory print out

[00:17:27.800] all the information I want right over

[00:17:29.200] here. So, it actually printed out all

[00:17:30.720] the stuff where it actually says

[00:17:32.840] colors are pink, blue, and red.

[00:17:35.240] Um for type

[00:17:37.640] uh for the dog as well. I can print out

[00:17:39.920] render the JSON view, I can render the

[00:17:41.800] YAML view, I can render

[00:17:44.000] a view that I defined as pretty.

[00:17:46.160] That's just like nested objects.

[00:17:48.200] >> I feel like I feel like there's a lot of

[00:17:49.520] purple going on in your your your your

[00:17:51.720] definition of pretty.

[00:17:53.040] >> Honestly, I think you you tell any model

[00:17:55.240] to generate code, it just says purple.

[00:17:57.440] Uh

[00:17:58.440] This actually isn't my choice.

[00:18:00.760] Um I promise.

[00:18:02.440] >> Um Javier would like to see the two I

[00:18:04.520] mean this code is open source, right?

[00:18:06.000] But can we quickly look at the prompts?

[00:18:08.680] >> We'll walk through the code in a couple

[00:18:10.160] seconds.

[00:18:11.400] Cuz this code is fully open source. It's

[00:18:13.160] going to be in the AI that works repo,

[00:18:14.600] so you'll all have access to it as well.

[00:18:16.760] Um but all this stuff is to say that

[00:18:19.080] like once you have this, there's just a

[00:18:20.640] couple kinks you have to do to iron out.

[00:18:23.120] Like you have to figure out how to do

[00:18:24.320] streaming. Turns out streaming is

[00:18:25.880] actually kind of annoying with these

[00:18:27.480] dynamic UIs.

[00:18:29.200] But the next step you can do here, if

[00:18:31.000] you go back to our whiteboard,

[00:18:33.720] is you can really just go and I'll take

[00:18:36.120] a screenshot. That's if you can take a

[00:18:37.440] screenshot and post them back over here.

[00:18:39.680] Uh I'll take the screenshots in a few

[00:18:41.720] seconds.

[00:18:42.600] >> You're just going to put it over there.

[00:18:43.960] >> of what we're doing, is all we did is we

[00:18:45.880] said, "Hey model, tell me the schema."

[00:18:48.360] Um

[00:18:49.480] and I guess there's technically one more

[00:18:50.880] thing that we added with the schema,

[00:18:52.040] which is not just a schema,

[00:18:54.000] but schema plus return type.

[00:18:59.510] And the reason the return type is

[00:18:59.520] important because as you saw in the

[00:19:01.040] previous example,

[00:19:02.840] one of the things that we did here is we

[00:19:05.080] did generate quite a few schemas.

[00:19:07.360] Technically, there's many schemas here.

[00:19:10.000] And we just have to know which of these

[00:19:11.160] schemas we actually want to return as

[00:19:12.920] the top level

[00:19:13.600] >> Uh okay, so this is like when you're

[00:19:16.200] doing a swagger and open API spec, you

[00:19:18.680] have all your object definitions, but

[00:19:20.320] then each endpoint has to specify, okay,

[00:19:22.360] which one of those does this thing

[00:19:24.000] return? So you need to tell, okay, which

[00:19:25.600] of those things is actually the top

[00:19:27.080] level?

[00:19:28.040] >> Or you might just return an array as a

[00:19:30.080] top level object, too, right? You might

[00:19:32.040] say, I want to return an array.

[00:19:34.320] And now the model's going to return an

[00:19:35.880] array as your top level object.

[00:19:38.000] >> With one with one item in it, but yeah,

[00:19:39.840] okay, cool.

[00:19:40.800] >> Yeah, exactly. But I think all of this

[00:19:42.360] is really really highly dependent based

[00:19:44.960] on the actual problem that you're

[00:19:46.000] solving. So like that's why the return

[00:19:47.800] type matters, because you can't just say

[00:19:49.960] that, hey, I want to go generate a

[00:19:52.000] schema, you also have to say what is a

[00:19:53.640] return type. So but once you have solved

[00:19:55.560] that problem, then you have a second

[00:19:57.360] problem, which is now you just take that

[00:19:58.760] schema and return type and you uh you

[00:20:01.240] ask the model

[00:20:03.120] uh return type to say, hey, give me that

[00:20:06.040] same image that I took the image of that

[00:20:08.120] I used to determine the schema, go

[00:20:09.440] return the return type.

[00:20:11.280] Now, there's a lot of layers of

[00:20:13.080] complexity that you can do over here to

[00:20:15.480] make this a lot better. Like for

[00:20:16.840] example, you could say that you save

[00:20:18.480] your schemas in a database. So instead

[00:20:20.840] of actually asking a model to generate,

[00:20:22.800] you're like, hey, if an image looks like

[00:20:24.240] another image from before, return the

[00:20:26.440] same schema that I have saved in my

[00:20:27.840] database. Don't ask a model for a new

[00:20:29.480] schema.

[00:20:30.640] So that adds a little bit Go ahead.

[00:20:32.880] >> I was going to say, um just quickly, do

[00:20:34.640] you want to try to get Eugene on? I know

[00:20:35.960] there's a little bit of a delay.

[00:20:38.800] So we might want to do

[00:20:40.200] >> I'll do that in a second.

[00:20:41.440] >> Yeah, that's okay.

[00:20:42.480] >> Uh Eugene, do you want to type out your

[00:20:43.720] question and then we'll get you in

[00:20:44.800] there? Cool. Uh thank you.

[00:20:46.960] Um

[00:20:47.720] So what you can do over here is you can

[00:20:50.200] actually go and build a lot of like

[00:20:51.800] stability in here, because one of the

[00:20:53.560] risks with dynamic schemas is your stuff

[00:20:56.240] is constantly changing. And if it's

[00:20:58.400] constantly changing, that

[00:21:00.400] is a superpower, but depending on the

[00:21:02.360] use case, it can also be a super

[00:21:03.760] weakness.

[00:21:04.840] >> But you may want to bake these, right?

[00:21:06.240] If you If you go process 100, you know,

[00:21:09.600] car loan applications or whatever it is,

[00:21:11.640] at a certain point, you want to be

[00:21:13.080] extracting the same thing from every

[00:21:14.600] every one of those, otherwise, you just

[00:21:16.240] have a bunch of JSON in your database

[00:21:17.920] rather than like structured columns.

[00:21:20.000] >> Exactly. And like I think the beautiful

[00:21:21.800] part about doing this stuff in such a

[00:21:23.320] nice way is technically we're using a

[00:21:25.920] model to solve this problem, but there's

[00:21:27.480] nothing that says that this model,

[00:21:28.960] "Please take this image and give me a

[00:21:30.200] schema."

[00:21:31.440] is actually a model problem.

[00:21:33.640] That could be a thing that says, "Hey,

[00:21:34.960] load these schemas from my database."

[00:21:37.880] Uh and then give me the schema and then

[00:21:39.480] ask the model to extract the schema from

[00:21:41.040] that image.

[00:21:42.440] And maybe we initially seed it with a

[00:21:45.200] database with a schema generated by a

[00:21:47.040] model, but really it's a human process

[00:21:48.800] that goes and edits it along the way.

[00:21:51.040] And all of these are really use case

[00:21:52.400] specific, but the premise that we have a

[00:21:54.400] schema that we save in our database that

[00:21:56.040] we then load and like re-render stuff

[00:21:58.440] with or extract data with

[00:22:01.480] is like one of the most common use case

[00:22:03.280] for LLMs, and I think most more people

[00:22:05.880] should definitely be looking at it along

[00:22:08.080] the way.

[00:22:09.600] But with this, I want to get to some

[00:22:10.920] code. Uh

[00:22:12.000] Eugene, if you have your question, feel

[00:22:13.120] free to type it out and then we can talk

[00:22:14.400] about it in a second uh along the way.

[00:22:16.880] But hopefully that gets everyone a

[00:22:18.040] really good concept around what we're

[00:22:19.800] going to be doing today. Cool. Let's do

[00:22:21.720] it.

[00:22:23.120] I'm going to pull up Cursor.

[00:22:26.200] >> Let's write some dang code. I'm really

[00:22:28.440] excited to see the uh the dynamic React

[00:22:30.480] component thing.

[00:22:32.680] >> I agree. I have been actually playing

[00:22:35.240] around with that, so I hope I can make

[00:22:36.520] it worthwhile of everyone's time.

[00:22:38.600] >> Looks like Eugene just had something he

[00:22:40.360] wanted to show off in a time-boxed

[00:22:42.800] window.

[00:22:43.760] >> Oh, let's do that at the end then,

[00:22:45.200] Eugene. Um

[00:22:46.640] well well well we'll get you on towards

[00:22:49.080] the end during the extra time once we've

[00:22:50.560] actually shown off all the code.

[00:22:52.680] >> I think that's good.

[00:22:54.120] Sorry for the false start, dude.

[00:22:55.880] >> Yes, I have lots of those as well.

[00:22:58.040] Um

[00:22:58.880] Cool.

[00:23:00.880] I'm just going to

[00:23:02.040] screen share my code.

[00:23:04.240] Share.

[00:23:05.760] I'll assume. Can you folks see VS code?

[00:23:08.040] Perfect. I'll try and make it pretty

[00:23:09.760] big.

[00:23:10.800] Um

[00:23:12.240] and

[00:23:13.360] I'm going to start off with just the

[00:23:14.560] prompts to show what it is.

[00:23:16.840] There's two prompts here. One is called

[00:23:19.480] generate panel, one is called execute

[00:23:21.280] panel. I'm going to start off with

[00:23:22.600] generate panel. This is all about schema

[00:23:24.600] generation. So, what I do over here is I

[00:23:27.560] say that

[00:23:29.200] I'm first going to define the function

[00:23:31.000] signature of the thing that I'm looking

[00:23:32.440] for.

[00:23:33.840] Along the way, let me just make the chat

[00:23:35.240] window correct size. Second.

[00:23:38.280] Okay.

[00:23:39.320] Um

[00:23:40.720] Cool. And this function is just a thing

[00:23:42.560] that says, I mean I'm this function will

[00:23:44.640] either take in a string, it'll take in

[00:23:46.720] an image, it'll take in an audio, or a

[00:23:48.680] list of images.

[00:23:50.360] And then it'll return a schema object

[00:23:53.000] out of it.

[00:23:54.240] A schema object is defined as an object

[00:23:57.080] that has a couple of fields. It has the

[00:23:59.880] interface code.

[00:24:01.320] It has the return type and then like

[00:24:03.000] some other code associated with this.

[00:24:05.040] I'll talk about why I did other code in

[00:24:06.560] a second. It was just a prompt

[00:24:07.760] engineering hack.

[00:24:09.760] Um and then I just do some prompt

[00:24:11.640] engineering here telling it to just not

[00:24:13.840] worry about escape characters because I

[00:24:15.320] found out schema is better. So, I just

[00:24:16.800] told it answer with backticks to prevent

[00:24:19.680] escape characters and that worked

[00:24:21.720] really well when I was generating code

[00:24:23.280] for me.

[00:24:24.360] >> Okay, so quickly question. Um

[00:24:26.800] this is you're having it output YAML

[00:24:30.200] code specifically. I've also seen

[00:24:32.560] examples of this where you just output

[00:24:34.120] like a JSON schema style thing as well,

[00:24:36.440] right?

[00:24:37.080] >> I have seen that, but I actually

[00:24:38.800] specifically found that the reason that

[00:24:40.280] outputting YAML code works a lot better

[00:24:42.240] is

[00:24:42.920] >> Well, there's less syntax, right? Or the

[00:24:44.800] syntax is easier for models to write.

[00:24:47.560] >> Yeah. So, uh

[00:24:49.960] I'll just give a quick primer over here.

[00:24:52.320] Um

[00:24:53.280] Screen share on my screen. I can't

[00:24:54.760] switch screen share very easily.

[00:24:56.920] Hide.

[00:24:58.280] Stop. Screen share again.

[00:25:00.120] Hide. Uh I'm just going to share my

[00:25:01.880] whole screen, so please don't um

[00:25:04.200] steal any API keys.

[00:25:05.960] Um

[00:25:07.160] >> Yeah, we're no longer on Zoom. We're no

[00:25:08.760] longer on uh AI that works circle of

[00:25:11.360] trust. We're on open internet.

[00:25:14.760] Hide your keys. Hide your wife.

[00:25:16.720] >> Well, let me just look at JSON schema

[00:25:18.040] for example. If I want the If I want

[00:25:19.840] something to be represented as string

[00:25:21.200] array, this thing is 23 tokens in JSON

[00:25:23.120] schema. I can just output string array.

[00:25:25.960] It's just way less tokens for the model

[00:25:27.640] to say that it wants a string array for

[00:25:29.120] some field. If it wants like If it wants

[00:25:31.200] to say something is like um

[00:25:33.080] like uh what's it called? If it wants to

[00:25:34.960] modify it from like a string string

[00:25:37.040] string and string to a like string array

[00:25:38.600] and int array,

[00:25:40.040] zero token change.

[00:25:41.760] If you want to say something is

[00:25:42.760] required,

[00:25:44.280] this is just 73 tokens to say stuff is

[00:25:46.320] required. Like same field, 23 tokens for

[00:25:48.400] the same data model.

[00:25:50.160] And it even snuck in some extra metadata

[00:25:52.080] about like what this is in ISO format.

[00:25:54.600] So, it's just that JSON schema is just

[00:25:56.120] extremely verbose.

[00:25:57.920] So, I have found historically that I get

[00:26:00.000] way worse results when I use JSON schema

[00:26:02.320] than when I just like have it output

[00:26:04.160] code something that looks way more like

[00:26:05.400] code along the way.

[00:26:07.720] >> Okay.

[00:26:08.680] Cool. What else what do let's what else

[00:26:10.600] what other what other code prompts you

[00:26:11.880] want to show?

[00:26:13.040] >> Um so, cool. Uh and then I want to talk

[00:26:16.120] about Well, I want to talk about the

[00:26:17.080] actual prompt. So, what is the prompt?

[00:26:18.640] Well, I learned it self-to-generate BAML

[00:26:20.200] schema. I give it this context. I gave

[00:26:21.720] it some background about BAML. I'll show

[00:26:23.040] what that is in a second. And then I

[00:26:24.760] just CTX that output format and then

[00:26:27.040] say, "Here's the content." That's It's a

[00:26:29.160] really really simple prompt.

[00:26:31.280] Yeah, I should have some test cases

[00:26:32.360] here, too.

[00:26:33.560] Um

[00:26:34.560] but I'll show what the BAML description

[00:26:35.960] is. It's literally about like

[00:26:38.160] How many lines of code is this? It's

[00:26:39.560] like roughly around Oh, it doesn't tell

[00:26:41.920] me.

[00:26:43.280] It's like roughly around like 30 lines

[00:26:45.360] of code or 40 lines of code that

[00:26:46.640] describe 50?

[00:26:48.960] 60?

[00:26:49.680] >> 60.

[00:26:50.240] >> 60 lines of code that describe all of

[00:26:52.120] BAML syntax. and like I just described

[00:26:53.720] the very basics of like

[00:26:55.440] here's a class, here's how you do

[00:26:57.080] nesting, here's how you do enums, here's

[00:26:58.800] how you do literals, etc. etc.

[00:27:01.080] >> This is your cursor rules for BAML. If

[00:27:03.320] you If you wanted If you wanted cursor

[00:27:04.960] rules for writing BAML, this is probably

[00:27:07.080] what should get injected into every AI

[00:27:08.960] prompt and when you're coding, right?

[00:27:10.640] >> Exactly. And then I said I said the most

[00:27:12.800] important thing. It's pretty much like

[00:27:13.880] TypeScript but with one difference,

[00:27:15.120] there's no colon.

[00:27:16.880] Uh that was a mistake on our end. We'll

[00:27:18.280] fix that later, but um that's about all

[00:27:20.520] we do.

[00:27:21.520] And once we tell the model that, then we

[00:27:22.920] just like try it out on a bunch of

[00:27:24.680] prompts.

[00:27:25.800] And the prompt that I tried out was just

[00:27:27.040] like simple resume example.

[00:27:29.000] I just go run this and

[00:27:35.030] it pretty much dumps out the code really

[00:27:35.040] really well.

[00:27:35.840] >> So the input is just this text string of

[00:27:38.400] your resume. Will you scroll up scroll

[00:27:39.800] up and just show that one more time? Or

[00:27:41.320] like yeah, make that visible. So it's

[00:27:43.280] literally just a markdown of your

[00:27:45.560] resume. And so it's looking at this and

[00:27:47.680] it's saying, "Cool, if I was going to

[00:27:49.880] turn this into a structured object, what

[00:27:51.480] would the fields in that object be?" And

[00:27:53.240] then that's the schema we have at the

[00:27:54.440] bottom.

[00:27:55.520] >> It's right here. So it's like person,

[00:27:57.160] full name, email, experience, skills.

[00:28:00.120] And that looks pretty reasonable given

[00:28:01.680] this resume.

[00:28:03.680] Um but what I've and position as a

[00:28:06.240] company title and then is current, which

[00:28:07.840] is kind of fascinating.

[00:28:09.440] I like that it decides that it is

[00:28:11.160] current in there.

[00:28:12.560] But what I think what I found is like

[00:28:15.440] the reason that I added other code or

[00:28:17.560] and you'll notice that the LM actually

[00:28:18.760] did a pretty good job of that takes in

[00:28:20.640] like outputting the schemas correctly.

[00:28:22.880] And then even over here is like, "Oh,

[00:28:24.200] maybe I'll add some other code."

[00:28:25.840] Is when I didn't have the other code

[00:28:27.440] example,

[00:28:28.760] it actually started putting like logic

[00:28:30.720] in the code and started being like,

[00:28:31.840] "This how I want to call it. This is

[00:28:32.960] what I want to do with this schema." And

[00:28:34.120] start doing a lot more than it needed to

[00:28:35.920] along the way.

[00:28:37.520] But once I started restricting it to

[00:28:40.400] interface code, return type, and other

[00:28:42.520] code, then if anytime it did dump out

[00:28:44.400] stuff like other code, it just put in

[00:28:46.040] other code. I didn't care.

[00:28:47.680] >> I see. So, you're using the field names

[00:28:50.240] to basically steer the model as to,

[00:28:54.040] okay, put the interface and the types in

[00:28:55.680] one place. And if you find the need to

[00:28:58.240] say anything else, put it over here. I'm

[00:29:00.200] just going to ignore it. But you give a

[00:29:01.600] model a dumping ground for, like, hey, I

[00:29:03.400] want to write an if if statement or a

[00:29:04.960] while loop or something.

[00:29:06.080] >> Exactly. Exactly. Cuz I found it was

[00:29:08.320] pretty often.

[00:29:09.800] >> Fascinating. That's a really cool topic

[00:29:11.640] that I or like concept technique that I

[00:29:13.320] don't think I've really heard about

[00:29:14.480] before, which is like giving the model

[00:29:16.960] other fields to dump the things that you

[00:29:18.720] don't want to so that your key fields

[00:29:20.680] that you're working with stay really

[00:29:22.000] clean and concise.

[00:29:23.160] >> Exactly. Like it worked really well for

[00:29:25.000] this problem.

[00:29:26.160] >> That's dope.

[00:29:27.560] >> It was like a It was one of the key

[00:29:29.120] things I had to do to make this UI to

[00:29:30.960] make this actually work in a very

[00:29:32.280] reliable way.

[00:29:33.800] >> How How did you come to that guess?

[00:29:37.040] Like, how many things did you try? Did

[00:29:38.680] you I imagine you tried a lot of

[00:29:39.920] prompting first. You're like, don't

[00:29:41.280] output code. Don't output code. Just

[00:29:42.840] output types. And it turned out this

[00:29:44.800] worked better.

[00:29:45.560] >> It turns out the model was dumb.

[00:29:47.400] At that So, then I did a couple of

[00:29:48.720] things. One, I renamed this to interface

[00:29:50.160] code. But even when I did that, it did

[00:29:52.160] the dumb thing and added more code

[00:29:54.000] sometimes.

[00:29:54.920] >> Yeah.

[00:29:55.560] >> And then I was like, okay, well, I need

[00:29:57.120] this to be really, really robust. Well,

[00:29:59.360] let me just give it a dumping ground.

[00:30:01.320] >> Okay.

[00:30:01.960] >> And giving it a dumping ground made a

[00:30:03.480] huge difference and

[00:30:06.200] in like update.

[00:30:08.560] >> And then

[00:30:09.280] >> I did this uh

[00:30:10.280] >> Yeah.

[00:30:11.160] >> Then like the back end code is really

[00:30:12.560] simple. It's just a fast API server.

[00:30:14.800] Um and all the back end code does is

[00:30:17.080] there's basically two API calls.

[00:30:19.040] One is called uh generate YAML stream.

[00:30:22.440] And I have different hooks for stream

[00:30:23.800] versus non-stream, by the way, just FYI.

[00:30:26.680] Um and then what I do is I just generate

[00:30:29.640] the stream with the simple function.

[00:30:31.320] This stream I just have a handle stream

[00:30:32.800] function.

[00:30:34.000] >> And that just streams it down to the UI.

[00:30:36.240] >> It literally just streams it down to the

[00:30:37.600] UI. It literally just And it there's

[00:30:39.000] like some some stuff that I have to do

[00:30:41.000] in the UI to tell if I'm like in the

[00:30:42.640] middle of streaming or if I'm done

[00:30:43.920] streaming or if an error happened along

[00:30:45.360] the way.

[00:30:46.720] So, I have to go build this out myself,

[00:30:48.440] and that part is kind of annoying. I

[00:30:49.800] thought about how to make this better

[00:30:51.120] from a BAML's perspective, but that's a

[00:30:53.560] different topic.

[00:30:54.640] >> Okay, so you're using the structured

[00:30:56.040] streaming from BAML, but in order to get

[00:30:58.080] FastAPI to talk to your front end, you

[00:31:00.080] still have to kind of take the like

[00:31:02.040] output chunks from that so the UI knows

[00:31:04.920] whether it's finished or not.

[00:31:06.240] >> Exactly, and there's just no way around

[00:31:08.160] that, sadly.

[00:31:09.360] >> Okay, at least

[00:31:10.120] >> for now. And then, what I do is I just I

[00:31:12.200] have a two-data function that says,

[00:31:13.480] "Hey, given this data I get, convert

[00:31:15.000] it." And if you go look at how generate

[00:31:18.040] stream works,

[00:31:21.630] generate

[00:31:21.640] >> It's funny, I think I cloned this

[00:31:22.800] example like 4 or 5 months ago, and I

[00:31:24.880] was like playing with it, and I remember

[00:31:26.560] being confused by like, "Okay, why do we

[00:31:28.200] need a bunch of custom streaming code?"

[00:31:29.680] But that makes sense.

[00:31:30.960] >> Yeah, exactly. It ends up being very

[00:31:32.440] tricky. Well, then you just do

[00:31:33.960] x.model.dump. So, I literally just send

[00:31:35.720] the raw JSON up as a part of the

[00:31:37.520] >> giving you back a Pydantic model, but

[00:31:39.480] you really want to just like emit JSON

[00:31:41.440] over the wire.

[00:31:42.160] >> Exactly, cuz what does generate This

[00:31:44.160] thing returns a We saw earlier what the

[00:31:46.880] generate stream return. Uh generate

[00:31:49.120] returns

[00:31:50.600] >> You should put mode equals JSON there in

[00:31:52.520] case you get datetimes in your in your

[00:31:54.880] output dictionary.

[00:31:56.360] >> Um you won't

[00:31:58.200] because it's generating BAML code, which

[00:32:00.160] has types.

[00:32:01.280] Uh so, it's returning a class that's a

[00:32:03.000] schema

[00:32:03.320] >> Okay.

[00:32:03.840] >> along the way. So, you have a schema

[00:32:05.040] type, and then you just do

[00:32:05.760] schema.to_json.

[00:32:08.080] Um I should be dropping the other code

[00:32:09.840] variable cuz I don't care about it, so

[00:32:11.040] that's a separate thing, but uh this

[00:32:13.080] seems to work pretty well for our use

[00:32:14.400] case. Um cool. So, that's that's one

[00:32:16.520] part of the system. So, that's how we

[00:32:18.040] stream, that's how we get it up and

[00:32:19.200] running, and then the front end side,

[00:32:21.400] I'll show you how that page works end to

[00:32:23.000] end as well. As I basically have like

[00:32:25.040] three states over here. It's like I

[00:32:26.680] would want to know if I'm executing

[00:32:27.840] anything.

[00:32:29.120] I want to know if I'm generating, and

[00:32:30.400] then here's the generated code, and I

[00:32:31.600] want to know if what the execution

[00:32:32.960] result is.

[00:32:35.160] And you go to is executing, let's just

[00:32:37.320] look at how generate works when someone

[00:32:38.760] clicks the generate thing.

[00:32:40.440] You literally set is generating to true.

[00:32:42.800] You say here's the current input and

[00:32:44.640] then you just call you build a form

[00:32:46.760] model that you have to. There's a lot of

[00:32:48.400] boilerplate code I have to do to send

[00:32:49.840] like files from the front end to back

[00:32:51.360] end and stuff.

[00:32:52.520] So like that's just like standard chat

[00:32:53.920] GPT code to go render.

[00:32:55.960] And then the other thing you have to do

[00:32:57.920] is because if you want to stream you

[00:32:59.120] have to build SSE events on your own is

[00:33:01.280] I have to build a utility layer to

[00:33:02.960] actually handle SSE events.

[00:33:04.920] And like pass that back and forth

[00:33:06.320] between my front end and back end.

[00:33:08.080] >> This is all

[00:33:09.640] >> go ahead.

[00:33:10.200] >> Those types are type arguments but this

[00:33:13.200] the the values into the fetch SSE like

[00:33:15.600] type constructor for the generics end up

[00:33:18.200] being types that were generated by the

[00:33:20.160] BAML TypeScript compiler, right?

[00:33:21.960] >> you Yeah, I'll show you where these come

[00:33:23.040] from. So this code is being generated on

[00:33:25.160] the fly from BAML

[00:33:27.440] automatically for you thanks to

[00:33:31.800] our generate file. So generate file says

[00:33:34.040] all my BAML code should have generate

[00:33:36.280] generate Python bindings and react

[00:33:39.320] bindings automatically for me.

[00:33:41.040] >> And you can guarantee type safety across

[00:33:43.200] the client and the server cuz it's all

[00:33:44.760] one source of truth that's generating

[00:33:46.360] both sides. Okay. Yeah, we've seen this

[00:33:48.400] a lot with like using open API specs to

[00:33:50.640] generate types but this is this is cool.

[00:33:59.030] >> streaming the type is this type. So it

[00:33:59.040] just makes like auto complete better.

[00:34:01.680] That's like the only thing it really

[00:34:02.880] does for our lives.

[00:34:05.040] Um

[00:34:06.200] and then you can actually set the gen

[00:34:07.720] and then you get the response which is

[00:34:08.919] the final type. So during streaming it

[00:34:10.800] says

[00:34:11.960] what this hook says is whenever you're

[00:34:13.639] streaming you get SSE events on every

[00:34:15.560] partial event run this run this

[00:34:18.480] function. As soon as the thing is done

[00:34:21.480] run this function and just set the final

[00:34:23.679] response which is of schema type.

[00:34:26.560] But this thing on partial is a partial's

[00:34:29.159] partial type version of it. So like the

[00:34:30.800] value during streaming along the way.

[00:34:34.280] Um yeah, with this you basically have no

[00:34:37.080] drift in your type system

[00:34:39.520] along the way. And then once you have

[00:34:41.480] this like rendering a string rendering

[00:34:44.639] this string and this string in this

[00:34:47.600] um UI component that I have. Rendering

[00:34:50.120] all of Let me

[00:34:52.200] pull out this onto a different window

[00:34:54.000] really fast. I think.

[00:34:55.440] Rendering rendering onto this window and

[00:34:57.760] showing the actual BAML code versus the

[00:34:59.600] return type. Well, now you guys know

[00:35:01.160] where that's coming from. That is

[00:35:02.600] literally just this variable generating

[00:35:04.440] BAML, which is of schema type, which has

[00:35:06.120] interface code and return type. And then

[00:35:08.160] I just render those two fields.

[00:35:10.160] >> I have a question. If you If you want to

[00:35:12.200] do more, you can. I can I can I can hold

[00:35:13.880] it for a second.

[00:35:14.720] >> I'll talk about the execution logic in a

[00:35:16.680] second cuz I think that code is also

[00:35:17.960] very fascinating.

[00:35:19.360] >> Cool. And there's Yeah, I think the

[00:35:21.440] question about SQL for UI schema is um

[00:35:23.560] we should tackle at the end. Um but

[00:35:25.200] there's this question of like type and

[00:35:26.400] workflow drift. Obviously, BAML lets you

[00:35:29.040] use static types and kind of manage your

[00:35:31.320] types really well for the pieces that

[00:35:33.920] you're working with. But one of the

[00:35:35.320] things that I know you say all the time

[00:35:36.760] is types are amazing and like

[00:35:39.480] there was a long time I think you

[00:35:40.480] support like dynamic types in BAML a lot

[00:35:43.200] better now. But there was a long time

[00:35:44.800] where it was like an opinion of the

[00:35:46.120] team. It was like you shouldn't have any

[00:35:47.760] types. You shouldn't have any types in

[00:35:49.240] your outputs because like any types suck

[00:35:51.600] and the whole point of using this is

[00:35:52.720] having like dynamic types. Or sorry,

[00:35:54.840] having static types that you can catch

[00:35:56.640] at compile time and make the dev flow

[00:35:58.360] easier. This doing dynamic schemas, you

[00:36:02.080] don't actually get any types. Or like

[00:36:05.440] you kind of have to start working with

[00:36:06.760] any types because the output of the

[00:36:09.200] object is some just like nested JSON

[00:36:13.000] thing that you get out. The schema

[00:36:14.280] itself is just code. But maybe we can

[00:36:15.720] talk about that when we get to the

[00:36:16.520] execute side cuz the thing you're

[00:36:18.360] rendering in the UI ends up being and

[00:36:20.800] yeah, any object. There you go.

[00:36:22.560] >> So, exactly. So, I actually have an any

[00:36:24.680] object that I defined

[00:36:26.520] uh that talks about this problem because

[00:36:28.640] you're right, we can do anything.

[00:36:31.400] Uh, and it is kind of bad that you can

[00:36:33.160] do anything. So, like how do you deal

[00:36:34.360] with this world where any type is now

[00:36:36.480] suddenly valid?

[00:36:38.040] Um, and this I think becomes really

[00:36:39.560] relevant during execution, but I just

[00:36:41.560] think you have to know that it is that

[00:36:43.120] type. And once you know that it is that

[00:36:44.640] type, then you can start writing code

[00:36:46.240] around

[00:36:47.640] around that world.

[00:36:49.640] Um, so I'll talk about that in a second.

[00:36:51.920] Let's talk about how execution works.

[00:36:53.480] So, we talked about how streaming works.

[00:36:55.240] Uh,

[00:36:55.840] key part about generating code is about

[00:36:57.320] having to build some sort of SSC bridge

[00:36:58.920] between your front and your back end and

[00:37:00.680] having some type safety guarantees so

[00:37:02.360] that even when you're streaming partial

[00:37:03.600] types,

[00:37:04.720] that you know exactly what it is.

[00:37:06.960] So, again, if you look at the fetch SSC

[00:37:08.680] world, I actually handle

[00:37:10.800] like my event data.partial versus event

[00:37:13.840] data.final versus event data.error.

[00:37:17.360] So, when I actually go send it from my

[00:37:18.720] back end, I do I do exactly that. Um,

[00:37:21.080] and I apologize if this is a little

[00:37:22.720] repetitive, but I think it

[00:37:24.480] this stuff is really easy to make small

[00:37:26.240] mistakes on that makes it really hard to

[00:37:28.040] go debug.

[00:37:29.280] Same thing here. I'm just sending

[00:37:30.400] partial, final, and error. And I just

[00:37:32.280] catch that response up there. But, the

[00:37:34.720] next step is actually about executing

[00:37:36.720] demo code. So, now I have a type system

[00:37:38.560] that I've defined, how do I actually

[00:37:39.800] execute that?

[00:37:41.160] >> So, you're taking the schema that was

[00:37:42.440] created by the first call and then using

[00:37:46.080] it to do the extraction during a

[00:37:47.680] follow-up call.

[00:37:48.800] >> Exactly. So, handle execute. Let's start

[00:37:51.120] from the front end and work backwards

[00:37:52.560] cuz we just sent our schema and our

[00:37:54.440] return type to our front end.

[00:37:56.920] Uh, and we can see that right here. See,

[00:37:58.400] we have our interface code and our

[00:37:59.680] return type. So, let's figure out how we

[00:38:01.200] do this. Well, the first thing we do

[00:38:03.280] is we ask we see if we have any code cuz

[00:38:05.640] maybe the person didn't generate a

[00:38:06.960] schema for whatever reason. And if they

[00:38:08.680] do, we return error. But, then we start

[00:38:10.560] executing.

[00:38:12.000] When we execute, we build the form

[00:38:13.240] builder however we want. We We take the

[00:38:15.120] code and the return type, send it along

[00:38:17.120] with the data.

[00:38:18.360] And now when we're expecting data, we're

[00:38:20.000] expecting an any type. It's any during

[00:38:22.320] streaming, it's any when it's done.

[00:38:23.880] There's no rendering there. And then we

[00:38:25.760] build some sort of rendering engine to

[00:38:27.520] render an any type object.

[00:38:30.360] So, before I again show all the prompts,

[00:38:32.400] I just want to we can just show really

[00:38:33.800] quickly what the

[00:38:36.080] what the rendering engine looks like, so

[00:38:37.720] then you can have an idea of what this

[00:38:38.880] is.

[00:38:43.710] I have a section for rendering this, and

[00:38:43.720] I just have a different ways of doing

[00:38:45.240] this

[00:38:46.520] along the way.

[00:38:47.920] Um

[00:38:48.640] execution result. If we don't have any

[00:38:50.400] result or return null, we don't render

[00:38:51.920] anything.

[00:38:53.040] But then I just have a switch that just

[00:38:54.400] says based on the tab, whether it's

[00:38:55.960] table, JSON pretty, or YAML, I just

[00:38:58.040] render the specific execution result.

[00:39:00.880] And in this case I have like

[00:39:02.960] in this case uh sorry.

[00:39:05.360] Let me show you. It's very, very simple

[00:39:07.120] code. JSON syntax highlighting is just a

[00:39:08.800] JSON highlighter.

[00:39:10.320] It's nothing fancy.

[00:39:12.880] Format is YAML.

[00:39:14.560] Take the JSON object, render it as YAML.

[00:39:16.480] Nothing fancy.

[00:39:18.480] Pretty print, make some random uh

[00:39:20.880] Tailwind CSS divs.

[00:39:22.640] Like I have

[00:39:23.080] >> Okay, so this is your this is your like

[00:39:26.160] dynamic renderer that just is the pretty

[00:39:28.240] pretty printer. And you're you're

[00:39:29.360] literally just recursively making little

[00:39:31.000] spans with different

[00:39:32.560] >> Exactly. That's all I'm doing. With some

[00:39:34.200] indentation along the way.

[00:39:36.320] Um

[00:39:37.440] so this is kind of what we've seen most

[00:39:39.760] people do. And like if you're doing

[00:39:40.920] dynamic schemas, no matter what you do,

[00:39:42.720] you will have to build some sort of

[00:39:43.800] dynamic rendering at some point if

[00:39:45.440] you're going to handle arbitrary

[00:39:46.800] schemas.

[00:39:47.880] So, you can download something off the

[00:39:49.640] fly, you can do whatever you want, you

[00:39:51.240] can make rules, but you're going to use

[00:39:52.640] this type of keyword and do different

[00:39:54.400] things based on what you got.

[00:39:56.720] It just is the way it is. I don't really

[00:39:58.880] see a shortcut around this. If other

[00:40:00.280] people have different ideas, would love

[00:40:01.880] to see them.

[00:40:03.240] But if you have more constraint schemas,

[00:40:05.160] um then you can do other things as well.

[00:40:08.280] >> You can do kind of a deterministic typed

[00:40:10.360] component tree where you know exactly

[00:40:11.920] what happens at every layer.

[00:40:13.280] >> Exactly. Um but for

[00:40:15.360] >> For let's go back to actually executing

[00:40:17.440] this code. So, we have this We What we

[00:40:19.720] have is we have the content, so the

[00:40:21.280] image that we're sending back from the

[00:40:23.200] front end. We have the BAML code that

[00:40:25.280] the front end told us that another LLM

[00:40:27.920] told us what the schema should look

[00:40:29.280] like, and the return type.

[00:40:31.360] So, let's go look at what the back end

[00:40:32.680] code actually does. Well, the back end

[00:40:34.520] code actually does something really

[00:40:35.720] simple.

[00:40:36.840] We use a concept called type builder,

[00:40:39.600] which is our way to do dynamic type

[00:40:41.560] registration in BAML world.

[00:40:44.600] >> And this is This is how you get the, you

[00:40:47.960] know, BAML execution function to

[00:40:50.880] actually, hey, take this dynamic schema

[00:40:54.120] that was generated ahead of time, but is

[00:40:55.800] not in code, and is not compiled into

[00:40:58.520] the types, but take this schema and

[00:41:01.160] generate something for me using that

[00:41:03.120] schema.

[00:41:04.320] >> Exactly.

[00:41:05.800] So, then what you can do here is you can

[00:41:07.440] actually just add the BAML code that was

[00:41:08.960] generated from the last return type, our

[00:41:11.560] last source code, you just inject it

[00:41:13.240] into here, and you just say, "Hey, this

[00:41:15.520] response class that I have is a dynamic

[00:41:17.360] response class with a field called data,

[00:41:20.200] which is going to be of the return type

[00:41:21.880] the previous thing generated."

[00:41:23.800] So,

[00:41:24.800] in this world, let me find where this

[00:41:27.120] is.

[00:41:28.080] Uh

[00:41:28.720] So, in this world, what this ends up

[00:41:30.560] looking like is this schema gets

[00:41:32.800] injected

[00:41:34.320] right where it says

[00:41:36.440] BAML code,

[00:41:37.800] and the return type gets injected

[00:41:40.800] right where it says return type. So,

[00:41:43.280] image description array would go right

[00:41:44.960] over here.

[00:41:46.320] And then, once we do this, we get a

[00:41:48.160] couple things. The first thing we get is

[00:41:49.440] an exception. If for whatever reason the

[00:41:51.360] source code is bad, we can just tell the

[00:41:52.680] front end the source code is bad without

[00:41:54.040] calling an LLM.

[00:41:55.600] So, that's a nice benefit that you get

[00:41:57.200] right out of free. And then, the error

[00:41:58.720] message is nice, so you can feed that

[00:42:00.040] error back through the generator code

[00:42:01.320] and say, "This schema is bad. Don't

[00:42:02.560] generate anything along the way."

[00:42:04.720] And then, the next thing you can do is

[00:42:06.960] if the person is streaming, you can just

[00:42:08.360] execute this code, and and just pass in

[00:42:10.560] the type builder along the way. So, let

[00:42:11.920] me show you what the execution code

[00:42:13.280] looks like cuz I think it's fascinating.

[00:42:14.720] Now, the execution code is also really

[00:42:16.200] simple. The execution code is a thing

[00:42:18.560] that says

[00:42:20.080] execute baml. So, I'm that's just my

[00:42:21.960] function name. I'm going to pass in any

[00:42:23.520] content I want, so it's the exact same

[00:42:25.000] type signature along the way.

[00:42:27.280] And then you're going to return response

[00:42:28.440] type. This response type actually has no

[00:42:30.200] fields defined in it at at compile time.

[00:42:34.320] The only field that exists in it is the

[00:42:35.680] data field, which is defined at runtime

[00:42:38.320] with the return type that was provided

[00:42:39.960] to us. So, now we can

[00:42:41.360] >> Okay.

[00:42:42.160] >> So, what ends up happening in practice

[00:42:44.680] is the model doesn't actually have to

[00:42:45.880] know anything. It's a very, very simple

[00:42:47.760] prompt that says extract data with the

[00:42:49.040] given content

[00:42:50.560] you with this format, and then you just

[00:42:52.160] dump the content. And because the return

[00:42:53.800] type is dynamically extended

[00:42:55.440] automatically,

[00:42:56.920] you kind of get this for free. So, let

[00:42:58.480] me show you what that ends up looking

[00:42:59.640] like. And then the last thing I do,

[00:43:01.520] which I think is relevant, is

[00:43:03.760] when I actually handle the stream, if

[00:43:05.120] you remember in in generate baml, what I

[00:43:07.880] do is x.model.dump. In execute baml, all

[00:43:10.840] I say is

[00:43:12.080] the thing I should return to the front

[00:43:13.280] end is actually my return type.data,

[00:43:16.080] which is this dynamic field that I have

[00:43:17.800] defined.

[00:43:19.040] >> Do you have to model dump that, or is it

[00:43:21.040] like there's a chance it might be a

[00:43:22.280] primitive?

[00:43:23.280] >> Um

[00:43:25.520] I think actually the handle stream thing

[00:43:27.160] does it for me, so I it works, but you

[00:43:29.360] can also do it this way.

[00:43:31.320] >> Okay. And so, the the reason why you

[00:43:33.120] have response within dynamic inside of

[00:43:35.360] it is because you have to have something

[00:43:37.240] typed in the com- compiled schema to be

[00:43:39.520] the return type of this function, but

[00:43:41.280] then you're basically saying, "Okay, but

[00:43:43.480] the body of this object can be updated."

[00:43:45.880] And then when you add the baml code,

[00:43:47.360] you're basically overriding that that

[00:43:50.080] dynamic thing with just a single field

[00:43:52.240] called data.

[00:43:53.840] >> Exactly. Okay. So, what ends up

[00:43:56.640] happening is let's just show what this

[00:43:58.640] does. So, let's just write a test case.

[00:44:01.040] So, this test case is doing exactly this

[00:44:02.880] code

[00:44:04.040] over here, tb.add_baml just doing the

[00:44:05.840] testing world. So, these are the schemas

[00:44:07.920] that I added in. So, this is part of

[00:44:09.200] YAML code. And then dynamic class

[00:44:11.200] response result person. So, we can name

[00:44:13.240] this data just to be more consistent

[00:44:15.160] with what this is.

[00:44:16.960] And this is exactly the code that's

[00:44:18.320] being added. And then given this test

[00:44:20.240] case, what would end up happening

[00:44:22.360] >> Okay, so in the test you can't

[00:44:24.480] dynamically write code to call the add

[00:44:27.080] types function, but you can define what

[00:44:29.280] goes into the type builder as part of

[00:44:31.400] your test case.

[00:44:32.200] >> Exactly. So, it's basically you can just

[00:44:33.840] test what would have happened if the

[00:44:35.240] model did generate this thing.

[00:44:37.400] So, in this case the model generated

[00:44:38.680] this and this is basically what the LLM

[00:44:40.160] sees. The LLM doesn't even know it's a

[00:44:41.640] dynamic schema. It just thinks it is the

[00:44:43.720] schema.

[00:44:45.080] So, when the LLM goes and runs this, it

[00:44:47.000] dumps it out and then you get this type

[00:44:48.520] and you just do dot data.

[00:44:50.640] >> And then when you use when you use type

[00:44:52.360] builder in a test like that, um does

[00:44:54.800] that override all existing types or is

[00:44:57.240] that additive? Does that merge in?

[00:44:59.080] >> It's additive. It It doesn't merge.

[00:45:00.920] It doesn't merge for all things named

[00:45:02.480] dynamic. If you add a new type like

[00:45:04.120] this, it tells you like this cannot be

[00:45:06.080] redefined.

[00:45:07.240] >> Okay, cool. So, it is merging those in.

[00:45:10.920] Cool.

[00:45:11.880] >> So, it actually gives you a really nice

[00:45:13.800] way to go and test stuff out.

[00:45:16.440] Um so, now what you have is

[00:45:18.920] boom, you get this out and then what you

[00:45:20.480] return to the front end is dot data,

[00:45:23.320] which is the inner part of this, which

[00:45:24.600] is exactly the return type that we told

[00:45:26.480] the front end we wanted. And what's nice

[00:45:28.080] here is even if the LLM messes this up,

[00:45:29.960] so like

[00:45:32.000] um I'll do something for the sake of

[00:45:34.040] doing it, but it won't really matter. Um

[00:45:37.320] so, I'm going to lie to the LLM in this

[00:45:38.840] prompt really fast.

[00:45:41.200] Um technically I still want a data field

[00:45:44.000] out, but I will not tell the LLM I want

[00:45:45.880] a data field out.

[00:45:47.280] So, I'll do something that's kind of

[00:45:49.240] uh I'll trick it.

[00:45:51.680] Cuz this is this is actually part of the

[00:45:53.240] reason why it ends up working so well.

[00:45:54.560] So, as you can see here, the prompt has

[00:45:55.840] nothing about the data field. It's just

[00:45:57.280] answering the internal schema. But even

[00:45:59.200] though the model did that, you still got

[00:46:00.560] the data field out.

[00:46:02.160] >> Okay, so this is the baml parser doing

[00:46:04.480] some magic to figure out how do we take

[00:46:06.360] this data how do we take this object and

[00:46:08.760] map it into the schema that we were

[00:46:10.560] supposed to be

[00:46:11.840] >> Which is this one. Which is the response

[00:46:13.520] schema.

[00:46:14.400] >> Cool.

[00:46:15.200] >> A lot of times the model actually we've

[00:46:16.920] seen it mess up in a lot of dynamic

[00:46:18.280] schema generation especially like deeply

[00:46:19.960] nested schemas and stuff.

[00:46:22.200] But the fact that you can just not think

[00:46:24.480] about that and just know that you're

[00:46:26.280] going to get something that models the

[00:46:28.160] schema that you defined even purely

[00:46:29.720] dynamically.

[00:46:31.760] Has we've seen increased accuracy a lot

[00:46:33.920] for these dynamic situations. And what

[00:46:35.840] for context like the rules of like how

[00:46:38.240] complicated can dynamic schemas be?

[00:46:40.920] Like honestly you can do whatever you

[00:46:42.040] want. Like

[00:46:44.360] if you want to do

[00:46:47.040] this and like write a dumb schema that

[00:46:48.760] looks like this.

[00:46:50.840] You are welcome to do that.

[00:46:53.200] It will do the thing for you and it'll

[00:46:55.080] behave as if you randomly wrote a schema

[00:46:57.200] at runtime. Uh people are like what the

[00:46:59.040] heck is a schema? The schema is a

[00:47:01.800] values that fit into the schema are

[00:47:04.840] arrays of empty arrays. Um so

[00:47:08.000] it the type type systems are beautiful

[00:47:09.920] in my opinion. These are all valid uh

[00:47:12.560] values of food.

[00:47:13.920] Uh

[00:47:15.040] >> I'm terrified to see what happens when

[00:47:16.480] you run this.

[00:47:19.040] >> I don't know either.

[00:47:20.800] You get an empty array.

[00:47:21.640] >> Okay. Okay.

[00:47:24.240] Um

[00:47:26.080] >> I'm going to

[00:47:26.600] >> okay, we got about 5 minutes left on the

[00:47:27.960] proper live stream. Do we want to bring

[00:47:30.320] up Eugene to demo what he's working on

[00:47:32.040] and then we can like go over a little

[00:47:33.360] bit for questions?

[00:47:35.800] >> I'm almost done describing this

[00:47:37.480] workflow.

[00:47:38.840] So once this thing is done, now that we

[00:47:40.800] can get all the code out. So there's a

[00:47:42.480] couple key takeaways.

[00:47:44.040] Why do we not like JSON schema? Well,

[00:47:45.680] because JSON schema is going to be way

[00:47:47.080] more dense to go generate. I'll take the

[00:47:48.600] same thing and like let's just generate

[00:47:50.280] a JSON schema for this really fast.

[00:47:52.440] Just to give you an idea of what I mean.

[00:47:54.120] Give me a JSON schema for this. I'll

[00:47:57.440] generate a JSON schema really fast.

[00:47:59.760] And see what it does.

[00:48:01.840] Like this is the thing the model would

[00:48:03.200] have to generate.

[00:48:05.200] And like we can just

[00:48:06.520] look at this.

[00:48:08.560] >> Uh

[00:48:09.880] organizer. Like did it do it? Yes, at

[00:48:12.000] 333 tokens.

[00:48:13.960] But it's also way less legible about

[00:48:15.920] what's actually going on. This is a

[00:48:17.280] fairly simplistic schema.

[00:48:20.120] If I take the same thing and just like

[00:48:21.960] take this,

[00:48:23.200] I think we can all guess that this is

[00:48:24.280] less than 333 tokens, but we can just

[00:48:26.240] look at how many less.

[00:48:28.280] 69 tokens.

[00:48:29.760] >> And it's more information-rich, right?

[00:48:31.680] Like like the all of the like quotes and

[00:48:34.120] parentheses just kind of add noise.

[00:48:36.840] >> Exactly. And I did I did some cheating

[00:48:38.600] here. And like even now, uh even when I

[00:48:40.600] have extra white space here and way more

[00:48:42.240] white space than I actually would have

[00:48:43.560] if I were actually doing this, like I

[00:48:44.680] have used two white spaces,

[00:48:47.200] it doesn't even matter.

[00:48:48.000] >> Third the size or a fourth the size.

[00:48:50.280] >> We can just do the math, 333 / 86 /

[00:48:53.160] this.

[00:48:54.560] It's just like literally a fourth of the

[00:48:56.320] size.

[00:48:57.400] So, in general, if you're going to do

[00:48:58.880] dynamic schemas, you get way more

[00:49:00.320] accuracy not having to generate

[00:49:01.960] something that is four times as dense

[00:49:03.920] with way less information.

[00:49:06.520] >> This is also kind of like I think when

[00:49:07.920] they leaked the GP or not leaked, when

[00:49:09.280] the GPTO SS models came out, we saw that

[00:49:11.680] that their tool calling format wasn't

[00:49:13.560] actually They take a JSON schema from

[00:49:15.160] you over the API, but what they give to

[00:49:17.240] the model is actually more like

[00:49:18.920] something that's like a TypeScript-ish

[00:49:20.840] syntax, which has less requirements for

[00:49:23.560] like quotes and things like that cuz

[00:49:25.040] it's more concise, right? And that's

[00:49:26.360] what they are all on, I think probably

[00:49:27.920] for the same reason.

[00:49:29.440] >> Exactly. It's just you don't want

[00:49:31.040] something that's dense.

[00:49:33.080] Um

[00:49:34.320] So, like in general, the idea is like

[00:49:35.960] you want to have the model go generate

[00:49:37.400] your schemas. You want to then use your

[00:49:39.200] schemas for dynamic extraction of data.

[00:49:42.640] You might put a human review process at

[00:49:44.520] the point of generating the schemas, and

[00:49:45.880] you might build a custom type form-like

[00:49:47.600] thing to render your schemas in an

[00:49:48.920] interesting way.

[00:49:50.760] Um and you might also do a couple more

[00:49:52.840] things along the way to make your life

[00:49:54.640] easier as a developer.

[00:49:56.800] Um, for example, you might put a cash

[00:49:59.080] layer semantic cash layer that says,

[00:50:01.000] "For this type of image, this is a great

[00:50:02.920] schema." So, instead of generating a

[00:50:04.720] schema, you might recommend an existing

[00:50:06.440] schema to help the users minimize schema

[00:50:08.840] clash. You might build more workflows

[00:50:10.480] around merging schemas after a bunch

[00:50:12.920] have been generated. And these are all

[00:50:15.080] tools that you can build as an engineer

[00:50:17.560] based on the use case of your actual end

[00:50:20.000] users.

[00:50:20.720] >> And And we actually talked about this a

[00:50:22.160] lot in the episode where we talked about

[00:50:23.640] like taking a resume and mapping it like

[00:50:25.360] doing entity resolution and entity

[00:50:27.040] mapping, which is like over time you

[00:50:29.160] start to build up a set of entities or a

[00:50:31.080] set of schemas, a set of types that

[00:50:32.880] matter. And then when you do or doing

[00:50:35.000] something expected and there's a large

[00:50:36.600] drift or there's a new type of thing,

[00:50:38.320] that's when you can say, "Okay, this

[00:50:39.640] schema that we generated for an object

[00:50:41.320] that we've seen a lot of before is very

[00:50:43.760] different from all the other schemas

[00:50:45.280] we've seen. Let's like put that in a

[00:50:47.440] queue for human review." And you start

[00:50:49.800] making more concrete. Like over time

[00:50:52.400] it's just like, "Okay, yes, like we have

[00:50:54.840] seen every single version of the word

[00:50:56.920] Microsoft Corporation including Xbox,

[00:50:59.200] including Azure, including all the All

[00:51:01.080] these map to the same entity." And I

[00:51:03.000] think it's the same thing of like when

[00:51:04.200] we're generating schemas after off of

[00:51:05.960] arbitrary images or document scans or

[00:51:08.280] bank statements or whatever it is, over

[00:51:10.600] time you want to start consolidating and

[00:51:12.240] have be more opinionated on what it is.

[00:51:14.240] And then you want to have ways to

[00:51:15.600] incorporate if the standard changes, the

[00:51:17.520] AI can highlight, "Okay, here's what's

[00:51:18.840] different in this one." Human should

[00:51:20.480] review that. Should we add that to our

[00:51:21.840] whole schema or is that a sign that

[00:51:23.360] there's a bug in this document or a bug

[00:51:25.120] in the prompt or that the model

[00:51:26.400] regressed?

[00:51:28.000] >> Exactly that. Uh

[00:51:30.200] Exactly that. Um, and these are

[00:51:32.000] workflows. And you can build a I I It

[00:51:33.920] sounds like we can't get to the React

[00:51:35.040] workflow today, which is very

[00:51:36.280] unfortunate. Uh, we will do that in a

[00:51:38.120] second episode.

[00:51:40.120] I think it was Hopefully people didn't

[00:51:41.560] mind that we didn't

[00:51:42.120] >> didn't get the React component working.

[00:51:43.880] I knew it.

[00:51:44.840] >> worried about

[00:51:45.800] I'll show you the thing.

[00:51:47.200] >> All right, we'll do it. We'll do it.

[00:51:48.280] We'll do it on another episode.

[00:51:49.600] >> Actually getting it really close to

[00:51:50.760] working.

[00:51:51.680] >> Okay. Cool.

[00:51:53.400] >> Ed has a question real fast about any

[00:51:55.600] plans that help us to convert in JSON

[00:51:57.400] schema to BAML type builder?

[00:51:59.280] Um we have considered this very

[00:52:01.480] strongly. You should be I would be

[00:52:04.360] surprised if we ship it this week. I'd

[00:52:06.400] be surprised if we don't ship it by end

[00:52:07.880] of year.

[00:52:08.960] Uh is kind of the time frame that I

[00:52:10.680] would give. We think that there probably

[00:52:12.720] is a way to do JSON schema to BAML type

[00:52:15.040] builder more natively through like a

[00:52:16.640] native function that we support.

[00:52:18.720] Um the tricky part is there's just many

[00:52:20.720] many different ways that a schema can be

[00:52:22.560] converted

[00:52:23.840] because JSON schema is not very um

[00:52:27.880] descriptive on schemas in terms of how

[00:52:30.400] it does things. Um so we're thinking

[00:52:32.320] about the best ways to do conversions.

[00:52:34.360] And we're also thinking about adding a

[00:52:35.760] top-level dynamic type. So even the

[00:52:37.800] return type directly can be dynamic and

[00:52:39.600] you don't need anything statically

[00:52:40.760] defined.

[00:52:45.390] Um any more questions from the audience

[00:52:45.400] before we do any more demos? Eugene,

[00:52:47.320] what do you want to show us? Do you want

[00:52:48.360] to give us a quick TLDR before you show

[00:52:49.760] it off?

[00:52:50.320] >> Um first off, uh thanks to both you

[00:52:52.880] guys. Um

[00:52:54.480] but I have a BAML.

[00:52:57.200] Um I think

[00:52:59.400] the thing that sucks the most about BAML

[00:53:02.040] is you guys hide the magic

[00:53:05.120] someone putting in a prompt and then um

[00:53:07.920] it just does everything correctly.

[00:53:10.920] Um

[00:53:12.480] where like mistakes are impossible. I

[00:53:15.240] think removing process in general

[00:53:18.320] um where like, you know,

[00:53:21.520] often there's like a process that's good

[00:53:25.680] quite good for like 90% of people.

[00:53:29.200] And when you remove it, people kind of

[00:53:31.400] have to go for outcomes and it's that

[00:53:33.400] whole like

[00:53:34.600] Jevons paradox people like talk about,

[00:53:36.800] right? Where

[00:53:38.480] you get to try more things and people

[00:53:40.040] just work completely differently. They

[00:53:41.680] try ideas they would have never tried.

[00:53:44.600] Second, um

[00:53:46.440] Dex, uh I really appreciate um

[00:53:49.640] some of the stuff you've described for

[00:53:52.280] agents, like in terms of orchestration.

[00:53:55.960] I think you probably killed several like

[00:53:58.560] graph theory um like mathematicians

[00:54:03.080] with that stuff. Um

[00:54:05.880] cuz it was intense, but it was

[00:54:07.840] necessary. Um because um a lot of people

[00:54:12.440] um

[00:54:14.120] um there are like things that work and

[00:54:16.360] don't work.

[00:54:17.680] So, uh just wanted to thank you guys. Um

[00:54:21.400] for the stuff I wanted to show is um how

[00:54:24.840] we've been approaching some of this.

[00:54:27.280] Which is inspired

[00:54:28.240] >> got This is FYI, we've got 5 minutes and

[00:54:30.280] I have to go to a meeting.

[00:54:32.040] So, just want to give a heads-up

[00:54:34.160] on timing.

[00:54:34.680] >> I can hang out if you got to drop.

[00:54:36.520] So, first off, um

[00:54:38.840] for example, we follow we're big on

[00:54:41.280] workflows. Like Bezos and his whole

[00:54:44.640] like, you know, intentions don't good

[00:54:46.560] intentions don't works, mechanisms do.

[00:54:49.720] Uh we go harder. We'll just say like

[00:54:51.800] mechanize because if you do that, you

[00:54:55.120] know, worst case you'll fail, but

[00:54:57.720] most things can be and you start getting

[00:55:00.560] better at it and you kind of figure out

[00:55:03.000] the building blocks. So, for example,

[00:55:05.760] this is our spec for exposing like

[00:55:09.600] an MCP

[00:55:10.680] >> What what's up? Here, let me help you

[00:55:12.480] out. What's the problem you're trying to

[00:55:14.040] solve?

[00:55:15.360] >> What we're trying to solve here is we

[00:55:16.280] have our own custom product. It's kind

[00:55:17.200] of cloud codish.

[00:55:18.320] >> Oh.

[00:55:18.760] >> And we want to let other people use it

[00:55:21.400] via MCP.

[00:55:29.470] So,

[00:55:29.480] >> What what problem are you solving?

[00:55:31.880] >> Huh? Uh people suck at using cloud code.

[00:55:36.800] Uh they run out of array elements. They

[00:55:38.720] also scream that cloud code is lying to

[00:55:42.120] them.

[00:55:42.400] >> Let's Maybe we should talk about this on

[00:55:44.560] a different concept that's not about

[00:55:45.960] dynamic UI, then we can bring this back

[00:55:47.560] in that scenario in that case cuz it

[00:55:49.200] sounds not super related to the current

[00:55:51.440] topic.

[00:55:52.000] >> Um

[00:55:53.320] Sure. I just

[00:55:55.720] um

[00:55:57.120] That's fine.

[00:55:58.800] Um

[00:56:00.200] I just

[00:56:02.560] That That's fine.

[00:56:04.400] Um I just want to say that I think um

[00:56:07.200] generally people can think and discuss

[00:56:10.680] more than one thing and like this isn't

[00:56:14.920] um

[00:56:15.760] you know, a one-track course, but it's

[00:56:18.360] not my thing, so that's fine.

[00:56:20.840] >> Let's do it Let's do this on an episode

[00:56:22.680] when we're talking about cloud code and

[00:56:23.960] like general like how to write workflows

[00:56:25.680] better in that world.

[00:56:27.200] >> Um

[00:56:28.800] Okay. It was going to be a short thing,

[00:56:30.720] but that's fine. No worries.

[00:56:32.680] >> Let's keep it on topic. But let's get

[00:56:34.600] you on on a different episode when we

[00:56:35.760] talk about cloud code.

[00:56:37.640] >> Uh you said that last time, so um

[00:56:40.880] anyway, it's fine.

[00:56:43.280] I'm more interested in like customers

[00:56:46.880] than

[00:56:48.240] um that this helps customers

[00:56:51.200] um

[00:56:52.160] So, can I If you don't mind, I just want

[00:56:55.400] to finish because this was written by my

[00:56:57.600] co-founder. He doesn't write

[00:57:00.320] He's not a web developer.

[00:57:02.480] Um he doesn't know anything about this.

[00:57:05.080] He wrote this

[00:57:06.120] keywords.

[00:57:06.720] >> Let's just keep going with it. Bye, Bob.

[00:57:08.000] You got to drop. I'll hang out with this

[00:57:09.360] on the stream.

[00:57:10.720] >> Yeah. So,

[00:57:12.360] this is an RFC, right?

[00:57:15.600] And it's better than anything most I've

[00:57:18.280] written.

[00:57:20.000] But it's all spec'd.

[00:57:22.240] from a YAML.

[00:57:24.000] We used to do YAML, then we switched to

[00:57:26.400] Zod.

[00:57:28.240] Um

[00:57:29.480] and um it's nicely rendered both for

[00:57:32.720] humans

[00:57:33.800] and machines.

[00:57:35.640] Um, source tracing and the beauty of

[00:57:38.920] this is that um

[00:57:41.080] it lets people who you know

[00:57:43.760] know how to solve problems skip the skip

[00:57:46.200] the process and just get outcomes. So,

[00:57:48.760] that's all I wanted to say. Sorry.

[00:57:50.760] >> Okay, so this is basically for people

[00:57:52.320] who are a little less technical. You've

[00:57:54.480] written a system where people someone

[00:57:56.240] who's less technical can build out an

[00:57:57.680] ADR.

[00:57:58.960] >> This guy made the Kindle. So, I think

[00:58:01.600] you have to have like problem-solving

[00:58:03.480] kind of mindset. But, it's more like you

[00:58:06.640] don't have to become a language lawyer

[00:58:09.000] in some you know react or view or

[00:58:12.600] MongoDB or whatever.

[00:58:14.840] >> Okay, cool. Where can people learn more

[00:58:16.600] about this? Is this open source

[00:58:18.000] anywhere?

[00:58:19.640] >> We're trying to open source it as

[00:58:21.120] quickly as possible because

[00:58:24.240] um, this stuff should be open source

[00:58:26.920] because if it's not inference gets

[00:58:29.520] wasted.

[00:58:31.080] Where Well, essentially you're having

[00:58:33.720] like you're asking Einstein

[00:58:37.000] hey, count my loose change.

[00:58:39.760] >> Every single day over and over and over

[00:58:42.000] again.

[00:58:42.680] >> it hurts me. So, that's why we want to

[00:58:46.040] like

[00:58:47.160] um, make that stop

[00:58:49.480] uh cuz there's so much better to go for.

[00:58:51.560] So, so I guess sorry.

[00:58:53.560] >> let's let's say you know when when this

[00:58:55.160] actually um, is open source and you can

[00:58:57.280] go a little bit deeper and show some of

[00:58:58.720] the code. I think it would be really

[00:58:59.920] cool to do a little bit of a deeper

[00:59:01.120] dive. How's that sound?

[00:59:02.080] >> Yeah, I'm happy to go on the code. We

[00:59:04.120] have uh customers and um, whatever

[00:59:07.880] if you guys anyone has feedback of what

[00:59:10.880] people feel is most valuable to open

[00:59:13.200] source like in what order.

[00:59:16.080] Um, we're more than open to feedback and

[00:59:18.400] we're like self-funded here. So, we can

[00:59:20.880] do whatever we want like

[00:59:23.640] >> Cool. I mean, this sounds

[00:59:25.000] >> 2011.

[00:59:26.920] >> This sounds like a great thing to drop

[00:59:28.600] like maybe have a discussion in the

[00:59:30.560] boundary ML discord about and like work

[00:59:32.840] a little bit a sync and people can can

[00:59:34.840] kind of like chat about and you can

[00:59:37.040] maybe just describe it and we can we can

[00:59:38.920] start to build momentum for for a future

[00:59:40.880] conversation. That sounds really fun.

[00:59:42.720] >> Yeah, thank you. And of course

[00:59:44.840] couldn't have been possible without

[00:59:47.520] like Baml. I think we all build kind of

[00:59:50.040] on the shoulders of giants like people

[00:59:52.640] who came before us. So

[00:59:55.000] >> Yeah. Sorry I pointed to myself cuz I

[00:59:56.760] also build on the shoulders of giants. I

[00:59:58.600] was I wasn't trying to say I was the

[01:00:00.440] giant and here's who the giant is.

[01:00:02.240] >> I'm taller and taller.

[01:00:03.640] >> I feel

[01:00:04.440] like a [ __ ] So uh

[01:00:07.360] >> Yeah, we should find a I don't think

[01:00:08.520] there's any photos of you and me hanging

[01:00:10.040] out um and maybe we should keep it that

[01:00:12.040] way.

[01:00:16.590] >> I'm Roger Federer.

[01:00:16.600] >> I'm going to stay for one more question.

[01:00:18.440] >> Cool.

[01:00:20.200] I was like, wait a minute. That's not

[01:00:21.360] you I we don't that's not our DM. Our DM

[01:00:23.320] has way more memes in it. Okay. Bye Bob,

[01:00:25.480] you're late for a call. This was

[01:00:26.840] awesome.

[01:00:27.360] >> you at all.

[01:00:28.920] >> Wait, really? Peace y'all. See you next

[01:00:30.600] week.
