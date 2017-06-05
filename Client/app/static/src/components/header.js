/**
 * Created by vlad on 20.11.16.
 */
var React = require('react');
import { Link } from 'react-router';
import { AppBar, MenuItem, Drawer, IconButton, Subheader, ListItem, Divider } from 'material-ui';
import { ActionDashboard, ActionViewList, SocialGroup, SocialPerson, FileCloud, NavigationMenu } from 'material-ui/svg-icons';
import methods from '../store'


class Header extends React.Component{
    constructor(...args) {
        super(...args);
        this.state = {open: false, collector_users_methods: [], collector_groups_methods: []};
        this.get_collector_methods = this.get_collector_methods.bind(this);
        this.get_collector_methods();
        this.handleToggle = this.handleToggle.bind(this);
        this.handleClose = this.handleClose.bind(this);
    }
    handleToggle = () => this.setState({open: !this.state.open});
    handleClose = () => this.setState({open: false});

    get_collector_methods(){
        methods.collector.groups.forEach((method) => {
            this.state.collector_groups_methods.push(
                <ListItem
                    linkButton
                    onTouchTap={this.handleClose}
                    primaryText={method.name}
                    containerElement={<Link to={'/collector/groups/'+method.path} />}
                    onTouchTap={this.handleClose}
                />
            )
        });
        methods.collector.users.forEach((method) => {
            this.state.collector_users_methods.push(
                <ListItem
                    linkButton
                    onTouchTap={this.handleClose}
                    primaryText={method.name}
                    containerElement={<Link to={'/collector/users/'+method.path} />}
                    onTouchTap={this.handleClose}
                />
            )
        });
    }

    render(){
        return(
            <header>
                <AppBar
                    title="ShiftUp"
                    iconElementLeft={
                    <IconButton onTouchTap={this.handleToggle}>
                        <NavigationMenu />
                     </IconButton>
                     }
                />
                <Drawer
                    open={this.state.open}
                    onRequestChange={(open) => this.setState({open})}
                    docked={false}
                >
                    <MenuItem
                        linkButton
                        onTouchTap={this.handleClose}
                        containerElement={<Link to="/" />}
                        primaryText="Дашбоард"
                        leftIcon={<ActionDashboard />}
                    />
                    <MenuItem
                        linkButton
                        onTouchTap={this.handleClose}
                        containerElement={<Link to="/tasks" />}
                        leftIcon={<ActionViewList />}
                        primaryText="Задачи"
                    />
                    <MenuItem
                        leftIcon={<FileCloud />}
                        primaryText="Сбор данных"
                        primaryTogglesNestedList={true}
                        nestedItems={[
                        <ListItem leftIcon={<SocialGroup />} primaryText="Сообщество" primaryTogglesNestedList={true} nestedItems={this.state.collector_groups_methods}/>,
                        <ListItem leftIcon={<SocialPerson />} primaryText="Пользователь" primaryTogglesNestedList={true} nestedItems={this.state.collector_groups_methods}/>
                        ]}
                    />
                </Drawer>
            </header>
        );
    }
};

export default Header