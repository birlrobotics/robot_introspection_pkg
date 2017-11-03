modalities_store = {
    "endpoint_pose": [
        '.endpoint_state.pose.position.x',
        '.endpoint_state.pose.position.y',
        '.endpoint_state.pose.position.z',
        '.endpoint_state.pose.orientation.x',
        '.endpoint_state.pose.orientation.y',
        '.endpoint_state.pose.orientation.z',
        '.endpoint_state.pose.orientation.w'
    ],
    'wrench': [
         '.wrench_stamped.wrench.force.x',
         '.wrench_stamped.wrench.force.y',
         '.wrench_stamped.wrench.force.z',
         '.wrench_stamped.wrench.torque.x',
         '.wrench_stamped.wrench.torque.y',
         '.wrench_stamped.wrench.torque.z',
    ] 
}

modality_options = [
    'endpoint_pose',
    'wrench',
    'endpoint_pose_and_wrench'        
]
modality_chosen = modality_options[2]

modality_split = modality_chosen.split("_and_")
interested_data_fields = []
for modality in modality_split:
    interested_data_fields += modalities_store[modality]
interested_data_fields.append('.tag')

