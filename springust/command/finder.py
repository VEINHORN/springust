import os.path

def find_package(project_root, class_type):
    """Package search algorithm

    We assume that we start in root directory, so we go to search in src/main/java

    1. Try to find package with name controller/service/repository/etc.
    2. Try to find any Java classes whichs ends on Controller/Service/Repository
    """
    source_path = source_folder(project_root)
    
    for root, dirs, files in os.walk(source_path):        
        for dir in dirs:
            if "controller" in dir:
                package_path = root + os.sep + dir
                print("found package with path: " + package_path)
                return package_path, package_name(source_path, package_path)
        
        for file in files:
            if "Controller" in file:
                print(root)

    return "unknown package"

def package_name(source_path, package_path):
    return package_path.replace(source_path + os.sep, "").replace(os.sep, ".")


def source_folder(project_root):
    return os.path.join(project_root, "src", "main", "java")