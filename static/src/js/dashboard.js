/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, onWillStart } from "@odoo/owl";

export class SchoolDashboard extends Component {

}

SchoolDashboard.template = "student_information.SchoolDashboard";

// Register as client action
registry.category("actions").add("school_dashboard_action", SchoolDashboard);