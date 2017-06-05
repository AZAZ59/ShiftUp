/**
 * Created by vlad on 18.11.16.
 */

var React = require('react');
import Home from './home';
import GetAllMembers from './collector/groups/get_all_members'
import schema from './collector/groups/get_all_members'


class Task extends React.Component {
    constructor(props) {
        super(props);
        this.state = {value: 'Collector.Groups.get_all_members'};
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(event) {
        this.setState({value: event.target.value});
    }


    alert_some(msg){
        alert(msg);
    }

    renderComponent(){
        switch(this.state.value){
            case 'Collector.Groups.get_all_members':
                return <GetAllMembers />;
            case 'Home':
                return <Home/>;
            default:
                return <Home/>;
        }
    }

    render() {
        return (
            <div>
                <form>
                    <select value={this.state.value} onChange={this.handleChange}>
                        <option value="Home">Home</option>
                        <option value="Collector.Groups.get_all_members">Группы: сбор подписчиков</option>
                    </select>
                </form>
                {this.renderComponent()}
            </div>
        );
    }
}

export default Task