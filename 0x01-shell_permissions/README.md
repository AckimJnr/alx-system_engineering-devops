0-iam_betty	#Switch current user to betty
1-who_am_i	#Print username of current user
2-groups	#List all groups current user is part of
3-new_owner	#Change owner of file hello to betty
4-empty		#Create an empty file called hello
5-execute	#Add execute permission to owner of file hello
6-multiple_permissions	#Add execute permission to owner and group owner and read permisson to other users
7-everybody	#Give execution permission to everyone
8-James_Bond	#Give all permissions to others and none to all remaining users
9-John_Doe	#Change mode of hello to -rwxr-x-wx
10-mirror_permissions #Mirror olleh's permissions to hello
11-directories_permissions #Add execute permitions to all subdirectories of the current directory for the owner and the group owner and other users
12-directory_permissions #Create directory called my_dir with permissions 751 in the working directory
13-change_group	#Change group owner of file called hello in current dir to school
######Advanced####
100-change_owner_and_group	#change owner to vincent and group owner to staff for all the files and directories in the working directory
101-symbolic_link_permissions	#Change owner of _hello to vincent and sstaff(group)
102-if_only	#Change owner of the file hello if and only if it is owned by the user guillaume
103-Star_Wars	#play the start wars episode in the terminal
