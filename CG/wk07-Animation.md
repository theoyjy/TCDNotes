Hierarchical Transformation

>[!example] Arm
>Parent -> children: base, wrist, finger
>`global_wrist = global_base * local_wrist;`
>`global_finger = global_wrist * local_finger`

Use a stack to remember the global matrix