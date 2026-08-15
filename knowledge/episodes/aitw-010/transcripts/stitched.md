# S02E06 – Entity Resolution: Extraction, Deduping, and Enriching



Source: YouTube captions (automatic:en)



[00:00:04.070] Um, okay. So, a lot of you have been

[00:00:04.080] here before, some of you are new. Uh,

[00:00:05.839] this is AI that works, where me and Vibb

[00:00:08.240] talk about AI that works. Uh, it's a

[00:00:11.440] very, uh, straightforward title. Um, my

[00:00:14.240] name is Dex. I'm the founder of a

[00:00:15.920] company called Human Layer. We help

[00:00:17.199] people build better, safer, more

[00:00:18.960] interesting, more useful agents. Um, and

[00:00:22.320] Vibb, I'll let you do your intro. Cool.

[00:00:25.439] I'm Vibb. I'm Vibb. Um, I work on BAML

[00:00:29.359] and if you don't know what BAML is,

[00:00:31.039] check it out. It's an interesting way to

[00:00:33.120] use LMS in a way that's kind of fun.

[00:00:37.040] With that, yeah, today we're going to

[00:00:39.440] talk about entities and entity

[00:00:41.520] resolution and dduping and resolving.

[00:00:44.399] And um I think we've got a pretty

[00:00:46.160] interesting kind of like it's it's kind

[00:00:48.000] of a toy use case, but I think it really

[00:00:49.760] will demonstrates really well some of

[00:00:51.760] the um kind of core ideas there and um

[00:00:55.120] will be a fun thing that you can pick up

[00:00:56.800] and we'll try to keep it simple enough

[00:00:58.079] that you can pick it up and run with it.

[00:00:59.600] Um this meeting is being put it in your

[00:01:01.920] own put it in your own code and then um

[00:01:05.199] we will push all the code that we write

[00:01:06.720] today as well. All right. So what is

[00:01:10.960] entity resolution? What is entity

[00:01:12.799] duping? Um, and how are all these terms

[00:01:15.439] kind of related? I think that's the

[00:01:16.640] first thing I want to start with over

[00:01:18.000] everything else. So, I'm going to screen

[00:01:19.600] share. I'm going to talk about uh empty

[00:01:21.840] resolution. I realized I need my mic or

[00:01:23.759] my mouse for today.

[00:01:31.429] All right. Well, he's getting that. Oh,

[00:01:31.439] he's back.

[00:01:34.079] All right. So really quickly, I think a

[00:01:37.280] lot of people mix up entity resolution

[00:01:39.040] to these smaller problems into a giant

[00:01:41.360] problem and that makes the problem much

[00:01:42.799] much harder. So I'm going to really

[00:01:45.119] quickly clarify exactly what we're going

[00:01:46.720] to go cover and what we're going to talk

[00:01:48.000] about.

[00:01:50.079] So step one is we always have entities.

[00:01:53.280] So we have like some sort of name that

[00:01:55.439] we want to extract or some class of

[00:01:56.960] names that we want to pull out. So the

[00:01:59.119] most common example that I think

[00:02:00.240] everyone can relate to is let's say

[00:02:01.920] company names. I have a database of

[00:02:04.479] people that are registered that I know

[00:02:06.000] about that are legal entities of

[00:02:07.680] companies and I want to say that no

[00:02:09.440] matter what someone says I want to pull

[00:02:10.959] out that sort of data and there's

[00:02:13.120] different ways that we can go about this

[00:02:14.560] problem. So let's take a couple sample

[00:02:16.879] names so we all can think about this. So

[00:02:18.959] someone might write the word Xbox

[00:02:21.599] someone might write the word MSFT when

[00:02:23.840] talking about the stock price ticker.

[00:02:25.599] Someone might write the word Microsoft.

[00:02:34.150] um someone might misspell Microsoft

[00:02:34.160] and we might even have other things like

[00:02:36.400] um Microsoft Inc. uh or whatever they're

[00:02:39.680] called. All of these kind of map to the

[00:02:42.720] same entity as far as I'm concerned

[00:02:45.120] assuming that I don't care about

[00:02:46.160] subsidiaries. I'm going to make that

[00:02:47.440] claim right now. And they all kind of

[00:02:49.840] map to this entity that I have

[00:02:51.440] specifically. This entity isn't just a

[00:02:53.120] plain entity. I also often have some ID

[00:02:55.120] attached to it in my database that is

[00:02:57.360] very very specific.

[00:02:59.519] And what I want to be able to do is

[00:03:01.120] somehow get this information out. Now,

[00:03:03.840] there's two different problems that

[00:03:05.200] exist in here. And we're going to skip.

[00:03:07.040] And there's one last problem that we

[00:03:08.159] didn't mention, I guess. Uh, enriching.

[00:03:12.720] Um, so in this case, we're dduping

[00:03:15.440] entities. So no matter what everyone

[00:03:16.800] says, we're going to spit out the same

[00:03:17.920] ID. We're resolving them to the same

[00:03:19.840] exact entity, and we're going to extract

[00:03:21.360] this data out of it. So we want to

[00:03:22.720] extract from whatever information the

[00:03:24.640] model gives us this independent process.

[00:03:29.200] Now there are a couple ways that we can

[00:03:30.720] go do this. We can prompt our way to

[00:03:32.720] trying to do this. We give it the LLM

[00:03:35.360] all of the companies and we say only use

[00:03:37.920] this list of companies. Yeah. What's the

[00:03:40.319] what's the naive approach to this? I

[00:03:42.159] guess like what does that look like?

[00:03:43.360] Like what similar to like the

[00:03:44.640] classification problem, right? Let's

[00:03:46.560] write the let's write the function

[00:03:47.760] signature because I think that helps.

[00:03:49.280] Def. Yep.

[00:03:52.480] D and we'll we'll assume we're going to

[00:03:55.200] extract a single entity for now. We

[00:03:56.959] might have multiple but we'll take that

[00:03:58.480] out. Uh input will be a string and the

[00:04:01.599] output will be an entity type. Um an

[00:04:05.840] entity type

[00:04:13.270] will have a name stir which doesn't

[00:04:13.280] really matter and some ID that is like

[00:04:14.799] some sort of database ID that does

[00:04:17.680] matter. And the most naive way to do

[00:04:20.079] this is my function will also take in a

[00:04:23.520] uh list of entities.

[00:04:27.199] And I ask super dumb. I just ask Alm to

[00:04:30.960] pick one of these. So I can write

[00:04:33.199] something like this. Pick best choice

[00:04:45.430] equals ask lm input options. And I'm

[00:04:45.440] certain many of us can write a prompt to

[00:04:47.040] go do this. This isn't that interesting.

[00:04:49.280] The next level of uh complexity that we

[00:04:51.919] can add is we can say now if best choice

[00:04:56.320] not in options for some sort of stir

[00:04:58.639] match function

[00:05:00.800] or some sort of match function that we

[00:05:02.320] write return none

[00:05:05.360] else

[00:05:07.360] best return best choice. So now we've

[00:05:11.039] done Go ahead. And this could even be a

[00:05:13.919] place where you would incorporate some

[00:05:15.280] of those um the stuff we talked about in

[00:05:17.759] the eval episode of like having runtime

[00:05:19.759] guards of like Okay, cool. We know for

[00:05:22.000] sure that it has to be in this list. So

[00:05:23.600] if it's not, we just kind of like add

[00:05:25.840] more error context to it and ask the LM

[00:05:28.160] to try again at least once. Yeah. So we

[00:05:30.479] could exactly we could be like oh um we

[00:05:33.120] could literally just do it like try

[00:05:34.639] again. It's like we could put a thing

[00:05:38.000] here. is like num tries

[00:05:42.639] equals

[00:05:45.280] uh int

[00:05:48.080] equals like three by default.

[00:05:52.160] Uh if

[00:05:55.520] if num tries

[00:05:58.479] less than uh greater than zero

[00:06:02.880] return.

[00:06:07.909] We just recursively call itself and you

[00:06:07.919] should do recursion but for now

[00:06:21.510] um so we could do this uh we could go

[00:06:21.520] escalate to a human. We can do all these

[00:06:23.199] things that we want to go do in here.

[00:06:25.759] But there's a couple other reasons that

[00:06:27.199] it might not exist. There are other

[00:06:28.960] reasons that it might not exist such as

[00:06:30.319] like our entities array itself might be

[00:06:32.080] incomplete. Like imagine that in

[00:06:34.960] Microsoft case, great. We can we can

[00:06:36.880] scrape the S&P 500. We can get all the

[00:06:38.800] top businesses that we know about and we

[00:06:40.720] pass them into here. But in Microsoft's

[00:06:43.520] case, we might actually run into an

[00:06:44.960] issue where let's say someone's looking

[00:06:47.039] for the company Human Layer. Human Layer

[00:06:49.360] probably doesn't exist in most public

[00:06:50.960] registries yet. And I say yet, it will

[00:06:53.360] in about a year or two. Whoa, buddy.

[00:06:55.360] We're on Crunch Base. That's true. Um,

[00:06:58.400] but uh if you're on there, you might not

[00:07:01.120] find the right entity because it's just

[00:07:02.560] missing information. You might want to

[00:07:04.560] have an option to enrich data.

[00:07:08.479] So, you might want to actually consider

[00:07:10.240] enriching your options array itself over

[00:07:12.400] here and then updating your options

[00:07:14.080] array for next time around. And the

[00:07:16.240] options for enriching are kind of what

[00:07:17.680] you said, Dexter. You could escalate to

[00:07:19.360] a human to go enrich it. You can

[00:07:21.680] escalate for another pipeline that's

[00:07:23.840] completely independent that scrapes the

[00:07:25.199] web and searches for everything along

[00:07:26.800] that lays and builds a list of

[00:07:28.479] candidates and then passes off to a

[00:07:30.319] human or does it yourself.

[00:07:33.199] Or you can always just sorry one more

[00:07:36.000] thing

[00:07:38.080] or you can just do the thing that we did

[00:07:40.000] in this current code which says we will

[00:07:41.840] do nothing and we'll just return none in

[00:07:43.520] that scenario. So there's it's kind of

[00:07:46.000] up to the caller to decide what to do if

[00:07:48.479] it's none. Exactly. It's your choice how

[00:07:50.880] much rigor you want to have on your

[00:07:52.240] pipeline, how much automation you add in

[00:07:54.560] this process. But the actual process of

[00:07:56.960] entity extraction, as it turns out, like

[00:07:58.960] this this method of doing this, I find

[00:08:01.440] this to be a little bit easier than um

[00:08:04.000] than even this goes along. And I think

[00:08:05.759] actually the best way to show this is

[00:08:07.520] code, not even whiteboarding. Uh because

[00:08:10.240] it's surprisingly very very

[00:08:12.479] straightforward. So let's just go ahead

[00:08:14.720] into the AI that works repo. Um, cd

[00:08:18.479] repos

[00:08:42.070] Okay, clear. Okay. Um ls maker

[00:08:42.080] 2025 06

[00:08:44.640] 17

[00:08:46.320] uh entity extraction

[00:08:54.389] let's see

[00:08:54.399] cool uh uv init and then uv add baml-py

[00:09:00.320] oops

[00:09:05.670] uv

[00:09:05.680] we run baml cli test sorry we do this

[00:09:08.080] usually ahead of time, but Oh, it

[00:09:12.560] all right. It's good. This demonstrates

[00:09:14.640] how easy it is to do this. And while

[00:09:16.480] he's doing that, Derrick, you had a

[00:09:17.839] question?

[00:09:24.630] Yeah, I was just gonna maybe if it if I

[00:09:24.640] could take the liberty to add like a use

[00:09:26.480] case in real world where I've done this

[00:09:29.440] kind of with TF diff and Excel as human

[00:09:32.160] in the loop when it didn't get above a

[00:09:34.160] threshold match which now I can see

[00:09:36.720] these identified pipelines being another

[00:09:39.360] level. So I tried to take like a

[00:09:41.680] deterministic approach with a threshold

[00:09:43.760] first and then fall back to like this

[00:09:46.160] type of thing. Anyway, long story short

[00:09:48.160] was a Barnes & Noble Digital Nook. They

[00:09:51.040] they had like so many uh contracts with

[00:09:54.240] Adobe. And so they had a a database of

[00:09:57.279] contracts of 10,000 contracts they had

[00:09:59.519] that they some of them were were weren't

[00:10:02.480] assigned to people. Some they were

[00:10:03.920] paying and not using. And uh we did this

[00:10:08.800] process to align all of the Adobe Adobe

[00:10:11.360] systems, Adobe, you know, into basically

[00:10:14.640] Adobe products and Adobe consulting and

[00:10:18.160] literally took like it turned out there

[00:10:20.160] were 40 kind of unique like contracts

[00:10:23.040] under different things that weren't

[00:10:24.560] visible and brought them all into those

[00:10:26.959] two categories. So they had a total

[00:10:29.200] aggregate view of their Adobe spend.

[00:10:31.519] They found the ones that had no owner

[00:10:33.760] and that they could actually save and

[00:10:36.079] that like five or 10 minutes paid for

[00:10:38.399] our project. Nice. Um so I just wanted

[00:10:41.440] to mention this is like type of things

[00:10:43.839] that you could use this and I could give

[00:10:45.360] other examples. Uh yeah I think

[00:10:48.000] resolving something to the same shared

[00:10:50.000] ID is generally useful when things have

[00:10:52.079] many many multitudes of inputs. It's a

[00:10:54.240] very very general problem and I think

[00:10:55.760] the problem that we're going to talk

[00:10:56.880] about today is one that should be

[00:10:58.640] obvious to everyone which is like

[00:10:59.760] resumes. Obviously, if I have a Caner

[00:11:02.000] database, how many of you use some ATS

[00:11:03.600] system and you just want to search for

[00:11:05.200] the person that works in my shop at

[00:11:06.320] Amazon? Like people wrote like AWS or

[00:11:08.160] something else that isn't really

[00:11:09.120] relevant, but really I just want to

[00:11:10.959] search for all employees of Amazon. I

[00:11:12.560] know when we go and hire people, we

[00:11:14.240] always look for people by candidate

[00:11:16.000] references of different companies,

[00:11:17.360] different backgrounds, different skill

[00:11:18.560] sets. Like for example, I wrote CV

[00:11:20.880] engineer, but I just want to look for

[00:11:22.000] people that have computer vision

[00:11:22.959] expertise. that's going to be hard to go

[00:11:25.040] find unless I can do some sort of

[00:11:26.959] resistant entity resolution. Like skills

[00:11:30.959] tags are another example of where you

[00:11:32.560] want to do entity resolution. You want

[00:11:34.160] some level of entities that are well

[00:11:35.839] known, well established, and highly

[00:11:37.360] useful. And you also want to have

[00:11:39.279] adaptability of that. For example, in

[00:11:41.360] this case, Boundary ML should be its own

[00:11:43.760] entity, but likely that a database won't

[00:11:46.320] have that on day zero. So, I want to be

[00:11:48.480] able to track and amend my entities

[00:11:50.640] database while I go do this. And that

[00:11:52.720] part is the part I think that makes this

[00:11:54.240] problem so interesting and so

[00:11:55.519] fascinating. It's not merely by

[00:11:57.200] extracting.

[00:11:58.800] It's about how do you build and maintain

[00:12:00.720] an entity database that is changing ever

[00:12:03.040] so often all all the time. And I think

[00:12:06.399] that's the problem that we should dive

[00:12:07.600] into today. Cool.

[00:12:10.959] Well, let's look at this code. So in

[00:12:12.160] this case, I have something really

[00:12:13.120] really simple. I have a thing that is a

[00:12:15.279] functional extract resume. It's going to

[00:12:16.560] extract a resume from uh this place and

[00:12:19.360] we're just going to have experiences.

[00:12:21.279] But now I want to go do this. I'm going

[00:12:22.800] to go add some um test cases really fast

[00:12:26.240] just so I know because I know that this

[00:12:28.079] is going to be a problem. I want this to

[00:12:30.800] be Microsoft obviously. Um I'll put like

[00:12:33.680] GCP.

[00:12:35.200] Uh and hopefully we'll figure out what

[00:12:36.959] it figures out on there. Um and I

[00:12:39.519] specifically left ambig ambiguous

[00:12:43.440] uh ambiguous uh so I know what it is. Um

[00:12:47.360] and now let's go play around with this.

[00:12:49.120] Obviously, if I go do this, it's not

[00:12:50.880] going to work off the top of my off the

[00:12:52.800] top of my head. If I just say like at

[00:12:54.880] description get the real company name

[00:12:59.519] legal

[00:13:01.519] legals name.

[00:13:04.079] Uh, let's run this.

[00:13:09.509] And like it did some stuff. It did

[00:13:09.519] Alphabet Inc., it did Microsoft. And

[00:13:11.200] like if I spin it down to GPT4 mini, who

[00:13:13.200] knows? Maybe this will work, maybe it

[00:13:14.399] won't. It kind of did, but there's no

[00:13:17.200] guarantee. I'm really relying on the

[00:13:18.800] vibes of the LM to hope that I get this

[00:13:21.279] correct. And I think that's the thing

[00:13:22.800] that we should go up take upscale a

[00:13:24.720] little bit. So let's just make this an

[00:13:26.320] experience data model.

[00:13:31.910] And I'm just going to focus on company

[00:13:31.920] and title. I won't even add anything

[00:13:33.760] else. Description.

[00:13:36.399] I don't need this.

[00:13:38.800] The legal

[00:13:41.519] company name.

[00:13:43.519] And this will kind of work

[00:13:46.240] I think but it really didn't like Google

[00:13:48.480] isn't actually a legal company name.

[00:13:49.680] Neither is my shop. It's actually like

[00:13:51.040] my shop inc or something else. So let's

[00:13:53.040] make another object in here to help the

[00:13:55.120] model really understand what we mean.

[00:13:58.079] Name

[00:14:00.639] as verbatim

[00:14:07.750] batum from

[00:14:07.760] content.

[00:14:09.360] uh legal name

[00:14:15.030] um

[00:14:15.040] is subsidiary.

[00:14:17.360] Let's just know if it's a subsidiary

[00:14:18.720] really fast. Mhm. And let's run this.

[00:14:28.150] Cool. Uh it pulled this out. This is for

[00:14:28.160] viob resume. Let's run the other test

[00:14:29.839] case now, the ambiguous one,

[00:14:33.040] and see what it does. The ambiguous test

[00:14:35.120] case, you remember, has boundary ML,

[00:14:36.639] GCP, and Xbox. GCP legal name Xbox and

[00:14:40.079] it it's really not understanding what I

[00:14:42.160] want. So let's do the first thing and

[00:14:43.839] just like beef up the model.

[00:14:50.550] Uh really not understanding what I want

[00:14:50.560] either. Um name I'm telling you man peak

[00:14:54.079] peak working hours they make all the

[00:14:55.600] models dumber. It's my new conspiracy

[00:14:58.160] theory. Uh let's get rid of is

[00:15:00.560] subsidiary and then let's ask legal

[00:15:02.320] name. What I want to know is if

[00:15:04.160] available

[00:15:06.000] best guess at the legal name of the

[00:15:09.440] company

[00:15:17.189] and we might find that we actually it's

[00:15:17.199] interesting right we immediately got

[00:15:19.519] Microsoft Corporation Google LLC and

[00:15:22.079] Boundary ML Inc. which is not the real

[00:15:24.320] name. So now let's go over here. Company

[00:15:26.639] type uh wellestablished well-known

[00:15:36.710] uh startup because those are really the

[00:15:36.720] two established companies that I might

[00:15:38.639] have. So let's just go and establish

[00:15:40.639] this. Yeah, because you kind of and

[00:15:43.120] that's basically you're helping to

[00:15:44.399] filter between like how likely is this

[00:15:46.399] to be something that the model made up?

[00:15:48.800] Because if the model doesn't pick well

[00:15:51.040] known then it's more likely that it's

[00:15:52.800] not in the training set basically right

[00:15:55.600] or owning

[00:15:58.399] exactly and now we're noticing it's

[00:16:01.360] listing on Google cloud platform um and

[00:16:04.079] then we can say we can add more uh

[00:16:07.600] well let's add another one known

[00:16:10.480] subsidiary which I think is good

[00:16:14.800] over here if

[00:16:18.480] If well known

[00:16:29.189] of

[00:16:29.199] the owning company. So let's read my

[00:16:30.720] prompt really fast. What I have out here

[00:16:32.639] I changed my data model. The name I

[00:16:34.160] still want to be verbatim from the

[00:16:35.519] content. Then I want it to tell me that

[00:16:36.959] what company type I am. I'm either

[00:16:38.959] wellknown a well-known subsidiary or a

[00:16:42.160] startup. And then I want to tell me in

[00:16:44.480] the legal name, I want it to actually

[00:16:46.320] tell me if it's well-known, best guess

[00:16:48.800] of the legal name of the company. If

[00:16:50.480] it's a well-known subsidiary, best case

[00:16:51.920] of the owning company. So I'm actually

[00:16:53.199] being very deliberate with the actual

[00:16:56.240] model itself. And I'm actually going to

[00:16:58.560] make this an optional field because in

[00:17:00.079] the case of a startup, I don't want to

[00:17:01.759] spit out a legal name.

[00:17:12.390] Okay. So this is almost like forcing a

[00:17:12.400] very specific flavor of reasoning onto

[00:17:15.280] the extraction process. Exactly. And you

[00:17:17.760] can see now the model is actually like

[00:17:19.280] kind of understanding what I want to do

[00:17:20.640] a lot better.

[00:17:22.559] Um and it's actually spinning out what I

[00:17:24.480] want. Now this is only half the battle

[00:17:26.720] because at this point I now have

[00:17:28.000] something. Let's just see if GP4 mini

[00:17:29.679] works really fast. Why not? Right. This

[00:17:32.320] doesn't let you leverage your database

[00:17:34.799] of named entities and it doesn't let you

[00:17:36.559] evolve the database over time. Exactly.

[00:17:39.039] And we can see that hey GCP uh a

[00:17:42.320] well-known um

[00:17:44.880] what's it called well-known subsidiary

[00:17:46.559] is probably not working as well uh or

[00:17:49.360] like uh like GCP isn't working as well

[00:17:51.840] in G uh GP uh GP 40 because 40 Mini

[00:17:54.960] still says Google Cloud Platform. Yeah,

[00:17:57.120] but that's okay. We actually don't want

[00:17:59.520] to worry about that too much because we

[00:18:01.039] could spend forever prompting this or we

[00:18:03.200] can add a multiaceted approach to go

[00:18:05.200] solve this problem. Cool. So let's take

[00:18:07.280] a look at what that approach would look

[00:18:08.559] like.

[00:18:10.320] So now what we're going to do is do

[00:18:11.840] something like this.

[00:18:31.270] I'll put I'll put a real example here.

[00:18:31.280] Um, I'll just take this example. As I

[00:18:33.120] said,

[00:18:40.630] also be interesting to see this with

[00:18:40.640] like the actual raw text from like a

[00:18:43.200] real resume rather than this little like

[00:18:45.120] fake markdown thing. I will Yeah, I'll

[00:18:47.440] do that in a second. Um, I just think

[00:18:49.200] it's I like to use toy examples because

[00:18:51.440] then we don't have to all digest all the

[00:18:52.960] examples at first. Yeah, like resume

[00:18:55.760] equals this. Cool. So now we have a

[00:18:57.679] resume and what we're going to do now is

[00:18:59.440] we're actually going to go access all

[00:19:00.960] the experiences

[00:19:02.720] for company in

[00:19:06.640] for EXP

[00:19:09.039] exp.

[00:19:15.350] No, there's a company type. Oh, I have

[00:19:15.360] to set up my UV environment.

[00:19:17.840] U packetic.

[00:19:26.150] This is a company type for company dot

[00:19:26.160] uh let's say legal name. So I want to

[00:19:28.720] first get the legal name. So I'm going

[00:19:30.080] to do a couple of things um and be like

[00:19:32.480] uh in uh extract companies in here. So

[00:19:36.640] company

[00:19:39.120] exp.

[00:19:42.000] Okay. What I'm going to do over here is

[00:19:43.600] first I'm going to go ahead and actually

[00:19:44.880] get the actual type of the company.

[00:19:47.039] match exp

[00:19:53.190] type

[00:19:53.200] case

[00:19:54.880] uh startup I don't really care and I'll

[00:19:58.880] just like print it out and I don't

[00:20:00.400] really want to do anything

[00:20:02.880] uh I don't actually know if I have to

[00:20:04.080] break I might have to

[00:20:07.360] okay

[00:20:09.600] do nothing in fact I might even want to

[00:20:11.679] do one more thing where I like

[00:20:12.960] specifically will set the legal name of

[00:20:14.640] the company explicitly to none

[00:20:18.080] because I do not want in the case of a

[00:20:20.400] startup, even if the LM hallucinates

[00:20:21.840] something, I'm just going to ignore it.

[00:20:22.960] It doesn't matter to me. It's like it's

[00:20:24.799] garbage data. If it's a well-known

[00:20:27.679] company, um I'm going to see if it has a

[00:20:29.919] legal name.

[00:20:32.320] Uh if it if it does if it doesn't have a

[00:20:35.039] legal name and it's a well-known

[00:20:36.240] company, I might figure out um to do ask

[00:20:40.320] an LM

[00:20:42.799] else. Now if I have to go do this now I

[00:20:45.520] want to do the next thing which is

[00:20:46.400] validate names

[00:20:48.720] which I will do is like validate company

[00:20:53.039] which I'll take in the exp company

[00:20:54.880] itself and I want to go validate this

[00:20:56.559] somehow.

[00:20:58.960] Now what I will do over here is write a

[00:21:00.880] validate function.

[00:21:10.070] There you go. And the way I'll validate

[00:21:10.080] this is I'll assume that I have a list

[00:21:11.600] of companies def load companies.

[00:21:16.000] Um, and what this will return is this

[00:21:19.120] will return a list of tupils. Oops.

[00:21:24.799] Of like name,

[00:21:27.840] comma, like legal name

[00:21:31.280] or like maybe I'll what I'll do is

[00:21:32.640] actually something slightly different.

[00:21:33.600] Sorry. legal name and then also return a

[00:21:37.840] list of actual descriptions about that

[00:21:40.640] company. So in the case of Go ahead. Are

[00:21:43.919] we going to end up doing something

[00:21:44.799] similar to what we did in the

[00:21:46.080] classification where we kind of have a a

[00:21:48.000] internal class that our program manages

[00:21:50.480] and controls the view that is like what

[00:21:53.840] the database sees versus what the LM

[00:21:55.760] sees versus what the what the code sees.

[00:21:58.320] Exactly. It's a very very similar

[00:21:59.919] pattern but it's slightly different. In

[00:22:02.320] the case of what I will be doing here is

[00:22:04.000] I'll say like company valid equals load

[00:22:08.799] companies

[00:22:10.320] valid companies both this and then for

[00:22:13.440] valid company invalid companies I'm

[00:22:16.400] going to just see if the legal name

[00:22:19.600] of this thing that I have over here

[00:22:22.400] matches this. If the legal name is

[00:22:25.440] coming in my database I am good. That

[00:22:27.919] doesn't Okay. So, so it's almost like a

[00:22:29.679] a group by where you have the where you

[00:22:32.480] have like an index from legal name to

[00:22:34.559] all of the known company names

[00:22:36.960] basically. Exactly. Exactly. And in the

[00:22:40.159] case of me not finding some valid

[00:22:42.240] company that I like, then what I will do

[00:22:44.640] after this is now I need to to do ask an

[00:22:49.039] LLM

[00:22:51.280] to update

[00:22:53.520] uh ask an LLM to

[00:22:57.760] uh update the company to find. Yeah, you

[00:23:01.679] have a lot of ask LLMs in here and I'm

[00:23:04.080] not they seem to be different things in

[00:23:07.200] different parts of the workflow. Yeah.

[00:23:09.039] So, I'm just writing to-do comments

[00:23:10.240] here. But what I want to do is I'm just

[00:23:11.600] going to load all the companies from my

[00:23:12.720] database and if I find if I find one it

[00:23:15.760] matches the legal names that I am aware

[00:23:17.600] of in my database, I'm good. If I'm

[00:23:20.720] unable to find one, then what I want to

[00:23:23.760] do is I want to ask the LM. So in this

[00:23:25.280] case, it's been out Google Cloud

[00:23:26.559] Platform. So I literally just dump the

[00:23:28.559] valid companies into my uh LLM and ask

[00:23:32.960] them to pick one. I basically turn this

[00:23:34.640] problem into a classification problem.

[00:23:37.600] Why not just dump the list of valid

[00:23:39.440] companies in any like at the start in

[00:23:42.559] the original prompt? Well, a couple of

[00:23:44.880] reasons for that and I think that's a

[00:23:46.240] really really good question. Well, one

[00:23:48.159] of them is I can get a good bang for my

[00:23:51.120] buck without doing that. Like I see you

[00:23:54.080] use the cheap model with a small prompt

[00:23:56.240] and like a lot of times it will just get

[00:23:58.159] it right. Exactly. And then if you're if

[00:24:00.640] you're any reasonably sized company,

[00:24:02.240] your ATS of legal companies that you're

[00:24:04.480] going to be hiring from is going to be

[00:24:06.080] massive.

[00:24:08.400] Just has to be by definition. So

[00:24:11.679] instead, okay, so you're you're just

[00:24:13.120] like pre-optimizing this basically,

[00:24:14.640] right? like our our normal advice is

[00:24:16.080] like use the biggest model and the

[00:24:18.240] biggest prompt and the most powerful

[00:24:20.080] thing first and then break it down when

[00:24:21.919] it becomes a performance bottleneck. But

[00:24:24.159] in this case, you're just saying like

[00:24:26.080] I'm going to actually start with a

[00:24:27.840] smaller tighter tighter model and then

[00:24:29.840] zoom back out to a bigger model if I

[00:24:32.000] don't find something that kind of

[00:24:33.039] matches my expectations. Yes. And then

[00:24:35.440] one last caveat is that like I can't

[00:24:37.520] actually put together my actual um I

[00:24:42.159] can't fit all the companies I know about

[00:24:44.240] into the prompt. I know that from the

[00:24:46.480] get. I see. Yeah. Right. Like we all

[00:24:48.559] know that from the very beginning. We

[00:24:50.000] can't do that. Like for this problem of

[00:24:52.400] extracting resumes. It's not possible

[00:24:53.919] for the PDF contract problem. It's not

[00:24:56.080] possible to put all the contracts into

[00:24:59.279] most problem that have an entity

[00:25:00.799] resolution problem can't do this on day

[00:25:03.279] one. You can't just put it all in a

[00:25:04.480] prompt. That's actually a much better

[00:25:06.480] answer. Yeah. So like it it kind of it

[00:25:08.880] would be wasteful for me to go even

[00:25:10.240] write the base prompt because it it I

[00:25:12.320] know up front by definition of the

[00:25:14.240] problem, I can't do it. Cool. And so I

[00:25:16.799] imagine there's some stage where we kind

[00:25:18.240] of like if we if we do want to push them

[00:25:20.240] in, we would narrow down the set that we

[00:25:22.720] pass into the LM. Exactly. And that's

[00:25:24.559] literally what we do over here. We do

[00:25:26.080] the same thing we did in the

[00:25:27.279] classification problem. This is

[00:25:28.559] basically this is a classification

[00:25:30.480] problem.

[00:25:32.000] Cool.

[00:25:34.320] Okay. At this point, because all I'm

[00:25:35.520] doing is I'm taking the legal name of

[00:25:36.799] the company like Google Cloud Platform

[00:25:38.880] and trying to classify it against the

[00:25:40.240] known companies and we all know how to

[00:25:41.840] do classification problems. There's many

[00:25:44.080] different approaches. One example is we

[00:25:45.679] just dump all the companies into there.

[00:25:47.760] Another example is we go ahead

[00:25:53.039] and go do the whole thing. So it's

[00:25:54.960] really up to us how we go about this

[00:25:56.799] problem. But this basically becomes a

[00:25:58.000] classification problem at this point.

[00:25:59.679] And in the case, the only difference is

[00:26:01.600] now I'm allowed to return other or like

[00:26:03.440] no company found.

[00:26:06.080] And if I find no company found, then I

[00:26:08.400] have a choice of what I do at this

[00:26:10.159] point. This Okay. So, we're actually

[00:26:11.919] going to kind of like skip over that

[00:26:13.600] classification part and just zoom out

[00:26:15.279] and look at the B bigger broader

[00:26:17.279] pipeline. Right. Exactly. Because

[00:26:18.960] there's no point in rewriting that

[00:26:20.240] process again. Um I think if someone is

[00:26:23.360] interested they can go look at the

[00:26:24.400] classification video we did a couple

[00:26:25.840] weeks back and just know we will put a

[00:26:27.600] we'll put a link to that in the uh in

[00:26:29.760] the show notes. Yeah. Uh but like once

[00:26:32.480] you do the classification refer

[00:26:35.360] to video. Um

[00:26:38.720] once you do that then you're basically

[00:26:40.080] able to go move on. Now you have a valid

[00:26:41.760] company. Now the problem is this won't

[00:26:43.039] always return a valid company. Sometimes

[00:26:44.640] it'll return something not found. So we

[00:26:46.799] want to go update this and make this a

[00:26:50.159] little bit better for ourselves. So

[00:26:51.440] sometimes we'll return this otherwise

[00:26:52.960] we'll return none for now. Very

[00:26:55.520] simplistic.

[00:26:57.440] Now what we want to do over here is I

[00:26:59.919] need to enumerate this.

[00:27:02.159] If uh result equals this, if result is

[00:27:08.400] none,

[00:27:09.919] if the result is none, then I kind of

[00:27:11.760] want to val invalidate the company and

[00:27:14.960] mark it as such.

[00:27:17.600] Otherwise, I'm okay leaving it as that.

[00:27:19.520] I kind of want to say this legal name is

[00:27:21.120] not valid.

[00:27:26.230] So even because the legal name is what

[00:27:26.240] you're going to use to map that's like

[00:27:27.919] you're using that as a proxy to the

[00:27:29.520] database ID basically. Exactly. Exactly.

[00:27:32.080] I'm using this as a database ID. So if

[00:27:34.240] I'm unable to find a valid company for

[00:27:36.080] this legal name, I'm going to go and

[00:27:37.840] like just not care about it. If I am

[00:27:40.480] able to find a valid legal name, then

[00:27:41.840] I'll go do this. And in this

[00:27:42.799] classification problem, what I do is

[00:27:44.240] like I'd call an LLM. If it found a

[00:27:46.799] valid legal name, I would just change

[00:27:48.080] the legal name of the object that I have

[00:27:49.600] and return it back. Cool. Cool. So now I

[00:27:54.559] have this. I'm able to go do this. Now

[00:27:56.320] there's a couple scenarios in here that

[00:27:58.559] all that all fail. Same with the legal

[00:28:01.039] name over here. This is also like

[00:28:02.960] classified. So like let me just write a

[00:28:04.559] function really fast. Class pick

[00:28:08.320] potential

[00:28:10.320] uh name company

[00:28:19.510] uh uh content

[00:28:19.520] stir and what this will return is like a

[00:28:21.919] stir or none passed.

[00:28:26.880] So what is the content that got that

[00:28:28.559] gets passed in there? Exactly. So what I

[00:28:30.559] would do is I'd pass into here potential

[00:28:32.799] company.name.leal

[00:28:34.320] name. So I pass in the legal name of the

[00:28:35.840] company and ask it that if

[00:28:40.480] return

[00:28:42.159] company.leal name equal potential

[00:28:44.000] company uh return company. So this is

[00:28:46.960] what I I think this I keep getting

[00:28:48.799] tripped up by the tupils. Are you down

[00:28:50.480] to put a couple like actual examples in

[00:28:52.399] there instead of like the names of the

[00:28:54.240] columns? That's a good idea. Microsoft

[00:28:58.799] Corporation,

[00:29:00.960] uh, Xbox,

[00:29:03.360] uh, Xbox, Azure,

[00:29:06.480] um, MSFT,

[00:29:11.669] and maybe there should be a dictionary.

[00:29:11.679] Maybe that'll be easier.

[00:29:14.399] Sure. Uh, there we go. Cool. Uh, Google

[00:29:18.159] does not own GitHub.

[00:29:20.240] Um, this is like one example of

[00:29:23.039] companies. Sorry about that. Good call

[00:29:24.720] on that. Um

[00:29:26.960] it items

[00:29:29.279] valid company. Um cool.

[00:29:33.760] There we go. Cool. All right. So now

[00:29:35.760] what I would do is I just pass in legal

[00:29:37.120] name. I pick the uh potential company.

[00:29:39.840] And what I can do over here is like or

[00:29:42.799] legal name and how many and I just

[00:29:44.960] return this. So now I'm doing something

[00:29:46.399] very very simple, very simple, which is

[00:29:49.919] I just see if any of the aliases match

[00:29:53.120] the content and if they do then I'll

[00:29:54.640] return the legal name. This could be an

[00:29:56.720] LM function but I'm choosing to use a

[00:29:58.480] very basic heristic here instead.

[00:30:02.240] Does that make sense Dexter? Yeah. So so

[00:30:05.520] this content is really like a like

[00:30:07.840] company name.

[00:30:10.000] Yeah. Which one? This one. So I mean we

[00:30:12.480] use content in the main function and in

[00:30:14.720] that case content is like the source of

[00:30:17.279] the resume. I just I don't want to mix

[00:30:18.880] up those we're going to do something

[00:30:20.320] over here. So in this scenario where the

[00:30:22.159] legal name wasn't provided for a company

[00:30:24.399] then we're going to do this potential

[00:30:31.430] but it's not the full resume it's the

[00:30:31.440] company.name.

[00:30:33.039] Exactly. So if the legal name is none

[00:30:35.360] I'm going to pick a potential company by

[00:30:37.600] passing in the legal name. So I guess my

[00:30:39.679] point was like in pick potential company

[00:30:41.360] should that v variable be called company

[00:30:43.679] name? Uh

[00:30:46.320] it's not always going to be the company

[00:30:48.559] name because in different places I'm

[00:30:49.919] passing different things in the valid

[00:30:52.080] where I have a valid company. I'm going

[00:30:54.880] to pass in the legal name. In the case

[00:30:57.360] of where the legal name was not filled

[00:30:58.960] out by the LLM, I'm going to pass in the

[00:31:00.480] actual name of the company verbatim from

[00:31:02.080] the resume.

[00:31:03.760] Okay? Using different things to go do

[00:31:06.080] this. And you can imagine that I pass in

[00:31:07.600] like different piece of content. I might

[00:31:08.960] pass in the whole experience block into

[00:31:10.720] here. It's really up to me as a

[00:31:12.960] developer to decide what I want to go

[00:31:14.640] do.

[00:31:16.320] But the goal of this function is to say

[00:31:18.000] given some string, tell me all the

[00:31:20.960] relevant pieces of content that might

[00:31:22.720] match that company. And if I have it,

[00:31:25.120] then I update my company name into here.

[00:31:28.240] Now, the nice thing that I'm able to do

[00:31:29.840] about all this is I'm also invalidating

[00:31:32.080] names that come back to me from the LM.

[00:31:34.159] If the LM gives me a name, I'm

[00:31:36.159] invalidating it if it's not valid.

[00:31:43.750] In addition to that, I also am going to

[00:31:43.760] go ahead and do the same thing with

[00:31:44.720] subsidiaries. I'll do the exact same

[00:31:46.320] thing. So, I'll just like put this over

[00:31:48.640] here.

[00:31:50.240] Oh, I can't do that in Python. I didn't

[00:31:52.000] know that. Okay.

[00:31:58.070] You might be able to use an or

[00:31:58.080] something.

[00:31:59.679] Um Oh, maybe. Oh, I can. Nice.

[00:32:04.000] I didn't know that. Cool. Match is

[00:32:05.679] pretty freaking cool. Um, so now I can

[00:32:08.320] actually go do this and I can handle the

[00:32:09.519] scenario really nicely. Now I can build

[00:32:12.159] a Now that I've done this, I basically

[00:32:13.760] have a pipeline that is able to go ahead

[00:32:15.200] and validate all sorts of things in

[00:32:17.200] here. Let's go run this really fast.

[00:32:24.230] Um, I'm actually going to make the

[00:32:24.240] problem a little bit simpler and change

[00:32:27.360] what model I used to be a very very bad

[00:32:29.919] model.

[00:32:44.710] I don't know if this will work, but it

[00:32:44.720] might.

[00:32:50.950] Oh, lsv

[00:32:50.960] run python-fellow.

[00:32:57.509] Mhm. There we go. So, I'm going to go

[00:32:57.519] run this with an oama model really fast

[00:32:59.279] and see what happens.

[00:33:14.710] Oops.

[00:33:14.720] Uh, there we go. Okay, there you go.

[00:33:18.159] Something happens. So, the model Oh, I

[00:33:20.080] forgot to print out stuff. That's funny.

[00:33:23.360] Um,

[00:33:25.760] let's go ahead and go print this out.

[00:33:44.950] There you go. That's what I wanted.

[00:33:44.960] And I'm also going to print out the

[00:33:46.159] response ahead of time.

[00:33:49.679] Uh before and then after enriching.

[00:34:03.509] after. Okay. Um and then BMA log equals

[00:34:03.519] Oh.

[00:34:13.109] this can't actually happen. That's

[00:34:13.119] cool. Python yells at me. Um

[00:34:19.510] so now we can see what happens before.

[00:34:19.520] So before we have boundary ML null um

[00:34:23.119] the Google cloud platform subsidiary of

[00:34:25.119] Alphabet and then this thing did

[00:34:27.919] actually not do this.

[00:34:30.879] I might have to debug this a little bit

[00:34:32.320] really fast.

[00:34:34.560] Um this thing did not get enriched. Uh

[00:34:37.919] let's see what happened.

[00:34:40.960] Well-known subsidiary should have gone

[00:34:42.639] into here. Expco company name. Uh let me

[00:34:46.000] print this out.

[00:34:51.589] You could just tell cursor agent to add

[00:34:51.599] a bunch of print statements. That's

[00:34:53.839] probably true. Add some debug print

[00:34:57.200] statements.

[00:34:58.960] Okay. Well, it does this.

[00:35:02.240] Did it do it? Command ki.

[00:35:07.680] This is the only problem with AI

[00:35:08.880] generate code. It takes a while to

[00:35:10.880] write.

[00:35:24.470] We're gonna have a lot of print

[00:35:24.480] statements.

[00:35:27.359] Um, have you ever used the cursor

[00:35:29.119] debugger that lets you like step through

[00:35:30.720] Python code? No, I haven't.

[00:35:35.040] It's uh sometimes pretty good.

[00:35:43.750] Uh, company type of startup. Did I make

[00:35:43.760] something silly and not actually go

[00:35:45.520] through every company?

[00:35:54.150] Oh, I see. I didn't know Python this

[00:35:54.160] break actually breaks out of the loop.

[00:35:56.400] Out of the loop. Yeah. Yeah. I don't

[00:35:58.000] think you want that. Okay, let's get rid

[00:36:00.400] of more debug statements.

[00:36:10.470] So now when we're able to go do this in

[00:36:10.480] theory, um

[00:36:13.359] this should

[00:36:16.640] null out the actual legal name of the

[00:36:18.560] GCP because it didn't actually work.

[00:36:22.160] Okay, so this is just detecting which

[00:36:23.920] ones can you accurately extract. This is

[00:36:26.079] and then after that you could do another

[00:36:28.079] pass to go try to ask an LLM to better

[00:36:31.119] pick or do a lookup or do a rag against

[00:36:33.200] the list or something like that.

[00:36:34.640] Exactly. And now we can actually go

[00:36:36.160] further and say if the result is none

[00:36:37.760] what I can say is like

[00:36:40.000] other names other names equals

[00:36:43.760] pick potential uh sorry let's go to

[00:36:45.839] validate company what I can say here's

[00:36:47.839] if this is none what I also want to do

[00:36:49.760] is another option uh from name equals

[00:36:54.000] pick

[00:36:56.240] and then I just return this. So, if I if

[00:36:59.280] the actual legal name doesn't find it,

[00:37:01.119] then I'll also try from the original

[00:37:02.560] name that I got from the LLM when I'm

[00:37:04.160] validating a company and we'll see what

[00:37:07.280] this does.

[00:37:17.750] So, the goal here is to say that there

[00:37:17.760] are many ways that I could enrich it.

[00:37:19.119] You can see right over here I was able

[00:37:20.320] to enrich it to Google now

[00:37:22.960] because what I said was oh even if the

[00:37:25.359] LLM doesn't initially get a good legal

[00:37:27.760] name which it did not. It got Google

[00:37:29.520] Cloud Platform.

[00:37:32.079] What I will do is I will go ahead and

[00:37:33.839] try and find a good match. If I am

[00:37:35.599] unable to find a good match from the

[00:37:37.119] legal name I'll try the original name in

[00:37:38.960] my database and see if I can go find it.

[00:37:41.359] So you see we're going to go check does

[00:37:43.920] the original name match one of the

[00:37:46.320] aliases. space. Exactly. Match one of

[00:37:48.160] the aliases. And this is again the most

[00:37:49.839] simplistic algorithm that I could

[00:37:51.359] implement here. I could do something

[00:37:53.119] more sophisticated here such as calling

[00:37:55.040] an LLM, asking another model to go save

[00:37:57.440] things um or go do something. But now

[00:38:01.760] this is still only half of the battle.

[00:38:03.680] I'm still not done yet because we have

[00:38:06.000] Boundary ML. Boundary ML is clearly not

[00:38:09.119] going to be found in my database. So

[00:38:10.560] what I need to do is I almost need to

[00:38:12.160] build a totally separate workflow to

[00:38:14.480] solve for that problem. And the best way

[00:38:16.960] Yeah. And you could you could almost do

[00:38:18.320] something aentic. I I I want to hear

[00:38:20.079] what you were going to say, but I was

[00:38:20.960] like you can almost do something aentic

[00:38:22.320] here where it's like there's a LLM is

[00:38:24.480] picking a tool that is like actually the

[00:38:27.440] next step is to update our list of

[00:38:28.960] companies because of some input or some

[00:38:31.680] human input or whatever it is. Yeah, I

[00:38:34.079] may not even need uh like really I might

[00:38:36.000] just know that hey if it's a startup I

[00:38:37.520] always need to do an agentic workflow

[00:38:40.480] and I might want to maintain my list of

[00:38:42.160] startups separately than my list of well

[00:38:44.880] well-known companies or even mark these

[00:38:46.800] as startups versus well-known companies.

[00:38:48.720] So then what I could do now is like

[00:38:50.400] build a database pipeline that says as

[00:38:53.280] soon as I save a data into there, I push

[00:38:55.119] something to an SQSQ that says go look

[00:38:57.760] up information about Boundary ML and

[00:39:00.720] here's database IDs that could be

[00:39:02.560] impacted by Boundary ML. So if you find

[00:39:04.640] a company called Boundary ML in the

[00:39:06.800] cloud somewhere. So let's let's go back

[00:39:09.040] to our whiteboard.

[00:39:11.520] Uh where do they go? So now the next

[00:39:14.400] step now that we have this pipeline

[00:39:15.839] where we're pretty good about legally

[00:39:17.280] known companies that we have in our

[00:39:18.720] database. Now we have a separate thing.

[00:39:20.880] Now what we're going to do is we're

[00:39:21.920] going to create an AWS SQSQ that's going

[00:39:24.160] to do a couple of things. It's going to

[00:39:25.440] submit a job that says look for

[00:39:29.839] info on

[00:39:32.320] boundary ML. Also, by the way, the the

[00:39:35.839] row ID that I just inserted is equal to

[00:39:38.560] like uh like 50 uh 51.

[00:39:43.599] And then So, your goal is basically

[00:39:45.040] you're going to you're going to put in

[00:39:46.160] what you extracted and then you're going

[00:39:47.440] to say like, "Hey, we need to get a

[00:39:48.800] legal name for this company." Exactly.

[00:39:51.280] So, I'm going to give it I'm going to

[00:39:52.480] give it give it the information I

[00:39:53.839] extracted. I might even give it the raw

[00:39:55.440] resume. Something else that I might want

[00:39:56.800] to give it just to give it more context

[00:39:58.240] on it. I might want to give it the full

[00:39:59.760] resume, the original text or whatever I

[00:40:01.760] have. But specifically, I'm going to

[00:40:03.280] tell it I care about

[00:40:05.680] I care about this company Boundary ML in

[00:40:08.240] this resume. So now I can build a

[00:40:09.920] pipeline whose job it is to first say

[00:40:14.079] give me everything

[00:40:16.960] every clue from the resume

[00:40:20.160] about boundary ML.

[00:40:29.750] And this becomes again a very simple

[00:40:29.760] prompt that we can go do. Now I can use

[00:40:32.480] web search or some other tool that I

[00:40:34.400] want

[00:40:36.400] uh to go find all the relevant

[00:40:37.839] information. Then I can build a whole Go

[00:40:40.880] ahead. Okay. So you would use those

[00:40:42.720] clues you extracted from the resume to

[00:40:44.560] build good web searches. Basically it's

[00:40:46.480] like basically like if you didn't know

[00:40:48.079] Boundary ML was an AI dev tools company.

[00:40:50.320] Maybe you could figure that out from the

[00:40:51.520] resume and then you would look search

[00:40:53.280] for BAML AI instead of searching just

[00:40:55.599] BAML and getting a bunch of things about

[00:40:57.280] Bank of America. Exactly. or I might

[00:40:59.440] have the location of the person and

[00:41:00.800] where they live on or go do something

[00:41:02.400] like that. I might find all sorts of

[00:41:03.839] clues that might give me information

[00:41:05.119] about that. Then you can make a bunch of

[00:41:07.280] search queries, build a web search

[00:41:08.880] pipeline and at some point this thing

[00:41:11.920] will end. It'll put together a proposal

[00:41:14.560] or it'll put together no proposal. It's

[00:41:16.480] really up to you.

[00:41:18.960] And now now that we have a proposal, we

[00:41:21.520] have our list of databases. This becomes

[00:41:23.680] an entry into there with a status of

[00:41:26.400] proposed instead of committed.

[00:41:29.680] And it is some other agent's job

[00:41:34.160] to migrate us from proposed to

[00:41:36.319] committed.

[00:41:37.839] Now I see and that might be human input.

[00:41:40.079] That might be more searches against the

[00:41:41.760] database. You you decide the logic for

[00:41:44.000] what lets you commit a new entity to the

[00:41:46.319] database. Exactly. Uh information.

[00:41:50.000] Right. If you're if you're doing this

[00:41:51.200] for tax information, you want to

[00:41:53.040] probably have a human in the loop. If

[00:41:55.119] you're doing this for like resume ATS

[00:41:57.119] information, it's just like small

[00:41:58.160] enrichment for like making searches

[00:41:59.680] better. Automate that sucker. It doesn't

[00:42:01.599] matter. You might even want to go

[00:42:03.119] straight to committed in that scenario.

[00:42:04.800] It's up to you, right? I mean, it's also

[00:42:07.839] like you there's two kinds of human in

[00:42:09.440] the loop, right? There's human the loop

[00:42:10.800] like do not commit this until someone

[00:42:13.359] has reviewed it and then there's like

[00:42:15.200] commit it and then anyone has the

[00:42:17.280] ability to come back later and edit it

[00:42:18.720] and update it. Right. Exactly. Exactly.

[00:42:21.440] And we can just email our Slack channel

[00:42:23.200] saying we added a new company. Go review

[00:42:24.960] it pre uh whenever you have time. Yeah.

[00:42:28.880] That async or batch human in the loop.

[00:42:31.280] Exactly. And all of this whole thing

[00:42:33.040] just becomes like a workflow that we've

[00:42:35.119] built out. And now we have this other

[00:42:37.760] last piece of information which is row

[00:42:39.359] ID 51. Once it becomes committed, what I

[00:42:42.240] need to do is I need to go to the other

[00:42:43.440] database where I've stored this

[00:42:44.720] information and then right because you

[00:42:46.640] have two tables. You have tables of like

[00:42:48.240] your abstractions, your extractions that

[00:42:50.480] are like in progress or pending and then

[00:42:52.400] you have the lookup table of all the

[00:42:53.920] companies you know. Exactly.

[00:43:03.109] And now update row 51 for boundary.

[00:43:03.119] That's it. Once that is committed

[00:43:09.589] and now we've actually built a pipeline

[00:43:09.599] in a fully automated way or as automated

[00:43:12.400] as this process is for proposed to

[00:43:14.240] committed that can go find information

[00:43:16.480] do web search and then go figure this

[00:43:18.079] out.

[00:43:19.599] Um before we go into the next part of it

[00:43:22.480] any questions from anyone,

[00:43:31.829] you can type in the chat or raise your

[00:43:31.839] hand uh and come on.

[00:43:39.829] I guess my question is like is there a

[00:43:39.839] zooming out here bigger? Like is there

[00:43:44.640] like what what what else is here?

[00:43:47.839] Honestly, this is it. I've seen this

[00:43:49.599] work a couple of places for different

[00:43:51.040] couple of different companies. This

[00:43:52.480] works for all sorts of processes. So

[00:43:54.480] like another process that doesn't sound

[00:43:56.160] the same but is exactly the same is

[00:43:57.839] topic clustering.

[00:43:59.760] So if you think about what topic

[00:44:00.880] clustering is, let's say I want to have

[00:44:02.400] like the most semantic mill, let's say

[00:44:04.400] I'm building like a giant news media

[00:44:06.079] company and I want to know what topics

[00:44:08.079] are sensational in the world that I

[00:44:09.520] should talk about right now. That's

[00:44:11.839] basically the same pipeline. I have a

[00:44:14.000] bunch of data because a topic is an

[00:44:15.760] entity with like an official thing.

[00:44:18.240] Exactly. What if I was making a tool to

[00:44:20.800] like label all my Gmails for me? It's

[00:44:23.839] same thing. I want to go do the same

[00:44:25.760] thing. Um, and go do that. So, you don't

[00:44:28.960] have to really think about any of those

[00:44:30.400] concept because those labels are

[00:44:32.079] entities and you want to you don't want

[00:44:33.599] to make new labels all the time. You

[00:44:35.520] want to resolve them to the same labels

[00:44:37.280] whenever possible.

[00:44:39.440] We got a question. Can Sorry. Go ahead.

[00:44:42.000] Uh, and you can also do interesting

[00:44:43.599] things with like not just labels but

[00:44:45.440] also with um hierarchal labels. So you

[00:44:48.640] can have like topics that are like

[00:44:49.680] saying like we want to go up down up

[00:44:51.520] down and you can go figure that out

[00:44:54.880] uh along the way. So it's like do I want

[00:44:56.240] the higher level category or the lower

[00:44:57.760] level category? It's up to me and all of

[00:45:00.640] that is almost the same problem. So in

[00:45:03.599] the case like news media, I might want

[00:45:04.880] to say like have global news and have

[00:45:06.800] like Britain news or like US news and

[00:45:09.839] those could be hierarchal design or

[00:45:13.119] where I look for global news first and

[00:45:14.880] then I find the subcategories around it

[00:45:17.200] that are around like environmental stuff

[00:45:19.119] or um

[00:45:21.520] uh environmental stuff or like financial

[00:45:23.119] news under global news or I can go

[00:45:24.960] straight to financial news or global

[00:45:26.480] news or uh financial stuff or

[00:45:28.240] environmental notes along the way. Yeah,

[00:45:30.480] the the multi- multi-entity grouping is

[00:45:33.520] kind of tricky where something could

[00:45:34.800] have multiple different categories and

[00:45:36.720] like there's it's one of n instead of

[00:45:38.560] exactly one company, then you just

[00:45:41.359] return an array

[00:45:44.720] and it's the same. And then you can run

[00:45:46.079] through the same validation checks on

[00:45:47.760] each thing in the array. Exactly. If you

[00:45:50.079] if we're doing multilel thing, it's

[00:45:51.680] actually really easy. All we do is let's

[00:45:54.400] go do this really fast. I'm going to

[00:45:55.920] turn on my Python type checker so we can

[00:45:57.440] see how we actually catch these bugs.

[00:46:00.000] Uh

[00:46:01.760] um oh

[00:46:08.790] let's add this in here. Sorry, static

[00:46:08.800] analysis is very important to me. Um

[00:46:13.200] so now that we go down here, let's go

[00:46:14.880] ahead and like add this in our way. So

[00:46:16.960] what what do I do over here? Well, maybe

[00:46:18.960] there are multiple legal names that make

[00:46:20.640] sense. So let's make this an array.

[00:46:24.000] Let's pretend you worked at Palunteer

[00:46:25.680] and you consulted for six companies but

[00:46:27.520] it was one experience. Exactly.

[00:46:31.359] Now what I have to do here is this will

[00:46:33.040] return instead of a string. I mean this

[00:46:35.359] can still return a string because this

[00:46:36.560] is just like for content.

[00:46:38.800] Uh legal name company.leal name.

[00:46:43.280] We have a bunch of questions stacking up

[00:46:44.960] by the way. Um sorry. No, you're good.

[00:46:47.440] You're good. I didn't want to interrupt

[00:46:48.560] you. Um

[00:46:50.880] so uh I just I just want to do if you're

[00:46:54.079] uh if you're let me do this one all we

[00:46:57.760] have to do here is now we just make this

[00:46:59.040] a for loop

[00:47:02.319] and we have to do the same kind of code

[00:47:03.920] wrapping to make this a for loop and

[00:47:05.520] then we might want to resolve the same

[00:47:07.520] if the for loop for some reason dumped

[00:47:09.760] out like GCP G Google Cloud Platform we

[00:47:11.920] want to resolve them both to one entry

[00:47:13.920] called Google.

[00:47:16.240] That's the only other you have to Oh,

[00:47:18.000] and then you end up flattening the the

[00:47:19.599] list. Exactly. It doesn't flatten the

[00:47:20.960] list. Exactly. That's all that. Um,

[00:47:23.440] cool.

[00:47:26.079] Um, cool. Uh, um, can BAML use lower

[00:47:29.839] level models like BERT or Alberta? Um,

[00:47:32.560] right now we have just LM support, but

[00:47:35.280] uh, you can if you wrap BERT or Alberta

[00:47:37.839] around an LM API, uh, which I don't

[00:47:39.920] think you can because they're just

[00:47:41.040] embedding models really then, uh, for

[00:47:44.720] now. But eventually, yeah. Yeah,

[00:47:46.960] Michaela has a really cool example of

[00:47:48.319] like if if the Baml run didn't didn't

[00:47:50.480] return return like null for one of the

[00:47:52.319] fields, they would go do a web search

[00:47:54.000] with Tavali and then just pass that

[00:47:55.599] context in. That's it sounds like they

[00:47:58.240] they naturally discovered the same

[00:47:59.599] process we just discovered today, which

[00:48:01.040] is like if you got an empty field, which

[00:48:02.720] is in this case got this data out of

[00:48:04.640] here, you just run web search and do the

[00:48:06.400] same thing again. That's kind of cool.

[00:48:08.160] Yep. Um okay, when does the database

[00:48:10.720] pipeline get triggered? Right after the

[00:48:12.480] ML pipeline or was that from one of the

[00:48:14.400] BAML functions? Oh, the database

[00:48:17.040] pipeline would get triggered right over

[00:48:18.480] here. So, what I can do now is I can say

[00:48:20.160] like uh at the very end of the code.

[00:48:23.440] Let's actually write that out. Yeah.

[00:48:24.559] It's like Yeah, exactly. It's like you

[00:48:26.640] you exit the loop, you've done all the

[00:48:28.160] repairs you can, then you find the ones

[00:48:30.000] that didn't get satisfied and you go

[00:48:31.599] kick off jobs, right? Exactly. Is none,

[00:48:34.640] then I just kick off a job.

[00:48:38.400] Is none.

[00:48:41.200] print uh kick

[00:48:45.760] off AWS uh kick off job to find better

[00:48:50.480] match.

[00:48:58.470] So now I can go do this

[00:48:58.480] and this is when I would go do this at

[00:49:00.079] the very very end of this. Cool.

[00:49:04.480] Um propose to committed is a bit vague.

[00:49:07.599] You're updating data in a database in

[00:49:09.440] prod for the company info search

[00:49:11.119] results, but AI could commit on wrongful

[00:49:13.359] information. Yeah. So, that's what we

[00:49:15.359] talked about is like you need to uh look

[00:49:16.960] at your risk and and your use case and

[00:49:18.960] you may want to have kind of human in

[00:49:21.040] the loop or you may want to have it push

[00:49:22.559] it to like a stage database that gets

[00:49:24.480] reviewed regularly and it gets queried.

[00:49:27.280] Exactly. You can view your SQL table for

[00:49:29.440] this company information table to look

[00:49:31.359] something like this. Like you have like

[00:49:33.280] a table called like company uh name

[00:49:43.349] company uh uh like ID, company

[00:49:43.359] attributes, like other keywords or

[00:49:45.599] something that you might want to have

[00:49:46.559] about it. Keyword you could have a I

[00:49:49.280] guess like you could have a flag that

[00:49:50.559] like whether it was human reviewed or

[00:49:52.480] like how how hard committed it was,

[00:49:54.400] right? And then you'd basically have

[00:49:56.319] like company.status

[00:50:01.910] company. status and status would be one

[00:50:01.920] of like uh like uh proposed

[00:50:06.720] uh ready.

[00:50:09.359] Yeah. And you could even store the like

[00:50:11.440] human comment or whatever it is. And you

[00:50:13.920] could actually asynchronously go through

[00:50:15.599] with an LM and try to repair this. Like

[00:50:17.200] if a human said, "No, that's wrong."

[00:50:18.640] Like go search for this that you could

[00:50:20.559] you could kick off new jobs periodically

[00:50:22.640] based on that. It's really important

[00:50:24.400] that your data model represent the

[00:50:26.240] complexity of your problem. So if you

[00:50:27.839] need multiple drafts of a company before

[00:50:29.680] you can get to a good resolution, you

[00:50:31.200] need a data model that can go do that

[00:50:33.520] and this is independent of an LLM. Like

[00:50:36.160] this is even like if in Wikipedia for

[00:50:37.920] example, they keep track of every edit

[00:50:39.599] that every human makes so they can roll

[00:50:41.119] them back really easily. That's what we

[00:50:42.800] do with git. You just need to find the

[00:50:44.720] right data model that represents the

[00:50:46.079] complexity of your task. So in this

[00:50:48.319] case, I did something very very basic

[00:50:50.000] where I only have two booleans proposed

[00:50:51.680] and ready. And I can make a web UI that

[00:50:54.240] literally shows everyone on my at my

[00:50:57.440] company internal dashboards a view of

[00:50:59.280] these tables and people can manually

[00:51:01.440] promote promote promote. And I can have

[00:51:04.000] like a last updated column on top of

[00:51:06.240] here is like um

[00:51:09.440] last updated

[00:51:11.599] that I sort by. So in the UI, people can

[00:51:13.920] go see this and I can have information

[00:51:16.000] about who the last person that updated

[00:51:17.599] was or I can do what Dexter says and

[00:51:19.839] keep a full edit log of the entire edit

[00:51:23.359] history of that row and go make that

[00:51:26.000] possible as well. It's up to me as the

[00:51:28.480] developer of this application to decide

[00:51:31.040] the requirements for this task. And this

[00:51:34.319] is what we always say is it's it's

[00:51:36.000] mostly engineering. If you can do the

[00:51:37.920] software engineering behind this, you

[00:51:39.520] can build the tool that fits your

[00:51:41.359] problem and it's going to work a lot

[00:51:42.800] better than one of these like

[00:51:43.839] one-sizefits-all just like rag against a

[00:51:46.319] thing and push it in and hope it works.

[00:51:48.960] Yes. Does that answer your question?

[00:51:51.920] Sure. Yes. Very cool. Uh I I really like

[00:51:54.079] Sean's question. I was wondering if

[00:51:55.359] you'd be down to come off mute and kind

[00:51:56.960] of clarify a little bit more what you're

[00:51:58.240] thinking about.

[00:52:04.390] Um how do I think about performances of

[00:52:04.400] large numbers of these matches? I guess

[00:52:06.160] for if you're going to classify emails,

[00:52:07.680] you could have 10,000 plus calls. Yeah.

[00:52:10.480] Can you hear me? Okay. Yep. I'm actually

[00:52:13.520] on the the train at the moment. So the

[00:52:16.160] um yeah, there's that N plus1 thing. If

[00:52:19.200] I have lots of emails, I want to, you

[00:52:21.599] know, maybe I would think about batching

[00:52:23.040] them. Um, or training

[00:52:26.319] smaller models on my custom task, you

[00:52:29.280] know, would be how I'd want to do it in

[00:52:32.160] production potentially if I have lots of

[00:52:34.800] similarly structured documents. So just

[00:52:37.040] kind of curious your general philosophy

[00:52:38.640] on using LMS in

[00:52:41.599] your BAML framework and like am I just

[00:52:44.640] kind of being old school and worrying

[00:52:46.000] about that or just like just do the API

[00:52:47.920] calls and and move on or should I be

[00:52:50.880] thinking about something else here?

[00:52:54.000] Yeah. Um well just as uh just as I think

[00:52:58.400] we say a lot of times like this stuff is

[00:53:00.960] pretty much just functions. So in this

[00:53:02.720] case we have like a type signature. The

[00:53:05.200] thing that implements this type

[00:53:06.319] signature could be a really really

[00:53:07.920] complicated model like 04 that we toss

[00:53:10.240] at it. It could be GVD26, who knows? Um,

[00:53:13.520] it could be a very tiny model that we've

[00:53:16.480] custom trained to actually take a

[00:53:19.280] specific content and then spit out the

[00:53:21.040] actual company that we have trained on.

[00:53:23.119] It can only output valid companies,

[00:53:24.960] nothing else. It could be a really

[00:53:26.800] really cheap heristic like the one I

[00:53:28.480] wrote here that just matches on aliases.

[00:53:31.359] So that becomes your prerogative. But

[00:53:33.359] the most important thing is you just

[00:53:34.559] need to collect data on what makes this

[00:53:37.280] function really good. What makes this

[00:53:38.880] type signature perform accurately.

[00:53:41.760] So once you have large scales of

[00:53:44.160] problems like and there's different ways

[00:53:45.839] when you use the word performance. If

[00:53:47.280] you're thinking about speed and cost and

[00:53:48.800] latency

[00:53:50.319] then yeah the answer is try not to use

[00:53:52.079] an LLM right a really dumb heristic. Now

[00:53:55.280] the problem is this heristic might not

[00:53:57.200] balance very well for accuracy. So you

[00:53:59.119] might need to use a bigger model. So

[00:54:00.800] then you try a GPD, try like the 54

[00:54:04.400] models like I was trying right now. And

[00:54:06.640] if that doesn't work, then bump it up to

[00:54:09.359] 04 because so you can just ship the prod

[00:54:11.280] and not have to write 5,000 lines of

[00:54:12.720] code trying to optimize your model away.

[00:54:14.400] And then collect data, use that data to

[00:54:16.720] go train a tiny model, eval it against

[00:54:19.680] your system by having a benchmark

[00:54:21.200] because this system can be benchmarked

[00:54:23.040] with an F1 score. So we can get a

[00:54:24.800] numerical benchmark on this and then

[00:54:26.880] just run that in a loop until you have a

[00:54:28.960] type signature that meets the

[00:54:30.319] constraints of your problem. But it's

[00:54:32.720] really about thinking of it as type

[00:54:34.079] signatures and once you think of it that

[00:54:36.400] way then you choose what part of the

[00:54:37.920] system you want to optimize as a

[00:54:39.440] developer.

[00:54:41.760] Does that answer the question? Yeah, I

[00:54:43.920] love that. Um

[00:54:45.839] very compelling part of the whole stack.

[00:54:48.240] The uh the kind of last little follow up

[00:54:50.640] is

[00:54:52.640] my natural language.

[00:54:59.670] Uh you're going to have to type that

[00:54:59.680] out. Your audio is cutting out.

[00:55:16.870] Step and then linking step. and you're

[00:55:16.880] kind of doing it as a oneshot

[00:55:19.599] sort of thing here.

[00:55:25.190] Okay, I'll let him type it out while he

[00:55:25.200] goes and that's it. Um, Dexter, is that

[00:55:27.839] kind of how you think about optimization

[00:55:29.280] as well?

[00:55:31.920] Um,

[00:55:36.870] yeah, I mean I think that tracks I mean

[00:55:36.880] I'm still always all about this like

[00:55:40.720] use the it's like what we did on the the

[00:55:43.680] policy to props episode, right? It's

[00:55:45.359] like take a subset, work through,

[00:55:47.599] iterate on a small subset of a hundred

[00:55:49.520] and then move up to a thousand and

[00:55:51.200] understand the performance and like at

[00:55:53.520] the end of the day, yes, if you want AI

[00:55:54.960] to do the work, then like you're going

[00:55:56.319] to have to spend the tokens to go do the

[00:55:58.480] work on all the things, but like iterate

[00:56:00.640] and get it tight on a small subset,

[00:56:02.319] figure out learn what you can do with

[00:56:03.920] smaller models before you like 10x the

[00:56:06.559] number of records you're you're

[00:56:07.920] processing on each run. Yeah, I agree. I

[00:56:10.960] agree. I think that's a general

[00:56:12.160] philosophy as well. Um, while we wait

[00:56:14.400] for Sean's question, um, if anyone else

[00:56:16.240] has more questions, feel free to type

[00:56:17.440] them out in the chat. I'm going to show

[00:56:18.480] you how to do some of the enrichment

[00:56:19.839] tasks that we had like handwaved away if

[00:56:22.720] that's useful. Function, uh, extract

[00:56:31.990] uh, company clues

[00:56:32.000] uh,

[00:56:33.680] resume string uh, content uh, company

[00:56:38.319] target company string. Okay. Um, given

[00:56:43.520] this resume, tell me all the clues that

[00:56:47.839] may help

[00:56:55.430] me find information

[00:56:55.440] about the company, target company.

[00:57:04.470] Yeah. Or you could even just have it

[00:57:04.480] output like queries for web search. So,

[00:57:07.520] I will do that in a second, but I'm

[00:57:08.799] going to go break this up. Um, so I'm

[00:57:11.440] going to go run this in a very very

[00:57:13.920] basic format

[00:57:16.720] and like let's go do this

[00:57:20.559] company clues

[00:57:22.559] resume target company

[00:57:25.280] uh boundary ML and what's interesting

[00:57:28.319] about this is because I know that

[00:57:29.760] extract company clues will only ever be

[00:57:31.520] run on like large smaller companies I

[00:57:34.079] build my test cases like that

[00:57:35.280] accordingly as well. I don't actually

[00:57:36.480] build my test case. I have Google. I

[00:57:37.920] don't care because the input to this

[00:57:39.520] function is guaranteed by my software

[00:57:42.079] layer by the API definition of I have of

[00:57:44.319] how I'm using this function that the

[00:57:46.799] scope is only ever going to be unknown

[00:57:48.400] companies. Now, that scope can change

[00:57:50.160] like in regular software. Your function

[00:57:51.920] can suddenly be used for concepts

[00:57:53.280] they're not used to. And you just have

[00:57:55.119] to keep that in mind. So, you might want

[00:57:56.400] to drop a comment to let people know.

[00:57:58.240] But let's go run this and see what it

[00:58:00.640] does. Yep.

[00:58:03.440] Um,

[00:58:05.359] so it's giving me a bunch of clues. Uh,

[00:58:07.440] this is not very good. U, let's go do

[00:58:10.079] this. Uh, and go do this here. Class

[00:58:14.720] clues,

[00:58:16.319] uh, clues string array. Uh, good

[00:58:20.799] searches. Good.

[00:58:23.680] Google searches

[00:58:31.510] string array. We'll change the data type

[00:58:31.520] here to be a little bit better.

[00:58:34.880] And I'm doing this in one shot.

[00:58:41.510] And that's kind of interesting over

[00:58:41.520] here. So now it's like

[00:58:44.160] and it's interesting. It actually says,

[00:58:45.520] oh, it might Boundary ML might be doing

[00:58:47.359] computer vision stuff. It might be C++

[00:58:49.520] and Rust might be parts of Boundary ML

[00:58:51.200] stack. And now you can it actually gives

[00:58:53.520] me pretty good

[00:58:55.599] information about how to go find this.

[00:58:58.160] What is your target company? Okay, so

[00:59:00.079] it's it's still asking about the other

[00:59:01.920] things. Interesting. Well, it might

[00:59:04.319] because that might still be a good

[00:59:05.680] search in terms of what it is. So, let's

[00:59:08.000] make this better because I think you're

[00:59:10.640] getting ambiguity on here. class search

[00:59:14.400] uh like uh priority

[00:59:18.559] I may

[00:59:23.990] based on

[00:59:24.000] which queries I should run first.

[00:59:31.750] Oh cool. And then you can do like a

[00:59:31.760] group buy and run them in in batches.

[00:59:34.079] Exactly. Then I just run all my queries

[00:59:35.839] that are high first

[00:59:38.240] and like this is probably a good query

[00:59:39.599] by Gupta foundry founder of mail that'll

[00:59:41.359] probably get you to the legal name of

[00:59:42.480] our company. Um found it and it's just

[00:59:46.000] like helping you go do this and like I

[00:59:48.720] would go just build a now we can imagine

[00:59:50.640] how to build a pipeline off of you can

[00:59:52.960] go iterate on that prompt and test this

[00:59:54.559] and be like oh hey you're a expert

[00:59:56.880] researcher whatever whatever prompt

[00:59:58.640] tricks you want to use. Exactly. Uh and

[01:00:01.680] then you can toss web search at it. You

[01:00:03.119] can do whatever you want and you can

[01:00:04.160] find information about this. Uh, tell me

[01:00:05.839] clues that may help me find information.

[01:00:08.000] Specifically,

[01:00:09.520] I want to find the legal

[01:00:12.640] name

[01:00:14.640] of the company.

[01:00:18.000] And I can like prompt my way through

[01:00:19.280] this and just see what it does.

[01:00:22.319] And now you can see the that the queries

[01:00:24.240] got a lot better. And it's actually

[01:00:26.640] really funny what the queries are doing.

[01:00:28.160] It's actually giving me like search

[01:00:29.680] queries of like who is patterns and like

[01:00:32.079] actually really restricting this to this

[01:00:34.240] and it's like looking for my name in

[01:00:36.960] like quotes because it knows Google will

[01:00:38.400] search for this specifically.

[01:00:40.880] Oh man, I uh I almost want to give you

[01:00:43.839] my Exa API key and have you run some of

[01:00:45.920] these. I Yeah, so this is basically what

[01:00:49.520] we would end up building. We'd go build

[01:00:50.799] this out, then we'd actually go build

[01:00:51.920] the search part of it and then we'd pull

[01:00:53.760] the data out. We build an agent to

[01:00:55.280] evaluate the results of the web search

[01:00:57.040] to see if we have we basically write a

[01:00:58.640] function that says extract legal name

[01:01:02.160] function extract legal name from like

[01:01:06.160] content uh and like search results.

[01:01:09.920] Exactly. And just pull that out and then

[01:01:12.400] I'd go do this

[01:01:14.720] and I just go do this over and over

[01:01:16.240] again until I have a good legal name.

[01:01:19.599] Cool. And you could have it output like

[01:01:21.520] six and then have a model do the judge

[01:01:23.280] thing and pick one or two or three of

[01:01:25.359] the best ones and then send three of

[01:01:26.720] them to a human in Slack and be like

[01:01:28.480] pick which one is the best and kind of

[01:01:30.160] all that kind of stuff. Exactly. All

[01:01:31.359] this basically just becomes software.

[01:01:32.799] That's the point because all we're doing

[01:01:34.079] is we're just designing like API

[01:01:35.920] contracts that have some guaranteed data

[01:01:38.000] model and now we know how to go deal

[01:01:39.440] with this data model in one way. And

[01:01:41.599] like for example like you naturally

[01:01:43.520] being like a systems engineer you went

[01:01:45.200] to being like oh I'll just run all the

[01:01:47.040] high ones in batch parallel. Someone

[01:01:49.280] might not do that. They may do

[01:01:50.319] everything sequentially. They may write

[01:01:51.760] all of them in parallel. It doesn't

[01:01:53.200] matter. It's up to you as an engineer to

[01:01:55.359] decide the trade-offs that you want to

[01:01:56.799] make and the amount of system resources

[01:01:58.880] you want to spend to find the answer.

[01:02:02.960] Um, let's take Sean's question really

[01:02:04.799] fast. Um, normally I do entity linking

[01:02:08.640] as a two-step process, uh, with an

[01:02:10.559] entity reference as a span and then a

[01:02:12.319] link, but then I realized it's more of a

[01:02:14.559] comment than a question. Um, yeah. So, I

[01:02:17.680] see what you're saying. Cool. Yeah, the

[01:02:20.000] span is kind of the only problem that

[01:02:21.680] I've seen with the span is sometimes the

[01:02:24.000] model if you like use URLs, we discussed

[01:02:26.079] this last time in our prompt hacking

[01:02:27.359] thing, a model is just less likely to

[01:02:29.040] actually dump out a URL correctly. So, I

[01:02:31.280] would just recommend swapping out the

[01:02:32.480] URL with some like with some indexed ID.

[01:02:35.200] So instead of having the model dump out

[01:02:36.880] like

[01:02:38.720] https

[01:02:40.240] google.com like this

[01:02:47.510] oops like this query is just going to be

[01:02:47.520] way worse than having the model spit out

[01:02:49.920] like um Google search idx0

[01:02:55.280] like there's just way less tokens and

[01:02:57.119] way way fewer things will go wrong

[01:02:59.599] especially once the URLs have like

[01:03:01.119] something like like ref equals like like

[01:03:04.559] once you get to these things where

[01:03:05.920] things aren't really mattering, your

[01:03:07.119] tokens get completely screwed and hard

[01:03:08.799] to go extract. So you want to be really

[01:03:10.400] careful about what strings you have the

[01:03:12.720] model actually spit out and you want to

[01:03:14.079] reduce the noise or like entropy of

[01:03:16.079] those strings to be as stable as

[01:03:17.920] possible.

[01:03:20.000] Um, and we discussed that last week. We

[01:03:21.599] had a really fun time discussing all

[01:03:22.720] sorts of techniques.

[01:03:24.720] Are you on team beef up models as you

[01:03:26.559] can as you dev or team weaken down

[01:03:28.799] models as you dev? Um, personally I'm on

[01:03:32.720] team of use the best model possible

[01:03:34.480] initially cuz shipping your product is

[01:03:36.160] way more important than um than cost in

[01:03:40.480] the very beginning unless you know for

[01:03:42.319] sure you have cost constraints. I

[01:03:44.799] personally use the maximum amount of

[01:03:46.799] resources that I can for a given project

[01:03:49.359] without optimization in the very

[01:03:50.960] beginning. Dex, what about you?

[01:03:54.640] I like to use big models first and then

[01:03:58.799] pair it down. Um, it depends on the

[01:04:00.799] question. It's the same thing with

[01:04:01.680] developing agents, too. Like the

[01:04:02.960] 12-factor agent stuff is all about like,

[01:04:04.960] hey, let's get right in the weeds and

[01:04:06.319] make things really, really good and

[01:04:07.520] engineer everything. Like,

[01:04:10.160] if you can just give a model 10 tools in

[01:04:12.240] a prompt and it can get it right for

[01:04:13.920] every single use case that you care

[01:04:15.359] about, then do that. And then when you

[01:04:17.359] find the things it can't get right,

[01:04:18.559] that's when you start decomposing and

[01:04:20.079] engineering. Exactly. Or like in our

[01:04:23.039] case today, we knew for sure that it's

[01:04:25.200] impossible for us to dump all the legal

[01:04:27.119] companies into the problem. So, we're

[01:04:29.520] not going to waste our time doing that

[01:04:30.799] because it's it's it's it's not in the

[01:04:33.359] constraints of our problem. So, we'll

[01:04:35.359] start with the minimount of work that we

[01:04:36.799] can. But, you you still need to know

[01:04:38.160] where the walls of the box are and know

[01:04:39.839] like, oh, yeah, I'll I'll never no

[01:04:41.359] matter how good the no matter how big

[01:04:43.280] the model is, this is just never going

[01:04:44.640] to yield good results. So, we're going

[01:04:46.319] to skip trying to do that. But, you'll

[01:04:48.319] notice that I did not write an LLM

[01:04:49.839] prompt for validate company, pick

[01:04:51.280] potential company. I just did the dumb

[01:04:52.559] thing where I just use aliases.

[01:04:55.280] And it might work to be completely

[01:04:56.960] honest. A lot of resumes probably use

[01:04:58.880] like one of 50 words to mention a

[01:05:00.640] company. I may not need an LM for this,

[01:05:03.520] but I might want to use an LM anyway uh

[01:05:05.920] because it's faster. I think one of our

[01:05:07.680] engineers said a really really funny

[01:05:09.039] thing um recently where they mentioned

[01:05:13.039] that we don't actually want to do like a

[01:05:15.280] standard library like languages might

[01:05:17.839] not need a standard library anymore

[01:05:20.240] because technically everything can be an

[01:05:22.480] LLM function. Uh, actually I'll show his

[01:05:24.480] expose.

[01:05:26.319] Um, and I think that was better Antonio

[01:05:31.280] because I thought this was very very

[01:05:32.720] funny.

[01:05:34.240] Uh, he talked about how when you're

[01:05:37.200] actually doing a

[01:05:43.910] uh you could technically do URL encoding

[01:05:43.920] using an LLM instead of actually using

[01:05:47.280] string interpolation and format strings.

[01:05:49.760] And this becomes really interesting

[01:05:51.200] behavior in the future as we as

[01:05:52.640] developers can go out. And right now

[01:05:54.400] this looks extremely silly because we

[01:05:56.559] all know how to do URL encoding uh with

[01:05:59.200] just like string interpolation. But this

[01:06:02.079] might not be as crazy as it sounds

[01:06:03.920] anymore like 5 years from now. Just like

[01:06:06.799] Slack using 70 gigs of RAM would have

[01:06:08.960] been insane 10 years ago, 20 years ago.

[01:06:11.760] And now it's like it's okay. Every

[01:06:13.280] laptop's got enough. We just go spend

[01:06:14.799] the RAM. It might be true for compute as

[01:06:17.440] well.

[01:06:19.039] I love it. Um, anything else before we

[01:06:22.799] close out?

[01:06:31.510] Going once, going twice.

[01:06:31.520] All right. Well, today we covered entity

[01:06:33.520] extraction. Um, thank you guys for

[01:06:36.720] joining us. Next week I think is going

[01:06:38.480] to be really fun. Dex, do you want to

[01:06:40.640] give them a preview of what we're

[01:06:41.599] talking about? Yeah, so I dropped the

[01:06:43.039] link in there. Um, so we do a lot of

[01:06:44.720] work on this show. Um, but we also do a

[01:06:46.400] lot of riffing. And our favorite thing

[01:06:47.839] is to get on and talk with you about

[01:06:49.359] your real problems. And the things that

[01:06:51.680] we don't like doing as much is

[01:06:53.520] downloading videos and creating

[01:06:54.640] transcripts and writing up notes and

[01:06:56.079] things like that. And so we want to

[01:06:59.039] we're going to get a bunch of we're

[01:07:00.319] going to get all the boring stuff set up

[01:07:01.359] ahead of time, but we want to walk

[01:07:02.559] through kind of building live a AI

[01:07:04.960] content pipeline where you can take a

[01:07:06.480] video like this, whether it's sessions

[01:07:09.200] uh that we're doing, whether it's a

[01:07:10.480] video you find online, whether it's a

[01:07:12.240] meeting you have with the customer,

[01:07:13.760] whatever it is, like take recorded

[01:07:15.280] content and turn it into a content

[01:07:17.599] pipeline of like a small blog post, uh

[01:07:20.480] uploading the events in GitHub, pulling

[01:07:22.240] out the transcript, um and kind of just

[01:07:24.720] like doing as as much as we can do get

[01:07:26.960] done in an hour of like how we run the

[01:07:29.520] show in the background and how we use AI

[01:07:31.839] to kind of make it better and how we

[01:07:33.760] apply the we come here and talk about

[01:07:35.119] all these like toy problems. So, next

[01:07:36.799] week we're going to solve a real

[01:07:37.680] problem.

[01:07:39.440] Cool. We're going to be fun.

[01:07:42.720] I have a quick question if you if you

[01:07:46.079] don't mind if you have just a few

[01:07:47.760] seconds. Um the the
