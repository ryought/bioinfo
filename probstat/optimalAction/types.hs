-- define new typeclass
-- ==と/=が成り立つクラスですよ，っていうクラスの集まり
class Eq' a where  
    (==') :: a -> a -> Bool  
    (/=') :: a -> a -> Bool  
    x ==' y = not (x /=' y)  
    x /=' y = not (x ==' y)  

--class (Eq a) => Num a where

data TrafficLight = Red | Yellow | Green

-- make our types instances of typeclasses
-- ==のこのクラスでの使い方を教えている
instance Eq' TrafficLight where
    Red == Red        =  True
    Green == Green    =  True
    Yellow == Yellow  =  True
    _ == _            =  False

instance (Eq m) => Eq' (Maybe m) where
    Just x == Just y  =  x == y
    Nothing == Nothing = True
    _ == _  = False

instance Show TrafficLight where
    show Red = "red light"
    show Yellow = "yellow light"
    show Green = "green light"



class YesNo a where
    yesno :: a -> Bool

instance YesNo Int where
    yesno 0 = False
    yesno _ = True

instance YesNo [a] where
    yesno [] = False
    yesno _  = True

instance YesNo Bool where
    yesno = id

instance YesNo (Maybe a) where
    yesno (Just _) = True
    yesno Nothing  = False


instance YesNo TrafficLight where
    yesno Red = False
    yesno _   = True

yesnoif :: (YesNo y) => y -> a -> a -> a
yesnoif yesnoVal yesResult noResult = if yesno yesnoVal then yesResult else noResult
