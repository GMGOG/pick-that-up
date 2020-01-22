from django.shortcuts import render
import random

data = ['''I will never play hide and seek with you because someone like you is impossible to find.''',
        '''Do you have a name or can I call you mine?''',
        '''You may fall from the sky, you may fall from a tree, but the best way to fall… is in love with me.''',
        '''I am going to complain to Spotify about you not being this weeks hottest single.''',
        '''Roses are red, violets are blue, I’m not that pretty but damn look at you.''',
        '''I’m no organ donor but I’d be happy to give you my heart.''',
        '''Roses are red, my face is too, that only happens when I’m around you''',
        '''Your hand looks heavy can i hold it for you?''',
        '''Can I follow you? Cause my mom told me to follow my dreams.''',
        '''I heard you’re good in algebra, can you replace my X without asking Y.''',
        '''There’s only one thing I want to change about you. Your last name.''',
        '''Are you a camera? Because every time I look at you, I smile.''',
        '''(Holds out hand) Hey I’m going for a walk. Will you hold this for me?''',
        '''Roses are red violets are blue I didn’t know what perfect was until I met you.''',
        '''Guess what I’m wearing? The smile you gave me!''',
        '''You’re That “Nothing” When People Ask Me What I’m Thinking About.''',
        '''Are you a keyboard? Because you’re just my type.''',
        '''Are you a bank loan? Because you got my interest.''',
        '''Even though there aren’t any stars out tonight, you’re still shining like one.''',
        '''You look familiar, didn’t we take a class together? I could’ve sworn we had chemistry.''',
        '''Your lips look lonely would they like to meet mine?I’d''',
        '''You know you’re in love when you can’t fall asleep because reality is finally better than your dreams.''',
        '''If I had to rate you out of 10 I’d rate you a 9… because I am the one that you are missing!''',
        '''Are you a time traveler? Cause I see you in my future!''',
        '''Do you know if there are any police around? Cause I’m about to steal your heart.''',
        '''There isn’t a word in the dictionary to describe how beautiful you are.''',
        '''My friends bet I can’t talk to the prettiest girl. Wanna use their money to buy drinks?''',
        '''If I had 4 quarters to give to the 4 prettiest girls in the world, you would have a dollar.''',
        '''You remind me of the 21 letters in the Alphabet (She: there 26 letters) Oh I forgot the U R A Q T.''',
        '''Of all your beautiful curves, your smile is my favourite.''',
        '''Roses are red violets are blue, I can’t rhyme but can I date you?''',
        '''You know what’s beautiful? Read the first word.''',
        '''I would take you to the movies but they don’t allow snacks.''',
        '''I’m not a hoarder but I really want to keep you forever.''',
        '''Roses are red, violets are blue, lava is hot and so are you.''',
        '''I have had a really bad day and it always makes me feel better to see a pretty girl smile. So, would you smile for me?''',
        '''Roses are red, violets are blue, it would be a shame if I couldn’t date you!''',
        '''You know what’s beautiful? Read the first word.''',
        '''I would take you to the movies but they don’t allow snacks.''',
        '''I’m not a hoarder but I really want to keep you forever.''',
        '''Roses are red, violets are blue, lava is hot and so are you.''',
        '''I have had a really bad day and it always makes me feel better to see a pretty girl smile. So, would you smile for me?''',
        '''Roses are red, violets are blue, it would be a shame if I couldn’t date you!''',
        '''Most people like to watch the Superbowl cuz it only happens once a year, but Id rather talk to you cause the chance of meeting someone like you only happens once in a lifetime.''''',
        '''I should call you Google, because you have everything I’m looking for.''',
        '''Do you have a band aid? Cause I scrapped my knees falling for you.''',
        '''I lost my teddy bear can i sleep with you tonight?''',
        '''If kisses were snowflakes, I’d send you a blizzard.''',
        '''If I were a cat i’d spend all 9 lives with you.''',
        '''Can you touch me? I want to tell my friends I was touched by an Angel.''',
        '''I don’t really believe in love at first sight, until I saw you.''',
        '''If you were a basketball, I’d never shoot. [Why?] Because I’d always miss you.''',
        '''Roses are red and violets are blue there’s nothing in the world more prettier than you.''',
        '''Are you the sun? Because you’re so beautiful it’s blinding me.''',
        '''Are you made of copper and tellurium? Because you’re CuTe!''',
        '''I just had to come talk with you. Sweetness is my weakness.''',
        '''A boy gives a girl 12 roses. 11 real, 1 fake and he says to her ” I will stop loving you when all the roses die”''',
        '''Do you play soccer? Because you’re a keeper!''',
        '''Even though there aren’t any stars out tonight, your’e still shining like one.''',
        '''Are you australian? Because you meet all of my koalafications.''',
        '''Give her 12 roses. 11 real, 1 fake and say “I will stop loving you, when all the roses die”''',
        '''You really shouldn’t wear makeup. You’re messing with perfection!''',
        '''I want to be your tear drop, so I could be born in your eyes, live on your cheeks, and die on your lips.''',
        '''I’m feeling a little bit off today, but you definitely turned me on.''',
        '''I’m no electrician, but I can light up your day.''',
        '''If you were a potato you’d be a sweet one.''',
        '''Do you smoke pot? Because weed be cute together.''',
        '''Is Your Dad A Preacher? Cause Girl You’re A Blessing.''',
        '''Wanna grab a coffee because i like you a latte!''',
        '''If I was an octopus, all my 3 hearts would beat for you?.''',
        '''I know somebody who likes you but if I weren’t so shy, I’d tell you who.''',
        '''Your so cute its distracting.''',
        '''Want to know what I’m wearing? The smile you gave me.''',
        '''I used to be a Gambler, but then I realized that all I needed was the Queen of my Heart.''',
        '''When I look into your eyes, it is like a gateway into the world of which I want to be a part.''',
        '''I lost my rubber duckie. Would you bathe with me instead?''',
        '''Your smile lit up the room, so I just had to come over.''',
        '''You dropped something! [What?] Your smile.''',
        '''As she’s leaving….Hey aren’t you forgetting something? She: What? Me!''',
        '''Is your name dunkin? Because i donut want to spend another day without you.''',
        '''Roses are red, I have a crush, whenever I’m around you, all I do is blush.''',
        '''What does it feel like to be the most beautiful girl in this room?''',
        '''Did you die recently? Cause girl, you look like an angel to me.''',
        '''I don’t believe in love at first sight, but I’m willing to make an exception in your case.''',
        '''Can you kiss me on the cheek so I can at least say a cute girl kissed me tonight?''',
        '''If I’d follow you home, would you keep me?''',
        '''Is your body from McDonald’s? Cause I’m loving it!''',
        '''Are you a 45 degree angle? Because you’re acute-y!''',
        '''Are you the ocean? Cuz baby I want to swim in you all day.''',
        '''Are you a volcano? Because i lava you.''',
        '''Are you from Russia? ‘Cause you’re russian my heart rate!''',
        '''You look cold. Want to use me as a blanket?''',
        '''I might be ugly but I’ll treat you right!''',
        '''Are you netflix? Because i could watch you for hours.''',
        '''Charzards are red Squitals are blue if u were a Pokemon i would choose you!''',
        '''Do you like star wars? Because yoda only one for me!''',
        '''Are you made out of grapes? Because you are fine as wine!''',
        '''You can’t be my first, but you can be my last.''',
        '''I’m afraid of the dark… Will you sleep with me tonight?''',
        '''Do you drink Pepsi? Because you’re so-da-licious!''',
        '''You Sexy, You Fine. I Really Wanna Make You Mine.''',
        '''Is your name Ariel? Cause we Mermaid for each other!''',
        '''Are you the cure for Alzheimer’s? Because you’re unforgettable.''',
        '''You can’t be my first, but you could be my next.''',
        '''Spoon me like your favorite ice cream!''',
        '''Keep an eye out for elves with ropes and a blindfold! Why? Cause I asked Santa for you this Christmas.''',
        '''Can I borrow a quarter? [“What for?”] I want to call my mom and tell her I just met the man/woman of my dreams.''',
        '''When I’m older, I’ll look back at all of my crowning memories, and I’ll think of the day my children were born, the day I got married, and the day that I met you.''',
        '''Are you as beautiful on the inside as you are on the outside?''',
        '''I may not be good at dancing but i can tangle with with you all night long.''',
        '''The letter ‘X’ scares me [Why?] Because I never want to be yours.''',
        '''You so lovely, you make me wanna go out and get a job.''',
        '''You know how I got these guns? [Point to biceps] Lifting children out of poverty.''',
        '''Your mom told me to say “Hi” to you.''',
        '''I just got dumped, and I think that you could make me feel better.''',
        #Chees''y
        '''Are you a magician? Because whenever I look at you, everyone else disappears!''',
        '''I’m not a photographer, but I can picture me and you together.''',
        '''Do I know you? ‘Cause you look a lot like my next girlfriend/boyfriend.''',
        '''Do you know what my shirt is made of? Boyfriend/girlfriend material?''',
        '''They say Disneyland is the happiest place on earth. Well apparently, no one has ever been standing next to you.''',
        '''For some reason, I was feeling a little off today. But when you came along, you definitely turned me on.''',
        '''Are you religious? Because you’re the answer to all my prayers.''',
        '''I seem to have lost my phone number. Can I have yours?''',
        '''I’m lost. Can you give me directions to your heart?''',
        '''Are you a parking ticket? ‘Cause you’ve got fine written all over you.''',
        '''Are you sure you’re not tired? You’ve been running through my mind all day.''',
        '''Is there an airport nearby or is it my heart taking off?''',
        '''Was your dad a boxer? Because damn, you’re a knockout!''',
        '''I was wondering if you had an extra heart. Mine was just stolen.''',
        '''Would you grab my arm, so I can tell my friends I’ve been touched by an angel?''',
        '''There’s only one thing I want to change about you, and that’s your last name.''',
        '''Aside from being sexy, what do you do for a living?''',
        '''Hi, how was heaven when you left it?''',
        '''Do you believe in love at first sight or should I pass by again?''',
        '''Is your dad a terrorist? Cause you’re the bomb.''',
        '''Did the sun come out or did you just smile at me?''',
        '''Kiss me if I’m wrong, but dinosaurs still exist, right?''',
        '''Hey, you’re pretty and I’m cute. Together we’d be Pretty Cute.''',
        '''Did it hurt? When you fell from heaven?''',
        '''Can I follow you home? Cause my parents always told me to follow my dreams.''',
        '''Is your name Google? Because you have everything I’ve been searching for.''',
        '''Are you from Tennessee? Because you’re the only ten I see!''',
        '''Hello, I’m a thief, and I’m here to steal your heart.''',
        '''I may not be a genie, but I can make your dreams come true.''',
        '''If nothing lasts forever, will you be my nothing?''',
        '''There must be something wrong with my eyes, I can’t take them off you.''',
        '''I’m sorry, were you talking to me? [No] Well then, please start.''',
        '''Was you father an alien? Because there’s nothing else like you on Earth!''',
        '''Was your father a thief? ‘Cause someone stole the stars from the sky and put them in your eyes.''',
        '''Do you have a pencil? Cause I want to erase your past and write our future.''',
        '''I’d say God Bless you, but it looks like he already did.''',
        '''I must be in a museum, because you truly are a work of art.''',
        '''Are you my phone charger? Because without you, I’d die.''',
        '''Can you take me to the doctor? Because I just broke my leg falling for you.''',
        '''You don’t need keys to drive me crazy.''',
        '''Are you a dictionary? Cause you’re adding meaning to my life.''',
        '''You remind me of a magnet, because you sure are attracting me over here!''',
        '''I’m no mathematician, but I’m pretty good with numbers. Tell you what, give me yours and watch what I can do with it.''',
        '''Didn’t I see you on the cover of Vogue?''',
        '''Somebody call the cops, because it’s got to be illegal to look that good!''',
        '''Sorry, but you owe me a drink. [Why?] Because when I looked at you, I dropped mine.''',
        '''You must be a broom, ‘cause you just swept me off my feet.''',
        '''My buddies bet me that I wouldn’t be able to start a conversation with the hottest person in the bar. Wanna buy some drinks with their money?''',
        '''Is it hot in here or is it just you?''',
        '''Hello. Cupid called. He wants to tell you that he needs my heart back.''',
        ]

types = []
def home(request):
        line = data[random.randint(0,164)]
        return render(request,'home/index.html',{'lines':line})

