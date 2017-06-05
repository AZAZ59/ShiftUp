/**
 * Created by vlad on 21.11.16.
 */
var React = require('react');
import Nav from 'react-bootstrap/lib/Nav';
import NavItem  from 'react-bootstrap/lib/NavItem';
import LinkContainer from 'react-router-bootstrap/lib/LinkContainer';
import Collapse  from 'react-bootstrap/lib/Collapse';

class CollectorUsersMenu extends React.Component{
    constructor(props) {
        super(props);

        this.state = {open: false};
    }
    render(){
        return(
            <div>
                <h4  onClick={()=> this.setState({ open: !this.state.open })}>Сбор данных пользователей</h4>
                <Collapse in={this.state.open}>
                    <Nav bsStyle="pills" stacked>
                        <LinkContainer to="/collector/users/get_friends" activeClassName="active">
                            <NavItem>Сбор друзей пользователей</NavItem>
                        </LinkContainer>
                        <LinkContainer to="/collector/users/get_groups" activeClassName="active">
                            <NavItem>Сбор групп пользователей</NavItem>
                        </LinkContainer>
                        <LinkContainer to="/collector/users/get_subscriptions" activeClassName="active">
                            <NavItem>Сбор людей, на которых подписаны пользователи</NavItem>
                        </LinkContainer>
                        <LinkContainer to="/collector/users/get_users_posts" activeClassName="active">
                            <NavItem>Сбор постов пользователей</NavItem>
                        </LinkContainer>
                    </Nav>
                </Collapse>
            </div>
        );
    }
}

export default CollectorUsersMenu
