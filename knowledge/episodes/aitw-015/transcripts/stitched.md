# S02E11 – PDFs, Multimodality, Vision Models



Source: YouTube captions (automatic:en)



[00:00:02.389] Otherwise, if

[00:00:02.399] >> Oh, were we not recording today?

[00:00:04.400] >> I think probably someone else joined

[00:00:06.160] with a noteaker or something.

[00:00:07.680] >> Awesome.

[00:00:08.160] >> Yeah. Um, if we do this then now the

[00:00:10.800] transaction is actually going to

[00:00:11.759] continue and I can go do dupes. Now,

[00:00:13.360] this might also be kind of annoying. So,

[00:00:15.599] I'll do the dumb thing and I'll just say

[00:00:17.119] like TXNS equals

[00:00:20.320] get TXNS

[00:00:25.910] without

[00:00:25.920] dupes. I'll just pass in the old TXNS

[00:00:27.920] and the new TXNS. pass through the

[00:00:30.000] model, give it context that these are

[00:00:31.679] coming from some new pages that might

[00:00:33.120] have overlaps from the previous page and

[00:00:35.360] then get out a new full array from the

[00:00:37.200] model

[00:00:38.960] and now we have our answer.

[00:00:41.280] >> Um, and this is only if I actually

[00:00:43.680] continued from a previous page. Uh,

[00:00:46.239] otherwise I wouldn't do it. Uh,

[00:00:48.640] otherwise I would just append everything

[00:00:50.000] all there on its own. And now I' have

[00:00:52.399] built a pipeline that is pretty good at

[00:00:54.800] extracting all this data.

[00:00:57.280] Um, before I get into it, any questions

[00:00:58.879] for people uh, as we're doing this? Does

[00:01:00.960] this kind of make sense? Like the

[00:01:02.399] process that we went through of all the

[00:01:04.080] way originally trying the PDF raw didn't

[00:01:06.320] work. Figuring out how to go do that.

[00:01:08.479] Well, we're going to apply some filters

[00:01:09.600] and only find pages with actual

[00:01:11.119] transactions for every single subsequent

[00:01:12.960] step. Then we're going to go ahead and

[00:01:15.119] solve the biggest problem, which is

[00:01:16.400] headers and footers. Get rid of that.

[00:01:18.479] And then we're going to solve the next

[00:01:19.520] big problem, which is data breaking,

[00:01:21.280] having page breaks. and continuing that

[00:01:23.759] down with a similar problem where I just

[00:01:25.119] ask an LLM, do these pages have

[00:01:27.520] continued data or break points? If the

[00:01:29.360] LM says yes, I do some special stuff

[00:01:31.920] like merge the image into a new image or

[00:01:34.240] paste both images in.

[00:01:48.149] >> Yeah, I mean this approach makes sense.

[00:01:48.159] Um, I'm trying to restrain like the

[00:01:50.960] receptive field of of an LLM basically.

[00:01:54.399] >> Um,

[00:01:55.600] >> I'm just wondering if like there are

[00:01:58.079] pretty good OCR models that do bounding

[00:02:01.040] box detection. Um, so would like

[00:02:05.600] would it make sense to

[00:02:08.000] restrain the field even more just by

[00:02:10.560] using a bounding box of the line item

[00:02:13.280] instead of trying to like do this the

[00:02:15.440] this page magic?

[00:02:18.160] You can try that. In general, what I

[00:02:20.000] have seen with bounding box models is

[00:02:21.360] that they're generally worse than LLMs

[00:02:22.959] at a lot of things. Um, so like it's the

[00:02:26.319] same as like using an OCR model instead

[00:02:28.720] of an LLM. On average, you're probably

[00:02:30.480] right. It might work, but like what I

[00:02:32.160] have seen in practice that the LM just

[00:02:33.760] does a much better job. I think LM can

[00:02:36.080] do more than you think. Um, but they

[00:02:38.720] just need a little bit more stability to

[00:02:40.480] help with them. So like if we get rid of

[00:02:43.120] all the transaction data, I think that

[00:02:44.959] like you you're definitely right. you

[00:02:46.640] will get that transaction pulled out.

[00:02:48.640] But I have found very very few bounding

[00:02:51.200] box algorithm that'll actually detect

[00:02:53.680] like every single bounding box on this

[00:02:55.519] correctly because the semantic meaning

[00:02:57.519] of a bounding box here is very

[00:02:59.760] different. The semantic meaning of a

[00:03:01.120] bounding box here is like this whole

[00:03:02.480] thing.

[00:03:04.560] Good luck getting a bounding box to give

[00:03:06.480] you that shape.

[00:03:08.400] That's just not going to work. What the

[00:03:09.519] batting box algorithm will do is they'll

[00:03:10.720] give you this one and it'll give you

[00:03:12.800] this maybe if you're lucky and then I'll

[00:03:16.319] give you this

[00:03:18.560] and then I'll give you this

[00:03:21.360] and now you're still stuck in a world of

[00:03:23.680] pain of connecting all this stuff

[00:03:24.959] together and that is a really really

[00:03:27.519] really really hard problem. This is why

[00:03:30.879] I think the math approach didn't really

[00:03:32.720] work and why like training models end to

[00:03:35.840] end would ended up being the answer

[00:03:37.040] because the math approach would connect

[00:03:38.400] all these together. Can you do this?

[00:03:40.080] Yes.

[00:03:41.840] It will just take more time, more tuning

[00:03:43.840] and more correctness to go do this

[00:03:46.720] >> and it will work on a less diverse set

[00:03:49.599] of data and inputs. The reason that I

[00:03:52.319] shared the header technique is not

[00:03:53.760] because I think that's one of the best

[00:03:54.879] techniques, but because there's a level

[00:03:57.200] of standardization that I know is true

[00:03:59.519] in headers,

[00:04:01.280] it's like almost definitively true in

[00:04:03.360] headers.

[00:04:04.159] >> And so why not give yourself the extra

[00:04:06.159] 1% by just forcing the model to ignore

[00:04:08.640] everything there basically.

[00:04:11.040] >> Exactly. And this is only after finding

[00:04:13.360] out that like in in the case of

[00:04:14.640] financial data like headers are like a

[00:04:16.079] big problem. In the case of medical

[00:04:17.280] records, headers are a big problem. uh

[00:04:19.600] the model just gets like confused by a

[00:04:21.600] bunch of like numbers and stuff at the

[00:04:22.880] bottom. Uh is kind of what we found.

[00:04:25.199] It's like like these numbers end up

[00:04:27.199] hurting the model's performance a lot

[00:04:28.720] more. Uh passing in a page like this

[00:04:32.400] hurts the model's performance a lot

[00:04:33.919] more. So like just like

[00:04:37.120] removing extra context from the model

[00:04:39.280] does help that it doesn't need for sure,

[00:04:42.320] but I also don't want to accidentally be

[00:04:44.240] stuck in a world of pain where I have to

[00:04:45.520] go and find all these weird edge cases

[00:04:47.759] myself. I want to do the simplest thing

[00:04:49.680] that takes almost no code that I can go

[00:04:51.919] vibe code up that gives me that 1%. It's

[00:04:54.880] a time to ROI problem over everything

[00:04:57.120] else. Does that answer the question, AJ?

[00:05:00.160] >> Yeah, it does. Cool. No, that makes

[00:05:01.680] sense. Thanks.

[00:05:02.639] >> Yeah, of course. Uh VJ, you got a

[00:05:04.080] question?

[00:05:06.479] >> Yeah, I I had a similar scenario

[00:05:09.680] previously when we were processing

[00:05:11.919] invoices. Yeah,

[00:05:13.840] >> this is pre-LM days when we were all

[00:05:16.080] building RPA boards and automations and

[00:05:18.160] stuff.

[00:05:20.400] >> So, we had different uh invoices coming

[00:05:24.080] in from different vendors and we were

[00:05:26.160] trying to build these automation

[00:05:27.360] pipelines

[00:05:29.039] uh and as as you can imagine like a

[00:05:31.440] large enterprise has so many vendors and

[00:05:33.680] each vendor might have their own format

[00:05:35.759] for invoice and headers and stuff and

[00:05:38.080] they have their own different sizes. So

[00:05:40.720] what we ended up doing is we we again

[00:05:43.680] took the uh paro principle there. We

[00:05:46.000] took around 80% of the uh invoices which

[00:05:48.720] had like five or six formats and try to

[00:05:51.039] automate that another another 20%

[00:05:54.240] uh sort of either now you could say

[00:05:57.039] those are human in the loop but those

[00:05:58.720] are processed manually.

[00:06:00.800] uh I think that approach might be

[00:06:02.880] applicable here as well where let's

[00:06:05.360] let's imagine if you have a repo of a

[00:06:07.520] million records historically you want to

[00:06:09.520] process your entire data bank then uh

[00:06:13.440] then I think you'll have to adapt these

[00:06:14.960] pipelines using that uh uh approach as

[00:06:18.240] well correct exactly so what I would do

[00:06:21.919] if I really building this pipeline out

[00:06:23.440] from like scratch on my own is I

[00:06:26.000] actually wouldn't build headers and

[00:06:27.280] footers out on every single process what

[00:06:29.919] I would do is I would just save this per

[00:06:32.160] type of vendor that's coming in. Do a

[00:06:33.919] quick extraction of like what vendor is

[00:06:35.280] this like Chase, US Bank or like the top

[00:06:37.600] 500 banks that exist.

[00:06:39.919] save PDFs

[00:06:42.160] together

[00:06:43.759] and just like have that saved forever

[00:06:46.319] and then literally every single week

[00:06:48.400] pull one% of my pipeline through this

[00:06:50.960] script to see if the header changes

[00:06:52.720] dramatically and if it does put a human

[00:06:55.520] in the loop in that process and then

[00:06:57.680] once I put a human in the loop in that

[00:06:59.199] process I will basically just go ahead

[00:07:02.080] and um solve um like validate the data

[00:07:07.680] that it's doing is not randomly a header

[00:07:09.360] and footer because it's financial data,

[00:07:10.960] I don't accidentally want to lose

[00:07:12.639] something critical.

[00:07:14.400] And that's kind of how I would solve

[00:07:15.759] this problem like more long term. I do a

[00:07:17.840] hybrid of exactly what you were

[00:07:18.960] repeating, Vay, which is like specialize

[00:07:21.120] for

[00:07:22.720] um specialize for um specific vendors

[00:07:26.880] and as much as possible and then the

[00:07:28.639] other 90% just get slightly worse

[00:07:30.160] quality or other 10% get slightly worse

[00:07:32.880] quality.

[00:07:34.960] >> Correct.

[00:07:40.550] Everyone that's listening should 100% do

[00:07:40.560] that for as much of their pipelines as

[00:07:42.000] they can. It's like you drive really

[00:07:43.759] high quality for u certain vendors that

[00:07:46.560] you know are well understood and like

[00:07:48.400] represent 80 to 90% of your data and

[00:07:50.560] like sacrifice some lower quality on

[00:07:52.000] 10%. You have to understand that as a

[00:07:53.759] part of building your AI pipeline.

[00:07:56.639] um

[00:07:57.360] >> where sorry if I can have a follow-up

[00:08:00.240] question where I have difficulty in

[00:08:03.120] extracting since we are talking about

[00:08:04.720] multimodality

[00:08:06.400] uh is extracting legal clauses for

[00:08:08.879] example I have a use case where I'm

[00:08:10.720] building uh extracting contracts like

[00:08:13.360] vendor contracts vendor clauses those

[00:08:16.160] are so random and they're defined per

[00:08:18.960] use case per vendor one vendor can have

[00:08:22.160] 100 contracts which with you know

[00:08:24.639] different contexts

[00:08:26.000] So it's so complex to extract these

[00:08:28.479] legal clauses that uh the the I mean

[00:08:31.680] writing EAS for that is is just a

[00:08:33.760] nightmare for me. What I would recommend

[00:08:36.560] for a scenario like um abstract

[00:08:39.360] scenarios like legal clauses where it's

[00:08:41.279] not even concrete what is a legal clause

[00:08:43.200] or not is I would honestly just go and

[00:08:46.240] write take 50 documents and by hand pull

[00:08:49.200] out what you would want to pull out and

[00:08:51.440] then see if you can semantically

[00:08:53.200] understand them. So I think a similar

[00:08:55.040] problem that we worked with a company on

[00:08:56.399] was around SEC violations like detect

[00:08:58.880] SEC violations from like emails. That's

[00:09:03.040] a really

[00:09:03.760] >> this was our uh policy to prompts

[00:09:05.440] episode that was like the example we did

[00:09:07.120] >> right.

[00:09:09.839] >> And the thing is like instead of trying

[00:09:11.440] to solve all of SEC in one prompt

[00:09:13.440] because models can't do that today maybe

[00:09:14.959] they can tomorrow but not today. Um

[00:09:17.839] we'll pick one policy and we'll make it

[00:09:20.320] work on that. Then we'll pick another

[00:09:21.760] policy make it work on that. It's

[00:09:23.279] exactly the same as an invoice problem

[00:09:24.720] where you instead of specializing per

[00:09:26.320] vendor, we take the general thing of

[00:09:28.720] legal clause and we break it down to

[00:09:30.320] specialized clauses and we get really

[00:09:32.399] high performance on those specialized

[00:09:33.920] clauses and we plan that out. So you

[00:09:37.680] could manually do something. Let me vib

[00:09:40.240] I think this is building a little bit

[00:09:41.600] but let me know if this sounds crazy is

[00:09:43.200] you could do something like take 50 to

[00:09:46.320] 100 like legal clauses that you know

[00:09:49.600] turn them into kind of like almost like

[00:09:52.000] their own classification sets with

[00:09:53.680] really good descriptions. Have the LLM

[00:09:55.440] try to categorize into one of those

[00:09:56.959] hundred. If it can't do it, it goes into

[00:09:59.040] the other category. It goes into your

[00:10:00.640] manual queue to go, "Oh, this is belongs

[00:10:02.720] in this category. we need to change the

[00:10:04.240] prompt for that category or this doesn't

[00:10:07.279] belong in any category, we need to make

[00:10:08.720] a new category. And like that you can

[00:10:10.720] kind of build up where like even if the

[00:10:12.240] wording is slightly different, if

[00:10:13.920] semantically it fits into one of your

[00:10:15.519] hundred categories, then you have a

[00:10:17.360] solution. Does that sound accurate?

[00:10:20.399] >> Dexter has basically become the ultimate

[00:10:22.880] to value translator.

[00:10:25.360] A lot of words and Dexter says a lot of

[00:10:27.040] more better words and it's much better I

[00:10:29.920] say. Uh um I'll take one more question

[00:10:32.959] and then I think we're going to hop out

[00:10:34.399] for today. Um sadly can't go the full 90

[00:10:36.720] minutes, but if you post a question in

[00:10:38.079] Discord, we'll get to it by the end of

[00:10:39.519] the day.

[00:10:40.399] >> Also, for the for the record, this show

[00:10:42.320] runs an hour, so every minute after

[00:10:44.240] after 60 minutes. Uh you're welcome. Uh

[00:10:47.120] but thank you for bringing good

[00:10:48.399] questions. This has been super fun. Um

[00:10:50.720] yeah, Andre, you want to take us out

[00:10:51.920] with the last one?

[00:10:53.360] >> Yeah, really interesting techniques with

[00:10:55.040] cropping. So I'll tell you how I've done

[00:10:56.720] this with um medical records. So I I do

[00:11:00.079] the OCR and then just extract the text

[00:11:03.200] and the the OCR is pretty accurate um

[00:11:06.240] for the text and then I pass the

[00:11:08.240] language model both the text from the

[00:11:09.920] OCR and attach the PDF and for medical

[00:11:13.360] records that just seems to work and it

[00:11:15.760] might work for for bank statements too.

[00:11:17.920] Um but you would have to dduplicate

[00:11:20.560] things probably and check with your

[00:11:22.320] technique.

[00:11:23.519] >> Yeah, exactly. Yeah,

[00:11:24.959] >> exactly. That that's um yeah, this

[00:11:27.600] technique with OCR, we found the same

[00:11:29.200] thing for a lot of medical companies.

[00:11:30.399] They do OCR first, but what they found,

[00:11:32.720] what we found is actually every company

[00:11:35.120] that was doing that has now stopped

[00:11:36.480] doing that. They just pass the data

[00:11:37.760] directly to the model with no OCR in the

[00:11:39.519] middle and it actually works better.

[00:11:43.360] >> Nice.

[00:11:44.000] >> So, I would try that in the more newer

[00:11:45.680] models and see if you get better results

[00:11:47.040] and report back. We'd love to hear and

[00:11:48.640] see if that works for you as well.

[00:11:50.320] >> Thanks. Good stuff.

[00:11:52.399] >> Cool. Would that
