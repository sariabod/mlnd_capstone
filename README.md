# mlnd_capstone
Udacity MLND Capstone

# Dataset #
course_ratings.zip

# Sample #
user,course,category,rating,job,institution,state
f18c20ed7945edb779041249a71b3a54a29442c56ca2cd537cea51f25ba3ff766e7f535b53aef09ede8e1a3b9f7df98ca1f7ba8d7b28f88ed930dd5904f2b562,bd493d60ac1cfa834fd7c0b46f56e5851a53b55565d5f5949212b10524b2e541f597cbf63665c4ee1e6dab75cdf0fa3c7904a07ffafc264baabd143a736d17e9,884327c7b57992580657deec4be99eb94b9db6e9a8a959bb1168d0db0838ad45e4fba776d14ba16f1453113972c0f23ab73833e6cc35de70e295f5ed5266bc6e,4.68,195a1d28540a6b0a055c52af095e364f22ee0e6d81ac481428ce3a644053d07e48b2a668007c09fa602eaee82ebc8bf8abc25521f35107d6278c4bcabcde2ead,3c371752bc0e561f8daa5f1b2af08093dc33039c9f1146db3fcb1a340a1e42cc2cf11cba33e5422cac35fa52a1331cf63daba8a2f0ec0362b61aedc991be6ef0,76933d647fd0c27575dd9ec2691befc07300515ca8ab915f1d674c65f962b72f03d63dd61aea2d8862d0bb5d8e09535157bf1a7a96d4040aed2769745d0cb7b6

# User, Course, Category, Job, Institution, State #
These fields have all been one way hashed using SHA2-512 to keep the data anonymous. Rating is a on a 5 point floating number scale.

# how to set up
1. Create a new directory and change into new directory: mkdir /path/to/new/dir; cd /path/to/new/dir
2. Create a new virtual environment:  python3 -m venv /path/to/new/dir/venv
3. Activate new environment: source venv/bin/activate
4. Clone the repo: git clone https://github.com/sariabod/mlnd_capstone.git
5. Install Reqs: pip install -r requirements.txt
6. Unzip course_ratings.zip: unzip course_ratings.zip

from here you can start the notebook or run the api: python app.py
this will start on your localhost port 5000

## Sample Json Call ##
```json
{
	     "user":"f18c20ed7945edb779041249a71b3a54a29442c56ca2cd537cea51f25ba3ff766e7f535b53aef09ede8e1a3b9f7df98ca1f7ba8d7b28f88ed930dd5904f2b562",
"course":"bd493d60ac1cfa834fd7c0b46f56e5851a53b55565d5f5949212b10524b2e541f597cbf63665c4ee1e6dab75cdf0fa3c7904a07ffafc264baabd143a736d17e9",
"category":"884327c7b57992580657deec4be99eb94b9db6e9a8a959bb1168d0db0838ad45e4fba776d14ba16f1453113972c0f23ab73833e6cc35de70e295f5ed5266bc6e",
"job":"195a1d28540a6b0a055c52af095e364f22ee0e6d81ac481428ce3a644053d07e48b2a668007c09fa602eaee82ebc8bf8abc25521f35107d6278c4bcabcde2ead",
"institution":"3c371752bc0e561f8daa5f1b2af08093dc33039c9f1146db3fcb1a340a1e42cc2cf11cba33e5422cac35fa52a1331cf63daba8a2f0ec0362b61aedc991be6ef0",
"state":"76933d647fd0c27575dd9ec2691befc07300515ca8ab915f1d674c65f962b72f03d63dd61aea2d8862d0bb5d8e09535157bf1a7a96d4040aed2769745d0cb7b6"
}
```

# there are 2 blocks for the actual learner. The smaller one is to test locally, the bigger one should be run on a GPU enabled system

#files
1. proposal.pdf - Initial Project Proposal
2. report.pdf - Final Report
3. project.ipynb - Project Notebook
4. analysis.ipynb - Data Analysis Notebook
5. course_ratings.zip - Compressed Course Ratings
6. app.py - Simple flask app as a proof of concept api
7. requirements.txt - python module requirments 
8. models - Directory that holds model info, tmp file, and also serialized data needed to rebuild the model and lookup tables for the api


