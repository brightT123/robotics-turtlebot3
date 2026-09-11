import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'lab_comm'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Gunakan sintaks os.path.join dan glob berikut:
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dev',
    maintainer_email='dev@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [
            'main_sensor = lab_comm.sensor_publisher:main',
            'main_processing = lab_comm.processing_node:main',
            'main_reset = lab_comm.reset_service:main',
            'main_motion = lab_comm.motion_action_server:main',
        ],
    },
)