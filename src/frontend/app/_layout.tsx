import { Tabs } from "expo-router"
import Ionicons from '@expo/vector-icons/Ionicons'
import { Icon } from "react-native-paper"

export default function RootLayout() {
    return <Tabs>
      <Tabs.Screen 
        name="index" 
        options={{ 
          title:"index",
          href: null,
          headerShown: false}}
      />
      <Tabs.Screen
        name="searchTournaments"
        options={{ 
          title:"Turniere suchen", 
          tabBarIcon: () => (<Ionicons name="search-outline" size={24} color="black"/>),
          tabBarActiveTintColor: "black",
          headerShown: false}}
      />
      <Tabs.Screen
        name="savedTournaments"
        options={{
          title:"gespeicherte Turniere",
          tabBarIcon: () => (<Ionicons name="cloud-download-outline" size={24} color="black" />),
          tabBarActiveTintColor: "black",
          headerShown: false}}
      />
      <Tabs.Screen 
        name="settings" 
        options={{ 
          title:"Einstellungen",
          tabBarIcon: () => (<Ionicons name="settings-outline" size={24} color="black" />),
          tabBarActiveTintColor: "black",
          headerShown: false}} 
      />
    </Tabs>
}
