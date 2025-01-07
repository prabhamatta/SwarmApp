import os
import logging
from swarm import Swarm, Agent
from dotenv import load_dotenv

#Set up logging
logging.basicConfig(
    filename="agentlogs.log",
    level=logging.INFO,  # Set the logging level to INFO
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Load environment variables
load_dotenv()
# Initialize the Swarm client
client = Swarm()
productarea = "Slack App for Remote Teams"
agent1 = Agent(
    name="Market Trends Agent",
    instructions=f'Analyze current market trends in the {productarea}, focussing on customer preferences, emerging technologies and competitor offerings',
)
agent2 = Agent(
    name="Product Developement Advisor",
    instructions=f'Based on the market trends, recommend features, specificiations and design elements for the {productarea}.',
)
agent3 = Agent(
    name="Launch Strategy Advisor",
    instructions=f'Develop a launch strategy for the {productarea} considering the recommended features and current market trends.',
)


#Messages for Agent1
messages1 = [{"role": "user", "content": f'As the CEO, I need an analysis of the current product market trends to get information on the {productarea} development .'}]

#Run the agents with inter agent communicaiton
try:
    #run agent 1: Market Trends Agent
    response1 = client.run(
        agent=agent1,
        messages=messages1,
    )
    print("Market Analyst Response:")
    print(response1.messages[-1]["content"])
    logging.info(f'Agent1 response: {response1}')  # Log the response

    #Messages for Agent2
    messages2 = [{"role": "user", "content": f"Based on the market trends analysis:{response1} , I need recommendations on the {productarea} features and specifications."}]
    #run agent 2: Product Development Advisor
    response2 = client.run(
        agent=agent2,
        messages=messages2,
    )
    print("Product Development Advisor Response:")
    print(response2.messages[-1]["content"])
    logging.info(f'Agent2 response: {response2}')  # Log the response   

    #Messages for Agent3
    messages3 = [{"role": "user", "content": f'Based on the market trends analysis:{response1} and the product development recommendations:{response2} , develop a launch strategy for the {productarea}.'}]

    #run agent 3: Launch Strategy Advisor
    response3 = client.run(
        agent=agent3,
        messages=messages3,
    )
    print("Launch Strategy Advisor Response:")
    print(response3.messages[-1]["content"])
    logging.info(f'Agent3 response: {response3}')  # Log the response

except Exception as e:
    print(f"An error occured: {e}")
    logging.error(f"An error occured: {e}") # Log the error message


