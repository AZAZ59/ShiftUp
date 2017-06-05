import React from 'react';
import { Router, Route, browserHistory, IndexRoute } from 'react-router';

// Layouts
import MainLayout from './components/main-layout';

// Pages
import Home from './components/home';
// Task
import TasksList from './components/tasks'
import ResultList from './components/tasks/result-list'
// Collector
import Collector from './components/collector/'
// Collector | Groups
import Groups from './components/collector/groups'
import GetAllMembers from './components/collector/groups/get_all_members'
import GetGroupsPosts from './components/collector/groups/get_groups_posts'
import GetMembersFriends from './components/collector/groups/get_members_friends'
import GetMembersGroups from './components/collector/groups/get_members_groups'
import GetMembersRelations from './components/collector/groups/get_members_relations'
import GetMembersRelatives from './components/collector/groups/get_members_relatives'
import GetMembersSubscriptions from './components/collector/groups/get_members_subscriptions'
// Collector | Users
import Users from './components/collector/users'
import GetFriends from './components/collector/users/get_friends'
import GetGroups from './components/collector/users/get_groups'
import GetSubscriptions from './components/collector/users/get_subscriptions'
import GetUsersPosts from './components/collector/users/get_users_posts'

export default class Routers extends React.Component{
    render(){
        return (
            <Router history={browserHistory}>
                <Route path="/" component={MainLayout}>
                    <IndexRoute component={Home} />
                    // Tasks
                    <Route path="tasks" component={TasksList}/>
                    <Route path="tasks/:result_id" component={ResultList}/>
                    // Collector
                    <Route  path="collector" component={Collector}/>
                    // Collector | Groups
                    <Route path="collector/groups" component={Groups}/>
                    <Route path="collector/groups/get_all_members" component={GetAllMembers}/>
                    <Route path="collector/groups/get_groups_posts" component={GetGroupsPosts}/>
                    <Route path="collector/groups/get_members_friends" component={GetMembersFriends}/>
                    <Route path="collector/groups/get_members_groups" component={GetMembersGroups}/>
                    <Route path="collector/groups/get_members_relations" component={GetMembersRelations}/>
                    <Route path="collector/groups/get_members_relatives" component={GetMembersRelatives}/>
                    <Route path="collector/groups/get_members_subscriptions" component={GetMembersSubscriptions}/>
                    // Collector | Users
                    <Route path="collector/users" component={Users}/>
                    <Route path="collector/users/get_friends" component={GetFriends}/>
                    <Route path="collector/users/get_groups" component={GetGroups}/>
                    <Route path="collector/users/get_subscriptions" component={GetSubscriptions}/>
                    <Route path="collector/users/get_users_posts" component={GetUsersPosts}/>
                </Route>
            </Router>
        );
    }
}