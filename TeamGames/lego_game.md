# Notes for the legendary Lego Game in teams

## Introduction

This is a game for which I got the original idea at a [teacher_seminar](https://tinyurl.com/inspirace-z-krouzku) from Lubos Racansky. I just turned this idea into a competitive team game where two teams battle agains each other for eternal glory.

## History

First this game was implemented at Python Summer Camp and it was quite a success. The kids wanted to play multiple times and also offered to bring their own lego pieces to make the game more interesting next time.

Second run of this game was done during a DDM Coding Club. One team was using coordinates and they had the best result so far I have ever seen. Their building was almost a perfect copy of the prototype.

Diary entries after played the game in DDM:
```md
- tymova hra s Legem
  - dva tymy - popisovac a stavitel
  - tri kola - postupne tezsi a tezsi stavby
    - casy na stavbu: 5,7,10 (minut)
  - holky pouzivaly souradnice a fakt se jim to povedlo (Simca,Emi)
  - kluci (Riki,Tom)

- znovu tymova hra s legem
  - Simca + Riki VS Jake + Tom + Dan
  - Simca a Riki pouzivali souradnice a slo jim to hodne dobre
  - hrali jsme 2 kola po 10 minutach
  - priste by bylo fajn, kdyby ten lepsi tym poradil tomu horsimu, jak na to sli (muzou az uplne na konci, kdyz uz je jistota, ze se nebude hrat dalsi kolo a nevyzradi tak svoje tajemstvi k uspechu)
```

Here is general overview of the game the game:

## Rules:

### Setting
  - 2 teams competing against each other
  - each team has following roles:
    - `describer`
    - `communicator`
    - `builder`
  - there is one prototype lego building that the builder has to build using the available pieces
    - all the pieces necessary are ready to be used for builder
    - all pieces will be used somehow


### Rules by role

#### Describer

- can see:
  - `prototype building`

- movement:
  - `prototype building` <-> `describer-communicator meeting point`
  
- skills:
  - describing precisely (like a programmer)


#### Communicator

- can see:
  - nothing

- movement:
  - `describer-communicator meeting point` <-> `communicator-builder info sharing site`

- skills:
  - memory and speaking skills


#### Builder

- can see:
  - `constructed building`

- movement:
  - none (just sits at the `constructed building`) which is covered so it is invisible from `communicator-builder meeting point`

- skills:
  - understanding instructions (he is the computer that performs commands from the communicator)


### Locations

- team rooms are:
  - the pc-room
  - the studio room

- prototype room is:
  - the elevator room

- the `constructed buildings` will be somewhere in the team rooms far from the doors to the elevator room

- the `prototype building` will be set up between the rooms where the elevator is (above the stairs)
  - it will be somewhere behind so it is not easily visible from the doors of both rooms

- `describer-communicator` meeting points will be the doors between the elevator rooms and the team rooms

### Time limit

- time limit will be between 5 and 10 minutes
  - then it can be extended if both teams agree, otherwise end it

### Game variations

- with less people, there does not have to be the communicator role
  - instead we have `describer-communicator` as one person

- with more people, we can have more `communicators`