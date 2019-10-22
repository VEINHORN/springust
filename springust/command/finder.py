import os.path

def find_package(project_root, class_type):
    """Package search algorithm

    We assume that we start in root directory, so we go to search in src/main/java

    1. Try to find package with name controller/service/repository/etc.
    2. Try to find any Java classes whichs ends on Controller/Service/Repository
    """
    source_path = source_folder(project_root)
    print(source_path)
    
    for root, dirs, files in os.walk(source_path):        
        for dir in dirs:
            if "controller" in dir:
                package_path = root + os.sep + dir
                print("found package with path: " + package_path)
                return package_path, package_name(source_path, package_path)
        
        for file in files:
            if "Controller" in str(file):
                package_path = root
                print("Trying to search file: " + package_path)
                return package_path, package_name(source_path, package_path)

    return "unknown package"

def find_package_new(project_root, class_type, what_search):
    """Package search algorithm

    We assume that we start in root directory, so we go to search in src/main/java

    1. Try to find package with name controller/service/repository/etc.
    2. Try to find any Java classes whichs ends on Controller/Service/Repository
    """
    source_path = source_folder(project_root)
    
    for root, dirs, files in os.walk(source_path):        
        for dir in dirs:
            if what_search in dir:
                package_path = root + os.sep + dir
                print("found package with path: " + package_path)
                return package_path, package_name(source_path, package_path)
        
        for file in files:
            if what_search.capitalize() in str(file):
                package_path = root
                print("Trying to search file: " + package_path)
                return package_path, package_name(source_path, package_path)

    return "unknown package"

def find_entity(what_search):
    """Searches first entity in the project
    """
    source_path = os.path.join(".", "src", "main", "java")

    for root, dirs, files in os.walk(source_path):

        for file in files:
            if what_search.capitalize() + ".java" == str(file):
                package_path = root
                entity_name = str(file).replace(".java", "")
                return package_name(source_path, package_path), entity_name
    return None, None

def package_name(source_path, package_path):
    return package_path.replace(source_path + os.sep, "").replace(os.sep, ".")


def source_folder(project_root):
    return os.path.join(project_root, "src", "main", "java")