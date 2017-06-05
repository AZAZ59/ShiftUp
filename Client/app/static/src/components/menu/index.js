/**
 * Created by vlad on 21.11.16.
 */

var React = require('react');
import Nav from 'react-bootstrap/lib/Nav';
import NavItem  from 'react-bootstrap/lib/NavItem';
import LinkContainer from 'react-router-bootstrap/lib/LinkContainer';
import IndexLinkContainer from 'react-router-bootstrap/lib/IndexLinkContainer';


class Menu extends React.Component{
    constructor(...args) {
        super(...args);

        this.state = {};
    }
    render(){
        return(
            <Nav>
                <IndexLinkContainer to="/" activeClassName="active" >
                    <NavItem>Дашборд</NavItem>
                </IndexLinkContainer>
                <LinkContainer to="/tasks" activeClassName="active">
                    <NavItem>Задачи</NavItem>
                </LinkContainer>
                <LinkContainer to="/collector" activeClassName="active">
                    <NavItem>Сбор данных</NavItem>
                </LinkContainer>
            </Nav>
        );
    }
};

export default Menu
