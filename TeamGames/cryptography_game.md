# Notes about Cryptography Team Game

This is a new game I am just developing and will test tomorrow at DDM Coding Club

## Rules

### Motivation

- each team of 2 players is a secret intelligence service CIA, MI6, KGB or whatever
- the two teammates are agents that are located in different parts of the world
- they can only communicate over a channel that spies from the other teams can see and read
- they each get 3 secret codes that they have to send to their teammate over the channel
- secret code is a discount code for Alza.cz that will help the other agent buy really strong weapons to fight their enemies

### Setup

- two sides with computers
  - team mates sit on opposite sides of the room
- each member of team gets:
  - a piece of paper with 3 printed secret codes
  - a pencil to write down all received secret codes (also from other teams)
- the messages will be sent through Scratch studio created exactly for this purpose
  - comments section of the studio (cannot send more than two messages in less than 30 seconds)
- game consists of phases:
  - planning
  - mission execution
- during each phase, they get new secret codes

### Goal

- in limited amount of time (cca 5 minutes)
- get as many secret codes as possible and write them down
- each secret code is worth a point (even a code intercepted from enemy team)
- after time limit is done, we will calculate the scores together

### Rules

- mission execution
  - no other means of communication, only through Scratch channel
    - if the way they got it was over other channel, that is illegal
    - at the end, they have to be able to show us, how they got the message (at least from what) to prove that they didn't send it over another channel
  - no talking to your teammate
  - no looking at other people's screens
  - no moving around from their computer
  - when code written down, THEY MUST BE ABLE TO TELL AT THE END OF THE GAME HOW THEY GOT IT
    - if the way they got it is illegal -> no points scored
  - you are allowed to do whatever with the messages you got through the channel
    - talk about them with ChatGPT, try to break the cipher in any way

- planning
  - talk about strategy, of how they could transfer the secret message to themselves
  - use the fact, that they can agree on something even though they do not know the secret codes in advance

### Rounds

1. test round
- they will have no time to plan before
- will be short
- should make them realize, that it is quite a difficult task to achieve the goal
- have time to think themselves, how they could use time with their teammate to agree on something useful

2. planned round
- comes after a 5 min planning period
- they will get new secret codes (not known in advance)
- but they had possibility to agree on some secret beforehand (password for a cipher maybe, or just a method in which they will encrypt the message)
- this round will be interesting as they will be using their own ciphers which will likely be not so strong and could be possibly interpepted by other teams
  - by asking ChatGPT or using some decrypter on the internet

3. rsa-test-round
- last round after I explain them, how cool RSA is
- I will show them exactly what to do
- the task will be, if they remembered correctly what I showed them and are able to use that in practice (a good way to check if they understand the mechanism of the asymmetric cryptography)

### Prizes

- this time, I would like to include prizes as well
- ideas:
  - healthy snacks: nuts, fruit bar, not-to-sweet-cookies
  - pencils, notebooks or something similar
  - stickers