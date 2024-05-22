1 INK 0; PAPER 7; BORDER 7; RESTORE CLS
2 DIM mc(30)
3 DIM nc(30)
4 DIM wc(30)
5 DIM pc(30)
6 DIM ac(30)
7 DIM rc(30)
8 DIM uc(30)
10 DIM sc(30,15); DIM dc(30,15)
20 DIM bc(30,16)
30 DIM xc(30)
40 DIM yc(30)
43 PRINT "INSTRUCTIONS"
43 PRINT "You are the leader of a small band of weird characters whose job is to eliminate a group of evil creatures who are killing and destroying everything in their path. You have found them in the arena of vulcan and you fight them one by one. The computer chooses first and then you enter in the number corresponding to your choice. You both start off with 30 creatures and the first party to be killed off looses."
44 PRINT @ (AT 0,0); INK 4;"Press any key"; IF INKEY$="" THEN POKE 0,RND: GO TO 44
45 INPUT ""; PRINT "Your cleric and priest can turn the undead (mummy,skeleton,ghoul,and the zombie) see if they are lucky."
"You start off with 0 experience points but if you kill a strong creature with a weaker creature you gain points (you loose points for the reverse). Good luck."
50 FOR a=1 TO 30
60 READ a$(a); READ c$(a); READ m(a)
70 READ n$(a); LET a(a)=c(a); READ u(a)
80 READ mc(a); LET ac(a)=mc(a); READ r(a)
90 LET bc(a)=INT (RND*8)+1; NEXT
110 DATA "Minotaur","gored",7,1,6,2,"Giant rat","bit",1,4,0
120 DATA "Gremlin","speared",1,8,5,"Ghoul","touched",3,6,2
130 DATA "Hydra","bit",5,3,5,"Manticore","clawed and bit",6,2,4
140 DATA "White dragon","froze",3,6,7,"Acolyte","thumped",1,6,9
150 DATA "Troll","bit and clawed",6,2,2,"Ogre","clubbed",5,8,8
160 DATA "Cyclops","thumped",15,3,8,6
170 DATA "salamander","scorched",2,6,2,"Goblin","wounded",1,8,5
180 DATA "Skeleton","mace'd",1,6,8
190 DATA "Zombie","hit",3,3,6,6,"Giant scorpion","stung",4,3,8
200 DATA "Orc","sliced",2,8,4,"Mummy","paralysed",4,2,6,"Hobgoblin","thumped",3,6,9
210 DATA "Hell hound","burnt",4,3,6,"Chimera","hit",9,3,4
220 DATA "Wyvern","stung and burnt",7,2,4,"Stone Golem","hit",9,8,2
230 DATA "Bone Golem","mutilated",7,2,4
240 DATA "Hill giant","squashed",3,8,7".",8,16,4,"Bugbear","stabbed",3,8,5,"Gargoyle","fanged",4,16,5,"Harpy","charmed and bit",4,3,5
210 DATA "Sirine","drunk",1,3,1
220 FOR a=1 TO 30
230 READ b$(a); READ d$(a)
234 LET e=0
236 READ n(a); LET p(a)=c; READ r(a)
240 FOR b=1 TO c
250 LET f=f+INT (RND*8)+1; NEXT
270 LET y(a)=f
280 NEXT
290 DATA "Warlord","slashed",5,8,10,"Priest","maced",4,6,5
310 DATA "Assassin","stabbed",3,6,7,"Unicorn","horned",3,8,4
320 DATA "Mad dog","bit",5,8,6,5,"Storm giant","electrocuted",18,5,2
330 DATA "Gnome","hit",1,6,5,5,"Elf","sliced",2,10,8,3,"Theif","stabbed",1,4,8,7
350 DATA "Owl bear","hugged",5,3,5,"Werebear","hugged",5,4,5,4,2
360 DATA "Roc","Pecked",6,8,22,4,"Cleric","baptised",2,6,8,2
370 DATA "Dwarf","thumped",1,8,8,6,"Halfling","sliced",1,4,5
380 DATA "Hobbit","slashed",1,4,6,
5,2,"Centaur","knocked",6,8,20
390 DATA "Hippogriff","Pecked",
3,8,22,5,"Dwarven hero","chopped
400 DATA "Super-hero","sliced",
8,6,10,1,"Master thief","stabbe
d",9,4,4,2
410 DATA "Brass dragon","breath
ed on",8,8,30,2,"Pegasus","bit",
2,8,16,6
420 DATA "Giant hawk","Pecked",
3,8,6,"Blink dog","gnawed",4,
3,6,2
430 DATA "Lawful Goblin","struc
k",1,8,8,7
440 DATA "Giant weasel","bit",4,
8,7,"Bard","sung to",3,6,6,
"Druid","sickled",4,6,45
500 LET v=INT (RND*8)+1
501 IF x(v)=0 THEN GO TO 500
502 PRINT ; PRINT
520 PRINT "The computer chooses
530 PRINT "INVERSE 1; "LEVEL"
530 PRINT ; PRINT
535 PRINT BRIGHT 1;"YOU HAVE:"
535 PRINT "NO NAME LE
H.P.
540 FOR a=1 TO 30
545 LET m=a
550 IF x(a)<>0 THEN PRINT a;"
550 IF x(a)=0 THEN PRINT a);" "
550 PRINT AT 21,10;p(x);"AT 21
23)";NEXT a
560 NEXT
576 INPUT "Your Choice";a
576 IF a>30 OR a<1 OR INT x<a
THEN GO TO 576
580 IF y(a)<x THEN PRINT PAP
ER 3; INK 9; FLASH 1;"He's dead
Nice try! GO TO 570
585 LET i=m; FOR q=15 TO 2
STEP -1; IF m=1 THEN LET
i=i+1; NEXT q
586 LET l=m; FOR q=15 TO 2
STEP -1; IF l=1 THEN LET
l=l+1; NEXT q
587 LET p$=m; FOR q=15 TO 2
STEP -1; IF p$(a) = "" THEN LET
p$(m+x)=0; -1; NEXT q

