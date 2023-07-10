# Employee Relations Management Project
### Purpose
This was a simple demonstration to show how Django can be used to build a rudamentary application within 24 hours. It is essentially a table of fictitious current employees and information regarding their name, birthday, salary and reporting line. The various reporting levels are used to build a visual hierarchial demonstration of the relation between these employees. It was also a personal requirement that the application have a smooth UI and neat appearance.

### Setup and Installation
As part of making this easy to demonstrate, an installer was written which should automatically download and install this program. It will require some pre-existing packages to exist but it was in part to also demonstrate the use of bash scripting in such a project. 

### Demonstration
The home page is a simple view showing the data as stored in the SQLite file.
![image](https://github.com/OomBen/super-simple-django-demo/assets/58931477/cd87613b-f6c1-402d-ac9e-016f2981eb2f)

When clicking on any of the columns, the list is sorted by that column as indicated by the change in colour of the column name
![image](https://github.com/OomBen/super-simple-django-demo/assets/58931477/780eecfc-bb15-4696-8391-577d4738083c)

Searching for a particular value (in any of the existing fields) reduces the table only to the search result and makes visible the option to clear it.
![image](https://github.com/OomBen/super-simple-django-demo/assets/58931477/475f97cf-6134-4e5d-a787-714c93f84868)

Likewise a date range search can also be performed, this makes use of the browser's built in Calendar picker 
![image](https://github.com/OomBen/super-simple-django-demo/assets/58931477/7e94ab17-c97d-41f6-940a-5904e3b24e7b)

Finally by clicking on the "Treeview" page, it dynamically generates a tree structure based on the table values. This is a hierarchy of the employee relations.
![image](https://github.com/OomBen/super-simple-django-demo/assets/58931477/fe86d883-d4df-49c3-b98d-65a69ae40867)

Hovering over a particular employee highlights everyone reporting to that employee (directly or indirectly). Likewise hovering over any information highlights that block for better visibility.
![image](https://github.com/OomBen/super-simple-django-demo/assets/58931477/f094880c-f26c-40b2-a25c-cf9908f2cd3f)
![image](https://github.com/OomBen/super-simple-django-demo/assets/58931477/e0ff1f00-0337-4185-b1d1-552d0de2392e)
![image](https://github.com/OomBen/super-simple-django-demo/assets/58931477/a6c3aad8-4088-438d-b86f-eb8361faff97)

### Conclusion
Django is a very easy to use tool which comes with a lot of built in functionality and features. It can be used to make fully featured and high quality software products at a fraction of the development time and cost of other alternatives. That being said, it does have its limitations, but for now it is still one of my favourite tech stack components to work with. 

