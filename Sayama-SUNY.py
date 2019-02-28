#%% [markdown]
# A document seems to be a sequence of cells, each of which has one of markdown, code, Raw NBConvert or Heading as its type. This text is in a markdown cell and hence, presumably, I can have **bold** and _italic_ text.

#%%
# This is a code cell
for i in range(5):
    print (i + 1)
print ("Once I caught a fish alive.")

#%% [markdown]
# # This is a heading cell 
# but apparently headings are deprecated and instead Jupyter converts them to markdown cells and prepends your text with the hash sign to make it a markdown heading.
# 
# This image didn't want to display but I found the the markdown that Jupyter was entering was wrong. You need to manually edit it and remember to add the image itself to the git repo (ie the same directory as the ipynb file). 
# 
# ![This is just a test image](ref.png)
# 
# **git config --global credential.helper 'cache --timeout=7200'**
# 
# Let's try some maths:
# 
# $$\frac{\pi}{2\omega}$$
# 
# Seems rather small. Let's try the same using \[ \] instead of $$ $$:
# 
# \[ \frac{\pi}{2\omega} \]
# 
# Presumably we can use triple backticks to include code blocks in a markdown cell:
# 
# ```
# System.out.println("Yep");
# ```
# 
# But that isn't particularly nice looking. What about specifying the language:
# 
# ```python
# for matplotlib import plot
# print ("Now what?")
# ```
# 
# 

