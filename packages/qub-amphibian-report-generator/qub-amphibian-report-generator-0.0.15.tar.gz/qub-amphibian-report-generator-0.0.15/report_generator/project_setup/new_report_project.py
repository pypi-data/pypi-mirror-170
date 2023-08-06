"""# New Report Project. 

Setup configuration files and directories for report project.

Will have more info soon

"""

import os
import pathlib
import time

import yaml

import report_generator.excel_extraction.excel_to_sql
import report_generator.project_setup.locations_data_setup
import report_generator.project_setup.locations_db_setup
import report_generator.project_setup.locations_json_setup
import report_generator.project_setup.project_directory_setup


def create_new_project(settings_dict: dict = None) -> None:
    """Create new report project.

    Creates a new report project.

    Examples:
        Example of use.

    """
    HOME_DIR = pathlib.Path.home()

    try:
        settings = get_project_settings(settings_dict)
        dir_path = report_generator.project_setup.project_directory_setup.create_dirs(
            HOME_DIR, settings["project_name"]
        )
        settings["dir_path"] = dir_path
        create_project_config_file(settings)

        report_generator.project_setup.locations_data_setup.insert_default_data(
            dir_path
        )
        # dir_path = os.path.join(HOME_DIR, "c",)
        time.sleep(5)
        report_generator.project_setup.locations_db_setup.locations_database_setup(
            os.path.join(dir_path, "data", "locations")
        )
        time.sleep(5)
        report_generator.project_setup.locations_json_setup.locations_json_setup(
            os.path.join(dir_path, "data", "locations")
        )

        database_path = os.path.join(dir_path, "data", "database", "species.db")

        report_generator.excel_extraction.excel_to_sql.export_to_database(
            settings["data_set"], database_path
        )

        print("\nReport Project set up complete!")
    except FileExistsError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)
    except KeyboardInterrupt as e:
        print(e)
        print("Quitting Application...")


def get_project_settings(settings: dict = None) -> None:
    """CLI to query project setup from user.

    Gets a series of user inputs to set up the config
    files for the project.

    Examples:
        Example of use.

    Args:
        Settings (dict): Settings dict that is provided if user doing set up
                         from the GUI application rather than the CLI.

    """
    if settings is None:

        print("Creating new project")
        project_name = input("Please enter project name: ")
        report_name = input("Please enter report name: ")
        author_name = input("Please enter author name: ")
        school_name = input("Please enter School name: ")
        uni_name = input("Please enter uni name: ")
        data_set = input("Please enter path to data_set file: ")

        settings = {
            "project_name": project_name,
            "report_name": report_name,
            "author_name": author_name,
            "school_name": school_name,
            "uni_name": uni_name,
            "data_set": data_set,
            "fonts": {
                "default_header_colour": "Black",
                "default_header_font": "OpenSans-Bold",
                "default_header_size": 48,
                "default_paragraph_colour": "Black",
                "default_paragraph_font": "OpenSans-Bold",
                "default_paragraph_size": 10,
                "default_title_colour": "Red",
                "default_title_font": "OpenSans-Bold",
                "default_title_size": 56,
                "default_title_sub": "OpenSans",
            },
        }

    return settings


def create_project_config_file(settings: dict) -> None:
    """Create the project config file.

    Creates a Yaml file containing all project's
    basic settings.

    Examples:
        Example of use.

    """
    with open("config.yaml", "w") as file:
        yaml.dump(settings, file)


def main():
    """Create new Report.

    Main method for module.

    Example:
        Example use case.
    """
    create_new_project()


if __name__ == "__main__":
    main()
