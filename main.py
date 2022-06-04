import sys
import os
import xml.etree.ElementTree as ET

if len(sys.argv) <= 1:
    print("Usege:")
    print("python main.py <android_project_path>")
    exit(0)


def list_manifests(project_path, on_manifest):
    "List AndroidManifest.xml files"
    for dir_path, dir_list, file_list in os.walk(project_path):
        if "/build/" not in dir_path:
            for file_name in file_list:
                if file_name == "AndroidManifest.xml":
                    path = os.path.join(dir_path, file_name)
                    on_manifest(path)


def parse_android_manifest_xml(path):
    tree = ET.parse(path)
    root = tree.getroot()
    activities = root.findall("./application/activity")
    for activity in activities:
        print(activity.get("{http://schemas.android.com/apk/res/android}name"))


project_path = sys.argv[1]
list_manifests(project_path, parse_android_manifest_xml)
