class Solution {
public:
    bool isPalindrome(string s) {
       string text2,text3;

	bool tf;

	

	for(char ch : s){

		if(isalpha(ch)||isdigit(ch)){

		tf=true;
        break;}

		else{

			tf=false;}

		}

		if(tf){

			for(char ch : s){

		if(isalpha(ch)||isdigit(ch)){

		text2+=tolower(ch);	}

		}

		int x= text2.size();

		for(int i=x-1;i>=0;i--){

			text3+= text2[i];

			}

			if(text3==text2){
                
                  
                
                
                return true;}

			else{return false;}

			}

			else{ return true;}
    }
};
