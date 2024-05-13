def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            l=0
            r=len(image)-1
            while l<=r:
                image[i][l],image[i][r]=image[i][r],image[i][l]
                if image[i][l]==1:  image[i][l]=0
                else: image[i][l]=1
                if not l==r:
                    if image[i][r]==1:  image[i][r]=0
                    else: image[i][r]=1
                l+=1
                r-=1
        return image
