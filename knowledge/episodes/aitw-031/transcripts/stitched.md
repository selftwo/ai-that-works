# Dates, Times, and LLMs



Source: YouTube captions (automatic:en)



[00:00:02.790] We're just waiting on Dexter to show up.

[00:00:02.800] So, we should be starting fairly soon.

[00:00:05.359] Uh, but while we wait,

[00:00:08.080] as you all know, this is going to be AI

[00:00:10.000] that works. We've got a couple questions

[00:00:13.280] that we can take while we're just

[00:00:14.480] hanging out, uh, waiting for Dexter to

[00:00:16.080] show up.

[00:00:17.920] But, I think today's episode is going to

[00:00:19.680] be really fun. We're going to start

[00:00:21.039] doing some live coding. Uh, which

[00:00:24.160] usually we go to whiteboards, we go all

[00:00:25.680] these other things, but we're just going

[00:00:26.880] to go straight into it.

[00:00:32.790] So, I'll be back in a couple minutes,

[00:00:32.800] but I'll see you in a second.

[00:01:59.590] All right. Um, Dexter is actually having

[00:01:59.600] some phone difficulties. His phone is

[00:02:01.280] bricked um, as we have learned and he is

[00:02:04.000] all the way over in Egypt right now. So,

[00:02:06.960] international travel is um, exciting to

[00:02:09.920] say the least.

[00:02:11.680] But I think today's episode, we'll get

[00:02:13.680] it kicked off. Hopefully Dexter can join

[00:02:15.120] in a few. Uh and then as we go start,

[00:02:17.760] we're just going to go right into the

[00:02:18.800] coding side of it.

[00:02:22.400] As we're doing this, let's start talking

[00:02:24.879] about the most important thing, which is

[00:02:26.560] if we're going to go and talk about

[00:02:27.920] dates and LMS and time zones, how do we

[00:02:30.800] actually make them work? There's a lot

[00:02:32.319] of ambiguous questions that come out of

[00:02:33.840] it. For example, I could say, let's go

[00:02:35.840] meet up next Tuesday. And I think today

[00:02:38.560] being Tuesday right now, at least on the

[00:02:40.080] West Coast, it's unambiguously clear by

[00:02:43.120] that I mean November the 18th instead of

[00:02:46.400] November 11th, which is today or even

[00:02:48.160] the Tuesday after that. On the other

[00:02:50.080] hand, if we were yesterday on Monday and

[00:02:53.040] we are saying let's meet up next

[00:02:54.080] Tuesday, that almost probably means to

[00:02:56.720] meet up on November 18th as well. But

[00:02:59.440] yesterday if we had said let's meet up

[00:03:00.720] next Saturday I could see how someone

[00:03:02.720] could misinterpret that and say that

[00:03:04.879] actually the sat upcoming Saturday

[00:03:07.760] as opposed to the following. And as date

[00:03:10.400] times happen it's really hard to get a

[00:03:12.480] model to go and obey them. If your users

[00:03:15.280] are in a different time zone than your

[00:03:17.040] servers and you go and the user says

[00:03:19.280] let's meet up at midnight tonight. the

[00:03:22.159] LM can't possibly understand that if

[00:03:24.159] you're normalizing all your time zones

[00:03:25.599] to us like the UCT or your server's time

[00:03:29.200] zone, the Pacific Coast or US East SWAT.

[00:03:31.440] So, it's important to be really really

[00:03:32.720] careful about how time zones make sense

[00:03:34.640] because if you don't deal with dates and

[00:03:36.239] times correctly, a chat thread that is

[00:03:38.080] otherwise going perfectly can easily

[00:03:39.680] mess up and give you the wrong

[00:03:42.239] information. So to get started with

[00:03:44.400] today's conversation, I'm just going to

[00:03:46.319] go straight into screen sharing and

[00:03:48.159] start going through code because I think

[00:03:50.799] there's not much whiteboard to do here.

[00:03:52.239] We just have to write some code and

[00:03:53.360] prompt it a prompt our way to success.

[00:03:55.200] And what's awesome about this problem,

[00:03:57.120] it's actually not that hard to get

[00:03:58.640] right.

[00:04:00.560] So let me know if you have a hard time

[00:04:02.080] seeing my screen. I'll try and zoom in.

[00:04:04.000] Um, and as we go about it, we should

[00:04:06.879] hopefully be good to go. So I've already

[00:04:09.840] started a Python project here. Uh, but

[00:04:12.560] I'm just going to

[00:04:14.720] add BL pi

[00:04:27.510] Cool.

[00:04:27.520] And now we've got our project. As you go

[00:04:30.639] about this, let's make a datetime

[00:04:32.160] evaluator.

[00:04:38.550] So the first thing to go here is to talk

[00:04:38.560] about and

[00:04:40.880] think about exactly how are we going to

[00:04:42.720] actually build some of these functions.

[00:04:46.320] So the first thing that we're going to

[00:04:47.520] do is just say something like let's say

[00:04:50.160] we have a function that's going to say

[00:04:51.759] we're going to get a uh we're going to

[00:04:54.240] extract relevant dates out of a

[00:04:55.840] conversation

[00:05:03.749] string and we'll do like for now we'll

[00:05:03.759] just return a string array. We'll go

[00:05:05.280] here and we'll say uh client open AI

[00:05:09.600] GPT4 mini. I don't know why I like that

[00:05:11.600] model. So I just do prompt that I like

[00:05:14.320] because it's fast and cheap. Um, extract

[00:05:16.880] all the dates from the following text.

[00:05:18.560] Ctx

[00:05:20.080] output format

[00:05:32.390] text. So we got a really really basic

[00:05:32.400] prompt and we'll go about this. And why

[00:05:33.840] am I extracting dates first? Well, I

[00:05:35.680] think the most important part is can I

[00:05:36.960] have the model understand the dates?

[00:05:38.800] Understanding dates within semantics is

[00:05:40.720] even harder. But perhaps what I want the

[00:05:42.720] model to do is just like normalize every

[00:05:44.240] date that comes across some sentence in

[00:05:47.199] a much easier to understand way. So

[00:05:48.720] let's try and do that.

[00:05:50.880] So what am I going to do here now? I'm

[00:05:52.240] going to write a test case

[00:05:54.960] dates

[00:05:57.520] uh functions

[00:05:59.759] extract date and then args

[00:06:02.960] oops

[00:06:09.270] uh text

[00:06:09.280] and the text will be uh let's hang out

[00:06:13.680] next Friday. So we'll do

[00:06:17.520] relative dates.

[00:06:20.800] We'll make a couple test cases off the

[00:06:22.560] bat. Um,

[00:06:28.390] we'll do this November 15th, 10:00 a.m.

[00:06:28.400] Um,

[00:06:30.240] time zone.

[00:06:37.110] Uh, one second. Get rid of these time

[00:06:37.120] zones here

[00:06:44.390] at 6:00 p.m.

[00:06:44.400] Cool.

[00:06:46.080] And now as we go about this, let's think

[00:06:48.080] about how we can go answer this question

[00:06:49.600] really quickly.

[00:06:57.909] Now when we go run this, let's just run

[00:06:57.919] this prompt really quickly and see what

[00:06:59.520] happens. So the model seems to

[00:07:01.039] understand November 15th as a date. But

[00:07:03.120] the first first question I'm getting is

[00:07:05.120] okay, what about November 15th versus

[00:07:06.880] 11? How do we standardize date formats?

[00:07:09.360] Well, this is where it starts to get a

[00:07:11.199] little tricky. So let's just do this

[00:07:12.880] really fast. We'll do year, month, date

[00:07:18.000] over here. And then we'll return the

[00:07:19.280] date.

[00:07:24.150] And now when I do this, I get something

[00:07:24.160] a lot more standardized than what I

[00:07:26.080] could have done before because no matter

[00:07:28.000] what happens, it will just convert stuff

[00:07:29.520] to next Friday and everything else. So

[00:07:31.120] let's run actually all the tests because

[00:07:33.039] I don't want to just run this one test.

[00:07:44.950] So absolute date it got right 115. Uh

[00:07:44.960] date with time zone it got right. And

[00:07:47.520] then relative date it did not understand

[00:07:49.440] because next Friday doesn't mean

[00:07:50.800] anything. Well there's a couple other

[00:07:52.720] ways that we can do this. So we can say

[00:07:54.400] like absolute date

[00:07:59.039] relative date. And what you can do here

[00:08:01.120] is like you can make this a string

[00:08:03.840] uh

[00:08:09.909] string at description. I think there's a

[00:08:09.919] standardized timing format called uh

[00:08:12.960] it's not like uh let me look this up

[00:08:14.879] really fast and tell you what it is

[00:08:18.000] timing

[00:08:24.070] I think it's like there's a very

[00:08:24.080] standard way to go do this

[00:08:43.110] So, we'll just try this. And now inside

[00:08:43.120] of date, we're going to get a

[00:08:51.350] boom. So, now the prompt is still very

[00:08:51.360] simple. It's either going to be year,

[00:08:53.120] month, date, which is absolute, or a

[00:08:54.560] relative time.

[00:08:59.829] One more thing about what this did. Let

[00:08:59.839] me rerun all the tests.

[00:09:06.470] again.

[00:09:06.480] And this still works. It got us an

[00:09:08.080] absolute date. This got next Friday.

[00:09:09.920] Again, not very useful because next

[00:09:11.360] Friday still can't be read in a good

[00:09:13.040] way. So, I think there's a

[00:09:15.760] uh use date use duration

[00:09:21.279] strings like

[00:09:30.230] uh so there's different ways to do this.

[00:09:30.240] So for example, you could use a duration

[00:09:31.839] string like this format. Let me ask you

[00:09:34.240] what this format is. And now we get P7

[00:09:36.080] days. Why does it do P7 days? Because

[00:09:37.680] the model for some reason thinks that

[00:09:39.279] this is a week from now. It's still not

[00:09:41.200] understanding the problem. So let's

[00:09:43.200] think about what we're really doing

[00:09:44.240] here. The reason that this is struggling

[00:09:46.080] is because no matter what we do, the

[00:09:48.080] model isn't able to have context on what

[00:09:50.080] the day it is today and how you respond

[00:09:52.880] to a date in many different formats. So

[00:09:55.120] for

[00:09:55.600] >> like when you're like 10 minutes late.

[00:09:58.000] >> It's very different than saying

[00:10:00.240] something like let's hang out two days

[00:10:03.839] from now

[00:10:06.080] where this test should work with 100%

[00:10:08.320] accuracy because this is a good way to

[00:10:10.160] represent the data. P1D P2D it's very

[00:10:13.920] easy to understand what you're doing

[00:10:15.279] here. On the other hand a question like

[00:10:18.000] next Friday is much more ambiguous and

[00:10:21.360] this data model doesn't actually

[00:10:23.120] represent this. Let's try this again.

[00:10:26.160] >> Yo, Vipob, can you hear me?

[00:10:27.920] >> Relative date

[00:10:31.040] uh relative uh

[00:10:34.480] days

[00:10:36.959] and we can say

[00:10:39.760] from

[00:10:42.160] nearest

[00:10:48.230] and then we can put like a we can put

[00:10:48.240] some sort of like date type on here. So,

[00:10:50.399] let's just say like string for now. And

[00:10:53.200] then we can say relative

[00:10:59.350] date

[00:10:59.360] string

[00:11:01.040] description.

[00:11:03.519] So we can say is like we can say there's

[00:11:05.200] a source

[00:11:07.200] that comes from here. There's some

[00:11:08.480] relative source and then given the

[00:11:10.079] source here's the relative date string

[00:11:11.760] that we have.

[00:11:13.680] So if we start with this string and we

[00:11:15.519] do this this one will still work. Oops.

[00:11:25.350] with source

[00:11:25.360] and now we'll go into a different

[00:11:26.800] question that is if we're actually going

[00:11:29.200] to go about and answer this question

[00:11:30.959] what does this do relative days well

[00:11:33.600] let's try and run this it still didn't

[00:11:36.240] understand so let's try and add a source

[00:11:38.000] date to this

[00:11:40.399] source

[00:11:42.560] let's say Monday uh November 10th uh

[00:11:46.399] 2025

[00:11:48.000] is the date that I'm going to give

[00:11:50.000] And we'll add another optional parameter

[00:11:51.680] into here called source

[00:11:54.880] string right here

[00:11:58.880] without

[00:12:11.590] reference

[00:12:11.600] a refer and state.

[00:12:14.560] Boom. Let's try running this query

[00:12:17.360] really fast.

[00:12:19.519] If we do this, it's still not working.

[00:12:21.839] Let's try again.

[00:12:25.200] I suspect it's because these types are

[00:12:27.360] kind of confusing. So, let's just add a

[00:12:29.120] more metadata here

[00:12:38.629] and try running this now.

[00:12:38.639] So, now it kind of understood. It was

[00:12:40.480] able to go and say I want a relative

[00:12:41.920] date and the date is going to be 4 days

[00:12:43.920] from now. But it wasn't able to

[00:12:45.120] understand that's using some source.

[00:12:46.560] >> Hi Bob, turn your sound on. So, let me

[00:12:48.240] pause one more time and try and think

[00:12:49.600] again through this problem as we're

[00:12:51.040] going to go think about this in real

[00:12:52.240] time.

[00:12:54.160] >> Oh, Dex, you're there. I can't hear you.

[00:12:56.079] >> Dude, I've been here. Turn your sound

[00:12:58.000] on.

[00:13:03.670] >> Can you hear me? Can you hear me?

[00:13:03.680] >> Yes, I can hear you now.

[00:13:05.600] >> Fantastic.

[00:13:06.160] >> Okay, you're back alive. Sorry, I wasn't

[00:13:08.320] sure when you shut up.

[00:13:09.839] >> Dude, you missed it. I said joke about

[00:13:13.120] not understanding.

[00:13:15.600] >> Oh. Hey,

[00:13:21.670] >> guys.

[00:13:21.680] >> Also, your your echo is now.

[00:13:24.480] >> Oh,

[00:13:31.750] >> are we good?

[00:13:31.760] >> Can you hear me?

[00:13:32.320] >> Yes, I can. I think we're good.

[00:13:34.320] >> Amazing. Sorry for the interruption. I

[00:13:36.480] completely derailed everything. Uh, my

[00:13:39.360] god, do I have a story for you. But, uh,

[00:13:42.079] I just, uh, the amount I went through to

[00:13:45.760] get here. Oh, man. Anyways, back to

[00:13:48.959] dates and times. I'm so excited. Keep

[00:13:51.120] going what you were doing. I'll ask

[00:13:52.560] questions. We'll do the thing.

[00:13:54.079] >> Let's do the thing. Um, I'm so glad I'm

[00:13:56.639] I switch screens. I was like, I suspect

[00:13:58.480] Dexter is going to show up anytime now.

[00:14:04.470] >> U, let me switch over really fast. Let

[00:14:04.480] me find the window.

[00:14:06.480] Cool. So, as you go about this problem,

[00:14:08.959] let's first like reason about So, Dex,

[00:14:10.880] I'll catch you up. I don't know where

[00:14:11.839] where you're caught up to.

[00:14:15.120] >> Uh, catch me up.

[00:14:16.720] >> Okay. So, the problem is we want to go

[00:14:19.040] ahead and answer questions like, "Let's

[00:14:20.639] hang out next Friday. Let's hang out two

[00:14:22.560] days from now. The meeting is on

[00:14:23.760] November 15th. The meeting is at

[00:14:25.120] November 15th on 6 p.m." And there's all

[00:14:27.440] sorts of different semantics that get

[00:14:28.880] tricky here.

[00:14:29.360] >> Or like,

[00:14:31.680] >> can you add another one that is like the

[00:14:33.279] podcast is a 10 a.m. PT just like it is

[00:14:35.680] every week? Oh, yeah.

[00:14:39.360] >> 10 a.m. PT on Tuesday.

[00:14:42.399] >> We'll see if Claude is uh smarter than

[00:14:44.320] me.

[00:14:57.670] Cool. So what's really interesting about

[00:14:57.680] this is given all these date times,

[00:15:01.680] what I find personally really

[00:15:03.040] fascinating is there's so many different

[00:15:04.399] data models that you can use to

[00:15:05.839] represent all of these. Because for

[00:15:07.600] example, saying something like the

[00:15:09.360] podcast at 10:00 a.m. PT every Tuesday

[00:15:11.839] is a funly fundamentally different

[00:15:13.680] question than saying the meeting is on

[00:15:14.880] November 15th because this usually

[00:15:16.399] implies that there's a single

[00:15:17.519] occurrence. This is a regular

[00:15:19.440] reoccurring meeting. That means the year

[00:15:21.839] is not very as relevant. Even the date

[00:15:23.519] and everything is not relevant. In fact,

[00:15:25.760] in order to know where the next when the

[00:15:27.760] next podcast is, you have to know what

[00:15:29.519] today is. Otherwise, you can't possibly

[00:15:31.839] answer the question relative to the

[00:15:34.000] user.

[00:15:35.600] Um, and whereas everything else is kind

[00:15:37.839] of anchored to a very very specific

[00:15:39.440] date. So, I think the problem that most

[00:15:41.199] people run into when they try using

[00:15:42.800] dates with LLMs is as we're just seeing

[00:15:44.880] here on all these test cases, there's no

[00:15:47.279] single way to really represent them.

[00:15:50.160] There they all are genuinely very very

[00:15:52.560] different scenarios. What's your first

[00:15:54.880] instinct decks before I go into like at

[00:15:56.720] least what I have found works for this

[00:15:58.480] kind of scenario?

[00:16:07.829] Oh, did Dex die again? Dex is

[00:16:07.839] disappeared. Uh, we'll bring him back in

[00:16:10.639] a second. I suspect he's having internet

[00:16:12.399] issues.

[00:16:19.910] But at least for me, when I first think

[00:16:19.920] about this, my instinct,

[00:16:28.710] Welcome back, Dex, you are having

[00:16:28.720] massive echo.

[00:16:40.629] Hello. Can you hear me? There you go.

[00:16:40.639] >> Okay, I'm muted. Did we good? Sorry.

[00:16:43.360] >> You're going to have to

[00:16:43.920] >> I had to leave and come back to switch

[00:16:45.360] to my AirPods.

[00:16:46.720] >> That's okay. I think you're gonna have

[00:16:48.000] some echo based on the headphones you're

[00:16:49.680] using, but that's totally fine.

[00:16:52.000] But while we're here, as I go about this

[00:16:54.320] and I explain the few edge cases that we

[00:16:56.000] have, what's your first instinct to your

[00:16:57.519] decks when you look at this and you're

[00:16:59.199] like, I want to go ahead and go make

[00:17:00.959] this slightly better. How would you

[00:17:03.120] address the wide variety of date

[00:17:05.039] questions that people might be asking

[00:17:06.640] here?

[00:17:08.240] >> Number one is inject today's date into

[00:17:10.720] the prompt. Okay. So, you want to have

[00:17:13.360] like a today in there.

[00:17:16.640] Uh, so I'll call that source.

[00:17:19.600] And for now, we'll just use Monday,

[00:17:21.919] November 10th as our source everywhere.

[00:17:31.270] What else? What else would you do?

[00:17:31.280] >> Um, can you show me the extract dates,

[00:17:33.200] the prompt?

[00:17:34.960] >> Well, we'll update the prompt together

[00:17:36.480] because I actually want your thoughts on

[00:17:37.600] it. But I mean, like in terms like a I

[00:17:39.440] guess here, I'll show it to you. This is

[00:17:40.640] what we have. I have something very very

[00:17:42.480] simple at least for now.

[00:18:00.310] >> Yes. So what is your what's your first

[00:18:00.320] gut instinct on how you would solve like

[00:18:02.320] the wide variety of dates that we have

[00:18:04.080] here?

[00:18:13.430] Uh, I don't I don't know. I mean, I

[00:18:13.440] would want to just run one of these and

[00:18:14.720] see what we get and then I would tell

[00:18:16.080] you what needs to change.

[00:18:17.760] >> How about we run all of them?

[00:18:23.750] >> Okay, let it rip.

[00:18:23.760] >> Run all of them and let's just look at

[00:18:26.400] it. So, after running all of them,

[00:18:28.240] here's what we've got. Absolute dates,

[00:18:31.919] uh, which was absolute time. Absolute

[00:18:34.240] dates was this one, I believe. Where'd

[00:18:35.760] it go?

[00:18:36.960] The meeting is on November 15th. I think

[00:18:38.720] that detected it correctly. It detected

[00:18:40.400] 2025, 11:15. That worked.

[00:18:43.520] Absolute time did not seem to work.

[00:18:46.960] But that makes sense because like 10:00

[00:18:49.520] a.m. PT every Tuesday. You can't really

[00:18:51.440] extract a date from that. It's very hard

[00:18:53.280] to at least.

[00:18:59.750] Dates with time zones

[00:18:59.760] is this one. Monday, November 15th at 6

[00:19:03.120] p.m. That seems to work, but it didn't

[00:19:05.200] get the time because we don't model the

[00:19:06.640] time yet. Relative dates is this one.

[00:19:10.320] Let's hang out Friday, which is 4 days

[00:19:12.799] from Monday. P P P P P P P P P P P P P P

[00:19:13.840] P P P P P P P D4.

[00:19:16.000] And then relative date two days from now

[00:19:17.520] is PD2.

[00:19:22.390] >> Okay,

[00:19:22.400] >> so some of it

[00:19:24.000] >> some of it seems to be working, but I

[00:19:25.760] find that like what is not recurrence

[00:19:27.520] times. So, when you see that the

[00:19:28.960] recurrence time isn't working, what's

[00:19:30.240] your gut instinct?

[00:19:43.029] >> how do you prompt your way out of this

[00:19:43.039] hell?

[00:19:45.440] >> I would

[00:19:48.240] my really naive without thinking too

[00:19:50.000] much about it is I create a I create a

[00:19:52.000] new class that is a recurring date.

[00:20:02.789] Uh,

[00:20:02.799] >> sure. Like why not?

[00:20:05.360] >> Bronze string is fine. Okay. And maybe I

[00:20:07.360] I also want to know like when is the

[00:20:09.679] next one like next occurrence.

[00:20:13.919] >> So what's interesting about the next

[00:20:15.520] occurrence is technically if we have a

[00:20:16.720] chron string we can compute it using

[00:20:18.320] software.

[00:20:19.840] >> Okay, fair.

[00:20:21.039] >> Right. Like we don't actually need to go

[00:20:22.240] do this. We need to take the chron

[00:20:23.280] string and go proc it. I've actually

[00:20:24.799] never used a chron string. I have no

[00:20:26.000] idea what this means. So, we can just

[00:20:28.480] try this and then let's try.

[00:20:29.919] >> That's insane, by the way, that you've

[00:20:31.760] never used a cron string. I do not

[00:20:33.280] believe that.

[00:20:34.159] >> I really have not. Is this correct? I

[00:20:37.120] have no idea.

[00:20:39.600] Um, I want to ask cursive to explain

[00:20:42.559] this cron string to me.

[00:20:44.799] >> And the time zone is wrong or it's it's

[00:20:46.880] not time zone a crons are almost always

[00:20:49.520] UTC, I think.

[00:20:51.520] >> Um,

[00:20:53.120] okay. That's interesting. Well, because

[00:20:55.280] you run them on servers.

[00:20:57.760] >> Yeah. Yes, I recognize that. But I did

[00:21:00.240] not im immediately recognize that

[00:21:02.000] because um for obvious reasons. What

[00:21:04.799] does that cron string

[00:21:09.760] mean? Let's just double check this

[00:21:12.159] really fast. And if it's good, I'm just

[00:21:13.360] going to put an assert on this. Oh, 10

[00:21:16.159] a.m. every Tuesday. So every uh server

[00:21:18.159] time.

[00:21:19.760] >> Yeah. So the two is the day of week, the

[00:21:22.080] last one. So it's zero is Sunday, one is

[00:21:26.159] Monday.

[00:21:26.960] >> So let's do it this way then. Uh let's

[00:21:28.960] add a time zone

[00:21:31.280] defaulted.

[00:21:37.909] So let's add this in and see if this

[00:21:37.919] works.

[00:21:39.440] There we go. That looks a lot better. So

[00:21:42.320] I think your instinct here is perfectly

[00:21:43.840] spot on, which is you can always ask

[00:21:45.360] yourself like what is a relative time

[00:21:46.880] zone to every single date time that you

[00:21:48.640] have? And every daytime can come in and

[00:21:51.200] every there's like kind of like a uh

[00:21:54.480] there's kind of like a variety of

[00:21:55.919] questions you can do. But really the way

[00:21:57.760] to handle dates very well is what you do

[00:21:59.679] is for your use case you go ahead and

[00:22:01.840] come out with a bunch of edge cases that

[00:22:03.440] you really care about and that describes

[00:22:04.880] a behavior that your users have. And for

[00:22:07.600] each one of them you just go and make a

[00:22:09.760] data model. And you notice the first

[00:22:11.039] thing Dexter said is like oh this chron

[00:22:12.559] string is going to be wrong because it's

[00:22:13.360] not time zonaware. He's definitely right

[00:22:14.640] on that. Well, we can solve that problem

[00:22:16.720] by simply making it time zone aware by

[00:22:18.799] putting an optional time zone. I'm just

[00:22:20.080] saying default otherwise. And let's just

[00:22:22.320] see what happens if we don't put in PT.

[00:22:24.880] And I want to write another test case.

[00:22:28.799] Uh, no time zone.

[00:22:32.799] And let's get rid of PT and then see

[00:22:34.640] what this does.

[00:22:40.789] And what's interesting here is it time

[00:22:40.799] zone is null here, which I think is

[00:22:42.320] exactly what I want it to do because

[00:22:44.000] it's not that I want it to be null. I

[00:22:45.280] don't even want it to default to etc

[00:22:46.640] because that's probably wrong. Uh

[00:22:50.559] only if explicitly provided is probably

[00:22:53.520] what the real thing I want is. And the

[00:22:55.919] reason I [clears throat] want this is

[00:22:56.880] because you can easily imagine like if

[00:22:58.640] I'm a user, I'm not going to write 10

[00:23:00.159] a.m. PT when I go talk into a chatbot.

[00:23:02.640] I'm just going to write 10 a.m. every

[00:23:03.919] Tuesday.

[00:23:04.799] >> And I want the software is going to know

[00:23:06.480] my time zone. the software should know

[00:23:08.720] my time zone because client side I know

[00:23:10.640] exactly what time zone I'm in when I'm

[00:23:12.480] as accessing the software. So given that

[00:23:15.760] or like when I'm on Google calendar,

[00:23:17.360] Google calendar knows what time zone I'm

[00:23:18.799] rendering as right now. So given that it

[00:23:21.600] should be able to go ahead and say okay

[00:23:22.960] if the time zone is null use the user's

[00:23:25.120] time zone unless they have explicitly

[00:23:26.559] passed in a time zone. And I don't even

[00:23:28.720] think the user would be mad if you got

[00:23:30.080] the wrong time zone there. If your

[00:23:31.360] calendar shows ET, even if you're in PT,

[00:23:34.320] and you said 10 a.m. every Tuesday, I

[00:23:37.200] would expect it to do 10 a.m. ET every

[00:23:39.520] Tuesday, not 10 a.m. PT, even though

[00:23:42.080] that's the current time zone I'm in,

[00:23:43.360] because the UI of what I'm looking at is

[00:23:45.679] probably what I intend for it to go do.

[00:23:47.600] It's kind of like a best guess effort.

[00:23:49.760] But if I if I didn't recognize the fact

[00:23:51.679] that chronzone like I initially did not

[00:23:53.520] recognize that this was UTC or like

[00:23:55.120] non-standard time um time then I would

[00:23:58.640] just I wouldn't have even thought about

[00:23:59.840] adding the time zone strength. But now

[00:24:01.840] what I can is I can easily

[00:24:04.559] convert every single recurring date into

[00:24:08.000] an absolute date with just a simple data

[00:24:11.039] transformation of applying a today and

[00:24:12.960] look up the next time zone from a chron

[00:24:14.720] string in a simple Python program.

[00:24:18.240] Oops. So I can do something like main.py

[00:24:30.390] types. Oops.

[00:24:30.400] Import uh recurring date.

[00:24:34.320] I can say def

[00:24:37.120] uh next day

[00:24:41.360] date recurring

[00:24:45.520] date

[00:24:47.440] to daytime. time.

[00:24:50.400] Why is it so hard to type stuff out

[00:24:52.080] today?

[00:24:54.960] >> It's cuz you're not using code layer,

[00:24:56.559] dude.

[00:24:58.559] >> Probably to be honest. [laughter]

[00:25:10.789] H Let me go write this down. Oh, I have

[00:25:10.799] to go import this.

[00:25:20.789] Craw equals

[00:25:20.799] date dot

[00:25:23.039] recurrence

[00:25:30.310] convert

[00:25:30.320] cron

[00:25:32.480] to

[00:25:34.240] daytime.

[00:25:36.080] I don't know if this will actually work.

[00:25:37.600] Uh, but I can figure this out. I'm sure

[00:25:39.120] I can write a chatbt string to go

[00:25:40.720] convert this for me and see how well to

[00:25:43.120] go do this. And I can look up how to go

[00:25:44.480] do this in a really easy way. Uh, and

[00:25:46.799] I'll write I'll create I'll put a cursor

[00:25:48.559] agent on this.

[00:25:51.919] >> Yeah, this is not going to work.

[00:25:54.080] >> Yeah, probably not

[00:25:55.679] >> because time that's a format string. It

[00:25:58.080] wants it to do hours and minutes

[00:25:59.600] >> actually correct.

[00:26:02.640] Make this function actually correct.

[00:26:04.240] What I want to do is convert a cron time

[00:26:07.279] string that I'm getting from an LLM into

[00:26:10.240] a actual hard time stamp for the next

[00:26:13.039] time stamp that would occur that matches

[00:26:14.880] that cron string. And lastly, I also

[00:26:18.000] want to make sure that I'm accommodating

[00:26:19.600] for the fact that time zone is sometimes

[00:26:21.279] not provided in the recurring date

[00:26:23.200] string. So in that case, I just want to

[00:26:25.440] default to the time zone that is going

[00:26:26.960] to be passed in into the next day

[00:26:28.480] function explicitly as well. But if the

[00:26:31.279] recurring date has a explicit time zone,

[00:26:33.120] then use that one.

[00:26:36.320] I really like using voice uh to actually

[00:26:38.640] get this thing to work. So I'm sure this

[00:26:40.080] will work in the background and I will

[00:26:41.440] have a new function pretty soon.

[00:26:44.480] But I think the key part here is for

[00:26:46.320] every single test case that you have, if

[00:26:47.840] you're not writing each of these test

[00:26:49.279] and thinking through it, even over here,

[00:26:50.640] if I didn't think through PT versus

[00:26:52.000] nonPT, I have no idea if this model is

[00:26:54.000] actually going to do the right thing.

[00:26:55.679] And I think this problem is actually

[00:26:57.200] simple enough just like extracting dates

[00:26:59.279] that you can actually do it purely with

[00:27:01.840] like tiny models. You could probably use

[00:27:03.200] GT5 Nano Gemini Flash. Most of those

[00:27:06.960] models should just work. But what's

[00:27:09.840] really important to here is if you if

[00:27:11.679] dates are super sensitive to you because

[00:27:13.279] perhaps you're doing contract review or

[00:27:14.720] something else, every single date needs

[00:27:16.559] to be normalized through some process.

[00:27:18.720] Because if you just let the model try

[00:27:20.400] and do the math of what the date is,

[00:27:23.919] at least as of right now, it doesn't

[00:27:25.360] work really well. And even if it does

[00:27:26.640] look like it's going to work really

[00:27:27.760] well, there's a lot of boundary

[00:27:28.880] conditions which might fail. For

[00:27:30.480] example, leap years in like February

[00:27:32.720] 28th, 29th that might make your off by

[00:27:36.559] like 2 days from now be wrong in that

[00:27:38.720] one year scenario. And you really,

[00:27:40.480] really, really don't want that to

[00:27:41.840] happen. If you're dealing with let's say

[00:27:45.279] um if you're dealing with like end of

[00:27:46.559] year conditions like January 3 uh

[00:27:48.480] December 31st that's another edge case

[00:27:50.640] that's just likely to fail. And while

[00:27:52.640] these don't really matter the problem is

[00:27:55.919] questions like doing things like two

[00:27:57.360] months from now or five like five weeks

[00:27:59.360] from now can make a huge difference on

[00:28:01.679] what you actually need. And I think the

[00:28:04.320] product that I've seen do this the best

[00:28:05.679] is actually superhuman if for those of

[00:28:08.000] you that haven't seen it. Um I'll show

[00:28:09.600] you what I mean.

[00:28:10.080] >> Oh it's great.

[00:28:11.919] >> Exactly. And I think

[00:28:12.720] >> you did this before LLMs.

[00:28:14.640] >> Exactly. And I think that's really the

[00:28:17.279] hardest part on this is this stuff which

[00:28:19.360] is like let me share my screen again.

[00:28:24.000] >> Oh, we're going to read all your emails.

[00:28:25.919] >> Uh I have a You can see my u like for

[00:28:29.600] example if I want to set up Oh,

[00:28:31.520] >> no, not that one. If I want to set up

[00:28:33.440] like a reminder for this uh

[00:28:37.360] Thank you. I can just say next

[00:28:41.520] remind me two hours

[00:28:45.279] say like

[00:28:46.159] >> H is the reminder. Yeah.

[00:28:47.840] >> So you can say all sorts of things. You

[00:28:49.200] can say like next week and it just kind

[00:28:51.200] of works. You can say two weeks and it

[00:28:55.200] just works. It just swaps it to Tuesday

[00:28:56.559] and it does very rational things like it

[00:28:58.480] says if I want to be reminded on Tuesday

[00:29:00.399] by default I want to be reply into on

[00:29:02.559] Tuesday at 8 a.m. So it's not even

[00:29:04.559] saying just two days from now. It's like

[00:29:06.080] two weeks from now is two weeks from now

[00:29:08.000] exactly and it's going to be 8 a.m. on

[00:29:10.240] that day. So, it's all actually doing a

[00:29:11.840] lot of normalization for me no matter

[00:29:13.279] what the user does. And what's

[00:29:15.279] interesting about this is this is not

[00:29:17.120] really

[00:29:18.720] uh two weekends. It doesn't do that one.

[00:29:23.039] Uh this weekend, if you do this weekend,

[00:29:26.000] just say Saturday at 8 a.m. And you can

[00:29:28.240] say all sorts of weird strings here, but

[00:29:31.120] what's really important is it does a lot

[00:29:33.039] of normalization for you. and this

[00:29:35.279] autocomplete behavior this weekend at

[00:29:39.679] 8 p.m. It doesn't work. Saturday 8 there

[00:29:44.320] you go. You can do like more specific

[00:29:45.600] things and like as you can make strings

[00:29:47.120] more constraint and what they're really

[00:29:48.240] just doing here is they just have a

[00:29:49.279] massive reax parser that just works in a

[00:29:52.880] really easy way and it turns out for

[00:29:54.159] daytimes this is probably the easiest

[00:29:55.919] way to do this assuming you have some UI

[00:29:57.600] interface as you're typing out the date.

[00:30:00.080] But if you don't have that and you're

[00:30:02.320] going to go leverage an LLM for this,

[00:30:03.919] what you need to do is actually think

[00:30:05.200] about the final end experience for the

[00:30:06.559] user and what dates are really really uh

[00:30:10.080] what I would say uh meaningful in the

[00:30:12.720] end behavior. Have you seen a product in

[00:30:15.039] the AI world do this really well,

[00:30:16.159] Dexter? I personally have not.

[00:30:19.840] >> Like I haven't seen

[00:30:20.640] >> I like the superhuman one.

[00:30:22.799] >> Yeah, right. The superhuman one works

[00:30:24.480] beautifully for me. I've never had a

[00:30:25.760] problem with it.

[00:30:28.880] I'm trying to think. Um

[00:30:30.799] >> I know I know contract review software

[00:30:33.200] like a lot of B2B SAS that I've seen

[00:30:34.799] work on this. They've actually done this

[00:30:36.080] really well because they're reviewing

[00:30:37.279] contracts and like RFPs and other things

[00:30:38.960] all the time. And for them dates are

[00:30:41.279] super critical. So what they're doing is

[00:30:43.120] they're actually and it's very clear

[00:30:44.880] what their use case is. They need

[00:30:46.240] absolute dates. And the problem is the

[00:30:48.240] users mention dates in all sorts of

[00:30:50.399] formats but they are guaranteed that

[00:30:52.080] they need absolute dates from every

[00:30:54.080] single uh system. So like for example in

[00:30:57.679] the case of like the recurrent state

[00:30:59.120] that we're talking about what they would

[00:31:01.600] want is let me share my screen again.

[00:31:08.630] What they would really want in this

[00:31:08.640] recurrence date time frame is actually

[00:31:11.120] they'd want us to know hey tell me the

[00:31:12.880] podcast every Tuesday for every for this

[00:31:14.799] time frame and they always have a date

[00:31:16.080] time of like here's a range of time

[00:31:18.320] here's the end and start date of the

[00:31:19.760] engagement give me every occurrence of

[00:31:21.840] that and again we can imagine exactly

[00:31:24.320] how there we go I guess it did something

[00:31:27.600] here I don't actually know

[00:31:29.840] >> you probably need to UV add some stuff

[00:31:32.159] >> yeah I probably do uh and I can write

[00:31:34.720] some

[00:31:36.640] test cases for this as well. Maybe add

[00:31:49.430] uh and then what I found really

[00:31:49.440] interesting for them at least is what

[00:31:51.600] they would say is given a a start date

[00:31:53.519] and end date of the full engagement give

[00:31:55.200] every every occurrence of this and you

[00:31:56.399] can easily see how if you have a

[00:31:57.440] recurring date you can get every

[00:31:58.640] engagement in this given a time frame

[00:32:00.960] that matches that date time and that's

[00:32:03.760] actually fairly easy to go do. The other

[00:32:06.240] thing you can always do is you can

[00:32:07.440] always ask more follow-up questions. So,

[00:32:08.720] for example, in the case of the meeting

[00:32:09.919] is on November 15th. If you know that

[00:32:12.880] time is not provided,

[00:32:15.120] then you can just make this optional.

[00:32:18.720] And then if it doesn't exist, you can

[00:32:20.320] just ask a follow-up question in your

[00:32:21.679] chat window that says, "Here's a chat UI

[00:32:23.919] that shows you a UI component. Here's

[00:32:25.679] your date time, and we just don't have

[00:32:27.360] the time, and we need you to supply

[00:32:28.480] that." And you can either type that in

[00:32:29.679] by chat or you can go enter it in

[00:32:31.360] yourself using the UI component. Both of

[00:32:34.399] those are fine ways of modifying day

[00:32:36.080] times, but I actually think the most

[00:32:38.080] interesting way of modifying data time

[00:32:39.360] in a chat app is actually to integrate

[00:32:41.039] something like superhuman where as

[00:32:43.440] you're typing stuff out and it you're

[00:32:45.440] doing some reddex string like two weeks

[00:32:47.360] from now, it just it just swaps this out

[00:32:50.960] just like if you're in cursor and you

[00:32:52.159] start typing like at file and you start

[00:32:54.720] mentioning something like uh sorry

[00:32:58.080] uh main.py, it just autocompletes all

[00:33:01.039] the files that exist and you can just

[00:33:02.320] link to it. And this actually tells the

[00:33:04.799] UI element to go inject that in. I think

[00:33:07.679] day times are the the only real way to

[00:33:11.919] use daytimes in a really random scenario

[00:33:15.200] I think is that sort of approach kind of

[00:33:17.120] like adding file context.

[00:33:19.600] >> It's like parsing the user's intent into

[00:33:22.640] something structured, some intermediate

[00:33:24.720] representation that then can be

[00:33:26.399] deterministically evaluated. And we we

[00:33:28.799] talk about this for generating SQL

[00:33:32.000] queries, for generating SVGs, for doing

[00:33:35.679] all these things where the model's

[00:33:36.880] actually probably not going to token for

[00:33:39.039] token give you a really good

[00:33:41.760] representation. Like if you say, "Hey,

[00:33:43.440] give me every incurrence of this cron

[00:33:45.360] for the next year." It's more likely to

[00:33:47.840] get the cron tab, right? And so it's

[00:33:50.320] like there's this thing in designing

[00:33:52.000] like LLM between the LLM and the user in

[00:33:55.200] either direction is like creating some

[00:33:58.159] sort of intermediate thing that is easy

[00:33:59.919] for the LM to write and is easy for

[00:34:02.720] software to deterministically compile

[00:34:04.720] into whatever the actual result is. Like

[00:34:07.120] for SQL we have we talk about this all

[00:34:08.800] the time is like you have don't have it

[00:34:10.560] write the SQL statements because the

[00:34:12.320] logic in SQL is nonlinear. But if the LM

[00:34:15.359] writes actually the compiled SQL like

[00:34:18.000] the a parse tree of like actually how

[00:34:20.879] every like like token in the in the tree

[00:34:24.000] interacts with every other token. The LM

[00:34:26.079] can write it a lot better and then your

[00:34:29.040] program can turn that back in decompile

[00:34:31.520] the a into a SQL query to send to the

[00:34:34.159] database engine to then recompile it

[00:34:36.000] into an A and build a query plan on the

[00:34:38.159] other side. Right.

[00:34:39.760] >> Exactly. And like the second element of

[00:34:41.440] this is actually like if the user is

[00:34:42.800] saying that hey I want to have a podcast

[00:34:44.399] every Tuesday at 10 a.m.

[00:34:47.119] likely this cron string I save in my

[00:34:49.119] database is going to be in UTC time. So

[00:34:51.359] what's important is I have to remember

[00:34:52.720] that this is UTC time and the user's

[00:34:54.720] time zone is PT and every time I send

[00:34:57.680] that string to the LM I need to convert

[00:34:59.599] that UTC chron string to a PT time

[00:35:02.720] string. I in fact want any timestamp

[00:35:05.760] that I send to the LLM for that user to

[00:35:08.640] always be automatically converted to PT

[00:35:11.520] because then when the user says what's

[00:35:12.960] going

[00:35:14.000] >> but not by the LM so hardcoded. So like

[00:35:15.920] if if I enter another time it's like

[00:35:17.760] when was this file let's say part of

[00:35:19.680] this time stamp thing is I want to

[00:35:21.280] integrate Google Docs and part of that

[00:35:23.440] is I'm going to integrate the last time

[00:35:25.280] a file was modified by Google Docs so I

[00:35:27.839] can go do this well I need to do another

[00:35:29.440] time zone conversion because the user is

[00:35:31.520] always going to say what's the file I

[00:35:32.640] edited last night well how can the model

[00:35:35.440] do that correctly if the model is

[00:35:37.200] getting the time zone in UTC

[00:35:39.920] it's just it has almost incomplete

[00:35:42.240] information is sometimes under UTC

[00:35:44.400] sometimes under PT

[00:35:46.240] because the user is re referencing the

[00:35:48.720] time zone relative to PT. It's virtually

[00:35:51.119] impossible for the model to know what

[00:35:54.079] last night means because it doesn't know

[00:35:57.040] any better. It has complete incorrect

[00:35:59.200] information.

[00:36:00.880] >> Oh, last night is a tricky one. Yeah,

[00:36:03.040] because if it's less than 24 hours, then

[00:36:05.119] the time zones get really finicky.

[00:36:07.440] >> Exactly. Exactly. And it gets even worse

[00:36:10.240] than normal.

[00:36:12.480] >> Yeah. I I sent you a whiteboard. Um, I

[00:36:16.160] don't know if we want to use it, but

[00:36:17.359] this this reminds me a lot of um

[00:36:21.599] something that happens also in

[00:36:23.119] internationalization.

[00:36:25.359] >> Um, where like you want this really

[00:36:27.839] strong uh like separation between

[00:36:31.440] backend logic and client logic.

[00:36:34.720] >> And so you have like your like DB and

[00:36:37.520] then you have your like all your backend

[00:36:39.520] logic.

[00:36:41.280] I don't know why I made this so narrow.

[00:36:44.880] Uh

[00:36:46.640] and then it gets fetched by the front

[00:36:48.079] end, right? And you have your front end

[00:36:49.440] data layer

[00:36:52.400] >> and then you have your like display

[00:36:53.839] logic.

[00:36:56.000] And when you do strings in a data in a

[00:36:58.240] in an app that is internationalized,

[00:37:00.640] this JSON object that comes down to the

[00:37:02.720] front end is like instead of like

[00:37:07.440] >> as close to the client as

[00:37:09.680] >> close to the client as possible, you

[00:37:11.359] have like you know you know button and

[00:37:14.400] the text is like

[00:37:16.400] >> uh you know I don't know I don't know

[00:37:17.760] exactly like there's lots of different

[00:37:19.040] ways to do it react.

[00:37:19.839] >> It's like a lookup table basically. It

[00:37:21.440] turns into like and

[00:37:23.920] >> you know uh what is it like uh checkout

[00:37:28.640] button or

[00:37:32.079] dossubmit.

[00:37:34.480] There's all kinds of weird like

[00:37:35.760] syntactic stuff can do. But like under

[00:37:37.520] the hood you're doing something like you

[00:37:39.040] know lookup translation

[00:37:43.359] for this like key basically.

[00:37:46.480] And then in your source code, you have

[00:37:48.640] this big like giant lookup table of like

[00:37:52.160] what every string is in every language.

[00:37:54.000] You have like enus

[00:37:56.640] and then you have you know checkout

[00:37:59.599] button

[00:38:01.280] and then you have you know submit

[00:38:06.480] and in English it's uh you know finalize

[00:38:10.000] purchase or whatever it is right and

[00:38:12.560] then in somewhere else down here you

[00:38:14.160] have like you know uh ESP or whatever

[00:38:18.480] like in like Spain Spanish right and

[00:38:20.720] your checkout button submit is I don't

[00:38:22.480] know how I don't know do you know any

[00:38:23.839] Spanish. Should have picked a different

[00:38:25.599] language.

[00:38:26.000] >> I don't know how to say check out, but I

[00:38:27.280] do know poito espanol.

[00:38:36.950] >> Yeah. Okay, you get the idea, right? And

[00:38:36.960] so like the front end logic should be

[00:38:39.040] and so I think you can have the same

[00:38:40.160] thing for times, right? Which is like,

[00:38:41.760] you know,

[00:38:43.680] label,

[00:38:46.160] you know, user time and then it's like,

[00:38:49.200] you know, 2025,

[00:38:51.920] whatever your time stamp is. And maybe

[00:38:53.520] it's 2025, you know, some ISO thing, but

[00:38:57.040] maybe it's a Unix time stamp or

[00:38:58.880] something else, right?

[00:38:59.760] >> Exactly. I think it's also what's really

[00:39:01.680] interesting about this is typically if

[00:39:03.119] you think about how UIs are built, often

[00:39:05.520] dates do live in UTC and then at the

[00:39:07.760] very end, you just convert your datetime

[00:39:09.520] to like you just do a datetime

[00:39:11.280] conversion only on the display side.

[00:39:13.200] Literally, not even the data front end

[00:39:14.640] side. You just do like date to user

[00:39:16.160] lookup time in the browser

[00:39:17.680] >> and that's what you display.

[00:39:19.599] >> And if you're someone like Google

[00:39:20.880] calendar, go ahead. If you're someone

[00:39:22.480] like Google calendar then like you

[00:39:24.079] sometime have a setting of like here's

[00:39:25.359] the times that I want to show as a part

[00:39:26.640] of your data front end and then you

[00:39:29.040] convert all the dates on the client side

[00:39:30.480] to that but what ends up happening

[00:39:33.839] >> go ahead

[00:39:34.320] >> yeah go ahead no you go

[00:39:35.760] >> no okay I was going to say the only

[00:39:37.920] thing that's really happening here is

[00:39:38.960] you have a new thing now which is your

[00:39:40.880] LLM is part of your backend logic

[00:39:44.400] and in this part of your backend logic

[00:39:46.400] what's really interesting is you kind of

[00:39:48.960] need the whatever the logic you do in

[00:39:50.960] here needs to be the same logic as

[00:39:53.599] you're doing in this one

[00:39:56.240] because

[00:39:57.839] these two are basically talking in the

[00:40:00.640] same world. But the difference is the LM

[00:40:04.160] and the display logic which is what the

[00:40:05.760] user is interacting with and what the

[00:40:07.280] logic and the computation and the

[00:40:08.640] thoughts are happening off of are

[00:40:09.839] linked. And I think that's what makes

[00:40:11.599] this so tricky of a problem. Your code

[00:40:13.920] is now split in two different worlds

[00:40:16.320] where typically

[00:40:17.599] >> and they're very far away from each

[00:40:19.200] other. They're very far away from

[00:40:20.880] Exactly. And there's a lot of plumbing

[00:40:23.440] work you have to do to make this work

[00:40:24.960] and feel right. And I think that's

[00:40:26.800] really the bottleneck over here.

[00:40:30.960] >> Yeah. There's also some like interesting

[00:40:32.720] like math stuff happening here. I don't

[00:40:34.880] know if you're on the the bucketing

[00:40:36.480] challenges. If you go to the right a

[00:40:38.160] little bit, if your question is

[00:40:40.160] something like you know how many how

[00:40:43.119] many events happened in the last day and

[00:40:46.000] your day boundary is like over the data

[00:40:48.880] set.

[00:40:49.760] >> Exactly.

[00:40:51.839] >> Like it becomes very tricky or like if

[00:40:54.000] you want to bucket these events by day,

[00:40:55.839] it's like depending on who the user is,

[00:40:57.599] they have 20 in a day or they have 25 in

[00:41:01.200] a day or they have 40 in a day.

[00:41:04.640] So like it's not just literally showing

[00:41:07.040] the timestamp in the UI. There's all

[00:41:09.359] this like logic stuff that is dependent

[00:41:11.839] on time and time zones and daylight

[00:41:14.480] savings and all kinds of fun things.

[00:41:16.560] >> And I think it's really interesting

[00:41:18.000] because like for example like superhuman

[00:41:19.599] makes an obvious choice which is if I

[00:41:20.960] want to be reminded about an email, I

[00:41:22.560] probably want it to happen at 8 a.m.

[00:41:24.880] >> Like most people log into work, there's

[00:41:26.960] like a 95 percentile chance that 8 a.m.

[00:41:29.200] is a good enough reminder time for

[00:41:30.800] emails to come in. So you just have a

[00:41:32.880] really good default time. So what you

[00:41:34.800] need to do as a user is you need to

[00:41:36.079] think really hard about what is your

[00:41:38.160] actual like boundary time for like where

[00:41:41.520] the time stamps start making relative

[00:41:43.280] sense for your problem space for your

[00:41:45.040] domain and then you need to go

[00:41:46.880] discretise it. Oh, dude. I was gonna say

[00:41:50.079] before I got here, I was like, "We

[00:41:51.839] should ask Brian about this." And

[00:41:55.040] >> he was in the chat talking about it, and

[00:41:56.560] I know had him on before, so I was like,

[00:41:58.319] it's almost like a no-brainer to have

[00:42:00.240] him come and answer his last few

[00:42:01.839] thoughts.

[00:42:03.119] >> Yeah. Nice to see you guys. Happy to

[00:42:05.040] happy to answer whenever I can.

[00:42:06.720] >> Yeah.

[00:42:07.200] >> Well, now that Brian works at a applied

[00:42:09.599] AI lab, he's definitely qualified expert

[00:42:12.400] to share some uh share some thoughts

[00:42:14.240] here.

[00:42:17.040] I mean, I handle I handle a lot of this

[00:42:19.920] stuff. Um, I think you guys are on the

[00:42:21.520] right track, though. It's just like

[00:42:23.440] almost interesting to treat the AI

[00:42:25.440] almost as a user to the sense of like if

[00:42:27.920] our users operating in like central time

[00:42:29.839] zone will normalize everything that has

[00:42:31.920] to deal with dates and times to central

[00:42:33.599] time zone. Um, they're capable of of

[00:42:37.520] reasoning around time zones, but usually

[00:42:39.599] you just like don't want them to have

[00:42:40.880] to,

[00:42:42.000] >> you know.

[00:42:42.480] >> Yeah.

[00:42:44.240] work.

[00:42:45.280] >> I think I view the LM as kind of like a

[00:42:47.599] computation like engine of some kind and

[00:42:49.760] you can choose where the gas goes to and

[00:42:52.160] the gas going to time zone computation

[00:42:54.000] is a waste of gas.

[00:42:56.319] >> Yeah, it it's it's not a good use of uh

[00:42:58.800] good use of your reasoning capabilities.

[00:43:01.359] Um, but yeah, I think Dex is saying

[00:43:03.280] saying something correct where like once

[00:43:05.040] you have other things like memory or

[00:43:06.880] bucketing that's based on time, that

[00:43:09.040] also starts to get really challenging

[00:43:10.960] because then you're starting to make cut

[00:43:12.640] offs based on the user's time zone

[00:43:14.800] within a system that might not operate

[00:43:16.480] in the user's time zone.

[00:43:18.240] >> So it just gets it gets hairy pretty

[00:43:20.240] quickly.

[00:43:20.640] >> I have a question, Brian. Does that mean

[00:43:22.160] that to make this to make a system like

[00:43:24.400] memory and everything else really work?

[00:43:26.160] How do you deal with like in the case of

[00:43:29.280] like calendars, every time I switch into

[00:43:31.119] a different time zone, Google's like,

[00:43:32.880] "Hey, do you want to change time zones

[00:43:34.319] right now?" And I do because I obviously

[00:43:36.960] want to while I'm in the new city, I

[00:43:38.240] want to see my meetings in the time zone

[00:43:39.680] relative to where I'm at. Do you do the

[00:43:42.000] same thing in memories where you like

[00:43:43.839] you take memory and then you realign

[00:43:45.760] memories to the current time zone of the

[00:43:47.839] user all of a sudden and renap

[00:43:49.440] everything or does it kind of or for

[00:43:51.839] latent memories that are really long

[00:43:53.359] away you obviously don't have to do this

[00:43:54.960] but for things that happened recently

[00:43:56.480] let's say within the last week

[00:43:58.800] >> feels like you probably should do

[00:44:00.720] something

[00:44:06.309] >> there's two dimensions here so you can

[00:44:06.319] you you assign each memory bucket to a

[00:44:08.640] time stamp right Um, and you do want to

[00:44:12.800] shift the timestamp into the user's time

[00:44:14.960] zone of when that bucket was like like

[00:44:17.200] marked as. But, uh, and and you can also

[00:44:19.839] recomputee the buckets based on the time

[00:44:21.520] zones. For example, if you have a daily

[00:44:23.040] memory bucket that what counts as the

[00:44:25.359] day is going to change based on what

[00:44:26.960] time zone you're in,

[00:44:28.079] >> right?

[00:44:28.960] >> Uh, I don't do that. I I mean, you

[00:44:31.280] could. It just it's going to take a lot

[00:44:32.640] more tokens to recomputee your entire

[00:44:34.480] memory context, right? Uh, and I think

[00:44:37.119] you hit it on the head. like it's not

[00:44:38.560] really that important past the day like

[00:44:40.560] you know 24 hours ago.

[00:44:42.319] >> So we just

[00:44:43.200] >> for you I think it's

[00:44:45.359] >> for you I think it's like your memories

[00:44:47.359] are never stored at greater than day

[00:44:50.079] granularity. You're never storing things

[00:44:51.839] at the hour granularity. So you're never

[00:44:53.680] saying like you're doing one engagement

[00:44:55.520] a day or one engagement. I mean I guess

[00:44:57.920] if you have an email come in at 1:00

[00:44:59.760] a.m. like did that

[00:45:01.760] >> we definitely do more granular.

[00:45:04.400] >> Okay.

[00:45:05.359] >> Yeah. So we uh we go down to five

[00:45:07.280] minutes now. So we have five minute

[00:45:08.800] buckets and then hour buckets and then

[00:45:11.040] uh day buckets. So it it gets crazy.

[00:45:15.040] >> Yeah. Because I always I think the

[00:45:16.560] reason that time I've seen be tricky at

[00:45:17.839] least for like so for example the people

[00:45:19.599] I know that work in the legal domain

[00:45:21.599] >> um they have a problem like sometimes

[00:45:22.880] lawyers will use the word tomorrow

[00:45:25.119] >> and sometimes they'll be awake at like

[00:45:26.880] 1:00 a.m. talking about tomorrow.

[00:45:28.400] >> Yeah.

[00:45:28.880] >> And when I'm at 1:00 am talking about

[00:45:30.720] tomorrow I usually mean after I wake up.

[00:45:32.319] I do not mean actually tomorrow

[00:45:36.000] >> or I rarely mean the day after, right?

[00:45:38.000] It it's semantically relevant to what it

[00:45:39.839] is right now because it was just today.

[00:45:41.119] It's still today kind of in my brain.

[00:45:43.520] >> Yeah. And and you'll have that same

[00:45:44.880] issue with with agents because like it's

[00:45:47.040] a semantics issue, not an infrastructure

[00:45:48.720] one.

[00:45:49.200] >> Yes.

[00:45:49.599] >> Um but but yeah, we hit all of those

[00:45:52.720] things. Um, there is an unhandled edge

[00:45:55.839] case that I think Dex was pointing out.

[00:45:57.119] It's like if you get sent an email at

[00:45:58.800] like 1:00 a.m. I mean, recently we had

[00:46:01.839] uh daily sales time, right? Like

[00:46:05.441] [laughter]

[00:46:06.160] >> another

[00:46:08.400] >> Yeah, another like blow up your entire

[00:46:11.760] infrastructure.

[00:46:13.359] The worst project I am, the most

[00:46:15.040] humbling project of my entire career was

[00:46:17.599] doing this like hourly bucketing into

[00:46:20.160] daily buckets for like fast reporting in

[00:46:22.880] the future and handling it for multiple

[00:46:25.119] users in a single account across time

[00:46:27.599] zones and then figuring out what to do

[00:46:30.240] the day before and after daylight

[00:46:31.920] savings.

[00:46:33.607] [laughter]

[00:46:35.440] >> That's that's pretty much our memory

[00:46:37.040] problem. Yeah,

[00:46:38.800] >> I suspect the hardest problem here and

[00:46:40.720] with time zones is one, time zones are

[00:46:42.480] just hard even without AI. But what ends

[00:46:44.880] up happening is when you toss an AI

[00:46:47.280] element into this and your team hasn't

[00:46:49.520] spent any time thinking about the nuance

[00:46:51.520] of time zone relative to your domain

[00:46:53.440] specifically or like date times or

[00:46:55.920] relative dates at all, then users use

[00:46:58.640] your product and say it doesn't work.

[00:47:00.800] But in reality, you just haven't

[00:47:02.079] configured it to work in it anyway. Like

[00:47:03.760] it sounds like all this is solvable.

[00:47:05.760] None of this stuff sounds untenable.

[00:47:07.760] People just need to sit down, define

[00:47:08.960] edge case, and just like understand

[00:47:10.319] where the user going to expect it to

[00:47:11.680] work and where does it break. And for

[00:47:13.839] example, if it does break on daylight

[00:47:15.359] savings times, I suspect your users will

[00:47:16.880] forgive you.

[00:47:18.319] >> But if it breaks on saying tomorrow,

[00:47:22.000] >> like at 400 p.m. on a random day, the

[00:47:25.119] user will probably be unforgiving on

[00:47:26.880] that nature. And

[00:47:28.400] >> and this is the nice part about

[00:47:29.520] normalizing the time zone of the agent

[00:47:31.280] to be the same as the user is that the

[00:47:33.440] agent will also experience delight

[00:47:35.040] savings time,

[00:47:36.240] >> right? And so like it'll wake up an hour

[00:47:38.560] later based on when the time is shifted.

[00:47:41.520] >> And so like it might get the planning a

[00:47:43.280] little bit wrong if there's like a weird

[00:47:45.040] issue, but like overall it's going to

[00:47:46.960] basically fix it the day of and it's

[00:47:48.480] going to be fine.

[00:47:49.839] >> Yeah, I guess that's true because if you

[00:47:51.119] tell me remind me every Tuesday and then

[00:47:52.560] daylight at 8 a.m. daylight savings

[00:47:54.400] happen, it happens an hour earlier than

[00:47:56.079] you expected or an hour later than you

[00:47:58.400] expected. It's still almost correct is

[00:48:01.599] the way I describe it.

[00:48:02.880] >> Right. Uh who's sharing screen? Viv, you

[00:48:06.000] want to go down to the right a little

[00:48:07.280] bit? I just pasted an actual example of

[00:48:09.119] of uh something that was happening in

[00:48:11.359] one of our

[00:48:12.800] >> uh one of our sessions.

[00:48:15.359] >> Um I actually I sent this to a friend

[00:48:17.440] because I was like, "This is super

[00:48:18.480] sick." Right? So this is a friend of

[00:48:19.680] mine who was just on a test account,

[00:48:21.040] right? Um, and this is an example of

[00:48:23.760] where actually part of our uh system

[00:48:26.559] didn't have the right time zones. So

[00:48:28.160] down here it has UTC time zones, right?

[00:48:30.160] Because that was like a time for

[00:48:31.440] database.

[00:48:32.960] >> I'm going to highlight

[00:48:33.839] >> this is just like a reasoning chain of

[00:48:35.520] the of the model, right?

[00:48:37.200] >> Okay.

[00:48:37.920] >> Um, so he says, oh, this the agent's

[00:48:40.319] like, okay, this is a UTC time stamp,

[00:48:42.079] but I noticed that the agent or sorry

[00:48:43.760] that the the user metadata is given in

[00:48:46.960] PST, right? So, I should now be

[00:48:49.760] operating in PST and converting things

[00:48:52.319] into PST, which means that like he

[00:48:54.559] thought the session was going to be was

[00:48:56.800] an hour ago, but it's actually in an

[00:48:58.319] hour,

[00:48:59.200] >> you know,

[00:49:00.559] >> and so you can see this down here where

[00:49:02.240] he's actually able to reason through

[00:49:03.680] this in real time. So, you do have some

[00:49:05.760] leeway when you actually use these

[00:49:07.680] models because like this is 4.5 sonnet

[00:49:10.079] or a haiku by the way.

[00:49:11.760] >> Yeah.

[00:49:12.160] >> Okay. This is like a model seizure.

[00:49:18.014] >> [laughter]

[00:49:18.160] >> and like having like a thinking too hard

[00:49:20.319] like freaking out.

[00:49:23.119] >> Well, but but in this case it actually

[00:49:25.040] like it actually caught an error in our

[00:49:27.680] systems where like I should have

[00:49:29.200] returned a certain time stamp as a PST

[00:49:31.280] time stamp and not a UTC time stamp and

[00:49:33.440] it was able to actually get through that

[00:49:35.440] and just like continue as normal and and

[00:49:37.440] actually fix it for us basically.

[00:49:39.680] >> Yeah. When I think about like an LM like

[00:49:42.559] I think about this like the LM prompting

[00:49:44.240] infrastructure and everything else like

[00:49:45.359] how do you build this context correctly?

[00:49:47.119] Like the right way to do this is

[00:49:48.400] actually you as a developer just pass in

[00:49:50.400] a datetime object in Python and somehow

[00:49:54.559] like at some point the mo the prompt

[00:49:56.319] just renders you just say I want to

[00:49:57.599] render every datetime in this context as

[00:49:59.839] PST no matter what everything is always

[00:50:02.480] PST and you just don't think about it

[00:50:04.640] and when the model spits out a daytime

[00:50:06.319] object back it just spits out a daytime

[00:50:08.880] object and you say no matter what

[00:50:10.720] convert this to PST

[00:50:12.559] >> and just always give me back PS or give

[00:50:14.640] me back USC UCT time assuming that it's

[00:50:17.520] PSC from the model at all points.

[00:50:20.640] >> That's kind of what you want in like a

[00:50:22.559] time zone. You want like an automatic

[00:50:24.319] converter, I think, as a developer. And

[00:50:26.240] if I were writing like a framework of

[00:50:28.079] any kind, that's kind of what I would

[00:50:29.200] build if I'm if I deal with dates a lot.

[00:50:31.280] And dates are critical to my

[00:50:32.640] infrastructure.

[00:50:34.480] I just say this class always converts in

[00:50:37.680] the right way, no matter what.

[00:50:40.240] Yeah, you pretty much want to handle it

[00:50:41.599] on your ser serialization layer to just

[00:50:43.839] always be anything keyed to this user's

[00:50:46.400] account gets normalized to their

[00:50:47.920] accounts zone and that's stored

[00:50:49.359] somewhere in the database.

[00:50:50.559] >> And

[00:50:51.119] >> um we also let the agent change the

[00:50:53.760] account's time zone itself.

[00:50:55.839] >> So for example like we had a student who

[00:50:58.640] >> usually is in Pacific time but then they

[00:51:00.800] went to India for a month,

[00:51:03.040] >> right? And so you can like they'll tell

[00:51:06.240] the agent this like hey you know I'm

[00:51:08.079] going to India this month like we got to

[00:51:09.440] change our schedule. Uh and the agent

[00:51:11.760] can then change the time zone that's on

[00:51:13.359] the account. Uh which means that all of

[00:51:15.359] the stuff now is normalized to Indian

[00:51:17.119] standard time right. Um it's an edge

[00:51:20.319] case but it's in case you have users

[00:51:21.839] that like move around time zones it's uh

[00:51:24.160] it works.

[00:51:25.680] >> That's actually really interesting where

[00:51:26.880] the model can just like recognize it on

[00:51:28.319] their own.

[00:51:29.680] >> Yeah. Do you store the like event

[00:51:32.559] recorded like what was the user's time

[00:51:35.119] zone when the event was recorded

[00:51:38.079] with each event?

[00:51:41.200] No, we basically just like shift the the

[00:51:45.119] memory buckets as well as like the event

[00:51:46.800] ledger to be logged in the current time

[00:51:50.559] zone. So like there there are some like

[00:51:52.800] weird memory bucketing edge cases where

[00:51:54.800] if you bucket a memory in this daily set

[00:51:57.599] like this daily bucket and then you

[00:51:59.119] shift the European time

[00:52:01.520] >> maybe it shouldn't be in that bucket for

[00:52:03.119] European time but we just don't go back

[00:52:04.480] and recmp compute the entire thing.

[00:52:06.480] >> Yeah because you're like again you're at

[00:52:08.800] most error condition is like off by one

[00:52:10.720] day

[00:52:11.839] >> and in

[00:52:12.640] >> not even but yeah

[00:52:13.520] >> not yeah sorry like upper bound could be

[00:52:16.640] at most off by one day if someone flew

[00:52:18.079] to exactly the opposite side of the

[00:52:19.359] international date line. fair

[00:52:20.960] >> and did that like that's like the worst

[00:52:22.800] case scenario but

[00:52:24.319] >> and and they were on the flight working

[00:52:26.160] on this thing like it it involves them

[00:52:28.160] working on the flight while [laughter]

[00:52:30.160] while magically then also flying and

[00:52:33.119] then be like hey why didn't it work but

[00:52:34.880] even in that scenario I can't imagine

[00:52:36.160] the user being upset I think that's the

[00:52:38.000] most important part it's like

[00:52:39.200] understanding when will the user

[00:52:40.800] actually be upset versus when can the

[00:52:42.559] user understand

[00:52:44.880] and like when can the user understand

[00:52:46.400] that hey this is like a forgivable sin

[00:52:50.480] kind of approach.

[00:52:51.839] >> That's really cool. Thank you for

[00:52:53.119] sharing the chat log. I thought this is

[00:52:54.559] the fact that I think Haiku does this is

[00:52:57.599] very indicative of kind of what we were

[00:52:58.960] talking about earlier. It's like this is

[00:53:00.079] not a hard problem.

[00:53:01.680] >> No.

[00:53:02.000] >> And if you do it right 90% of the time

[00:53:04.079] in your software, if you make a mistake

[00:53:05.680] once, the model can fix itself.

[00:53:07.680] >> But if the model is doing this at every

[00:53:09.520] single step,

[00:53:10.960] >> it's just going to have a harder time

[00:53:12.400] because you can just see the chat log

[00:53:13.760] where it's doing this reasoning.

[00:53:15.280] >> It's going to have to do that. It's it's

[00:53:17.599] overhead on every interaction. And if

[00:53:20.000] every interaction is like 5% more

[00:53:22.079] overhead, that's just every interaction

[00:53:24.400] has a likelihood of failure of 5% more.

[00:53:27.520] And you don't want that cuz

[00:53:28.720] >> And it's more expensive and it's slower.

[00:53:31.200] >> Sure. Yes. That too. Yes. I forgot about

[00:53:33.440] that part.

[00:53:34.079] >> Right. [laughter]

[00:53:36.480] >> Thankfully, Haiku is crazy fast. I mean,

[00:53:38.240] this reasoning chain took, I think,

[00:53:39.599] under a second to get back to us

[00:53:41.040] streaming.

[00:53:42.559] >> Yeah. Then I guess that that explains

[00:53:45.359] it.

[00:53:46.160] I think it just goes back to the fact of

[00:53:47.520] like if you do a modic amount of work to

[00:53:49.280] go correct this for from your at the

[00:53:51.280] serialization and just do it the right

[00:53:52.640] way

[00:53:53.200] >> so models don't have to think then it

[00:53:55.599] will these systems will just work.

[00:53:58.319] >> Yeah.

[00:53:58.640] >> But if you don't do it the right way

[00:54:00.160] then like your app probably won't work

[00:54:02.160] especially datetimes are a common part

[00:54:03.599] of interactions. For example, like if

[00:54:05.359] you're doing a data analysis job of any

[00:54:07.760] kind,

[00:54:09.280] if you're doing a data analysis job,

[00:54:10.640] you're basically screwed if you don't

[00:54:11.839] handle time zones correctly and like

[00:54:13.119] you're doing time series data. Like of

[00:54:14.880] course that thing's not working because

[00:54:16.559] your users are talking relative time

[00:54:18.319] zones and you're not processing them

[00:54:20.800] correctly. You got to stand. And then

[00:54:22.800] Elizabeth brought up a good point of

[00:54:24.240] like use ISO standardization. It's a

[00:54:27.520] really good technique, but it fails for

[00:54:31.599] relative time. So you have to use like

[00:54:32.960] some sort of relative time zone

[00:54:34.160] technique and for that you usually need

[00:54:35.760] I is that what you guys do Brian? Do you

[00:54:37.280] guys have custom data models that

[00:54:38.480] represent like relative time zones like

[00:54:40.640] >> like recurrence or something else? How

[00:54:42.240] do you deal with those kinds of systems

[00:54:43.599] in your in your world?

[00:54:45.440] >> We just store everything in ETC and then

[00:54:47.359] normalize it on the way out of the API.

[00:54:50.079] >> Got it. And then uh but how do you model

[00:54:52.720] recurrence or do you have recurrence?

[00:54:55.599] I'm not sure I followed the question

[00:54:57.839] >> like like uh like hey this event happens

[00:55:01.280] every Tuesday at XYZ time like recurring

[00:55:03.760] events.

[00:55:04.240] >> Oh

[00:55:05.440] >> uh yeah we don't really have like a a so

[00:55:07.599] we have a calendar application.

[00:55:09.440] >> Um but there's not like a every two

[00:55:11.359] weeks kind of thing. We just kind of let

[00:55:12.559] the model decide like okay let's make

[00:55:14.400] the next event the next event the next

[00:55:16.079] event and the recurrence also gets

[00:55:18.079] somewhat structured in memory as well as

[00:55:19.599] like a user preference.

[00:55:20.960] >> Um

[00:55:21.359] >> got it. the combination of the two tends

[00:55:23.280] to work. But I would love I would love

[00:55:24.480] to like if someone's building a very

[00:55:27.280] like SDK,

[00:55:29.119] you know, SDKable calendar app that just

[00:55:31.119] handles these things, we'd love to use

[00:55:32.400] it.

[00:55:33.440] >> That's funny. Yeah.

[00:55:34.240] >> Like built for an agent because then we

[00:55:36.079] have to build it ourselves.

[00:55:38.240] >> We have uh we tried building recurrence

[00:55:40.960] into our previous data model. Uh we

[00:55:42.880] built a Slack competitor before we were

[00:55:44.400] building BAML

[00:55:45.520] >> and we did build recurrence into the

[00:55:47.200] calendar app that we had integrated and

[00:55:48.640] I can just tell you that it is not fun

[00:55:50.480] to data model.

[00:55:52.079] >> The Google calendar API or the data it

[00:55:54.319] gives you for recurrence is not fun. You

[00:55:57.200] do not want it uh at all because

[00:56:00.160] recurrence is

[00:56:02.240] people do recurrence and then they

[00:56:03.680] realize that hey what people want to do

[00:56:05.119] is they want to both edit every element

[00:56:06.960] in the recurrence chain and they also

[00:56:08.400] sometime want to edit individual

[00:56:09.680] elements say this one recurrence is

[00:56:11.599] going to change

[00:56:12.960] >> and we're and there's all sorts of

[00:56:15.119] modification you have to it's just not

[00:56:16.400] fun way.

[00:56:18.480] >> Yeah.

[00:56:19.040] >> Yeah. And if you edit and move it one

[00:56:21.440] day forward and you say edit all future

[00:56:23.839] events, that actually means move all the

[00:56:25.599] future events one day forward so they're

[00:56:27.200] all still a week apart. Or it's like no,

[00:56:29.119] I just wanted to update the description

[00:56:30.640] on all the future ones but leave them on

[00:56:32.559] the same date.

[00:56:33.760] >> Yeah, exactly. So it's really tricky how

[00:56:35.920] you have to go do that.

[00:56:37.599] >> I have not uh been confident enough to

[00:56:39.599] give an AI the uh the full capabilities

[00:56:42.400] of doing that and trusting it to do it

[00:56:44.000] accurately. And honestly, that's

[00:56:46.160] probably the best thing to do where it's

[00:56:47.520] like, hey, instead of letting your user

[00:56:48.960] shoot themselves in the foot with a

[00:56:50.079] broken feature, just don't like if you

[00:56:52.160] don't have confidence that you can go

[00:56:53.280] ship it, just don't do it.

[00:56:54.720] >> And like

[00:56:55.920] >> you build some UI to make your users

[00:56:57.680] interact with us. Like, hey, build a

[00:56:59.040] calendar app UI only interaction for

[00:57:01.119] recurrence.

[00:57:02.240] >> Agent just can't do this. Sorry.

[00:57:04.480] >> Yeah.

[00:57:06.000] >> So, we'll see.

[00:57:07.680] >> But yeah, sorry to crash the session.

[00:57:09.359] Figured it'd be interesting to share,

[00:57:10.480] but um I saw you on Twitter. I was like,

[00:57:12.480] I should talk about this. Uh this is

[00:57:14.799] hilarious. I think the chat thread is a

[00:57:17.680] perfect articulation of what we were

[00:57:19.440] talking about today happening in real

[00:57:21.200] time in a real production app. Uh so I

[00:57:23.680] think it's good that it uh echoes the

[00:57:26.160] same sentiment.

[00:57:27.760] >> Cool. Best luck in the rest of the rest

[00:57:30.559] of the workshop.

[00:57:31.680] >> Oh, I think we're gonna pretty soon we

[00:57:33.599] got a hard stop today. [laughter]

[00:57:35.520] >> Okay.

[00:57:35.839] >> Um Dexter, anything else you want to

[00:57:37.680] share for anyone else that's interested?

[00:57:39.040] We'll go post some of the learnings

[00:57:40.480] here. We'll include Brian's chat log.

[00:57:42.640] So, I think it'd be fun for people to go

[00:57:43.920] read. Uh, but this is AI that works.

[00:57:47.200] Today we talked about dates, times,

[00:57:48.720] LLMs. I think next week we're going to

[00:57:50.880] do another fun episode that Dexter might

[00:57:52.480] have in mind. So, we'll see how that

[00:57:54.160] goes.

[00:57:54.559] >> It's a It's a surprise. It's gonna be

[00:57:56.480] fun.

[00:57:57.440] >> Cool. All right. Good seeing everyone.

[00:57:59.839] >> Thanks, everybody.

[00:58:00.640] >> Bye, everyone.
