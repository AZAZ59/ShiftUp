/**
 * Created by vlad on 21.11.16.
 */
var React = require('react');
import Nav from 'react-bootstrap/lib/Nav';
import NavItem  from 'react-bootstrap/lib/NavItem';
import LinkContainer from 'react-router-bootstrap/lib/LinkContainer';
import Collapse  from 'react-bootstrap/lib/Collapse';

class CollectorGroupsMenu extends React.Component{
    constructor(props) {
        super(props);

        this.state = {open: false};
    }
    render(){
        return(
            <div>
                <h4 onClick={()=> this.setState({ open: !this.state.open })}>Сбор данных групп</h4>
                <Collapse in={this.state.open}>
                    <Nav bsStyle="pills" stacked>
                        <LinkContainer to="/collector/groups/get_all_members" activeClassName="active">
                            <NavItem>Сбор подписчиков сообществ</NavItem>
                        </LinkContainer>
                        <LinkContainer to="/collector/groups/get_groups_posts" activeClassName="active">
                            <NavItem>Сбор постов сообществ</NavItem>
                        </LinkContainer>
                        <LinkContainer to="/collector/groups/get_members_friends" activeClassName="active">
                            <NavItem>Сбор друзей подписчиков сообщества</NavItem>
                        </LinkContainer>
                        <LinkContainer to="/collector/groups/get_members_groups" activeClassName="active">
                            <NavItem>Сбор групп подписчиков сообщества</NavItem>
                        </LinkContainer>
                        <LinkContainer to="/collector/groups/get_members_relations" activeClassName="active">
                            <NavItem>Сбор пар подписчиков сообщества</NavItem>
                        </LinkContainer>
                        <LinkContainer to="/collector/groups/get_members_relatives" activeClassName="active">
                            <NavItem>Сбор родственников подписчиков сообщества</NavItem>
                        </LinkContainer>
                        <LinkContainer to="/collector/groups/get_members_subscriptions" activeClassName="active">
                            <NavItem>Сбор пользователей, на которых подписаны подписчики сообщества</NavItem>
                        </LinkContainer>
                    </Nav>
                </Collapse>
            </div>
        )
    }
}

export default CollectorGroupsMenu