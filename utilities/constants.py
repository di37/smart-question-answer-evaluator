import os
from dotenv import load_dotenv

_ = load_dotenv()

MODEL_NAME = "gemini-1.5-pro-exp-0827"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Expanded set of questions and answers
QA_PAIRS = [
    {
        "question": "Explain the process of photosynthesis and its importance for life on Earth.",
        "answer": "Photosynthesis is the process by which plants and other organisms convert light energy into chemical energy. It involves absorbing sunlight, water, and carbon dioxide to produce glucose and oxygen. This process is crucial for life on Earth as it provides oxygen for respiration and forms the base of most food chains.",
    },
    {
        "question": "Describe the impact of the Industrial Revolution on society and the economy.",
        "answer": "The Industrial Revolution, which began in the late 18th century, marked a major turning point in history. It led to the transition from hand production methods to machines, new chemical manufacturing and iron production processes, improved efficiency of water power, the increasing use of steam power, and the development of machine tools. This revolution had profound effects on society, including urbanization, improved living standards, and the rise of the working and middle classes. Economically, it led to the creation of factories, increased productivity, and the growth of international trade.",
    },
    {
        "question": "What are the main causes and effects of climate change?",
        "answer": "Climate change is primarily caused by human activities that release greenhouse gases into the atmosphere, such as burning fossil fuels, deforestation, and industrial processes. The main effects include rising global temperatures, melting ice caps and glaciers, sea level rise, more frequent and severe weather events, changes in precipitation patterns, and impacts on biodiversity and ecosystems. These changes have far-reaching consequences for human societies, including threats to food and water security, health risks, and economic disruptions.",
    },
    {
        "question": "Explain the concept of supply and demand in economics.",
        "answer": "Supply and demand is a fundamental concept in economics that describes how the price and quantity of a good or service in a market are related and how that relationship changes in response to buyer and seller behavior. The law of demand states that, all else being equal, as the price of a product increases, fewer people will demand that product. The law of supply states that, all else being equal, as the price of a product increases, the quantity supplied of that product will increase. The intersection of these two forces determines the market equilibrium price and quantity.",
    },
    {
        "question": "Describe the structure and function of DNA in living organisms.",
        "answer": "DNA (Deoxyribonucleic acid) is a molecule that carries the genetic instructions for the development, functioning, growth, and reproduction of all known living organisms. It consists of two strands coiled around each other in a double helix structure. Each strand is composed of a sequence of four nucleotide bases: adenine (A), guanine (G), cytosine (C), and thymine (T). The sequence of these bases determines the genetic information. DNA replicates itself during cell division and is transcribed into RNA, which is then translated into proteins, the building blocks of life.",
    },
    {
        "question": "What were the main causes and consequences of World War II?",
        "answer": "World War II (1939-1945) had multiple causes, including the harsh conditions imposed on Germany by the Treaty of Versailles after World War I, the rise of fascism in Europe, expansionist policies of Nazi Germany and Imperial Japan, and the failure of the League of Nations to prevent conflicts. The war resulted in massive loss of life, the Holocaust, the use of atomic weapons, the decline of European colonial empires, the rise of the United States and Soviet Union as superpowers, and the formation of the United Nations. It reshaped global politics and led to significant technological and social changes.",
    },
    {
        "question": "Explain the theory of evolution by natural selection.",
        "answer": "The theory of evolution by natural selection, proposed by Charles Darwin, explains how species change over time. It states that organisms with heritable traits that are beneficial for survival and reproduction are more likely to pass these traits to their offspring. Over many generations, this process can result in populations that are better adapted to their environments and can lead to the formation of new species. The theory is supported by evidence from fossils, comparative anatomy, embryology, molecular biology, and direct observation of evolutionary changes.",
    },
    {
        "question": "Describe the major features and importance of the U.S. Constitution.",
        "answer": "The U.S. Constitution is the supreme law of the United States, providing the framework for the organization of the federal government and outlining fundamental rights of American citizens. Key features include the separation of powers among three branches of government (executive, legislative, and judicial), a system of checks and balances, federalism (division of power between federal and state governments), and the Bill of Rights. The Constitution has been crucial in establishing and maintaining a stable democratic system, protecting individual liberties, and allowing for peaceful transitions of power.",
    },
    {
        "question": "What are the main principles of sustainable development?",
        "answer": "Sustainable development aims to meet the needs of the present without compromising the ability of future generations to meet their own needs. Its main principles include: environmental protection (preserving natural resources and ecosystems), economic viability (promoting economic growth without depleting natural resources), social equity (ensuring fair distribution of resources and opportunities), and good governance (implementing policies and practices that support these goals). It emphasizes the interconnectedness of environmental, social, and economic issues and promotes long-term thinking in decision-making processes.",
    },
    {
        "question": "Explain the concept of artificial intelligence and its potential impacts on society.",
        "answer": "Artificial Intelligence (AI) refers to the simulation of human intelligence in machines programmed to think and learn like humans. It encompasses various technologies including machine learning, natural language processing, and computer vision. AI has the potential to revolutionize many sectors including healthcare (through improved diagnostics and personalized medicine), transportation (with autonomous vehicles), education (via personalized learning), and many industries through automation and optimization. However, it also raises concerns about job displacement, privacy, bias in decision-making systems, and the long-term implications of creating machines that might surpass human intelligence.",
    },
]
