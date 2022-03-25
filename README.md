# Welcome to the ***Diabetes*** starter project.
 
And welcome to Domino--the data science and MLOps platform that accelerates research, speeds model deployment, and increases collaboration for code-first data science teams at scale. 

The Diabetes project uses National Institute of Diabetes and Digestive and Kidney Diseases data to determine the probability that a patient will experience the onset of diabetes type I.

# Let's Jump Right Into Publishing a Model API
The configuration, code, and datasets are stored in the project and are accessible through the navigation bar on the left. 

If you're new to Domino or not, you can start digging into the files and configuration: 
* ***onset_diabetes.ipynb***--click the files tab in the left navigation bar--quick research
* ***train_gb.py***--click the file tab and go to the model folder--quick research
* ***score_gb.py***--click the file tab and go to the model folder--fast model development
* ***pima-indians-diabetes.csv***--click the file tab and go to the data folder
* ***Settings*** tab on the left navigation bar
    * The ***Hardware and Environment*** tab provides configuration options.
    * The ***Access and Sharing*** tab allows you to bring in collaborators.

The rest of this ReadMe will take you directly to publishing a ***Model API***. If you need help launching workspaces and training data, please open the version of ***sample-project-1_bank-marketing*** in your project folder for a quick tutorial.

# Publish a Model API
We'll use the ***Model API*** tab from the navigation bar on the left. Go ahead and click on ***New Model***.

* Type in a ***name*** for your model.
* Click ***Next***. There may be a short pause here before the next configuration page arrives.
* Select an ***Environment***: ***Domino Analytics Distribution Py3.6 R3.6***.
* Set the ***file*** to ***model/score_gb.py***. For the starter projects, we consistently use score for models.
* The ***function*** name is ***score***. You can confirm this by looking at the function definition in ***score_gb.py*** 
* Don't check the box for creating an https.
* Click on the ***Create Model*** button.
* Next, a new window will appear.
    * You can navigate with the tab buttons on the top: Overview, Versions, Audit Log, and Settings. 
    * ***Versions*** is an easy place to monitor progress and view ***build logs***.
    * On the ***Versions*** tab, clicking on the number will show you the configuration details.
    * The status will quickly transition from ***Preparing to Build*** to ***Building***.
    * After about six minutes, you'll see ***Starting*** and ***Running***. 

![](https://try.dominodatalab.com/u/pbaumann22/sample-project-2_diabetes/raw/61b7038e2165771c483da244912416815764ec35/screenshots/73_publish.modelv4.el1.png?inline=true)

# Running the Model
After the model build, you'll be able to run the model.

* You can use the https address to send the model arguments.
* But first, start the model and use JSON to send the arguments to the model. Note that the model is running after the build is complete.
    * Click the ***Overview*** tab to see the API.
    * You can find the parameters by searching score.py for the parameters to the function call to ***score***.
    * Once you add the JSON in the ***Request*** box in the ***Tester*** tab, click ***Send***. We've provided sample ***JSON*** in the Files tab: [JSON-parameters-for-model-API.txt](https://try.dominodatalab.com/u/pbaumann22/sample-project-2_diabetes/view/JSON-parameters-for-model-API.txt).
    * The results will show up in the ***Response*** box on the right side of the run dashboard.

![](https://try.dominodatalab.com/u/pbaumann22/sample-project-2_diabetes/raw/61b7038e2165771c483da244912416815764ec35/screenshots/74_run_modelv3.el1.png?inline=true)

Congratulations! You've published a model. 

Once again, clean up by stopping the model API. The easiest way to do this is the three vertical dots on the right side in the ***Versions*** tab.

# Next Steps
>There are many ways to use density-based clustering to understand customer behavior. If you start with this project, you’ll quickly come up to speed on new techniques and help your organization recognize trends. You can either explore [other blog-based projects](https://try.dominodatalab.com/search?area=project&query=project.tag%3DDomino%20Data%20Science%20Blog) or [start your own](https://try.dominodatalab.com/projects).
___

Want to share this project with others? [Learn more about our sharing and collaboration features here](https://docs.dominodatalab.com/en/3.6/reference/projects/Sharing_and_collaboration.html).

# Need some extra help?

>* Check out our tutorials and help [documentation](https://docs.dominodatalab.com/en/4.4.2/).
>* Message us using the Intercom button.

You'll find a description of the project below.

# Forecast the onset of diabetes mellitus

This project performs exploratory data analysis and trains a machine learning model to predict the onset of diabetes type I, using a dataset provided by the National Institute of Diabetes and Digestive and Kidney Diseases.

Diabetes mellitus type 1 (also known as type 1 diabetes) is a form of diabetes mellitus in which not enough insulin is produced. This condition results in high blood sugar levels in the body. The typical symptoms are frequent urination, increased thirst, increased hunger, and weight loss. Additional symptoms may include blurry vision, feeling tired, and poor healing. Symptoms typically develop over a short time.[1]

![alt text](https://www.niddk.nih.gov/-/media/Images/Health-Information/Diabetes/landing/diabetes.png "Logo Title Text 1")

The dataset contains the following attributes:

* Number of times pregnant
* Plasma glucose concentration a 2 hours in an oral glucose tolerance test
* Diastolic blood pressure (mm Hg)
* Triceps skinfold thickness (mm)
* 2-Hour serum insulin (mu U/ml)
* Body mass index (weight in kg/(height in m)^2)
* Diabetes pedigree function
* Age (years)
* Class variable (0 or 1)

Several constraints were placed on the selection of these instances from a more extensive database. In particular, all patients here are females at least 21 years old of Pima Indian heritage.

The diagnostic, binary-valued variable investigated is whether the patient shows signs of diabetes according to World Health Organization criteria (i.e., if the 2-hour post-load plasma glucose was at least 200 mg/dl at any survey examination or if the condition was found during routine medical care). The population lives near Phoenix, Arizona, USA.

[1] [https://en.wikipedia.org/wiki/Diabetes_mellitus_type_1] https://en.wikipedia.org/wiki/Diabetes_mellitus_type_1

[2] Smith,~J.~W., Everhart,~J.~E., Dickson,~W.~C., Knowler,~W.~C., Johannes,~R.~S. (1988). Using the ADAP learning algorithm to forecast the onset of diabetes mellitus. In Proceedings of the Symposium on Computer Applications and Medical Care (pp. 261--265). IEEE Computer Society Press.