/**
 * Created by vlad on 18.11.16.
 */


const methods = {
    collector: {
        groups: [
            {path: 'get_all_members', name: 'Подписчики'},
            {path: 'get_groups_posts', name: 'Посты'},
            {path: 'get_members_friends', name: 'Друзья подписчиков'},
            {path: 'get_members_groups', name: 'Группы подписчиков'},
            {path: 'get_members_relations', name: 'Пары подписчиков'},
            {path: 'get_members_relatives', name: 'Родственики подписчиков'},
            {path: 'get_members_subscriptions', name: 'Подписки подписчиков'}
        ],
        users: [
            {path: 'get_friends', name: 'Друзья'},
            {path: 'get_groups', name: 'Группы'},
            {path: 'get_subscriptions', name: 'Подписки'},
            {path: 'get_users_posts', name: 'Посты'}
        ]
    }
};
export default methods;