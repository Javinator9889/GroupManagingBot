# Group directives
saveGroupID = "INSERT INTO `group` (chat_id) VALUE (%s)"
setGroupRules = "UPDATE `group` SET rules = %s WHERE chat_id = %s"
setGroupLink = "UPDATE `group` SET link = %s WHERE chat_id = %s"
setGroupName = "UPDATE `group` SET name = %s WHERE chat_id = %s"
setGroupStickersEnabled = "UPDATE `group` SET sitckers_enabled = %s WHERE chat_id = %s"
setGroupBotsEnabled = "UPDATE `group` SET bots_enabled = %s WHERE chat_id = %s"
setGroupAutoShortenLinks = "UPDATE `group` SET auto_shorten_links = %s WHERE chat_id = %s"

# User in group properties
setUserInGroup = "INSERT INTO `user_has_group` (user_id, chat_id, in_revision, spam, is_admin) VALUES (%s, %s, %s, %s, %s)"
setUserInRevision = "UPDATE `user_has_group` SET in_revision = %s WHERE chat_id = %s AND user_id = %s"
setUserAdmin = "UPDATE `user_has_group` SET is_admin = %s WHERE chat_id = %s AND user_id = %s"
setUserSpam = "UPDATE `user_has_group` SET spam = %s WHERE chat_id = %s AND user_id = %s"

# User properties
setUser = "INSERT INTO `user` (user_id) VALUE (%s) ON DUPLICATE KEY UPDATE user_id = %s"
setUserUsername = "UPDATE `user` SET username = %s WHERE user_id = %s"
setUserName = "UPDATE `user` SET name = %s WHERE user_id = %s"
