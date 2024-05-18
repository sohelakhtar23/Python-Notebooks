# Parse the given XML file to below given DICTIONARY

Basic Model(json) Format
```
{
	'mapping name':{
		name: mapping_name,
		parent_folder: folder_name,
		tasks: {
				taskname: {
					name: taskname,
					task_type: transformation type,
					transformation_name: transformation name,
					fields: []
				},
				task2: {
					name: task2name,
					task_type:
				},
				...
		}
	},
	'mapping2':{}

}
```


</br></br>

# add Transformation Fields

### by matching `<Transformation>` tag name with the Task(aka Instance) name in that mapping and then finally add the `<TransformField>`s
![alt text](image.png)



# JSON Format for Database Schema


```

{
	workflow_id (?): {    
		workflow_id: ?,
		project: (from variable),
		workflow_name: "NAME",
		workflow_description: "DESCRIPTION",
		tasks: {
					task_id (?): {
						task_id: ?,
						task_type: "TASKTYPE",
						name: "NAME",
						task_name: "TASKNAME",
						execution_order: 0,
						mapping: {
							mapping_id: 
							mapping_name: 
							mapping_description: 
							instances: {
								instance_id: {
									transformation_type:
									transformation_name:
									execution_order: ,
									transform_fields: [
										{
											field_id:
											field_name:
											field_type:
											is_input:
											is_output:
											is_lookup:
										},
										{
											field_id:
											field_name:
											field_type:
											is_input:
											is_output:
											is_lookup:
										},

									]
								},
								instance_id: {
									transformation_type:
									transformation_name:
									execution_order: 
								}

							}
						},
					},
	},
}

```

