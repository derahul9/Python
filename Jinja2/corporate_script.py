import jinja2
import csv

user_in_file = input("Please enter the variable file? ")
user_in_file1 = input("Please enter the template file? ")
local_datadir = r'/home/rahul/Documents/Python_Projects/Python/Jinja2/variables/'
local_datadir1 = r'/home/rahul/Documents/Python_Projects/Python/Jinja2/Templates/'
local_datadir_out = r'/home/rahul/Documents/Python_Projects/Python/Jinja2/variables/'

input_file = local_datadir + user_in_file + ".csv"
with open(input_file) as f:
 read_csv = csv.DictReader(f)
 for vars in read_csv:
     Change_Number = vars['Change_Number']
     Router_A = vars['Router_A']
     template_file = local_datadir1 + user_in_file1 + ".j2"
     with open(template_file) as a:
          corporate_template = a.read()

     template = jinja2.Template(corporate_template)
     output_file = local_datadir_out + Change_Number + "_" + Router_A + "_" + "Install_Backout_Script"+ ".txt"

     output = open(output_file, "a")

     with open(output_file, 'a') as f:
          output.write(template.render(vars))

     output.close()