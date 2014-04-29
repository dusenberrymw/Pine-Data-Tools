Pine-Data-Tools
---

Suite of scripts for working with data files (.csv &amp; .txt) and the Pine ANN
library.

#### Based partially on the FastML Phraug project (https://github.com/zygmuntz/phraug)

## Requirements
- Python3 installed (and accessible at '/usr/bin/env python3')
- Pine installed ('git clone https://github.com/dusenberrymw/Pine.git')
- Install the Pine shell command ('./installShellCommand.py' from within the Pine
project)


## Workflow
- Clone this to a directory for the project you're working on
- Open up pipeline.sh -> This is the main script.  Run this to go from start
(the original data) to finish (trained model, testing stats, predictions).
Customize this to meet your workflow needs.
- preprocess.py -> Use this as a first pass through your data for bulk
conversions, such as converting text features to numeric ones.  Customize the
'process()' method for your data.
- csv2pine.py -> Use this to convert the original data into Pine's data format,
which is very similar to that of Vowpal Wabbit.  Customize the
'construct_line()' method for your data.  By this point, you'll want all your data to
be numeric.
- split.py -> Use this to randomly split your data up into train and test sets.
Default is split 90/10.  Will print out the random seed used, and then can add
that to the pipeline.sh file to reproduce the same split.
- pine -> Use Pine for training and testing.  Pass in a network layout, where
the number of inputs neurons is equal to the number of features in your data,
and the number of output neurons is equal to the size of your output vector.
For testing, you can just pass in and underscore instead of a layout.  An
example of all of this is in pipeline.sh.
- classify.py -> Use this to convert raw prediction probabilities from Pine into
classes.  Can customize this to change threshold.  Only need this for
classification projects.
- stats.py -> Use this to calculate stats on how well the model is performing.
Customize this as needed.  Can redirect output into file as well.
- **Run with './pipeline.sh'**

##### Others
-  automate_passes_pine.py -> Can use this to determine ideal number of passes
through the data
- run_pine.py -> An older version of the pipeline workflow.  Basically a pipelined
version of bin/pineCLI.py in the Pine project.
- rmse.py -> Determines RMSE (root mean square error) of the model.  stats.py is
probably better to use now for classification projects.
