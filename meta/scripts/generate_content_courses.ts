import fs from 'fs-extra';
import * as yaml from 'yaml';

const coursesPath = 'contents/course_list.json';

(async () => {
  const groupedCourses: Record<
    any,
    { index: number; leadTopic: string; courses: any[]; project: any }
  > = {};

  const courses: string[] = await fs.readJSON(coursesPath);

  for (const course of courses) {
    const courseTopics = course.split('.');

    const leadTopic = courseTopics[0];

    if (!groupedCourses[leadTopic]) {
      groupedCourses[leadTopic] = {
        index: Object.keys(groupedCourses).length,
        leadTopic,
        courses: [],
        project: {},
      };
    }

    groupedCourses[leadTopic].courses.push({
      name: course,
      contents: [],
      tasks: [],
    });
  }

  for (const [leadTopic, courses] of Object.entries(groupedCourses)) {
    await fs.outputFile(
      `contents/courses/${String(courses.index + 1).padStart(
        2,
        '0'
      )}-${leadTopic}/courses.yml`,
      yaml.stringify(courses)
    );
  }
})();
