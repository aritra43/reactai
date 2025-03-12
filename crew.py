from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileReadTool, FileWriterTool
from dotenv import load_dotenv

tool_instance = FileWriterTool()
# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators
load_dotenv()
file_read_tool = FileReadTool("C:/Users/l43ar/Downloads/reactnew/webnew/src/webnew/srs.txt")
file_read_tool_new = FileReadTool("C:/Users/l43ar/Downloads/reactnew/webnew/src/webnew/web_requirement_list.txt")

@CrewBase
class Webnew():
	"""Webnew crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def srs_reader(self) -> Agent:
		return Agent(
			config=self.agents_config['srs_reader'],
			verbose=True,
			tools=[file_read_tool]
		)

	@agent
	def webpage_requirement_lister(self) -> Agent:
		return Agent(
			config=self.agents_config['webpage_requirement_lister'],
			verbose=True,
			tools=[file_read_tool,tool_instance]
		)

	@agent
	def component_expert(self) -> Agent:
		return Agent(
			config=self.agents_config['component_expert'],
			verbose=True,
			tools=[file_read_tool_new]
		)

	@agent
	def component_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['component_writer'],
			verbose=True,
			tools=[file_read_tool_new,tool_instance]
		)

	@agent
	def app_and_main_expert(self) -> Agent:
		return Agent(
			config=self.agents_config['app_and_main_expert'],
			verbose=True,
			tools=[file_read_tool_new]
		)

	@agent
	def main_app_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['main_app_writer'],
			verbose=True,
			tools=[file_read_tool_new,tool_instance]
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def srs_reader_task(self) -> Task:
		return Task(
			config=self.tasks_config['srs_reader_task'],
		)

	@task
	def webpage_requirement_lister_task(self) -> Task:
		return Task(
			config=self.tasks_config['webpage_requirement_lister_task'],
			output_file="C:/Users/l43ar/Downloads/reactnew/webnew/src/webnew/web_requirement_list.txt"
		)

	@task
	def component_maker_task(self) -> Task:
		return Task(
			config=self.tasks_config['component_maker_task'],
		)

	@task
	def component_writer_task(self) -> Task:
		return Task(
			config=self.tasks_config['component_writer_task'],
		)

	@task
	def app_and_main_maker_task(self) -> Task:
		return Task(
			config=self.tasks_config['app_and_main_maker_task'],
		)

	@task
	def main_and_app_writer_task(self) -> Task:
		return Task(
			config=self.tasks_config['main_and_app_writer_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Webnew crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
