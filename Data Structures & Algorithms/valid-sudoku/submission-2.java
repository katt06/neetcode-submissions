class Solution {
    public boolean isValidSudoku(char[][] board) {

        // need to use HashSet for checkign dupes

        //dealing with rows
        for(int i = 0; i < 9; i++){
            //instead of clearing, just make a new one every row
            HashSet<Character> rowSet = new HashSet<>();
            for (int j = 0; j < 9; j++){
                char curr = board[i][j];
                if (curr =='.') continue;
                if(!rowSet.add(curr)){
                    return false;
                } //this returns false is dupes
                
            }

        }

        //dealing with cols
        // every col, iterate through rows
        for (int j = 0; j < 9; j++){
            HashSet<Character> colSet = new HashSet<>();
            for (int i = 0; i < 9; i++){
                char curr = board[i][j];
                if (curr == '.') continue;
                if(!colSet.add(curr)){
                    return false;
                }
            }
        }

        //dealing with blocks
        // 3 blocks across, 3 blocks down
        for (int i = 0; i < 9; i+=3){
            for (int j = 0; j < 9; j+=3){
                HashSet<Character> threeSet = new HashSet<>();

                for (int k = i; k < i+ 3; k++){
                    for (int h = j; h < j + 3; h++){
                        char curr = board[k][h];
                        if (curr == '.') continue;

                        if (!threeSet.add(curr)){
                            return false;
                        }
                    }
                }
            }
        }
        return true;
    }
}
