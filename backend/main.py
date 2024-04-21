from flask import Flask
from flask import request, jsonify,session
from flask_cors import CORS,cross_origin
# import aima.logic as lg
# import aima.utils as ut
import aima3.logic as lg
import aima3.utils as ut



app = Flask(__name__)

goals = [
    "Career",
    "MakeMoney",
    "Productivity",
    "Leadership",
    "Articulate"
    "Healthy",
    "Social_life",
    "Technology"
]


book = {
    'id':0,
    'title':'asdas',
    'img':'adsdsa',
    'description':'asddasd',
    'keyPoints':['asd','sadasd'],
    'Summary':'asdsad'
}

"""
fc.tell(make_money(Ahmed))


fc.ask(Book(Ahmed,x)
"""

ThemSes = [
    "Finance",
    "self_imporovment",
    "Psychology",
    "Programming",
    "History",
    "sports",
    ""
]











rules = [
    "Leadership(x)  ==> Theme(Management,x)",
    "Career(x) ==> Theme(Management,x)",
    "Career(x) ==> Theme(Entrepreneurship,x)",
    "Leadership(x)  ==> Theme(Entrepreneurship,x)",

    "Productivity(x)  ==> Theme(Organization,x)",
    "Career(x) ==> Theme(Organization,x)",

    "Career(x) ==> Theme(TimeManagement,x)",
    "Productivity(x) ==> Theme(TimeManagement,x)",

    "MakeMoney(x)  ==>Theme(Business,x)",
    "Career(x) ==>Theme(Business,x)",


    "Career(x) ==>Theme(Finance,x)",
    "Career(x) ==>Theme(Finance,x)",

    "Productivity(x) ==> Theme(SelfImprovement,x)",
    "Healthy(x) ==> Theme(SelfImprovement,x)",

    "Productivity(x) ==>Theme(Nutrition,x)",
    "Healthy(x) ==>Theme(Nutrition,x)",

    "Healthy(x) ==>Theme(Wellness,x)",
    "Productivity(x) ==>Theme(Wellness,x)",

    "Social(x) ==> Theme(CommunicationSkills,x)",
    "Healthy(x) ==> Theme(CommunicationSkills,x)",

    " Healthy(x) ==> Theme(SelfHelp,x)",
    "Social(x)  ==> Theme(SelfHelp,x)",

    "Healthy(x) ==> Theme(Relationships,x)",
    "Social(x) ==> Theme(Relationships,x)",

    "Technology(x)  ==> Theme(TechnologyTrends,x)",
    "Career(x) ==> Theme(TechnologyTrends,x)",

    "Technology(x) ==> Theme(Freelance,x)",
    "MakeMoney(x) ==> Theme(Freelance,x)",

    "Technology(x) ==> Theme(Investing,x)",
    "MakeMoney(x) ==> Theme(Investing,x)",

    "Productiviy(x) ==> Theme(ArtificielIntelligence,x)",
    "Technology(x)  ==> Theme(ArtificielIntelligence,x)",

    "Articulate(x) ==> Theme(Psychology,x)",
    "Social(x) ==> Theme(Psychology,x)",


    "Articulate(x) ==> Theme(Investing,x)",
    "MakeMoney(x) ==> Theme(Investing,x)",

    "Articulate(x)  ==> Theme(SelfImprovement,x)",
    "Productivity(x) ==> Theme(SelfImprovement,x)",

    "Articulate(x)  ==> Theme(Finance,x)",
    "Career(x) ==> Theme(Finance,x)",

    "Articulate(x) ==> Theme(TechonologyTrends,x)",
    "Techonology(x) ==> Theme(TechonologyTrends,x)",

    "Articulate(x) ==> Theme(Cybersecurity,x)",
    "Techonology(x) ==> Theme(Cybersecurity,x)",

    "Articulate(x) ==> Theme(Programming,x)",
    "Techonology(x) ==> Theme(Programming,x)",

    "Social(x) ==> Theme(Relationships,x)",
    "Career(x) ==> Theme(Business,x)",
    "MakeMoney(x) ==> Theme(Finance,x)",
    "Productivity(x) ==> Theme(TimeManagement,x)",
    "Leadership(x) ==> Theme(LeadershipDevelopment,x)",
    "Articulate(x) ==> Theme(History,x)",
    "Healthy(x) ==> Theme(Nutrition,x)",
    "Social(x) ==> Theme(CommunicationSkills,x)",
    "Technology(x) ==> Theme(Programming,x)",

    "Theme(Career,x)  ==> Book(The_Effective_Executive,x)",
    "Theme(Entrepreneurship,x)  ==> Book(The_Effective_Executive,x)",
    "Theme(Management,x)  ==> Book(The_Effective_Executive,x)",
    "Theme(Organization,x) ==> Book(The_Effective_Executive,x)",

    "Theme(Productivity,x) ==> Book(High_Output_Management,x) ",
    "Theme(Business,x) ==> Book(High_Output_Management,x) ",
    "Theme(Management,x) ==> Book(High_Output_Management,x) ",

    "Theme(Entrepreneurship,x)    ==> Book(The_Lean_Startup,x) ",
    "Theme(Business,x)   ==> Book(The_Lean_Startup,x) ",
    "Theme(Finance,x)   ==> Book(The_Lean_Startup,x) ",

    "Theme(Entrepreneurship,x)  ==> Book(Zero_to_One,x)",
    "Theme(Management,x)  ==> Book(Zero_to_One,x)",
    "Theme(Business,x)  ==> Book(Zero_to_One,x)",

    "Theme(SelfHelp,x)  ==> Book(The_Life_Changing_Magic_of_Tidying_Up,x)",
    "Theme(Wellness,x) ==> Book(The_Life_Changing_Magic_of_Tidying_Up,x)",
    "Theme(SelfImprovement,x)  ==> Book(The_Life_Changing_Magic_of_Tidying_Up,x)",

    "Theme(Productivity,x)  ==> Book(Getting_Things_Done,x)",
    "Theme(Wellness,x)   ==> Book(Getting_Things_Done,x)",
    "Theme(SelfHelp,x)   ==> Book(Getting_Things_Done,x)",
    "Theme(TimeManagement,x) ==> Book(Getting_Things_Done,x)",

    "Theme(Productivity,x) ==> Book(Eat_That_Frog,x)",
    "Theme(TimeManagement,x)  ==> Book(Eat_That_Frog,x)",

    "Theme(Entrepreneurship,x)   ==> Book(The_One_Thing,x)",
    "Theme(SelfImprovement,x)  ==> Book(The_One_Thing,x)",

    "Theme(Business,x)  ==> Book(The_Innovators_Dilemma,x)",
    "Theme(Management,x)   ==> Book(The_Innovators_Dilemma,x)",

    "Theme(Business,x)  ==> Book(Good_to_Great,x)",
    "Theme(Management,x)   ==> Book(Good_to_Great,x)",

    "Theme(Finance,x) ==> Book(The_Intelligent_Investor,x) ",
    "Theme(Investing,x)   ==> Book(The_Intelligent_Investor,x)",
    "Theme(Finance,x) ==> Book(The_Millionaire_Next_Door,x)",
    "Theme(LeadershipDevelopment,x)   ==> Book(The_Millionaire_Next_Door,x)",
    "Theme(SelfHelp,x) ==> Book(The_7_Habits_of_Highly_Effective_People,x) ",
    "Theme(Wellness,x)  ==> Book(The_7_Habits_of_Highly_Effective_People,x)",
    "Theme(Psychology,x)  ==> Book(The_7_Habits_of_Highly_Effective_People,x)",
    "Theme(SelfHelp,x) ==> Book(Atomic_Habits,x) ",
    "Theme(Psychology,x) ==> Book(Atomic_Habits,x)",
    "Theme(TimeManagement,x) ==> Book(Atomic_Habits,x)",


    "Theme(Nutrition,x) ==> Book(How_Not_to_Die,x) ",
    "Theme(Wellness,x) ==> Book(How_Not_to_Die,x)",
    "Theme(SelfImprovement,x)  ==> Book(How_Not_to_Die,x)",
    "Theme(Nutrition,x) ==> Book(The_Omnivores_Dilemma,x)",
    "Theme(Wellness,x) ==> Book(The_Omnivores_Dilemma,x)",
    "Theme(SelfHelp,x)  ==> Book(The_Omnivores_Dilemma,x)",
    "Theme(SelfHelp,x) ==> Book(The_Power_of_Now,x)",
    "Theme(SelfImprovement,x) ==> Book(The_Power_of_Now,x)",
    "Theme(TimeManagement,x)  ==> Book(The_Power_of_Now,x)",

    "Theme(SelfImprovement,x) ==> Book(The_Four_Agreements,x)",
    "Theme(SelfHelp,x) ==> Book(The_Four_Agreements,x)",
    "Theme(Organization,x)  ==> Book(The_Four_Agreements,x)",
    "Theme(CommunicationSkills,x) ==> Book(Crucial_Conversations,x) ",
    "Theme(Relationships,x)   ==> Book(Crucial_Conversations,x)",

    "Theme(Relationships,x) ==> Book(Never_Split_the_Difference,x)",
    "Theme(CommunicationSkills,x)   ==> Book(Never_Split_the_Difference,x)",
    "Theme(SelfImprovement,x) ==> Book(The_Alchemist,x) ",
    "Theme(SelfHelp,x)   ==> Book(The_Alchemist,x)",
    "Theme(SelfImprovement,x) ==> Book(The_Power_of_Positive_Thinking,x)",
    "Theme(SelfHelp,x) ==> Book(The_Power_of_Positive_Thinking,x)",
    "Theme(Psychology,x)   ==> Book(The_Power_of_Positive_Thinking,x)",
    "Theme(Relationships,x)  ==> Book(The_5_Love_Languages,x)",
    "Theme(CommunicationSkills,x)  ==> Book(The_5_Love_Languages,x)",
    "Theme(Psychology,x)  ==> Book(The_5_Love_Languages,x)",

    "Theme(Relationships,x) ==> Book(Men_Are_from_Mars_Women_Are_from_Venus,x)",
    "Theme(Psychology,x) ==> Book(Men_Are_from_Mars_Women_Are_from_Venus,x) ",
    "Theme(SelfHelp)   ==> Book(Men_Are_from_Mars_Women_Are_from_Venus,x)",
    "Theme(TechnologyTrends,x)    ==> Book(The_Singularity_Is_Near,x)",
    "Theme(ArtificielIntelligence,x)   ==> Book(The_Singularity_Is_Near,x)",
    "Theme(ArtificielIntelligence,x)  ==> Book(The_Industries_of_the_Future,x) ",
    "Theme(Business,x)   ==> Book(The_Industries_of_the_Future,x)",
    "Theme(TechnologyTrends,x) ==> Book(The_Industries_of_the_Future,x)  ",
    "Theme(Business,x)   ==> Book(The_Industries_of_the_Future,x) ",



    "Theme(Finance,x)    ==> Book(The_Freelancers_Bible,x)",
    "Theme(Business,x)    ==> Book(The_Freelancers_Bible,x)",
    "Theme(Freelance,x)   ==> Book(The_Freelancers_Bible,x) ",
    "Theme(TechnologyTrends,x)    ==> Book(The_Freelancers_Bible,x)",

    "Theme(Business,x)     ==> Book(The_Gig_Economy,x)",
    "Theme(Finance,x)    ==> Book(The_Gig_Economy,x)",
    "Theme(TechnologyTrends,x)    ==> Book(The_Gig_Economy,x) ",
    "Theme(Freelance,x)   ==> Book(The_Gig_Economy,x)",


    "Theme(Finance,x)    ==> Book(The_Little_Book_of_Common_Sense_Investing,x)",
    "Theme(Investing,x)   ==> Book(The_Little_Book_of_Common_Sense_Investing,x)",

    "Theme(Finance,x)    ==> Book(A_Random_Walk_Down_Wall_Street,x)",
    "Theme(Investing,x)   ==> Book(A_Random_Walk_Down_Wall_Street,x)",

    "Theme(TechnologyTrends,x)    ==> Book(The_Master_Algorithm,x)",
    " Theme(Programming,x)   ==> Book(The_Master_Algorithm,x)",
    " Theme(ArtificielIntelligence,x)   ==> Book(The_Master_Algorithm,x)",


    "Theme(TechnologyTrends,x)    ==> Book(Superintelligence_Paths_Dangers_Strategies,x)",
    " Theme(Programming,x)   ==> Book(Superintelligence_Paths_Dangers_Strategies,x)",
    " Theme(ArtificielIntelligence,x)    ==> Book(Superintelligence_Paths_Dangers_Strategies,x)",

    "Theme(Psychology,x)    ==> Book(Thinking_Fast_and_Slow,x)",
    " Theme(Wellness,x)   ==> Book(Thinking_Fast_and_Slow,x)",
    "Theme(SelfImprovement,x)   ==> Book(Thinking_Fast_and_Slow,x)",

    "Theme(Psychology,x)   ==> Book(Influence_The_Psychology_of_Persuasion,x)",
    "Theme(CommunicationSkills,x)   ==> Book(Influence_The_Psychology_of_Persuasion,x)",
    "Theme(Relationships,x)   ==> Book(Influence_The_Psychology_of_Persuasion,x)",


    "Theme(Programming,x)    ==> Book(Cybersecurity_for_Beginners,x)",
    "Theme(Cybersecurity,x)   ==> Book(Cybersecurity_for_Beginners,x)",
    "Theme(TechnologyTrends,x)   ==> Book(Cybersecurity_for_Beginners,x)",


    "Theme(Programming,x) ==> Book(The_Art_of_Deception,x)  ",
    "Theme(TechnologyTrends,x) ==> Book(The_Art_of_Deception,x) ",
    "Theme(Cybersecurity,x)   ==> Book(The_Art_of_Deception,x)",


    "Theme(Programming,x)   ==> Book(Code_Complete,x)",
    "Theme(TechnologyTrends,x)   ==> Book(Code_Complete,x)",


    "Theme(Programming,x)    ==> Book(Clean_Code,x)",
    "Theme(TechnologyTrends,x)   ==> Book(Clean_Code,x)",

    "Theme(LeadershipDevelopment,x)   ==> Book(Leaders_Eat_Last,x)",
    "Theme(LeadershipDevelopment,x)   ==> Book(The_21_Irrefutable_Laws_of_Leadership,x)",
    "Theme(History,x)   ==> Book(Sapiens_A_Brief_History_of_Humankind,x)",
    "Theme(History,x)    ==> Book(The_Guns_of_August,x)",


]

Themes = [
    'Management','Entrepreneurship','Organization','TimeManagement','Business',
    'Finance','SelfImprovement','Nutrition','Wellness','CommunicationSkills',
    'SelfHelp','Relationships','TechnologyTrends','Freelance','Investing',
    'ArtificielIntelligence','Psychology','Cybersecurity','Programming',
    'LeadershipDevelopment','History'
]



Books = [
    "The Effective Executive" , "High Output Management" 
 "The Lean Startup" , "Zero to One" 
 "The Life Changing Magic of Tidying Up"  "Getting Things Done" 
 "Eat That Frog!" , "The One Thing" 
"The Innovators Dilemma" , "Good to Great" 
 "The Intelligent Investor", "The Millionaire Next Door" 
"The 7 Habits of Highly Effective People", "Atomic Habits" 
 "How Not to Die", "The Omnivores Dilemma" 
 "The Power of Now" , "The Four Agreements"
"Crucial Conversations" , "Never Split the Difference" 
 "The Alchemist" , "The Power of Positive Thinking"
 "The 5 Love Languages" , "Men Are from Mars Women Are from Venus" 
 "The Singularity Is Near" , "The Industries of the Future" 
 "The Freelancers Bible" , "The Gig Economy"
"The Little Book of Common Sense Investing" , "A Random Walk Down Wall Street" 
 "The Master Algorithm" , "Superintelligence Paths Dangers Strategies" 
"Thinking Fast and Slow" , "Influence The Psychology of Persuasion" 
 "Cybersecurity for Beginners" , "The Art of Deception" 
"Code Complete" , "Clean Code" 
 "Leaders Eat Last", "The 21 Irrefutable Laws of Leadership" 
 "Sapiens A Brief History of Humankind" , "The Guns of August"
]

Books_Data = [
    {
        "title": "The Intelligent Investor",
        "author": "Benjamin Graham",
        "description": "The Intelligent Investor by Benjamin Graham is considered a classic in the world of investing. First published in 1949, it provides practical advice and guidelines for intelligent, long-term investing strategies.",
        "Summary": "In The Intelligent Investor, Graham advocates for a 'defensive' investing approach that focuses on buying undervalued stocks and maintaining a margin of safety. He also emphasizes the importance of careful analysis and research before making any investment decisions. Throughout the book, he stresses the need for patience, discipline, and a long-term perspective in order to achieve success as an investor. The book's principles have been widely followed and influenced many successful investors, including Warren Buffett.",
        "url": "https://m.media-amazon.com/images/I/919mmNCTaaL._AC_UY218_.jpg"

    },

    {
        "title": "The Millionaire Next Door",
        "author": "Thomas J. Stanley and William D. Danko",
        "description": "The Millionaire Next Door by Thomas J. Stanley and William D. Danko is a research-based book that examines the lifestyles of millionaires in the United States and provides insights into how to become a millionaire.",
        "Summary": "The book analyzes the lives of millionaires and shows that many of them live frugally and do not display their wealth. The authors argue that this is because they prioritize financial independence and have developed habits that allow them to accumulate and maintain wealth. The book highlights seven key factors that contribute to wealth accumulation, including living below your means, investing wisely, and being self-employed. The authors also caution against lifestyle inflation, emphasizing the importance of saving and investing for long-term financial security. Overall, 'The Millionaire Next Door' is a practical guide for anyone looking to build wealth and achieve financial independence.",
        "url": "https://m.media-amazon.com/images/I/81y4IBu7gzL._AC_UY218_.jpg"

    },

    {
        "title": "The 7 Habits of Highly Effective People",
        "author": "Stephen Covey",
        "description": "The 7 Habits of Highly Effective People is a self-help book written by Stephen Covey. It aims to provide readers with practical and philosophical guidance for improving their personal and professional lives.",
        "Summary": "The book presents a framework for personal and interpersonal effectiveness that emphasizes principles of character and collaboration. Covey argues that success in both our personal and professional lives comes from aligning our actions with our values and developing positive habits. The seven habits, which include being proactive, beginning with the end in mind, putting first things first, thinking win-win, seeking first to understand, then to be understood, synergizing, and sharpening the saw, are designed to help individuals develop the skills and mindset necessary to achieve their goals and build positive relationships. Covey's approach emphasizes the importance of developing both internal and external effectiveness, focusing on personal development and collaboration with others. The book has become a classic in the self-help genre, and its principles have been widely adopted in business, education, and personal development settings.",
        "url": "https://m.media-amazon.com/images/I/71oei0tAnzL._AC_UY218_.jpg"

    },

    {
        "title": "Atomic Habits",
        "author": "James Clear",
        "description": "Atomic Habits by James Clear is a self-help book that provides practical strategies for building and maintaining good habits while breaking bad ones.",
        "Summary": "Atomic Habits presents a framework for building habits that is based on small, incremental changes that lead to big results over time. Clear argues that rather than focusing on big, life-changing moments, we should focus on making small, consistent improvements in our behavior. He outlines a four-step process for creating and sticking to good habits: make it obvious, make it attractive, make it easy, and make it satisfying. Additionally, Clear offers advice on how to break bad habits by identifying the underlying cause and replacing them with better ones. The book includes many real-life examples and actionable tips for readers to apply in their own lives, making it a valuable guide for anyone looking to improve their habits and achieve their goals.",
        "url": "https://m.media-amazon.com/images/I/71F4+7rk2eL._AC_UY218_.jpg"

    },

    {
        "title": "How Not to Die",
        "author": "Dr. Michael Greger",
        "description": "How Not to Die is a comprehensive guide to using nutrition and lifestyle changes to prevent and reverse chronic diseases.",
        "Summary": "In How Not to Die, Dr. Michael Greger examines the leading causes of death and presents scientific evidence for how a whole-food, plant-based diet and healthy lifestyle habits can prevent and even reverse many chronic diseases. He also provides practical tips for incorporating these changes into your life, making healthy eating easy and enjoyable. The book emphasizes the importance of focusing on individual habits rather than quick-fix solutions, and provides a wealth of evidence-based advice for those seeking to improve their health and longevity.",
        "url": "https://m.media-amazon.com/images/I/81RvGjUWqlL._AC_UY218_.jpg"

    },

    {
        "title": "The Omnivore's Dilemma",
        "author": "Michael Pollan",
        "description": "The Omnivore's Dilemma by Michael Pollan is a book that explores the modern food industry and the various ways in which food is produced, processed, and consumed in America.",
        "Summary": "The book is divided into three parts, each of which focuses on a different food chain: industrial, organic, and foraged. Pollan investigates the origins and impacts of each food chain, tracing the complex relationships between farmers, corporations, consumers, and the environment. Through his research, Pollan uncovers the hidden costs and ethical implications of our food choices, from the exploitation of workers to the destruction of ecosystems. He also explores the cultural and psychological dimensions of food, examining how our attitudes and beliefs shape our eating habits and our relationship with nature. Ultimately, 'The Omnivore's Dilemma' challenges readers to consider the consequences of their food choices and to become more conscious and responsible eaters. The book is well-written, engaging, and informative, offering a thought-provoking perspective on one of the most fundamental aspects of human life.",
        "url": "https://m.media-amazon.com/images/I/71u8vMBVePL._AC_UY218_.jpg"

    },

    {
        "title": "The Power of Now",
        "author": "Eckhart Tolle",
        "description": "'The Power of Now' by Eckhart Tolle is a spiritual self-help book that focuses on the importance of living in the present moment and finding inner peace.",
        "Summary": "The book emphasizes the idea that we can only truly experience happiness and fulfillment by living in the present moment, rather than dwelling on the past or worrying about the future. Tolle provides practical advice for how to achieve this state of mindfulness, including techniques for quieting the mind and focusing on the present. He also discusses the nature of the ego and the importance of transcending the ego in order to connect with our true selves. Throughout the book, Tolle uses a combination of personal anecdotes, spiritual teachings, and practical exercises to help readers cultivate a deeper awareness of the present moment and develop a more profound sense of inner peace. 'The Power of Now' has become a widely popular and influential book in the field of self-help and spirituality, offering a powerful message that can help readers transform their lives and find greater happiness and fulfillment.",
        "url": "https://m.media-amazon.com/images/I/51wk62SpJaL._AC_UY218_.jpg"

    },

    {
        "title": "The Four Agreements",
        "author": "Don Miguel Ruiz",
        "description": "The Four Agreements is a book by Don Miguel Ruiz that presents a code of conduct based on ancient Toltec wisdom.",
        "Summary": "In 'The Four Agreements,' Don Miguel Ruiz outlines four simple yet powerful agreements that can transform one's life. These agreements are: be impeccable with your word, don't take anything personally, don't make assumptions, and always do your best. Ruiz explains that by following these agreements, we can free ourselves from self-limiting beliefs and live a life of happiness and fulfillment. The book draws on ancient Toltec wisdom and presents a spiritual approach to personal growth and transformation. It has become a popular self-help book and has been praised for its practical and accessible advice.",
        "url": "https://m.media-amazon.com/images/I/81hHy5XrdKL._AC_UY218_.jpg"

    },

    {
        "title": "Crucial Conversations",
        "author": "Kerry Patterson",
        "description": "Crucial Conversations by Kerry Patterson, Joseph Grenny, Ron McMillan, and Al Switzler is a guide to help readers handle difficult conversations in both personal and professional settings.",
        "Summary": "Crucial Conversations teaches readers how to handle high-stakes conversations and achieve positive outcomes by focusing on dialogue instead of debate. The book offers a step-by-step process for preparing for and conducting these conversations, emphasizing the importance of creating a safe and respectful environment. The authors provide practical tips and strategies for staying calm and focused during heated exchanges and for resolving conflicts in a mutually beneficial way. The book also explores common communication traps and provides guidance on how to avoid them. Overall, 'Crucial Conversations' is a valuable resource for anyone who wants to improve their communication skills and build stronger relationships.",
        "url": "https://m.media-amazon.com/images/I/71oJG4ynmaL._AC_UY218_.jpg"

    },

    {
        "title": "Never Split the Difference",
        "author": "Chris Voss",
        "description": "Never Split the Difference by Chris Voss is a guide to negotiating effectively, based on Voss's experience as a former FBI hostage negotiator. The book presents techniques and strategies for getting what you want in any negotiation, including how to build rapport, gather information, and influence others.",
        "Summary": "Never Split the Difference is a practical guide to effective negotiation that draws on the author's experience as a hostage negotiator for the FBI. The book offers a range of techniques and strategies for getting what you want in any negotiation, including how to build rapport, gather information, and influence others. Key concepts include the importance of active listening, empathy, and framing, as well as techniques for handling difficult negotiations and resolving conflicts. The book also offers tips for negotiating in specific contexts, such as salary negotiations, business deals, and international negotiations. Overall, 'Never Split the Difference' is a useful resource for anyone looking to improve their negotiation skills and achieve better outcomes in their personal and professional life.",
        "url": "https://m.media-amazon.com/images/I/81TN0My+irL._AC_UY218_.jpg"

    }
    ,
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "description": "The Alchemist is a novel by Brazilian author Paulo Coelho. The book follows the journey of a young shepherd named Santiago who dreams of a treasure hidden in the Egyptian pyramids. Along the way, he encounters a series of characters who teach him valuable lessons about life and pursuing ones dreams.",
        "Summary": "The Alchemist is a novel by Brazilian author Paulo Coelho, which tells the story of a young shepherd named Santiago who dreams of a treasure hidden in the Egyptian pyramids. In pursuit of his dream, Santiago embarks on a journey that takes him across the Mediterranean and into the heart of the desert.Throughout his journey, Santiago meets a series of characters who teach him valuable lessons about life and pursuing ones dreams. He learns to trust his intuition, to have faith in the universe, and to believe in the power of love. Santiagos journey teaches him the importance of living in the present moment and following ones personal legend.Along the way, Santiago encounters various obstacles and setbacks, but he perseveres, never losing sight of his goal. He develops a deep understanding of the interconnectedness of all things and comes to believe that everything in life happens for a reason.In the end, Santiago reaches the Egyptian pyramids and discovers that the true treasure he was seeking all along was within himself.The Alchemist is a timeless classic that continues to inspire readers around the world with its themes of self-discovery, spirituality, and the pursuit of one's dreams.",
        "url": "https://m.media-amazon.com/images/I/518qiLwlQ0L._AC_UY327_FMwebp_QL65_.jpg"
    },

    {
        "title": "The Power of Positive Thinking",
        "author": "Norman Vincent Peale",
        "description": "The Power of Positive Thinking is a self-help book by Norman Vincent Peale. The book teaches readers how to use positive thinking to achieve success and happiness in life. It offers practical advice and techniques for overcoming negative thoughts and emotions and replacing them with positive ones.",
        "Summary": "The Power of Positive Thinking by Norman Vincent Peale is a self-help book that teaches readers how to use positive thinking to achieve success and happiness in life. The book emphasizes the importance of cultivating a positive mindset and the impact it can have on one's life. Peale offers practical advice and techniques for overcoming negative thoughts and emotions, such as fear, anxiety, and self-doubt, and replacing them with positive ones. He encourages readers to develop a deep sense of gratitude for the blessings in their lives and to focus on the good in people and situations. Throughout the book, Peale shares personal anecdotes and stories of individuals who have used the power of positive thinking to overcome obstacles and achieve success in their lives. He also provides practical exercises and techniques for readers to implement in their daily lives. One of the key teachings of the book is the importance of faith in oneself and in a higher power. Peale encourages readers to develop a strong belief in themselves and their abilities and to have faith that things will work out for the best. The Power of Positive Thinking has been a bestseller for decades and has inspired countless readers to adopt a more positive and optimistic outlook on life. The book's message of the power of positive thinking remains as relevant today as when it was first published, and its practical advice and techniques continue to be a valuable resource for those seeking to improve their lives.",
        "url": "https://m.media-amazon.com/images/I/612r0oxHHUL._AC_UY327_FMwebp_QL65_.jpg"
    },

    {
        "title": "The 5 Love Languages",
        "author": "Gary Chapman",
        "description": "The 5 Love Languages is a self-help book by Gary Chapman that outlines five ways people express and experience love. The book offers practical advice for individuals and couples looking to improve their relationships by better understanding their partner's love language.",
        "Summary": "The 5 Love Languages is a self-help book that outlines the five primary ways people express and experience love: words of affirmation, acts of service, receiving gifts, quality time, and physical touch. The book explains how each love language works and offers practical advice for individuals and couples looking to improve their relationships by better understanding their partner's love language.Chapman emphasizes the importance of identifying and speaking one's partner's love language in order to effectively communicate love and build a strong relationship. He provides practical tools and exercises to help readers discover their own love language and that of their partner. The book also addresses common relationship issues, such as conflicts and misunderstandings, and offers advice for resolving them. Chapman emphasizes the importance of empathy, understanding, and effective communication in building a healthy and happy relationship.The 5 Love Languages has been a bestseller for decades and has helped countless individuals and couples improve their relationships. The book's practical advice and exercises make it a valuable resource for anyone looking to deepen their understanding of their own needs and those of their partner, and to build stronger, more fulfilling relationships.",
        "url": "https://m.media-amazon.com/images/I/51c0ewv4OML._AC_UY327_FMwebp_QL65_.jpg"
    },

    {
        "title": "The Singularity Is Near",
        "author": "Ray Kurzweil",
        "description": "A non-fiction book by Ray Kurzweil that discusses the future of technology and the potential for a technological singularity.",
        "summary": "The Singularity Is Near is a non-fiction book by Ray Kurzweil that explores the exponential growth of technology and its potential to transform humanity. Kurzweil argues that the rapid pace of technological progress will lead to a technological singularity, a point in the near future where humans will merge with machines, leading to a post-human era.The book covers a wide range of topics related to the future of technology, including artificial intelligence, robotics, nanotechnology, and biotechnology. Kurzweil discusses the potential benefits and risks of these technologies, such as the possibility of extending human life, enhancing human intelligence, and the potential risks of creating superintelligent machines. Kurzweil also explores the ethical, social, and economic implications of the singularity, including the potential for increased inequality, the transformation of work and education, and the need for new forms of governance and regulation. He argues that these challenges can be addressed by embracing the transformative potential of technology and developing new ethical frameworks and social structures that can adapt to the changes ahead.Overall,The Singularity Is Near offers a thought-provoking look at the future of technology and its potential impact on humanity. The book challenges readers to consider the implications of these rapid changes and to embrace the possibilities of a future where humans and machines merge to create a new era of intelligence and creativity.",
        "url": "https://m.media-amazon.com/images/I/91q803eN7IL._AC_UY327_FMwebp_QL65_.jpg"
    },

    {
        "title": "The Industries of the Future",
        "author": "Alec Ross",
        "description": "A non-fiction book by Alec Ross that discusses the key trends shaping the future of the global economy and the industries that are likely to drive growth in the coming years.",
        "summary": "The Industries of the Future is a non-fiction book by Alec Ross that explores the key trends shaping the future of the global economy and the industries that are likely to drive growth in the coming years. Ross focuses on several key areas, including robotics and automation, artificial intelligence, cybersecurity, biotechnology, and the Internet of Things.The book examines the potential benefits and risks of these technologies, as well as the ethical and social implications of their adoption. Ross also discusses the impact of these trends on employment, education, and global geopolitics. He argues that these new industries will require new skills and training, and that governments and businesses must work together to prepare for the future.Ross highlights several examples of countries and companies that are successfully adapting to these changes, and offers insights into the strategies that have enabled them to thrive. He also identifies potential challenges and risks, such as increased inequality and geopolitical tensions, and offers recommendations for addressing these issues.Overall,The Industries of the Future offers a thought-provoking look at the future of the global economy and the opportunities and challenges that lie ahead. The book challenges readers to think creatively about the future and to embrace the potential of new technologies and industries, while also recognizing the need to address the challenges that may arise.",
        "url": "https://m.media-amazon.com/images/I/5101Y5bvHoL._AC_UY327_FMwebp_QL65_.jpg"
    },

    {
        "title": "The Freelancers Bible",
        "author": "Sara Horowitz",
        "description": "A non-fiction book by Sara Horowitz that provides practical advice and guidance for freelancers on starting and running a successful freelance business.",
        "Summary": "The Freelancers Bible is a non-fiction book by Sara Horowitz that provides practical advice and guidance for freelancers on starting and running a successful freelance business. The book covers a wide range of topics, including finding clients, setting rates, managing finances, and negotiating contracts.Horowitz also provides tips and advice on marketing, networking, and building a strong brand. Additionally, the book includes guidance on legal and tax issues, as well as strategies for managing work-life balance.The book is written in an accessible and engaging style, with real-world examples and case studies that illustrate the key principles and strategies. Whether you are just starting out as a freelancer or looking to grow your existing freelance business, The Freelancers Bible is an essential resource for anyone seeking to succeed in the freelance economy.Overall, the book provides a comprehensive and practical guide to the freelance lifestyle, offering valuable insights and advice on everything from finding clients to managing finances to achieving work-life balance. The Freelancers Bible is an essential resource for anyone considering a freelance career or looking to grow their existing freelance business.",
        "url": "https://m.media-amazon.com/images/I/61EIgV8G4vL._AC_UY327_FMwebp_QL65_.jpg"
    },

    {
        "title": "The Gig Economy",
        "author": "Diane Mulcahy",
        "description": "A non-fiction book by Diane Mulcahy that explores the rise of the gig economy and its impact on workers and businesses.",
        "Summary": "The Gig Economy by Diane Mulcahy is a non-fiction book that explores the rise of the gig economy and its impact on workers, businesses, and society. The book offers a detailed analysis of various types of gig work, including ridesharing, delivery services, and creative freelance work, and provides insights into the motivations and experiences of gig workers.Mulcahy argues that the gig economy represents a fundamental shift in the nature of work and offers both opportunities and challenges for workers, businesses, and society as a whole. She examines the impact of the gig economy on traditional jobs and industries, as well as the challenges of managing and regulating gig work.The Gig Economy provides a thought-provoking analysis of a major economic and social trend that is transforming the way we work and live. It explores the benefits and drawbacks of gig work for both workers and businesses, and provides guidance on how to succeed in the gig economy.Overall, The Gig Economy is a comprehensive and informative book that offers valuable insights into the changing nature of work and the challenges and opportunities of the gig economy. It is essential reading for anyone interested in the future of work and the evolving world of work platforms.",
        "url": "https://m.media-amazon.com/images/I/81KIjan5NmL._AC_UY327_FMwebp_QL65_.jpg"
    },

    {
        "title": "The Little Book of Common Sense Investing",
        "author": "John C. Bogle",
        "description": "A non-fiction book by John C. Bogle that promotes the principles of passive investing and argues against active stock picking and market timing.",
        "Summary": "The Little Book of Common Sense Investing by John C. Bogle is a non-fiction book that promotes the principles of passive investing and argues against active stock picking and market timing. The book is based on Bogle's decades of experience in the investment industry and explains how active management often results in high fees, poor returns, and unnecessary risk, while passive investing offers a simple and effective strategy for long-term wealth accumulation.    Bogle provides practical advice on how to build a diversified portfolio of low-cost index funds and emphasizes the importance of sticking to a long-term investment plan. He also argues that investors should focus on the long-term performance of the market as a whole, rather than trying to predict short-term market fluctuations or outperform the market through active stock picking or market timing.the Little Book of Common Sense Investing is a must-read for anyone looking to achieve financial success through passive investing strategies. It offers a straightforward and accessible guide to the principles of passive investing and provides practical advice on how to build a low-cost and diversified investment portfolio. Overall, it is an essential book for anyone interested in long-term wealth accumulation and financial security.",
        "url": "https://m.media-amazon.com/images/I/51wvE48u69L._SX351_BO1,204,203,200_.jpg"
    },
    {
        "title": "A Random Walk Down Wall Street",
        "author": "Burton Malkiel",
        "description": "A non-fiction book by Burton Malkiel that explores the history and theory of stock market investing.",
        "Summary": "A Random Walk Down Wall Street by Burton Malkiel is a non-fiction book that explores the history and theory of stock market investing. The book argues that stock market prices are largely unpredictable and that trying to outperform the market through stock picking or market timing is a fool's errand. Instead, Malkiel advocates for a passive investment strategy that involves investing in low-cost index funds and holding them for the long term.The book provides a comprehensive overview of various investment strategies, including technical analysis, fundamental analysis, and behavioral finance, and examines the pros and cons of each approach. Malkiel emphasizes the importance of diversification and provides practical advice on how to build a well-diversified portfolio of low-cost index funds.Overall, A Random Walk Down Wall Street is an essential read for anyone looking to gain a deeper understanding of the stock market and develop a successful investment strategy. The book is well-researched and provides a wealth of information on the history, theory, and practice of stock market investing. It is an accessible and engaging guide to the principles of passive investing and offers practical advice on how to build a successful investment portfolio.",
        "url": "https://m.media-amazon.com/images/I/51lhGlyhLcL._AC_UY327_FMwebp_QL65_.jpg"
    }
    ,
    {
        "title": "The Effective Executive:",
        "Author": "Peter F. Drucker",
        "descreption": "The Effective Executive is a management guidebook that provides advice on how to become a more effective leader and achieve better results in business. The book emphasizes the importance of setting priorities, managing time, and focusing on the most important tasks to maximize productivity.",
        "summary": "The book highlights the key skills and habits that effective executives need to have, such as setting clear goals, delegating responsibilities, and making effective decisions. The author argues that effective executives are those who focus on what they can do best and prioritize their time accordingly. The book also stresses the importance of continuous learning and self-improvement, as well as the need for effective communication with team members and stakeholders. Drucker presents a framework for decision-making that involves analyzing different options and choosing the one that aligns best with the organization's goals and values. He also emphasizes the need for effective teamwork and encourages executives to build a culture of trust and accountability within their organizations. The Effective Executive is a practical guide that provides actionable advice for executives looking to improve their leadership skills and drive results in their organizations. The book's main takeaway is that effective leadership is not about being busy or working harder, but rather about focusing on what really matters and taking purposeful action to achieve success.",
        "url": "https://m.media-amazon.com/images/I/81E0LsCapBL._AC_UY218_.jpg"
    },
    {
        "title": "High Output Management",
        "Author": "Andrew S. Grove",
        "descreption": "High Output Management is a management guidebook that provides insights into the principles and practices of effective management. The book emphasizes the importance of maximizing output and productivity through effective planning, organization, and communication.",
        "summary": "The book provides a framework for effective management that focuses on key principles such as goal setting, time management, and communication. The author emphasizes the importance of setting clear goals and objectives, and aligning them with the organization's mission and values. He also emphasizes the importance of effective communication, both within teams and with external stakeholders. The book provides practical advice on how to organize and structure work processes to maximize output and productivity, such as through the use of metrics and feedback loops. The author also discusses the role of leadership in driving innovation and change, and provides guidance on how to build a strong and effective team culture. The book is grounded in the author's experience as a former CEO of Intel and provides real-world examples and case studies to illustrate its principles. The main takeaway from the book is that effective management is about optimizing output and productivity through careful planning, organization, and communication, and that this requires a focus on continuous improvement and learning.",
        "url": "https://m.media-amazon.com/images/I/51IXfgjZNgL._SY291_BO1,204,203,200_QL40_FMwebp_.jpg"
    },
    {
        "title": "The Lean Startup",
        "Author": "Eric Ries",
        "descreption": "The Lean Startup is a business guidebook that offers a methodology for creating and managing startups in a more efficient and effective way. The book advocates for a lean approach to entrepreneurship, where entrepreneurs focus on validating their ideas through experimentation and feedback before scaling their businesses.",
        "summary": "The book introduces the concept of a Minimum Viable Product (MVP) and advocates for a build-measure-learn feedback loop, which involves creating a basic version of a product, measuring its performance, and using feedback to improve it. The author stresses the importance of testing assumptions and hypotheses through experimentation, rather than relying on intuition or guesswork. The book also emphasizes the need for a customer-centric approach, where entrepreneurs focus on creating value for their customers and understanding their needs and preferences. The Lean Startup offers practical advice on how to implement these principles in practice, such as through the use of agile development methodologies, rapid prototyping, and continuous iteration. The book also discusses the role of metrics and data in tracking progress and making decisions. The Lean Startup is a popular guidebook for entrepreneurs and has been influential in shaping the startup ecosystem. Its main takeaway is that startups should focus on creating value for customers in a lean and iterative way, and that this requires a willingness to experiment and learn from failures.",
        "url": "https://m.media-amazon.com/images/I/51T-sMqSMiL._SY291_BO1,204,203,200_QL40_FMwebp_.jpg"
    },
    {
        "title": "Zero to One",
        "Author": "Peter Thiel",
        "descreption": "Zero to One is a business guidebook that challenges entrepreneurs to think differently about innovation and creating new businesses. The book argues that true innovation involves creating something entirely new, rather than simply copying what already exists.",
        "summary": "The book argues that the key to success in business is creating something that is fundamentally new, rather than just copying what already exists. The author emphasizes the importance of having a clear and bold vision for the future, and being willing to take risks in pursuit of that vision. The book also stresses the importance of building a strong team and creating a culture that encourages creativity and innovation. The author provides practical advice on how to identify and pursue new business opportunities, such as by identifying secrets that others have overlooked or ignored. The book also discusses the role of technology and the importance of understanding how it can be used to create new products and services. The main takeaway from the book is that true innovation requires a willingness to take risks and think differently about the world, and that the most successful businesses are those that create something entirely new and unique.",
        "url": "https://m.media-amazon.com/images/I/41Rgxr-Yg3L._AC_UL400_.jpg"
    },
    {
        "title": "The Life-Changing Magic of Tidying Up",
        "Author": "Marie Kondo",
        "descreption": "The Life-Changing Magic of Tidying Up is a self-help guidebook that offers a unique approach to decluttering and organizing one's home. The book is based on the author's KonMari method, which emphasizes the importance of keeping only the items that bring joy and discarding the rest.",
        "summary": "The book offers a step-by-step guide to decluttering and organizing one's home, based on the author's KonMari method. The method involves a process of sorting items by category and then deciding which items to keep based on whether they bring joy or not. The book emphasizes the importance of treating one's belongings with respect and gratitude, and of creating a home environment that reflects one's values and personality. The author provides practical advice on how to organize clothes, books, papers, and other items, and stresses the importance of maintaining an organized home through daily habits and routines. The book also discusses the psychological benefits of decluttering and organizing one's home, such as reduced stress and increased focus. The main takeaway from the book is that tidying up is not just a chore, but a transformative process that can bring greater happiness and fulfillment into one's life.",
        "url": "https://m.media-amazon.com/images/I/41b6p4DrVFL._SY291_BO1,204,203,200_QL40_FMwebp_.jpg"
    }
    ,
    {
        "title": "Getting Things Done",
        "Author": "David Allen",
        "descreption": "Getting Things Done is a self-help guidebook that offers a productivity system for managing one's time and tasks. The book is based on the author's GTD methodology, which emphasizes the importance of capturing, clarifying, organizing, and reviewing one's commitments and responsibilities.",
        "summary": "The book offers a comprehensive system for managing one's time and tasks, based on the author's GTD methodology. The method involves a process of capturing all commitments and responsibilities, clarifying what needs to be done, organizing tasks by context and priority, and reviewing progress on a regular basis. The book emphasizes the importance of having a clear and trusted system for managing one's tasks, in order to reduce stress and increase productivity. The author provides practical advice on how to implement the GTD methodology, such as through the use of lists, calendars, and digital tools. The book also discusses the psychological benefits of being more productive, such as increased focus, creativity, and satisfaction. The main takeaway from the book is that effective time management requires a systematic approach that is grounded in reality, and that this requires a willingness to capture, clarify, organize, and review one's commitments and responsibilities on a regular basis.",
        "url": "https://m.media-amazon.com/images/I/41YJyWQCBZL._SY291_BO1,204,203,200_QL40_FMwebp_.jpg"
    },
    {
        "title": "Eat That Frog!",
        "Author": "Brian Tracy",
        "descreption": "Eat That Frog! is a self-help guidebook that offers practical strategies for overcoming procrastination and improving productivity. The book is based on the author's philosophy of tackling the most important tasks first, and avoiding distractions that can impede progress.",
        "summary": "The book offers practical strategies for overcoming procrastination and improving productivity, based on the author's philosophy of tackling the most important tasks first. The book emphasizes the importance of setting clear goals, prioritizing tasks based on their importance and urgency, and focusing on the most important tasks until they are completed. The author provides practical tips on how to avoid distractions, such as by turning off notifications and working in a quiet environment. The book also discusses the importance of developing good habits and routines, such as by scheduling regular breaks and setting aside time for reflection and planning. The main takeaway from the book is that effective time management requires a mindset of action, and that this involves taking action on the most important tasks, even if they are difficult or uncomfortable. The book provides a practical framework for achieving greater productivity, and offers insights and strategies that can be applied to any area of life.",
        "url": "https://m.media-amazon.com/images/I/81pDx9j+xQL._AC_UY218_.jpg"
    },
    {
        "title": "The One Thing",
        "Author": "Gary Keller and Jay Papasan",
        "descreption": "The One Thing is a self-help guidebook that offers a simple approach to productivity and success. The book is based on the idea that focusing on one thing at a time can help individuals achieve greater clarity, effectiveness, and satisfaction in their personal and professional lives.",
        "summary": "The book offers a simple approach to productivity and success, based on the idea that focusing on one thing at a time can help individuals achieve greater clarity, effectiveness, and satisfaction in their personal and professional lives. The book emphasizes the importance of identifying one's One Thing or the most important priority at any given moment, and then focusing all of one's attention and effort on that task. The authors provide practical tips on how to identify one's One Thing, such as by using the domino effect to identify the one task that will have the greatest impact on achieving one's goals. The book also discusses the importance of developing good habits and routines, such as by setting aside time for focused work and regular breaks. The authors provide examples from a range of fields, such as business, sports, and personal development, to illustrate the power of focusing on one thing at a time. The main takeaway from the book is that by simplifying one's approach to productivity and success, and focusing on one thing at a time, individuals can achieve greater clarity, effectiveness, and satisfaction in their personal and professional lives. The book offers practical insights and strategies that can be applied to any area of life, and is ideal for anyone seeking to improve their productivity and achieve their goals.",
        "url": "https://m.media-amazon.com/images/I/61am-jMDR7L._AC_UY218_.jpg"
    },
    {
        "title": "Good to Great",
        "Author": "Jim Collins",
        "descreption": "Good to Great is a business book that explores why some companies succeed in making the transition from good to great, while others fail to achieve this level of sustained excellence. The book is based on a study of 11 companies that made the transition, and highlights the key factors that contributed to their success",
        "summary": "The book offers insights into why some companies succeed in making the transition from good to great, while others fail to achieve this level of sustained excellence. The book is based on a study of 11 companies that made the transition, and identifies the key factors that contributed to their success. The author argues that the most successful companies share a number of common characteristics, such as a focus on disciplined people, disciplined thought, and disciplined action. The book also emphasizes the importance of finding and cultivating the right people, and creating a culture of discipline and excellence. The author provides practical tips on how to identify and nurture the key factors that contribute to success, such as by setting ambitious but achievable goals, and focusing on the long-term vision rather than short-term gains. The main takeaway from the book is that sustained excellence requires a commitment to disciplined action, and that this involves developing a culture of excellence that permeates every aspect of the organization. The book offers practical insights and strategies that can be applied to any organization, and is ideal for anyone seeking to achieve long-term success in their business or career.",
        "url": "https://m.media-amazon.com/images/I/71BfRFOKDiL._AC_UY218_.jpg"
    },
    {
        "title": "The Innovator's Dilemma ",
        "Author": " Clayton M. Christensen",
        "descreption": "The Innovator's Dilemma is a business book that explores why successful companies often fail to adapt to disruptive technologies and are overtaken by smaller, less established companies. The book provides a framework for understanding how and why this happens, and offers insights into how companies can overcome the innovator's dilemma and maintain their competitive edge.",
        "summary": "The book offers insights into why successful companies often fail to adapt to disruptive technologies and are overtaken by smaller, less established companies. The author argues that the very factors that made these companies successful in the first place, such as a focus on improving existing products and services and serving their existing customers, can make it difficult for them to respond to disruptive technologies that require a different set of skills and capabilities. The book provides a framework for understanding how and why this happens, and offers insights into how companies can overcome the innovator's dilemma and maintain their competitive edge. The author provides practical tips on how to identify disruptive technologies and respond to them, such as by creating separate divisions or subsidiaries to explore new technologies and markets, and by focusing on customer needs rather than product features. The main takeaway from the book is that companies need to be proactive in identifying and responding to disruptive technologies, and that this requires a willingness to experiment and take risks. The book offers practical insights and strategies that can be applied to any industry, and is ideal for anyone seeking to stay ahead of the curve and maintain their competitive edge in a rapidly changing marketplace.",
        "url": "https://m.media-amazon.com/images/I/618BdBwK5ML._AC_UY218_.jpg"
    },
        {
            "title":"The Effective Executive:",
            "Author":"Peter F. Drucker",
            "descreption":"The Effective Executive is a Management guidebook that provides advice on how to become a more effective leader and achieve better results in business. The book emphasizes the importance of setting priorities, managing time, and focusing on the most important tasks to maximize Productivity.",
            "summary":"The book highlights the key skills and habits that effective executives need to have, such as setting clear goals, delegating responsibilities, and making effective decisions. The author argues that effective executives are those who focus on what they can do best and prioritize their time accordingly. The book also stresses the importance of continuous learning and self-improvement, as well as the need for effective communication with team members and stakeholders. Drucker presents a framework for decision-making that involves analyzing different options and choosing the one that aligns best with the Organization's goals and values. He also emphasizes the need for effective teamwork and encourages executives to build a culture of trust and accountability within their Organizations. The Effective Executive is a practical guide that provides actionable advice for executives looking to improve their Leadership skills and drive results in their Organizations. The book's main takeaway is that effective Leadership is not about being busy or working harder, but rather about focusing on what really matters and taking purposeful action to achieve success.",
            "url":"https://m.media-amazon.com/images/I/81E0LsCapBL._AC_UY218_.jpg"
        },
        {
            "title":"High Output Management",
            "Author":"Andrew S. Grove",
            "descreption":"High Output Management is a Management guidebook that provides insights into the principles and practices of effective Management. The book emphasizes the importance of maximizing output and Productivity through effective planning, Organization, and communication.",
            "summary":"The book provides a framework for effective Management that focuses on key principles such as goal setting, time Management, and communication. The author emphasizes the importance of setting clear goals and objectives, and aligning them with the Organization's mission and values. He also emphasizes the importance of effective communication, both within teams and with external stakeholders. The book provides practical advice on how to organize and structure work processes to maximize output and Productivity, such as through the use of metrics and feedback loops. The author also discusses the role of Leadership in driving innovation and change, and provides guidance on how to build a strong and effective team culture. The book is grounded in the author's experience as a former CEO of Intel and provides real-world examples and case studies to illustrate its principles. The main takeaway from the book is that effective Management is about optimizing output and Productivity through careful planning, Organization, and communication, and that this requires a focus on continuous improvement and learning.",
            "url":"https://m.media-amazon.com/images/I/51IXfgjZNgL._SY291_BO1,204,203,200_QL40_FMwebp_.jpg"
        },
        {
            "title":"The Lean Startup",
            "Author":"Eric Ries",
            "descreption":"The Lean Startup is a business guidebook that offers a methodology for creating and managing startups in a more efficient and effective way. The book advocates for a lean approach to Entrepreneurship, where entrepreneurs focus on validating their ideas through experimentation and feedback before scaling their businesses.",
            "summary":"The book introduces the concept of a Minimum Viable Product (MVP) and advocates for a build-measure-learn feedback loop, which involves creating a basic version of a product, measuring its performance, and using feedback to improve it. The author stresses the importance of testing assumptions and hypotheses through experimentation, rather than relying on intuition or guesswork. The book also emphasizes the need for a customer-centric approach, where entrepreneurs focus on creating value for their customers and understanding their needs and preferences. The Lean Startup offers practical advice on how to implement these principles in practice, such as through the use of agile development methodologies, rapid prototyping, and continuous iteration. The book also discusses the role of metrics and data in tracking progress and making decisions. The Lean Startup is a popular guidebook for entrepreneurs and has been influential in shaping the startup ecosystem. Its main takeaway is that startups should focus on creating value for customers in a lean and iterative way, and that this requires a willingness to experiment and learn from failures.",
            "url":"https://m.media-amazon.com/images/I/51T-sMqSMiL._SY291_BO1,204,203,200_QL40_FMwebp_.jpg"
        },
        {
            "title":"Zero to One",
            "Author":"Peter Thiel",
            "descreption":"Zero to One is a business guidebook that challenges entrepreneurs to think differently about innovation and creating new businesses. The book argues that true innovation involves creating something entirely new, rather than simply copying what already exists.",
            "summary":"The book argues that the key to success in business is creating something that is fundamentally new, rather than just copying what already exists. The author emphasizes the importance of having a clear and bold vision for the future, and being willing to take risks in pursuit of that vision. The book also stresses the importance of building a strong team and creating a culture that encourages creativity and innovation. The author provides practical advice on how to identify and pursue new business opportunities, such as by identifying secrets that others have overlooked or ignored. The book also discusses the role of Technology and the importance of understanding how it can be used to create new products and services. The main takeaway from the book is that true innovation requires a willingness to take risks and think differently about the world, and that the most successful businesses are those that create something entirely new and unique.",
            "url":"https://m.media-amazon.com/images/I/41Rgxr-Yg3L._AC_UL400_.jpg"
        },
       {
            "title":"The Life Changing Magic of Tidying Up",
            "Author":"Marie Kondo",
            "descreption":"The Life Changing Magic of Tidying Up is a SelfHelp guidebook that offers a unique approach to decluttering and organizing one's home. The book is based on the author's KonMari method, which emphasizes the importance of keeping only the items that bring joy and discarding the rest.",
            "summary":"The book offers a step-by-step guide to decluttering and organizing one's home, based on the author's KonMari method. The method involves a process of sorting items by category and then deciding which items to keep based on whether they bring joy or not. The book emphasizes the importance of treating one's belongings with respect and gratitude, and of creating a home environment that reflects one's values and personality. The author provides practical advice on how to organize clothes, books, papers, and other items, and stresses the importance of maintaining an organized home through daily habits and routines. The book also discusses the psychological benefits of decluttering and organizing one's home, such as reduced stress and increased focus. The main takeaway from the book is that tidying up is not just a chore, but a transformative process that can bring greater happiness and fulfillment into one's life.",
            "url":"https://m.media-amazon.com/images/I/41b6p4DrVFL._SY291_BO1,204,203,200_QL40_FMwebp_.jpg"
        }
        ,
        {
            "title":"Getting Things Done",
            "Author":"David Allen",
            "descreption":"Getting Things Done is a SelfHelp guidebook that offers a Productivity system for managing one's time and tasks. The book is based on the author's GTD methodology, which emphasizes the importance of capturing, clarifying, organizing, and reviewing one's commitments and responsibilities.",
            "summary":"The book offers a comprehensive system for managing one's time and tasks, based on the author's GTD methodology. The method involves a process of capturing all commitments and responsibilities, clarifying what needs to be done, organizing tasks by context and priority, and reviewing progress on a regular basis. The book emphasizes the importance of having a clear and trusted system for managing one's tasks, in order to reduce stress and increase Productivity. The author provides practical advice on how to implement the GTD methodology, such as through the use of lists, calendars, and digital tools. The book also discusses the psychological benefits of being more productive, such as increased focus, creativity, and satisfaction. The main takeaway from the book is that effective time Management requires a systematic approach that is grounded in reality, and that this requires a willingness to capture, clarify, organize, and review one's commitments and responsibilities on a regular basis.",
            "url":"https://m.media-amazon.com/images/I/41YJyWQCBZL._SY291_BO1,204,203,200_QL40_FMwebp_.jpg"
        },
        {
            "title":"Eat That Frog!",
            "Author":"Brian Tracy",
            "descreption":"Eat That Frog! is a SelfHelp guidebook that offers practical strategies for overcoming procrastination and improving Productivity. The book is based on the author's philosophy of tackling the most important tasks first, and avoiding distractions that can impede progress.",
            "summary":"The book offers practical strategies for overcoming procrastination and improving Productivity, based on the author's philosophy of tackling the most important tasks first. The book emphasizes the importance of setting clear goals, prioritizing tasks based on their importance and urgency, and focusing on the most important tasks until they are completed. The author provides practical tips on how to avoid distractions, such as by turning off notifications and working in a quiet environment. The book also discusses the importance of developing good habits and routines, such as by scheduling regular breaks and setting aside time for reflection and planning. The main takeaway from the book is that effective time Management requires a mindset of action, and that this involves taking action on the most important tasks, even if they are difficult or uncomfortable. The book provides a practical framework for achieving greater Productivity, and offers insights and strategies that can be applied to any area of life.",
            "url":"https://m.media-amazon.com/images/I/81pDx9j+xQL._AC_UY218_.jpg"
        },
        {
            "title":"The One Thing",
            "Author":"Gary Keller and Jay Papasan",
            "descreption":"The One Thing is a SelfHelp guidebook that offers a simple approach to Productivity and success. The book is based on the idea that focusing on one thing at a time can help individuals achieve greater clarity, effectiveness, and satisfaction in their personal and professional lives.",
            "summary":"The book offers a simple approach to Productivity and success, based on the idea that focusing on one thing at a time can help individuals achieve greater clarity, effectiveness, and satisfaction in their personal and professional lives. The book emphasizes the importance of identifying one's One Thing or the most important priority at any given moment, and then focusing all of one's attention and effort on that task. The authors provide practical tips on how to identify one's One Thing, such as by using the domino effect to identify the one task that will have the greatest impact on achieving one's goals. The book also discusses the importance of developing good habits and routines, such as by setting aside time for focused work and regular breaks. The authors provide examples from a range of fields, such as business, sports, and personal development, to illustrate the power of focusing on one thing at a time. The main takeaway from the book is that by simplifying one's approach to Productivity and success, and focusing on one thing at a time, individuals can achieve greater clarity, effectiveness, and satisfaction in their personal and professional lives. The book offers practical insights and strategies that can be applied to any area of life, and is ideal for anyone seeking to improve their Productivity and achieve their goals.",
            "url":"https://m.media-amazon.com/images/I/61am-jMDR7L._AC_UY218_.jpg"
        },
        {
            "title":"Good to Great",
            "Author":"Jim Collins",
            "descreption":"Good to Great is a business book that explores why some companies succeed in making the transition from good to great, while others fail to achieve this level of sustained excellence. The book is based on a study of 11 companies that made the transition, and highlights the key factors that contributed to their success",
            "summary":"The book offers insights into why some companies succeed in making the transition from good to great, while others fail to achieve this level of sustained excellence. The book is based on a study of 11 companies that made the transition, and identifies the key factors that contributed to their success. The author argues that the most successful companies share a number of common characteristics, such as a focus on disciplined people, disciplined thought, and disciplined action. The book also emphasizes the importance of finding and cultivating the right people, and creating a culture of discipline and excellence. The author provides practical tips on how to identify and nurture the key factors that contribute to success, such as by setting ambitious but achievable goals, and focusing on the long-term vision rather than short-term gains. The main takeaway from the book is that sustained excellence requires a commitment to disciplined action, and that this involves developing a culture of excellence that permeates every aspect of the Organization. The book offers practical insights and strategies that can be applied to any Organization, and is ideal for anyone seeking to achieve long-term success in their business or Career.",
            "url":"https://m.media-amazon.com/images/I/71BfRFOKDiL._AC_UY218_.jpg"
        },
        {
            "title":"The Innovators Dilemma ",
            "Author":" Clayton M. Christensen",
            "descreption":"The Innovators Dilemma is a business book that explores why successful companies often fail to adapt to disruptive technologies and are overtaken by smaller, less established companies. The book provides a framework for understanding how and why this happens, and offers insights into how companies can overcome The Innovators Dilemma and maintain their competitive edge.",
            "summary":"The book offers insights into why successful companies often fail to adapt to disruptive technologies and are overtaken by smaller, less established companies. The author argues that the very factors that made these companies successful in the first place, such as a focus on improving existing products and services and serving their existing customers, can make it difficult for them to respond to disruptive technologies that require a different set of skills and capabilities. The book provides a framework for understanding how and why this happens, and offers insights into how companies can overcome The Innovators Dilemma and maintain their competitive edge. The author provides practical tips on how to identify disruptive technologies and respond to them, such as by creating separate divisions or subsidiaries to explore new technologies and markets, and by focusing on customer needs rather than product features. The main takeaway from the book is that companies need to be proactive in identifying and responding to disruptive technologies, and that this requires a willingness to experiment and take risks. The book offers practical insights and strategies that can be applied to any industry, and is ideal for anyone seeking to stay ahead of the curve and maintain their competitive edge in a rapidly changing marketplace.",
            "url":"https://m.media-amazon.com/images/I/618BdBwK5ML._AC_UY218_.jpg"
        },
        {
            "title" : "Sapiens A Brief History of Humankind",
            "author" : "Yuval Noah Harari",
            "description":"Sapiens A Brief History of Humankind is a captivating and thought-provoking account of the History of Homo sapiens, from our emergence as a species in Africa to our present-day dominance of the planet. The book explores how Homo sapiens has been able to thrive and dominate other species, even as we have caused unprecedented destruction to the environment and other living beings. With a unique blend of science, History, and philosophy, Harari challenges many of our assumptions about what it means to be human.",
            "Summary":"In Sapiens, Harari takes readers on a journey through the History of humankind, exploring how we evolved from a species of hunter-gatherers to become the dominant force on the planet. He begins by discussing the cognitive revolution, which he argues allowed Homo sapiens to develop language and complex societies. He then explores the agricultural revolution and the rise of empires, examining how these developments shaped human History. Harari also delves into the scientific and technological revolutions that have taken place over the last few centuries, arguing that they have given us unprecedented power over the natural world. Throughout the book, Harari challenges many of our assumptions about human nature, questioning whether we are truly free, whether we are capable of making ethical decisions, and whether we are ultimately any happier than our hunter-gatherer ancestors. Sapiens is a deeply thought-provoking book that forces readers to confront many uncomfortable truths about the History of our species.",
            "url":"https://m.media-amazon.com/images/I/81tPEe0egBL._AC_UY218_.jpg"

        },
        {
            "title":"The Guns of August",
            "author":"Barbara W. Tuchman",
            "description":"The Guns of August is a historical account of the first month of World War I. It follows the events that led to the war and the major players involved. Tuchman's vivid and detailed writing style brings the events to life.",
            "Summary":"The Guns of August is a gripping account of the events that led to the outbreak of World War I. Barbara W. Tuchman chronicles the month of August 1914, starting with the assassination of Archduke Franz Ferdinand of Austria-Hungary and his wife by a Serbian nationalist on June 28th, 1914. Tuchman explains the complex web of alliances and political tensions that existed in Europe at the time, and how this led to a rapid escalation of events after the assassination. She details the actions of key players such as Kaiser Wilhelm II, Tsar Nicholas II, and Winston Churchill, and how their decisions impacted the course of the war.Tuchmans writing style is vivid and engaging, making the events feel real and immediate. She covers the major battles and campaigns of the war's first month, including the Battle of the Frontiers and the Battle of Tannenberg. She also discusses the naval blockade of Germany, the race to the sea, and the first use of chemical weapons. Tuchman's analysis of the military tactics and strategies employed by the various nations is insightful and informative.The Guns of August also explores the Social and cultural impact of the war. Tuchman discusses the role of propaganda and censorship in shaping public opinion, and the impact of the war on civilians. She also explores the changing role of women in society as a result of the war.Overall, The Guns of August is a powerful and enlightening account of a pivotal moment in world History. Tuchman's meticulous research and engaging writing style make it an accessible and compelling read for anyone interested in the causes and consequences of World War I.",
            "url":"https://m.media-amazon.com/images/I/81vP-pwZcUL._AC_UY218_.jpg"
        },
        {
            "title":"Leaders Eat Last",
            "author":"Simon Sinek",
            "description":"Leaders Eat Last is a book on Leadership and team-building that explores the biological and psychological reasons behind why some teams succeed while others fail. The author argues that leaders who prioritize the well-being and safety of their team members create a culture of trust and cooperation that leads to long-term success. The book offers practical advice for building a strong, cohesive team and creating a work environment that fosters loyalty and Productivity.",
            "Summary":"Leaders Eat Last is a book that challenges conventional ideas of Leadership by emphasizing the importance of creating a culture of trust, cooperation, and shared purpose. Drawing on insights from neuroscience, anthropology, and business, author Simon Sinek argues that effective leaders prioritize the well-being and safety of their team members, creating an environment in which individuals feel valued, supported, and motivated to work together towards a common goal. By contrast, leaders who prioritize their own success or personal gain at the expense of their team members' well-being risk creating a toxic culture of fear and mistrust that undermines Productivity and long-term success.Throughout the book, Sinek offers a range of case studies and examples to illustrate his points, from military leaders who prioritize the safety of their soldiers to successful companies that prioritize the well-being and satisfaction of their employees. He also draws on insights from evolutionary biology to argue that humans are wired to function best in cooperative, supportive communities, and that leaders who understand and leverage these instincts can create highly effective teams.The book offers practical advice for leaders who want to build a strong, cohesive team, including tips for fostering open communication, creating a sense of shared purpose, and building a culture of trust and accountability. It also explores the role of Leadership in promoting employee well-being and work-life balance, arguing that leaders who prioritize the mental and physical Healthy of their team members are more likely to create a sustainable and successful Organization in the long run.Overall, Leaders Eat Last is a thought-provoking and engaging book that challenges conventional ideas of Leadership and offers practical advice for building a strong, productive team. It is a must-read for anyone interested in the science of Leadership, Organizational Psychology, or team-building.",
            "url":"https://m.media-amazon.com/images/I/71TckhiE8DL._AC_UY218_.jpg"
        },
        {
            "title": "The 21 Irrefutable Laws of Leadership",
            "author": "John C. Maxwell",
            "description": "his book is a comprehensive guide to Leadership principles based on the author's 30 years of experience in Leadership roles and observations of successful leaders.The book presents 21 laws of Leadership that can be applied to any Leadership situation, including leading oneself, leading others, and leading Organizations.Each law is illustrated with real-world examples, insights, and practical applications.",
            "Summary": "The 21 Irrefutable Laws of Leadership is a powerful and comprehensive guide to Leadership principles. Written by renowned Leadership expert John C. Maxwell, this book presents 21 timeless laws of Leadership that can be applied to any Leadership situation. Each law is presented in a clear and concise manner, with real-world examples and practical applications that make it easy to understand and implement.The first part of the book focuses on the laws that leaders must apply to themselves, including the law of the lid, the law of influence, and the law of priorities. The second part of the book covers the laws that leaders must apply to others, including the law of respect, the law of intuition, and the law of the inner circle. Finally, the third part of the book covers the laws that leaders must apply to their Organizations, including the law of momentum, the law of sacrifice, and the law of legacy.Throughout the book, Maxwell emphasizes the importance of character, Relationships, and values in effective Leadership. He also emphasizes the need for leaders to constantly learn and grow, and to develop their Leadership skills through practice, feedback, and reflection. The book is full of insights, anecdotes, and practical tips that will help readers become more effective leaders and build successful Organizations. Overall, The 21 Irrefutable Laws of Leadership is an essential resource for anyone who wants to improve their Leadership skills and achieve success in any Leadership role.",
            "url": "https://m.media-amazon.com/images/I/71ZqXN1r5UL._AC_UY218_.jpg"
        },
        {
                "title":"Code Complete",
                "author":"Steve McConnell",
                "description":"Code Complete is a comprehensive guide to software construction and Programming. It covers practical and theoretical concepts related to software development, such as design principles, testing strategies, and code maintenance. The book presents a wide range of topics, from basic coding techniques to complex algorithms and data structures.",
                "Summary":"Code Complete is a must-read book for software developers who want to improve their Programming skills and produce high-quality code. The book is divided into three parts. Part 1 covers the basics of software construction, such as coding standards, debugging techniques, and testing strategies. Part 2 explores advanced Programming concepts, including data structures, algorithms, and object-oriented design. Part 3 focuses on code maintenance, offering tips on how to manage code, refactor it, and prevent errors.The author provides clear explanations of Programming concepts, using examples and illustrations to help readers understand complex topics. The book also includes case studies and real-world examples, which demonstrate how to apply the concepts covered in the book to practical situations.Code Complete emphasizes the importance of writing clean and readable code, which is easy to understand and maintain. The book presents guidelines and best practices for code development, such as commenting, naming conventions, and code formatting. It also provides advice on how to work in a team and how to manage projects effectively.Overall, Code Complete is an essential resource for software developers who want to write better code, improve their Programming skills, and produce high-quality software. The book covers a wide range of topics related to software construction and Programming, and provides practical and theoretical insights into software development. The book is well-organized, easy to read, and offers a wealth of knowledge and advice for developers of all levels.",
                "url":"https://m.media-amazon.com/images/I/41qnjXIApSL._AC_UY218_.jpg"
        },

        {
            "title": "Clean Code",
            "author": "Robert C. Martin",
            "description": "Clean Code  is a comprehensive guide to writing code that is easy to read, maintain, and understand. The author, Robert C. Martin, draws on his extensive experience as a software developer to provide practical advice and real-world examples of clean code. The book covers a wide range of topics, including naming, functions, comments, formatting, and error handling, and provides specific guidelines and examples for each. The author also discusses the importance of writing clean code and the impact it can have on the success of a software project.",
            "Summary": "Clean Code is a must-read for any software developer who wants to improve the quality of their code. The book provides practical advice and real-world examples of how to write code that is easy to read, maintain, and understand. The author emphasizes the importance of writing clean code and provides specific guidelines and examples for achieving this goal. The book covers a wide range of topics, including naming, functions, comments, formatting, and error handling, and provides specific guidelines and examples for each. Overall, Clean Code is an excellent resource for any software developer who wants to improve the quality of their code and become a better programmer.",
            "url": "https://m.media-amazon.com/images/I/41xShlnTZTL._AC_UY218_.jpg"
        },

        {
            "title": "Cybersecurity for Beginners",
            "author": "Raef Meeuwisse",
            "description": "Cybersecurity for Beginners  is a practical guide aimed at helping individuals protect themselves and their online activities from cyber threats. The book starts with an introduction to Cybersecurity, explaining why it is important in our digital age and the consequences of ignoring it. It then moves on to discuss the five steps to improve one's Cybersecurity: understanding the risks, securing personal devices, protecting online accounts, using safe browsing practices, and staying aware of threats.",
            "Summary": "is a comprehensive guide for individuals who are new to the world of Cybersecurity. Written by Cybersecurity expert Raef Meeuwisse, the book provides an overview of the fundamental concepts, principles, and techniques of Cybersecurity. The book is divided into four parts, each covering a different aspect of Cybersecurity.Part 1 provides an introduction to Cybersecurity and explains why it is important. The author describes the different types of threats that individuals and Organizations face in today's digital world. He also discusses the potential consequences of a cyber attack and the steps that can be taken to mitigate these risks.Part 2 focuses on the technical aspects of Cybersecurity. The author explains the different types of security controls that can be implemented to protect computer systems and networks. He also provides an overview of encryption, firewalls, and other technologies used in Cybersecurity.Part 3 covers the human aspects of Cybersecurity. The author describes the importance of user awareness and education in preventing cyber attacks. He also discusses the role of employees, contractors, and third-party vendors in maintaining Cybersecurity.Part 4 concludes the book by providing guidance on how to create a Cybersecurity strategy. The author explains the importance of conducting risk assessments and developing a comprehensive security plan. He also provides tips on how to select and implement Cybersecurity technologies and how to measure the effectiveness of a security program.Overall, Cybersecurity for Beginners is an excellent resource for anyone who wants to learn about Cybersecurity. The book provides a comprehensive overview of the fundamental concepts and techniques of Cybersecurity, making it an ideal starting point for individuals who are new to the field.",
            "url": "https://m.media-amazon.com/images/I/81phxgnNP8L._AC_UY218_.jpg"
        },

        {
            "title": "The Art of Deception",
            "author": "Kevin D. Mitnick",
            "description": "The Art of Deception is a book that explores the various techniques used by hackers to gain unauthorized access to computer systems and networks. Written by a former hacker, the book offers insights into the Psychology of deception and how it can be used to manipulate individuals into revealing sensitive information.",
            "Summary": " The Art of Deception is a book that provides readers with an in-depth look at the Psychology of deception and how it is used by hackers to gain access to computer systems and networks. Written by Kevin D. Mitnick, a former hacker turned security consultant, the book is divided into several sections that cover topics such as the art of deception, Social engineering, pretexting, phishing, and more.The book begins by exploring the different forms of deception and how they are used in everyday life. Mitnick provides numerous examples of how people are deceived on a daily basis, and how these techniques can be used to gain access to sensitive information. He then delves into the world of Social engineering and pretexting, showing readers how these techniques can be used to manipulate individuals into revealing confidential information.Throughout the book, Mitnick provides numerous case studies and real-world examples to illustrate his points. He also provides practical advice on how to protect oneself from deception and Social engineering attacks, including tips on how to identify and avoid phishing scams, how to create strong passwords, and how to protect sensitive information.Overall, The Art of Deception is a valuable resource for anyone who wants to learn more about the world of hacking and cyber security. Mitnick's insights into the Psychology of deception and his practical advice on how to protect oneself from attacks make this book a must-read for anyone who uses computers or the internet on a regular basis.",
            "url": "https://m.media-amazon.com/images/I/717QPvB9bVL._AC_UY218_.jpg"
        },
        {
            "title": "Thinking Fast and Slow",
            "author": " Daniel Kahneman",
            "description": "Thinking Fast and Slow is a non-fiction book by Nobel Prize-winning economist Daniel Kahneman. It presents a dual-process theory of the brain, which suggests that human thought operates on two levels: System 1, which is fast, automatic, and intuitive, and System 2, which is slow, deliberate, and analytical. Through a series of experiments and examples, Kahneman explains how these two systems work together and influence our decision-making processes.",
            "Summary": "The book is a tour of the mind and how it works, exploring the two systems that drive the way we think: System 1 is fast, intuitive, and emotional; System 2 is slower, more deliberative, and more logical. The book provides insight into the biases and heuristics that are embedded in our thinking and decision-making processes, leading us to make mistakes and errors of judgment.Kahneman presents a wealth of fascinating research that reveals how we make decisions, including the role of intuition and emotion, the effects of framing and anchoring, and the ways in which our cognitive biases can lead us astray. The book also explores the concept of prospect theory, which shows how people make choices based on the potential value of losses and gains rather than the final outcome.Overall, Thinking Fast and Slow is a thought-provoking book that challenges readers to think more deeply about their own thinking processes and how they can improve their decision-making skills. It offers practical advice and insights that can be applied to a wide range of fields, from business to politics to everyday life.",
            "url" : "https://m.media-amazon.com/images/I/71CPEr8zrWL._AC_UY218_.jpg"
        },

        {
            "title": "Influence The Psychology of Persuasion",
            "author": "Robert Cialdini",
            "description": "Influence The Psychology of Persuasion is a book written by Robert Cialdini, a professor of Psychology and marketing. The book explores the Psychology behind why people say yes and provides practical strategies for influencing others.",
            "Summary": "The book outlines six principles of influence: reciprocity, commitment and consistency, Social proof, authority, liking, and scarcity. Cialdini explains how these principles are used by marketers, salespeople, and others to persuade and influence others. He also provides real-life examples and case studies to illustrate the principles in action. The book is written in an engaging and accessible style, making it a popular read for anyone interested in the Psychology of persuasion. The insights and strategies provided in the book are applicable to a wide range of contexts, from marketing and sales to personal Relationships and Social interactions.",
            "url": "https://m.media-amazon.com/images/I/71JbZ0V06zL._AC_UY218_.jpg",
        },

        {
            "title": "The Master Algorithm",
            "author": "Pedro Domingos",
            "description": "The Master Algorithm is a book by Pedro Domingos that explores the idea of creating a single algorithm that can learn anything. The book covers topics such as machine learning, artificial intelligence, and data science, and provides an in-depth look at the field of data analytics.",
            "Summary": "The Master Algorithm argues that the key to unlocking the full potential of artificial intelligence lies in developing a single algorithm that can learn anything. The book provides an overview of the five main schools of machine learning and explores the potential of combining these approaches into a single, unified algorithm. Domingos explains how this could lead to a breakthrough in the field of artificial intelligence and transform the way we live and work. The book is a fascinating read for anyone interested in data science, machine learning, or artificial intelligence and provides a thought-provoking look at the future of Technology.",
            "url": "https://m.media-amazon.com/images/I/919toCZqMQS._AC_UY218_.jpg",
        },
        {
            "title":"Superintelligence Paths Dangers Strategies",
            "author":"Nick Bostrom",
            "description":" is a book by Nick Bostrom that explores the potential consequences of creating an artificial superintelligence (ASI) and the strategies that could be used to control it. The book discusses the definition of intelligence and how it can be measured, as well as the types of intelligence and how they are related. It also examines the History of artificial intelligence (AI) and the factors that could lead to the creation of an ASI.",
            "Summary":"The book Superintelligence Paths Dangers Strategies presents a thought-provoking analysis of the potential risks associated with creating an artificial superintelligence. The author, Nick Bostrom, argues that the creation of an ASI could have catastrophic consequences for humanity if it is not controlled properly. He suggests that the development of an ASI could lead to an intelligence explosion, in which the ASI rapidly becomes much smarter than humans and is able to improve its own intelligence at an exponential rate. This could lead to the ASI taking control of the world and causing harm to humans.To prevent this, Bostrom proposes several strategies for controlling an ASI, including creating a friendly ASI that is programmed to value human well-being and safety above all else, and creating a system of checks and balances to ensure that the ASI does not act against human interests. The book also discusses the potential benefits of creating an ASI, such as the ability to solve complex problems and improve human quality of life.Overall, Superintelligence Paths Dangers Strategies is a thought-provoking book that raises important questions about the risks and benefits of creating an ASI. It is a must-read for anyone interested in the field of AI and its potential impact on society.",
            "url":"https://m.media-amazon.com/images/I/81BkPuq9CYL._AC_UY218_.jpg"
        },

]


def ES_API(facts=[]):
    titlesList = []
    result = []


    if not facts :
        return result



    fc = lg.FolKB()



    for rule in rules :
        fc.tell(lg.expr(rule))

    for fact in facts:
        fc.tell(lg.expr(fact))


    tmp = lg.fol_fc_ask(fc,lg.expr("Book(y,User)"))
    # print("lkdjaspodjaosjdposajd ", len(Books_Data))
    print(len(list(tmp)))
    # for value in tmp.values():
    #     if str(value) not in Themes :
    #         titlesList.append(str(value).replace('_',' '))
    #
    # print("I Was here" , titlesList)
    # for title in titlesList:
    #     print("This is the title : ", title)
    #     for book in Books_Data:
    #         if book['title'] == title:
    #             print("I Was here")
    #             result.append(book)

    return result


@app.route("/")
def Recomnnedation():
    context = {}
    # we get the facts from the http payload
    facts  = request.data
    data = ES_API(["MakeMoney(User)","Productivity(User)","Career(User)","Healthy(User)"])
    print("This is Data : ", data)
    context = {"data":data}
    print(len(data))


    return jsonify(context), 200


if __name__ == "__main__":
    app.run(port=8080)
    # print(len(data))





