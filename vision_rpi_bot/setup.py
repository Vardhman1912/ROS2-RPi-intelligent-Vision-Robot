from setuptools import find_packages, setup
import os 
from glob import glob

package_name = 'vision_rpi_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name,'launch'),glob('launch/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vardhman',
    maintainer_email='vardhman@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "publisher_rpi_node = vision_rpi_bot.publisher:main",
            "subscriber_rpi_node = vision_rpi_bot.subscriber:main",
            "cmdVel_to_pwm = vision_rpi_bot.cmd_to_pwm_driver:main",
            "image_publisher_node = vision_rpi_bot.image_publisher:main",
            "line_follow_drive_node = vision_rpi_bot.line_follow_drive:main",
            "image_publisher_rgb_node = vision_rpi_bot.image_publisher_rgb:main",

        ],
    },
)
