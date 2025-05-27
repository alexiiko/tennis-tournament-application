import { View } from "react-native";
import { Text } from "@react-navigation/elements";
import { TextInput } from "react-native";
import { Switch } from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";

export default function main() {
    return (
      <SafeAreaView>
        <View>
            <View style={{ paddingLeft: 10, paddingRight: 10}}>
                <Text style={{ fontWeight: "700", paddingTop: 10,  paddingLeft: 10, fontSize: 16}}>Adresse</Text>
                <TextInput style={{ paddingTop: 5, paddingLeft: 10, borderColor: "grey", borderWidth: 0.75, borderRadius: 10 }}/>
            </View>

            <View> 
                <Text>Benachrichtigungen</Text>
                <Switch></Switch>
            </View>
        </View>
      </SafeAreaView>
    )
}
