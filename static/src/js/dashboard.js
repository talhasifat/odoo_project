/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, onWillStart } from "@odoo/owl";
import { useState } from "@odoo/owl";
import { rpc } from "@web/core/network/rpc";

export class SchoolDashboard extends Component {
     setup() {
            this.state = useState({ studentCount: 0 });

            onWillStart(async () => {
            const studentResult = await rpc("/school_dashboard/student_count", {});
            const teacherResult = await rpc("/school_dashboard/teacher_count", {});
            this.state.studentCount = studentResult.count;
            this.state.teacherCount = teacherResult.count;
//                const result = await rpc("/school_dashboard/student_count", {});
//                this.state.studentCount = result.count;
            });
        }
}

SchoolDashboard.template = "student_information.SchoolDashboard";

// Register as client action
registry.category("actions").add("school_dashboard", SchoolDashboard); // 🔁 change from "school_dashboard_action"
