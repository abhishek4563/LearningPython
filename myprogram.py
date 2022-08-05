from MyMainPackage import some_main_script # Note that we are not sppecifiying .py in package name
from MyMainPackage.SubPackage import mysubscript # Note the syntax for referring to subpackage 
#from mysubscript import sub_report											#we could also import specific functions 
from MyMainPackage.SubPackage.mysubscript import sub_report # Note the syntax for referring to a mdoule in a sub-package 
															# Note tthat for adding specific functions, we need to refer to the (nested) module and import a function
some_main_script.report_main() # we are calling functions from the module by literally referring to modulename.funcname()
#mysubscript.sub_report() # if we imported the module then function name needs to be referred via the module
sub_report() # if we specifically imported a function, we can just call it 