#what i need to do 


#need to potentially do these things
  -1. change how the pycharm code parses the information using playwright instead of selenium
  - or 2. add more specification in how the current code formate the final csv file, making it into the same formate as the code,title,hour as the requirements file is in
  - or 3. make a new code that takes the data how it is currently, and then just formats it into a correct template so then i can compare
  - or 4. find a way to use the data as it currently is for the comparison code (might be more work than making a new code)


-after i fix that need to do this to finish the test of concept
  -1. make an actual knowldege base with all the csv files from the major requirments, minor requriemtns code, and the csv file with all the course list
  -streamline the code so it runs systematically
    -1. uses the degreeworks code to ask the student for their information
    -2, after that script takes the data and makes the csv file, the second the file is created the comparison code runs automatically
  - 3. the comparison code sees the csv is made and uses its made knowledge base of degree requirements and all course list and thier pre reqs , prints out the students still needed classes with its code,title, and credit hours, descrption, and pre requisites into a new csv file.
  - 2. need buy the account that lets me make a bunch of ai training prompts for college schedual building the llm
  - 3. feed all the cs files I currently have into a commerically free llm with the prompts
  - 4 Make the llm register the needed classes,taken classes etc so it can make an actual mock scquedual
  - 5. have the ai make me a mock schedual for next semester using all this data

#next steps

- find the code that scraps rate my professor api to get all the data from every sinlge last course and teacher at valdosta state universtiy
  -  have the ai find a way to see all classes that are currently being offered and are goign to be offered the next semester
  -  make a code that goes into my personal vsu, using a headless browser that takes my secruity questions, clickes on a bunch of stupid links and tabs and goes to my schedual builder  and makes a mock scheudal based on whatever the ai reccommended
  -  have the ai take a screenshot and then save it to a file and then show the file after
  -  using the knowledge base made with the rate my professor data have the ai answer any questions on teachers, how they teach, what do they teach, what do  students think about the proffesor, avergae difficutly of course and how do students do in it. ( basically rate my proffesor but in a sceucual builder)
     sing all of this, make the ai be able to make a schuedal based on spefici requirements, such as i want a 17 credit hr schuedal with teacher only rated 4.0 and above with no classes on friday for a sohpmpre astronomy major.


#sepetmeber 24th 2023

- train the ai on the courses data, so i can answer answer questions on specific classes, aka what is astronomy 1020k, name all math classes and credit hours etc
- train the same model on all the degree requirments so i can reate the classes in the degree requiremtns to the already trained knowledge base and for it to asnwer questions based on reuiremtnes and courses and credit hours
- train the ai model on mock student schedules, so it can relate what a in porgress student schedule looks like and for it to gain better knowledge when making schedules
- train the the ai on prompts, ( go to the sight and get a bunch of training prompts)
  #make it both base prompts like asking the ai basic questions about the classes, and prompts that actually build schedules,

- scrape the data from rate my professor
- train the ai model on the data from rate my professor, also train the ai model on example prompts asking questions about professors, example human> what do students say about this teacher : {teacher name} ai> students say {colums with the adjectives rate my professor give teacher }, and the teacher is rated {column giving rating in the scraped data}
- train the finetuned ai model on the rate my proffesor data
- finish the scheudle builder screenshot code that goes to my vsu clicks on secruity questions, types secruitiy asnwers, goes to banner, goes to my visual schedual builder, clicks on current year, makes a new mock schedule, then takes screenshot and saves te file,
-  make a wesbite to hold the ai, ( ask billy for help if he says no rip)
- FIX THE REQUIREMNTS CODE
- 1. after the trained model is good we want it to be able to intergrate with the website

- 2.  it asked for myvsu stuff then in the website the degree requirments code scrapes the data

- 3. formates it into strings and a easy way for the ai to realte it to its knowledge base

- 4. after it does that it trys to make a mock schedule based on all the cases the student has taken, and what classes the student can take

- 5. lists out differnt possible schedules,( propably one for one )

- 6. ask the student if they would like a visualazaiton of the schedule

- 7. then if they click yes, then the visual schedule builder code runs, and puts in the mock schedule the ai found into it and prints out the outcomes



- FIND OUT A WAY TO TRAIN AI WITHOUTH HAVING TO BUY GIGA COLLAB AND NOT BLOQING UP MACBOOK
- get help with code bc its way harder than i thought it was going to be, proably not though bc nobdoy else seems interesting in this
- be a man

- have the degree requiremnts code convert the students requirements to a prompt for the ai to base a schedule off of 


#updates october 12 
- what you want the code to end up doing, ask for input input goes to the backsend server where python code is running, then back to the frontend which is going to be the website
- make code that goes to registra clicks on each of the type of courses and scrapes the data on who teaches the course when it is being offered and  what times 
