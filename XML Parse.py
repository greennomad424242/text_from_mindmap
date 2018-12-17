#!/usr/bin/env python
# coding: utf-8

# In[117]:


import xml.etree.ElementTree as ET
tree = ET.parse('map.xml')
root_cal = tree.getroot()
root = root_cal.findall(".")


# In[118]:


import os
cwd = os.getcwd()
print (cwd)


# In[ ]:




 


# In[119]:


number_of_elements = len(root[0])
text_array = [] 
relationship_array = []
for i in range(0, number_of_elements):
  # print ('i:' + str(i))
   individual_cell = root[0][i]
  # print (individual_cell)
 #  print (root[0][i].attrib['id'])
   individual_cell_attributes = individual_cell.attrib 
   entry_type = 'unknown'
   if 'id' in individual_cell_attributes:
      id =root[0][i].attrib['id']
     # print ('id:' +  id )
   if 'label' in individual_cell_attributes:
      label =root[0][i].attrib['label']
     # print ('label:' +  label )    
   if 'treeRoot' in individual_cell_attributes:
      treeRoot =root[0][i].attrib['treeRoot']
     # print ('treeroot:' +  treeRoot )        
      parent_node = id
   if 'value' in individual_cell_attributes:
      val =root[0][i].attrib['value']
      if len(val) > 0:  
          entry_type = 'text'
          label = val  
      else:
          entry_type = 'geo' 
   else: 
      entry_type ="unknown"
   if 'source' in individual_cell_attributes:
      source =root[0][i].attrib['source']
     # print ('source:' + val) 
   if 'target' in individual_cell_attributes:
      target =root[0][i].attrib['target']
      #print ('target:' + val)
   geometry_within_cell= root[0][i].findall('mxGeometry')
   for child in geometry_within_cell:
       if 'y' in  child.attrib:
           y  = child.attrib['y']
      #     print ('y:' +  y )
           
   if entry_type == 'geo':
      relationship_array.append([id,source, target])
   elif entry_type == 'text':
      text_array.append([id, label,y])
   source= ""  
   target= "" 
   id = "" 

print (parent_node)


# In[120]:


for row in text_array: 
     print (row)


# In[121]:


for row in relationship_array: 
     print (row)


# In[122]:


merged_array = []
for row in  text_array:  
    name = row[0]
    text_val = row[1]
    y = row[2]
    parent_search= next((x for x in relationship_array if x[2] == name ), 'none')
    parent_name = parent_search[1]

    child_search = next((x for x in relationship_array if x[1] == name ), 'none')
 
    if child_search =="none" : 
       has_children = "false"
    else: 
       has_children = "true" 
    merged_array.append([ name,parent_name, has_children ,y, text_val ])

for row in merged_array: 
     print (row)


# In[137]:



def sortSecond(val): 
   # print  (val[3])
    return val[3]  

def recursive_print (target_name):
    
   find_entry = next((x for x in merged_array if x[0] == target_name ), 'none')
   if find_entry == 'none':
       has_children ='true'   
   else:     
       label_value = find_entry[4]
       has_children = find_entry[2]
       print (label_value)
  
   if (has_children == 'true'):
    
           # find all children and sort by y location 
           matches = [x for x in merged_array if x[1] == target_name ]
               #iterate over them in order 
           matches.sort(key = sortSecond)  
          # print ("Matches:")  
          # print (matches) 
  
           #for child_name in matches: 
           for child_name in matches: 
               # print (child_name[0])
                recursive_print(child_name[0])
  
   # print out the text   
   #print (label_value)

recursive_print('FppH65uxrcL7wk5XnBWe-1')
#FppH65uxrcL7wk5XnBWe-1


# In[ ]:





# In[ ]:





# In[ ]:





# In[33]:





# In[ ]:




